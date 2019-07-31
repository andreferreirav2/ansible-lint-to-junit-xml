import fileinput
import re
import xml.dom.minidom
import xml.etree.cElementTree as ET


LINE_REGEX = re.compile(r"^(.*?):(\d+?):\s(.*)$")


def get_input():
    """Read input from stdin or filenames passed through args
    """
    return [line.strip() for line in fileinput.input() if line and len(line.strip())]


def parse_lint_line(lint_line):
    """Parse an ansible lint line and extract fields filename, line, lint error
    """
    match = LINE_REGEX.match(lint_line)

    return (match.group(1), match.group(2), match.group(3))


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, "utf-8")
    reparsed = xml.dom.minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")


def lint_to_junit_xml(lint_output):
    """Convert lint output lines to junit xml
    """
    testsuite = ET.Element(
        "testsuite",
        name="ansible-lint",
        tests=str(len(lint_output)),
        errors=str(len(lint_output)),
    )

    if not lint_output:
        # Output an empty test case to avoid breaking some junit xml processors
        ET.SubElement(testsuite, "testcase", name="no linting errors found")
        return testsuite

    for line in lint_output:
        filename, linenr, lint_error = parse_lint_line(line)

        # TODO get lint error full description from ansible-lint
        error_description = """
        ansible-lint error: {0}
        ansible-lint error description: {0}
        filename: {1}
        line nr: {2}
        """.format(
            lint_error, filename, linenr
        )

        testcase = ET.SubElement(testsuite, "testcase", name=lint_error)
        ET.SubElement(
            testcase, "failure", message=line, type="ansible-lint"
        ).text = error_description
    return testsuite


def main():
    ansible_lint_output = get_input()

    testsuites = lint_to_junit_xml(ansible_lint_output)

    parsed_lines_xml = prettify(testsuites)
    print(parsed_lines_xml)


if __name__ == "__main__":
    main()

# pylint: disable=missing-function-docstring
import pytest

from cadena_pre_commit_hooks.pin_requirements_txt import FAIL
from cadena_pre_commit_hooks.pin_requirements_txt import main
from cadena_pre_commit_hooks.pin_requirements_txt import PASS


@pytest.mark.parametrize(
    ("input_s", "expected_retval"),
    (
        (b"", PASS),
        (b"\n", PASS),
        (b"# intentionally empty\n", PASS),
        (b"foo\n# comment at end\n", FAIL),
        (b"foo==1.0\n# comment at end\n", PASS),
        (b"foo\nbar==2.1\n", FAIL),
        (b"foo==2.2\nbar==2.1\n", PASS),
        (b"a\nc\nb\n", FAIL),
        (b"a==1\nc==2.2\nb===3.3\n", PASS),
        (b"a==1.*\nc==2.2\nb==3.3\n", FAIL),
        (b"a==1.*,===1.1.1\nc==2.2\nb==3.3\n", PASS),
        (b"pyramid-foo==1\npyramid>=2\n", FAIL),
        (b"pyramid-foo==1\npyramid>=2,==2.2\n", PASS),
    ),
)
def test_integration(input_s, expected_retval, tmpdir):
    path = tmpdir.join("file.txt")
    path.write_binary(input_s)

    output_retval = main([str(path)])

    assert output_retval == expected_retval

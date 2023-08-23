from checkoutput import checkout_positive
from config import arch_type
import pytest

folder_in = "/home/edan/tst/file"
folder_out = "/home/edan/tst/out"
folder_ext = "/home/edan/tst/ext"


def test_step_1(make_folders, clear_folders, make_files):
    # test 1
    res1 = checkout_positive("cd {}; 7z a -t{}/arx1.7z".format(folder_in, arch_type, folder_out), "All is Ok"), "Test 1 Fail"
    res2 = checkout_positive("ls {}".format(folder_out), "arx.7z"), "Test 1 Fail"
    assert res1 and res2, "Test Fail"


def test_step_2(clear_folders, make_files):
    # test 2
    res = []
    res.append(checkout_positive("cd {}; 7z a -t{}/arx1.7z".format(folder_in, arch_type, folder_out), "All is Ok"))
    res.append(checkout_positive("cd {}; 7z e arx1.7z -o{} -y".format(folder_out, folder_ext), "All is Ok"))
    for item in make_files:
        res.append(checkout_positive("ls {}".format(folder_ext), ""))
    assert all(res)


def test_step_3():
    # test 3
    assert checkout_positive("cd {}; 7z t -t{}/arx1.7z".format(folder_in, arch_type, folder_out), "All is Ok"), "Test 3 Fail"


def test_step_4(make_folders, clear_folders, make_files):
    # test 4
    assert checkout_positive("cd {}; 7z u -t{}/arx1.7z".format(folder_in, arch_type, folder_out), "All is Ok"), "Test 4 Fail"


def test_step_5(clear_folders, make_files):
    # test 5
    res = []
    res.append(checkout_positive("cd {}; 7z a -t{}/arx1.7z".format(folder_in, arch_type, folder_out), "All is Ok"))
    for item in make_files:
        res.append(checkout_positive("cd {}; 7z l arx1.7z".format(folder_out), item))
    assert all(res)


def test_step_6(make_folders, clear_folders, make_files):
    # test 6
    res = []
    res.append(checkout_positive("cd {}; 7z a -t{}/arx1.7z".format(folder_in, arch_type, folder_out), "All is Ok"))
    res.append(checkout_positive("cd {}; 7z x arx1.7z -o{} -y".format(folder_out, folder_ext), "All is Ok"))
    for item in make_files:
        res.append(checkout_positive("ls {}".format(folder_ext), ""))
    assert all(res), "Test Fail"

def test_step_7():
    # test 7
    assert checkout_positive("7z d -t{}/arx1.7z".format(arch_type, folder_out), "All is Ok"), "Test 7 Fail"


if __name__ == '__main__':
    pytest.main()
# Copyright (c) 2015-2019, XMOS Ltd, All rights reserved
import xmostest

def runtest():
    resources = xmostest.request_resource("xsim")
     
    tester = xmostest.ComparisonTester(open('unreachable_test.expect'),
                                       'lib_xassert', 'simple_tests',
                                       'unreachable_test', {})
     
    xmostest.run_on_simulator(resources['xsim'],
                              'unreachable_test/bin/unreachable_test.xe',
                              tester=tester)

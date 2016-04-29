from unittest import TestCase
from multimple import multimple


@multimple
class SomeMultimpler(object):
    IMPL1_INCR = 3
    IMPL2_INCR = 1

    def __init__(self, some_init_arg):
        self.init_arg = some_init_arg

    @multimple('impl1')
    def some_function(self, some_param):
        return some_param + self.IMPL1_INCR

    @some_function.multimple('impl2')
    def some_function(self, some_param):
        return some_param + self.IMPL2_INCR


class MultimpleTest(TestCase):
    def test_main(self):
        ImplDefault = SomeMultimpler
        Impl1 = SomeMultimpler.multimple('impl1')
        Impl2 = SomeMultimpler.multimple('impl2')
        Impl3 = SomeMultimpler.multimple('impl3')

        init_arg_default = 0
        init_arg1 = 3
        init_arg2 = 8
        init_arg3 = 1

        impl_default = ImplDefault(init_arg_default)
        impl1 = Impl1(init_arg1)
        impl2 = Impl2(init_arg2)
        impl3 = Impl3(init_arg3)

        # Make sure wrapping __init__ works as expected
        self.assertEqual(impl_default.init_arg, init_arg_default)
        self.assertEqual(impl1.init_arg, init_arg1)
        self.assertEqual(impl2.init_arg, init_arg2)
        self.assertEqual(impl3.init_arg, init_arg3)

        # Make sure the current implementation is set correctly
        attr_name = multimple.__self__._IMPL_ATTR_NAME
        self.assertFalse(hasattr(impl_default, attr_name))
        self.assertEqual(getattr(impl1, attr_name), 'impl1')
        self.assertEqual(getattr(impl2, attr_name), 'impl2')
        self.assertEqual(getattr(impl3, attr_name), 'impl3')

        # Now test actually multimple
        self.assertEqual(impl_default.some_function(1),
                         1 + SomeMultimpler.IMPL1_INCR)
        self.assertEqual(impl1.some_function(7), 7 + SomeMultimpler.IMPL1_INCR)
        self.assertEqual(impl2.some_function(3), 3 + SomeMultimpler.IMPL2_INCR)
        self.assertRaises(NotImplementedError, getattr, impl3, 'some_function')

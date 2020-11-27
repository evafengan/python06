# -*- coding: utf-8 -*-

import unittest

#创建类，继承unittest.TestCase
class demo(unittest.TestCase):
    #所有case执行之前，准备一次环境的话，执行之后再清理环境，比如数据库连接和销毁，就用setupclass()和teardown()
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    #类的释放
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    #执行用例前的登录，打开浏览器，数据库连接等操作，放在setUp里
    def setUp(self) -> None:
        print("setup")

    # 执行完用例后，关闭浏览器等操作，放在teardown
    def tearDown(self) -> None:
        print("teardown")

    #测试用例命名，都要以test开头
    def test_case01(self):
        print("testcase01")
        self.assertEqual(2, 2, "判断相等")
        # self.assertIn('h', 'this')

    def test_case02(self):
        print("testcase02")
        self.assertEqual(3, 3, "判断相等")
        # self.assertIn('h', 'this')

    #有些方法不想执行，用unittest.skip跳过
    @unittest.skipIf(1+1 == 2, "跳过这条用例")
    def test_case03(self):
        print("testcase03")
        self.assertEqual(4, 4, "判断相等")

#新增一个测试用例类
class demo1(unittest.TestCase):
    def test_demo1_case0(self):
        print("test demo1 case0")

    def test_demo1__case1(self):
        print("test demo1 case1")

if __name__ == '__main__':
    #如果只有一个测试类的话，就直接用unittest.main()
    #unittest.main()

    #有多个测试类时，加上unittest.TestSuite()
    suite = unittest.TestSuite()
    suite.addTest(demo("test_case01"))
    suite.addTest(demo1("test_demo1_case0"))

    unittest.TextTestRunner.run(suite)
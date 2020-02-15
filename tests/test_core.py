from cnabera import core


class TestCore:
    def test_main(self):
        expected_msg = 'print from application'
        assert core.main() == expected_msg

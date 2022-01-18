from Creational.Factory.factory import get_logger


class TestFactory:

    def test_one(self):
        logger = get_logger("file")
        assert logger.log() == "File Logger"
        logger = get_logger("stdout")
        assert logger.log() == "Stdout Logger"
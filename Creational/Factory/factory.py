class StdoutLogger:

    def log(self):
        return "Stdout Logger"


class FileLogger:

    def log(self):
        return "File Logger"


def get_logger(logger="file"):

    loggers = dict(stdout=StdoutLogger(), file=FileLogger())

    return loggers[logger]



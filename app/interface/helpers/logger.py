# -*- coding: utf-8 -*-
import logging
import traceback


class ConsoleLogger:

    def __init__(self):
        try:
            self.logger = logging
            self.logger.basicConfig(
                format='%(asctime)s [%(levelname)s] - %(name)s - %(message)s',
                datefmt='[%Y/%m/%d %I:%M:%S %p]'
            )
        except Exception as e:
            raise e

    def output(self, msg):
        self.logger.error('=' * 25)
        self.logger.error(msg)
        self.logger.error('=========== TRACEBACK ==========')
        print(traceback.format_exc())

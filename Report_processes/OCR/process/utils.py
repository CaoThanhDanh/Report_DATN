import winsound
import time
from datetime import datetime
import os
import platform
import unicodedata
import re

CURRENT = os.path.dirname(os.path.realpath(__file__))

START_AT = datetime.now()


class Utils(object):
    @staticmethod
    def playWarningSound(loopTime=2):
        for _ in range(loopTime):
            winsound.Beep(frequency=2500, duration=400)
            time.sleep(0.4)

    @staticmethod
    def reportTime():
        END_AT = datetime.now()

        print("\nDONE!\n")
        print(f"🕑 Start at: {START_AT}")
        print(f"🕑 End at:   {END_AT}")
        print(f"🕑 Duration: {END_AT - START_AT}\n")

    @staticmethod
    def kebabCaseToCamelCase(text):
        return ''.join(p.capitalize() or '-' for p in text.split('-'))

    @staticmethod
    def getImageMagickPath(exeName):
        return os.path.join(CURRENT, "external", platform.system(), exeName)

    @staticmethod
    def readAllText(filePath):
        with open(filePath, "r", encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def writeAllText(filePath, text):
        with open(filePath, "w", encoding='utf-8') as f:
            f.write(text)

    @staticmethod
    def writeAppendText(filePath, text):
        with open(filePath, "a", encoding='utf-8') as f:
            f.write(text)

    @staticmethod
    def slugify(value, allow_unicode=False):
        value = str(value)
        if allow_unicode:
            value = unicodedata.normalize('NFKC', value)
        else:
            value = unicodedata.normalize('NFKD', value).encode(
                'ascii', 'ignore').decode('ascii')
        value = re.sub(r'[^\w\s-]', '-', value.lower())
        return re.sub(r'[-\s]+', '-', value).strip('-_')

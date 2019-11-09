import unittest
from downloadDocuments import DownloadDocuments

import os

class TestDownloadDocuments(unittest.TestCase):

    def test_download(self):

        DownloadDocuments().download('https://sevc2019.com/index.php/es/programa-cientifico/anestesia-y-control-del-dolor/22-anestesia-en-pequenos-animales-con-enfermedad-renal-que-debo-hacer-como-por-que', 'parent')

        self.assertTrue(os.path.exists('./parent/anestesia-en-pequenos-animales-con-enfermedad-renal-que-debo-hacer-como-por-que.pdf'))

        os.remove('./parent/anestesia-en-pequenos-animales-con-enfermedad-renal-que-debo-hacer-como-por-que.pdf')
        os.rmdir('./parent')

    def test_makeDir(self):
        tempPath = os.getcwd() + '/testDownload'
        DownloadDocuments().makeCategoryDir('testDownload')
        
        self.assertTrue(os.path.exists(tempPath))
        os.rmdir(tempPath)
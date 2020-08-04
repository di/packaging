import os
import re
import tarfile
from zipfile import ZipFile


class Distribution:
    def __init__(self, filename):
        self.filename = filename

    def extract_pkginfo(self):
        raise NotImplementedError()


class SDist(Distribution):
    pass


class SDistTar(SDist):
    def extract_pkginfo(self):
        with tarfile.open(self.filename) as archive:
            dirname = os.path.commonprefix(archive.getnames())
            member = archive.extractfile("/".join([dirname, "PKG-INFO"]))
            if member:
                return member.read().decode("utf-8")
            raise NoMetadataFound


class SDistZip(SDist):
    def extract_pkginfo(self):
        with ZipFile(self.filename) as archive:
            names = archive.namelist()
            for name in names:
                if "PKG-INFO" in name:
                    data = archive.open(name).read()
                    if b"Metadata-Version" in data:
                        return data.decode("utf-8")


class Wheel(Distribution):
    def extract_pkginfo(self):
        with ZipFile(self.filename) as archive:
            names = archive.namelist()
            for name in names:
                if "METADATA" in name:
                    data = archive.open(name).read()
                    if b"Metadata-Version" in data:
                        return data.decode("utf-8")

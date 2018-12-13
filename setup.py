import os
from distutils.command.build import build

from django.core import management
from setuptools import setup, find_packages


try:
    with open(
        os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8'
    ) as f:
        long_description = f.read()
except Exception:
    long_description = ''


class CustomBuild(build):
    def run(self):
        management.call_command('compilemessages', verbosity=1, interactive=False)
        build.run(self)


cmdclass = {'build': CustomBuild}


setup(
    name='pretalx-socialauth',
    version='0.0.0',
    description="Use other websites, like GitHub or Twitter, to allow users to log in to pretalx.",
    long_description=long_description,
    url='https://github.com/pretalx/pretalx-socialauth',
    author='Tobias Kunze',
    author_email='r@rixx.de',
    license='Apache Software License',
    install_requires=[],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[pretalx.plugin]
pretalx_socialauth=pretalx_socialauth:PretalxPluginMeta
""",
)

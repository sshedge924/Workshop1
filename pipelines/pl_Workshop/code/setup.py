from setuptools import setup, find_packages
setup(
    name = 'pl_Workshop',
    version = '1.0',
    packages = find_packages(include = ('pl_workshop*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'faker==24.3.0', 'prophecy-libs==1.8.13'],
    entry_points = {
'console_scripts' : [
'main = pl_workshop.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)

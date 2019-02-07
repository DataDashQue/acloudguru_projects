from setuptools import setup

setup(
    name='snapshotalyzer-5000',
    version='0.1',
    author="Victor-Kevin Quiambao",
    author_email="vquiambao@shutterstock.com",
    description="Snapshot tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    package=['shotty'],
    url="https://github.com/DataDashQue/acloudguru_projects/",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=snapshot_aws.shotty:cli
    ''',
)
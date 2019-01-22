from setuptools import find_packages, setup

setup(
    name='unused_components',
    use_scm_version=True,
    description="Find unused vue components",
    keywords=[],
    url="",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    setup_requires=[
        'setuptools_scm',
    ],
    include_package_data=True,
    zip_safe=False,
)

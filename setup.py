from setuptools import find_packages, setup

setup(
    name="Ecommercebot",
    version="0.0.1",
    author="adarsh",
    author_email="a.a4273@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-openai','datasets','pypdf','python-dotenv','flask','pandas']
)
#!/usr/bin/env python3
import docker
from dateutil.parser import parse
conn = docker.from_env(version='auto')


def show_attrs(image):
    print("Image ID: "+image.attrs['Id'].split(':')[1][0:12])
    # print("From: "+str(image.attrs['RepoTags']))
    date = parse(image.attrs['Created'])
    print("Created:", date)
    print()


for image in conn.images.list():
    show_attrs(image)

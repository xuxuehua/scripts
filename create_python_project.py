#!/usr/bin/env python
# coding=utf-8

import os
import argparse


class Project(object):

    def __init__(self, *args):
        self.project_path_with_name = str(args[0])
        self.current_dir = os.path.dirname(__file__)
        self.sub_folder_name = os.path.basename(self.project_path_with_name).lower()

    def create_dirs(self):
        os.makedirs(r'%s/bin' % self.project_path_with_name)
        os.makedirs(r'%s/conf' % self.project_path_with_name)
        os.makedirs(r'%s/%s/tests' % (self.project_path_with_name, self.sub_folder_name))
        os.makedirs(r'%s/docs' % self.project_path_with_name)

    def create_files(self):
        open('%s/%s/tests/__init__.py' % (self.project_path_with_name, self.sub_folder_name), 'w')
        open('%s/%s/tests/testmain.py' % (self.project_path_with_name, self.sub_folder_name), 'w')
        open('%s/%s/__init__.py' % (self.project_path_with_name, self.sub_folder_name), 'w')
        open('%s/%s/main.py' % (self.project_path_with_name, self.sub_folder_name), 'w')
        open('%s/docs/conf.py' % self.project_path_with_name, 'w')
        open('%s/docs/docs.py' % self.project_path_with_name, 'w')
        open('%s/setup.py' % self.project_path_with_name, 'w')
        open('%s/requirements.txt' % self.project_path_with_name, 'w')
        open('%s/README.md' % self.project_path_with_name, 'w')


def argparse_ret():
    current_dir = os.path.dirname(__file__)
    parser = argparse.ArgumentParser(description='This is used to initial python project directory & files.')
    parser.add_argument('p', help="Project Name")
    parser.add_argument('-p', '--path', help="Absolute path")
    args = parser.parse_args()
    project_name = str(args.p).capitalize()
    project_path = str(args.path)

    if args.path and project_path.startswith('~/') is True and project_path.endswith('/') is True:
        arg_path_with_name = str(project_path).replace('~', os.environ['HOME']) + project_name

    elif args.path and project_path.startswith('/') is False:
        raise SystemExit('Please Input absolute path for optional arguments')

    elif args.path and project_path.endswith('/') is False:
        raise SystemExit('Please add "/" suffix at the end of optional arguments')

    elif args.path:
        arg_path_with_name = project_path + project_name

    else:
        arg_path_with_name = current_dir + project_name

    return arg_path_with_name

my_project = Project(argparse_ret())
my_project.create_dirs()
my_project.create_files()

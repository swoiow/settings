#!/usr/bin/env python
# -*- coding: utf-8 -*

from fabric.api import cd, settings, sudo

from _internal_utils import pf


def depend_debian():
    """
    apt-get install -y libncurses5-dev libncursesw5-dev
    """
    for line in depend_debian.__doc__.split("\n"):
        sudo(line)


def depend_redhat():
    """
    yum install -y ncurses-devel
    """
    for line in depend_redhat.__doc__.split("\n"):
        sudo(line)


def depend():
    depend_map = [
        ("debian", depend_debian),
        ("redhat", depend_redhat),
    ]

    dict(depend_map)[pf()]()


def download():
    """
    curl -sL https://github.com/vim/vim/archive/v8.1.0630.tar.gz | tar -xz
    """

    with cd("/usr/src/"), settings(warn_only=True):
        for line in download.__doc__.split("\n"):
            sudo(line)


def install():
    """
    ./configure --enable-python3interp --enable-luainterp --enable-cscope --prefix=/usr/local/vim/
    make -s -j2
    make install
    ln -sf /usr/local/vim/bin/vim /usr/bin/vim
    """

    depend()

    download()

    with cd("/usr/src/vim-8.1.0630"), settings(warn_only=True):
        for line in install.__doc__.split("\n"):
            sudo(line)

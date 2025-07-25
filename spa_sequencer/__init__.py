# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2023, The SPA Studios. All rights reserved.

from . import (
    editorial,
    keymaps,
    preferences,
    render,
    sequence,
    shared_folders,
    shot,
    sync,
)


bl_info = {
    "name": "SPArk Sequencer",
    "author": "Nick Alberelli & The SPA Studios",
    "description": "Toolset to improve the sequence workflow in Blender.",
    "blender": (4, 4, 0),
    "version": (0, 1, 4),
    "location": "",
    "warning": "",
    "category": "SPA",
}


packages = (
    sync,
    shot,
    sequence,
    render,
    editorial,
    shared_folders,
    preferences,
    keymaps,
)


def register():
    for package in packages:
        package.register()


def unregister():
    for package in packages:
        package.unregister()

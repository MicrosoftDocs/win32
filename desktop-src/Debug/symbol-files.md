---
description: Normally, debugging information is stored in a symbol file separate from the executable.
ms.assetid: 610e5cd3-9dc3-462c-98f8-6a63874464f8
title: Symbol Files
ms.topic: article
ms.date: 05/31/2018
---

# Symbol Files

Normally, debugging information is stored in a symbol file separate from the executable. The implementation of this debugging information has changed over the years, and the following documentation will provide guidance regarding these various implementations.

## PDB files

All modern versions of the Microsoft compilers store debugging information about a compiled executable in a separate *program database* (.pdb) file. This file is commonly referred to as a *PDB*. The data is stored in a separate file from the executable to help limit the size of the executable, saving disk storage space and reducing the time it takes to load the data. This methodology also allows the executable to be distributed without disclosing this significant information which could make the program easier to reverse engineer.

To create a PDB, build your executable file with debugging information according to the directions for your build tools.

The DbgHelp API is able to use PDBs to obtain the following information.

-   publics and exports
-   global symbols
-   local symbols
-   type data
-   source files
-   line numbers

## DBG files and embedded debug information

Previous versions of the Microsoft toolset used to embed the debugging information in the executable, however it would normally be stripped out into a separate file with a .dbg extension. This is commonly known as a *DBG* file. DBG files use the same PE file format as executables.

The DbgHelp API support for DBGs and embedded debugging information is limited and includes the following.

-   publics and exports
-   global symbols

 

 




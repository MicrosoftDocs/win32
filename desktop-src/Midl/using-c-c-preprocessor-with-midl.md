---
title: Using C/C++-Preprocessor with MIDL
description: The MIDL compiler does not preprocess source files.
ms.assetid: 0f62d2a4-cfc3-42a7-b3a6-4e5c67c7c849
keywords:
- MIDL compiler MIDL , C-preprocessor
- C-preprocessor MIDL
ms.topic: article
ms.date: 05/31/2018
---

# Using C/C++-Preprocessor with MIDL

The MIDL compiler does not preprocess source files. Rather, the MIDL compiler uses an available preprocessor to prepare the input stream for parsing. By default, MIDL uses the preprocessor for the Microsoft C/C++ compiler from the same building environment as MIDL. The user can indicate a different preprocessor to be used by MIDL, if needed.

MIDL spawns separate preprocessor runs for top-level IDL and ACF files, and for each file imported with the MIDL import directive. Files included with the **\#include** directive are handled by the preprocessor directly.

The following topics describe various aspects of MIDL-preprocessor interactions:

-   [C-Preprocessor Requirements for MIDL](c-preprocessor-requirements-for-midl.md)
-   [Verifying Preprocessor Options](verifying-preprocessor-options.md)
-   [Saving Preprocessor Output](saving-preprocessor-output.md)
-   [Dealing with \#defines in IDL Files](dealing-with-defines-in-idl-files-2.md)

 

 





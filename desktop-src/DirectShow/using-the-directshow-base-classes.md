---
description: Using the DirectShow Base Classes
ms.assetid: 7eab0e55-1566-4b4c-b37c-32c5a1f37363
title: Using the DirectShow Base Classes
ms.topic: article
ms.date: 05/31/2018
---

# Using the DirectShow Base Classes

To use the base classes in DirectShow, you must build and link the base class library.

The base class library is provided as a SDK sample in the Microsoft Windows Software Development Kit (SDK) (<https://go.microsoft.com/fwlink/p/?linkid=62332>). The exact location depends on the version of the SDK that you have installed, but the relative path is:

*(SDK samples root)*\\DirectShow\\BaseClasses

Header: Streams.h

Library: The sample builds retail and debug versions of the library:

-   Retail version: Strmbase.lib
-   Debug version: Strmbasd.lib.

For more information on setting up your build environment, see [Setting Up the Build Environment](setting-up-the-build-environment.md).

## Preprocessor Symbols

When you include the header file Streams.h, the following preprocessor symbols have special meaning:

-   PERF: Reserved. Do not use this preprocessor symbol.
-   VFWROBUST: Enables pointer validation in retail. For more information, see [Pointer Validation Macros](pointer-validation-macros.md). In debug builds, it is not necessary to define VFWROBUST.

> [!Note]  
> In Windows Vista and later, the pointer validation macros are empty.

 

 

 




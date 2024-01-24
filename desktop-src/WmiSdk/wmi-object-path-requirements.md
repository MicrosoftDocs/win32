---
description: WMI uses object paths in the reference properties of association classes to identify related objects, as well as using object paths in input or output parameters for several methods.
ms.assetid: 07fee6f8-810e-4dec-8f0f-787756ee3beb
ms.tgt_platform: multiple
title: WMI Object Path Requirements
ms.topic: article
ms.date: 05/31/2018
---

# WMI Object Path Requirements

WMI uses object paths in the reference properties of association classes to identify related objects, as well as using object paths in input or output parameters for several methods. Because object paths are treated as strings for the purpose of lookup and comparison, the value of an object path when used as a reference property is always the string itself and not the dereferenced object. String comparisons that deal with object paths are always case-insensitive.

An object path can use the following syntax:

-   Strings contained in single quotation marks.
-   Forward slashes as separators.
-   Backslashes as separators.
-   Hexadecimal constants for integers.
-   Boolean constants for classes with keys that take Boolean values.
-   URL notation to represent nonprinting characters, such as %20 for a blank space.

In addition, an object path string must obey the following restrictions:

-   An assumed local server with a partial namespace path. Thus, specifying the root and default namespace implies the root and default namespace on the local server.
-   No white space either within an element or between elements.
-   Embedded quotation marks in object paths are allowed but must delimit the quotation mark with escape characters, as in a C or C++ application.
-   Only decimal values are recognized as numeric portions of keys.

 

 




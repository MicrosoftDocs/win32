---
title: Using the __midl Predefined Constant
description: When the MIDL compiler processes the input IDL and ACF files, \_\_midl is defined by default and is used for conditional compilation to attain consistency throughout the build.
ms.assetid: ba9557f8-d398-4c87-993d-f4e545894cdd
keywords:
- MIDL compiler MIDL , using the _midl predefined constant
- _midl predefined constant MIDL
ms.topic: article
ms.date: 05/31/2018
---

# Using the \_\_midl Predefined Constant

When the MIDL compiler processes the input IDL and ACF files, \_\_midl is defined by default and is used for conditional compilation to attain consistency throughout the build. This phases out the use of define statements in the header files, such as **MIDL\_PASS**, and replaces them with a consistent flag. The value of the \_\_midl constant indicates the compiler version *major.minor* according to the formula *major* \* 100 + *minor*; for example MIDL ver. 6.0.x has the \_\_midl defined as 600.

If you choose, you can override this default by specifying the following on the command line: **/U\_\_midl**. For more information, see [**/U**](-u.md).

 

 





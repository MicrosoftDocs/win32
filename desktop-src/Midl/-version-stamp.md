---
title: /version_stamp switch
description: The /version\_stamp switch suppresses the generation of macros that specify the minimum required version number of the RPC header file, Rpcndr.h.
ms.assetid: ec03f68b-60f7-431e-9fba-4434ef082058
keywords:
- /version_stamp switch MIDL
topic_type:
- apiref
api_name:
- /version_stamp
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /version\_stamp switch

The **/version\_stamp** switch suppresses the generation of macros that specify the minimum required version number of the RPC header file, Rpcndr.h.

New MIDL features might require additional definitions to compile the stub correctly, so the stub has macros that check compatibility between MIDL binary files and the build environment. You might need to use this switch if you move MIDL to a different build environment than the one in which you first installed the MIDL binary files.

Note that mixing build environments is not supported.

``` syntax
midl /version_stamp
```

## Switch Options

This switch has no parameters.

 

 





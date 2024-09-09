---
description: Called by the compiler when you have more than one page of local variables in your function. (__chkstk)
title: '__chkstk Routine'
ms.topic: article
ms.date: 03/02/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __chkstk
api_type: 
- DllExport
api_location: 
- kernelbase.dll
---

# \__chkstk Routine

Called by the compiler when you have more than one page of local variables in your function.

## Remarks

\__chkstk Routine is a helper routine for the C compiler. For x86 compilers, \__chkstk Routine is called when the local variables exceed 4K bytes; for x64 compilers it is 8K.

 This function is not defined in an SDK header and must be declared by the caller. This function is exported from kernelbase.dll.

 




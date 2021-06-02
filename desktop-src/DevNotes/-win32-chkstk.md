---
description: Called by the compiler when you have more than one page of local variables in your function.
ms.assetid: 154dd992-88b5-44a4-9594-5d13afb71c28
title: '_chkstk Routine'
ms.topic: article
ms.date: 05/31/2018
---

# \_chkstk Routine

Called by the compiler when you have more than one page of local variables in your function.

## Remarks

\_chkstk Routine is a helper routine for the C compiler. For x86 compilers, \_chkstk Routine is called when the local variables exceed 4K bytes; for x64 compilers it is 8K.

 

 




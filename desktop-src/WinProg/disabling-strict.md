---
title: Disabling STRICT
description: To disable STRICT type checking, define the symbol name NO\_STRICT. In Visual C/C++, you can also specify this definition on the command line or in a makefile by specifying /DNO\_STRICT as a compiler option.
ms.assetid: 57b01d2e-1f64-4ac0-b4f0-624c241899d7
ms.topic: article
ms.date: 05/31/2018
---

# Disabling STRICT

To disable **STRICT** type checking, define the symbol name **NO\_STRICT**. In Visual C/C++, you can also specify this definition on the command line or in a makefile by specifying **/DNO\_STRICT** as a compiler option.

To define **NO\_STRICT** on a file-by-file basis, insert a **\#define** statement before including Windows.h:


```C++
#define NO_STRICT
#include <windows.h>
```



For best results, you should also set the warning level for error messages to at least **/W3**. This is always advisable with applications for Windows, because a coding practice that causes a warning (for example, passing the wrong number of parameters) usually causes a fatal error at run time if it is not corrected.

## Related topics

<dl> <dt>

[Enabling STRICT](enabling-strict.md)
</dt> <dt>

[STRICT Compliance](strict-compliance.md)
</dt> </dl>

 

 





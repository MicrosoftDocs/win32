---
description: Determines whether the Terminal Server is in the INSTALL mode.
ms.assetid: edf362e6-c1a4-49fe-8e07-1188c66616be
title: TermsrvAppInstallMode function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TermsrvAppInstallMode
api_type: 
- DllExport
api_location: 
- Kernel32.dll
---

# TermsrvAppInstallMode function

\[This function is not supported and should not be used. It may change or disappear completely without advance notice.\]

Determines whether the Terminal Server is in the INSTALL mode.

## Syntax


```C++
BOOL TermsrvAppInstallMode(void);
```



## Parameters

This function has no parameters.

## Return value

This function returns **TRUE** if the Terminal Server is in INSTALL mode and **FALSE** if it is in EXECUTE mode.

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Kernel32.dll</dt> </dl> |



 

 





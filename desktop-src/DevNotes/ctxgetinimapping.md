---
Description: Determines whether the Terminal Server is in INSTALL mode (only on Windows Terminal Server 4.0).
ms.assetid: f6cb7971-d4f5-49ca-938a-9c280028764a
title: CtxGetIniMapping function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CtxGetIniMapping function

\[This function is not supported and should not be used. It may change or disappear completely without advance notice. Instead, use **VerifyVersionInfo**.\]

Determines whether the Terminal Server is in INSTALL mode (only on Windows Terminal Server 4.0).

## Syntax


```C++
BOOLEAN CtxGetIniMapping(void);
```



## Parameters

This function has no parameters.

## Return value

This function returns **FALSE** if the Terminal Server is in INSTALL mode, **TRUE** if it is in EXECUTE mode.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Kernel32.dll</dt> </dl> |



## See also

<dl> <dt>

[**VerifyVersionInfo**](base.verifyversioninfo)
</dt> </dl>

 

 





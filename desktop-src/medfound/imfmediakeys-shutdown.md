---
ms.assetid: 464b598c-5fa7-40af-83ba-8619fbd84b04
title: IMFMediaKeysShutdown method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMFMediaKeys::Shutdown method

## Syntax


```C++
HRESULT Shutdown();
```



## Parameters

This method has no parameters.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

**Shutdown** should be called by the application before final release. The Content Decryption Module (CDM) reference and any other resources is released at this point. However, related sessions are not freed or closed.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                      |
| IDL<br/>                      | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMFMediaKeys**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfmediakeys?branch=master)
</dt> </dl>

 

 





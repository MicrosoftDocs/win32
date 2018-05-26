---
Description: Aborts the processing of the current media segment.
ms.assetid: 31253d0d-c53f-47bd-823a-fc564cb63b78
title: IMFSourceBufferAbort method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMFSourceBuffer::Abort method

Aborts the processing of the current media segment.

## Syntax


```C++
HRESULT Abort();
```



## Parameters

This method has no parameters.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                      |
| IDL<br/>                      | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMFSourceBuffer**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfsourcebuffer?branch=master)
</dt> </dl>

 

 





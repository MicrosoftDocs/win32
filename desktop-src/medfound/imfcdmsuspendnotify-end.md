---
Description: The actual suspend is about to occur and no more calls will be made into the Content Decryption Module (CDM).
ms.assetid: 7a319fbb-9757-45da-8a8b-51dd48f08464
title: IMFCdmSuspendNotifyEnd method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMFCdmSuspendNotify::End method

The actual suspend is about to occur and no more calls will be made into the Content Decryption Module (CDM).

## Syntax


```C++
HRESULT End();
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

[**IMFCdmSuspendNotify**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfcdmsuspendnotify?branch=master)
</dt> </dl>

 

 





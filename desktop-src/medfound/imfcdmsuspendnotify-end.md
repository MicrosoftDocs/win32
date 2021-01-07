---
description: The actual suspend is about to occur and no more calls will be made into the Content Decryption Module (CDM).
ms.assetid: 7a319fbb-9757-45da-8a8b-51dd48f08464
title: IMFCdmSuspendNotify::End method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMFCdmSuspendNotify.End
api_type: 
- COM
api_location: 
- mfmediaengine.h
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



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                      |
| IDL<br/>                      | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMFCdmSuspendNotify**](/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfcdmsuspendnotify)
</dt> </dl>

 

 





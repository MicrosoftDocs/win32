---
description: Closes the media key session and must be called before the key session is released.
ms.assetid: 97c6b4bd-a973-4475-a325-0373af9b54b1
title: IMFMediaKeySession::Close method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMFMediaKeySession.Close
api_type: 
- COM
api_location: 
- mfmediaengine.h
---

# IMFMediaKeySession::Close method

Closes the media key session and must be called before the key session is released.

## Syntax


```C++
HRESULT Close();
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

[**IMFMediaKeySession**](/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediakeysession)
</dt> </dl>

 

 





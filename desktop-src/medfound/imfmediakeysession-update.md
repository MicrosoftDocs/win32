---
description: Passes in a key value with any associated data required by the Content Decryption Module for the given key system.
ms.assetid: 29e66037-5f18-4724-b6f2-d85555e6af69
title: IMFMediaKeySession::Update method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMFMediaKeySession.Update
api_type: 
- COM
api_location: 
- mfmediaengine.h
---

# IMFMediaKeySession::Update method

Passes in a key value with any associated data required by the Content Decryption Module for the given key system.

## Syntax


```C++
HRESULT Update(
   const BYTE  *key,
         DWORD cb
);
```



## Parameters

<dl> <dt>

*key* 
</dt> <dd></dd> <dt>

*cb* 
</dt> <dd>

The count in bytes of *key*.

</dd> </dl>

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

 

 





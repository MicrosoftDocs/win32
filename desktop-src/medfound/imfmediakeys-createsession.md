---
description: Creates a media key session object using the specified initialization data and custom data. .
ms.assetid: 9f11433c-7cff-4a59-9d4a-7f4b56ba62cf
title: IMFMediaKeys::CreateSession method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMFMediaKeys.CreateSession
api_type: 
- COM
api_location: 
- mfmediaengine.h
---

# IMFMediaKeys::CreateSession method

Creates a media key session object using the specified initialization data and custom data. .

## Syntax


```C++
HRESULT CreateSession(
         BSTR                     mimeType,
   const BYTE                     *initData,
         DWORD                    cb,
   const BYTE                     *customData,
         DWORD                    cbCustomData,
         IMFMediaKeySessionNotify *notify,
         IMFMediaKeySession       **ppSession
);
```



## Parameters

<dl> <dt>

*mimeType* 
</dt> <dd>

The MIME type of the media container used for the content.

</dd> <dt>

*initData* 
</dt> <dd>

The initialization data for the key system.

</dd> <dt>

*cb* 
</dt> <dd>

The count in bytes of *initData*.

</dd> <dt>

*customData* 
</dt> <dd>

Custom data sent to the key system.

</dd> <dt>

*cbCustomData* 
</dt> <dd>

The count in bytes of *cbCustomData*.

</dd> <dt>

*notify* 
</dt> <dd>

notify

</dd> <dt>

*ppSession* 
</dt> <dd>

The media key session.

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

[**IMFMediaKeys**](/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediakeys)
</dt> </dl>

 

 





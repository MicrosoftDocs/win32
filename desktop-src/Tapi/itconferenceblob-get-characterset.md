---
description: The get\_CharacterSet method gets a BLOB\_CHARACTER\_SET descriptor of the character set used in the current conference blob.
ms.assetid: 9783d18c-79f6-4faa-b12d-9504c13d54e3
title: ITConferenceBlob::get_CharacterSet method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITConferenceBlob::get\_CharacterSet method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_CharacterSet** method gets a [**BLOB\_CHARACTER\_SET**](blob-character-set.md) descriptor of the character set used in the current conference blob.

## Syntax


```C++
HRESULT get_CharacterSet(
  [out] BLOB_CHARACTER_SET *pCharacterSet
);
```



## Parameters

<dl> <dt>

*pCharacterSet* \[out\]
</dt> <dd>

Pointer to a [**BLOB\_CHARACTER\_SET**](blob-character-set.md) descriptor of the character set.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                                   | Description                                                      |
|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                          | Method succeeded.<br/>                                     |
| <dl> <dt>**E\_POINTER**</dt> </dl>                     | The *pCharacterSet* parameter is not a valid pointer.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                 | Insufficient memory exists to perform the operation.<br/>  |
| <dl> <dt>**E\_FAIL**</dt> </dl>                        | Unspecified error.<br/>                                    |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>                     | This method is not yet implemented.<br/>                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                  | *pCharacterSet* is **NULL**.<br/>                          |
| <dl> <dt>**(HRESULT) ERROR\_INVALID\_DATA**</dt> </dl> | The current character set is invalid or unavailable.<br/>  |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITConferenceBlob**](itconferenceblob.md)
</dt> <dt>

[**BLOB\_CHARACTER\_SET**](blob-character-set.md)
</dt> </dl>

 

 





---
description: The SetConferenceBlob method commits changes to the conference blob. To initialize the conference blob for the first time, use the Init method instead.
ms.assetid: 4a65edb9-77de-42d9-85a1-1e3c41706417
title: ITConferenceBlob::SetConferenceBlob method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITConferenceBlob::SetConferenceBlob method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **SetConferenceBlob** method commits changes to the conference blob. To initialize the conference blob for the first time, use the [**Init**](itconferenceblob-init.md) method instead.

## Syntax


```C++
HRESULT SetConferenceBlob(
  [in] BLOB_CHARACTER_SET CharacterSet,
  [in] BSTR               pBlob
);
```



## Parameters

<dl> <dt>

*CharacterSet* \[in\]
</dt> <dd>

[**BLOB\_CHARACTER\_SET**](blob-character-set.md) descriptor of the conference blob's character set.

</dd> <dt>

*pBlob* \[in\]
</dt> <dd>

Pointer to a **BSTR** containing the conference blob.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *CharacterSet* or *pBlob* parameter is not valid.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>  |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                    |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                   |



 

## Remarks

The application must use [**SysAllocString**](/windows/win32/api/oleauto/nf-oleauto-sysallocstring) to allocate memory for the *pBlob* parameter and use [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) to free the memory when the variable is no longer needed.

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

 


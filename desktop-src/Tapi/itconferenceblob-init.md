---
description: The Init method initializes the conference blob based on a textual string. If pBlob is NULL, default values are used.
ms.assetid: ba492503-90ff-45dd-a39f-6d4451e57339
title: ITConferenceBlob::Init method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITConferenceBlob::Init method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **Init** method initializes the conference blob based on a textual string. If *pBlob* is **NULL**, default values are used.

## Syntax


```C++
HRESULT Init(
  [in] BSTR               pName,
  [in] BLOB_CHARACTER_SET CharacterSet,
  [in] BSTR               pBlob
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

Pointer to a **BSTR** representation of the conference name.

</dd> <dt>

*CharacterSet* \[in\]
</dt> <dd>

[**BLOB\_CHARACTER\_SET**](blob-character-set.md) descriptor of the character set.

</dd> <dt>

*pBlob* \[in\]
</dt> <dd>

Pointer to a **BSTR** containing the conference blob. If **NULL**, the conference blob is initialized with default values. Currently, default conference values are available only if the *CharacterSet* parameter is set to BCS\_ASCII.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                         | Meaning                                                                    |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                               |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *pName*, *CharacterSet*, or *pBlob* parameter is not valid.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>            |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                              |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                             |



 

## Remarks

**ITConferenceBlob::Init** will return a failure if the blob has already been initialized.

The application must use [**SysAllocString**](/windows/win32/api/oleauto/nf-oleauto-sysallocstring) to allocate memory for the *pName* and *pBlob* parameters. The application must use [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) to free the memory when the variables are no longer needed.

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

 


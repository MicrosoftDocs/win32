---
description: The get\_ConferenceBlob method gets a pointer to the textual conference blob currently stored in the conference blob object.
ms.assetid: eb378f84-11bc-4f6e-9133-bc303e07eb53
title: ITConferenceBlob::get_ConferenceBlob method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITConferenceBlob::get\_ConferenceBlob method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_ConferenceBlob** method gets a pointer to the textual conference blob currently stored in the conference blob object.

## Syntax


```C++
HRESULT get_ConferenceBlob(
  [out] BSTR *ppBlob
);
```



## Parameters

<dl> <dt>

*ppBlob* \[out\]
</dt> <dd>

Pointer to a **BSTR** containing the conference blob.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *ppBlob* parameter is not a valid pointer.<br/>       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Remarks

The application must use [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) to free the memory allocated for the *ppBlob* parameter.

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

 


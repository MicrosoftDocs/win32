---
description: The put\_MediaTitle method sets a textual title for the media that the application can use for informational or display purposes. This must be an ASCII convertible string if the character set is ASCII. Otherwise, it can be any BSTR string.
ms.assetid: bbab033b-bd37-4ef6-9e84-1d0b17ecbd4e
title: ITMedia::put_MediaTitle method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITMedia::put\_MediaTitle method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **put\_MediaTitle** method sets a textual title for the media that the application can use for informational or display purposes. This must be an ASCII convertible string if the character set is ASCII. Otherwise, it can be any **BSTR** string.

## Syntax


```C++
HRESULT put_MediaTitle(
  [in] BSTR pMediaTitle
);
```



## Parameters

<dl> <dt>

*pMediaTitle* \[in\]
</dt> <dd>

Pointer to a **BSTR** containing the title of the media.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pMediaTitle* parameter is not a valid pointer.<br/>  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *pMediaTitle* parameter is not valid.<br/>            |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Remarks

The application must use [**SysAllocString**](/windows/win32/api/oleauto/nf-oleauto-sysallocstring) to allocate memory for the *pMediaTitle* parameter and use [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) to free the memory when the variable is no longer needed.

This function may send data over the wire in unencrypted form; therefore, someone eavesdropping on the network may be able to read the data. The security risk of sending the data in clear text should be considered before using this method.

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITMedia**](itmedia.md)
</dt> <dt>

[**ITMedia::get\_MediaTitle**](itmedia-get-mediatitle.md)
</dt> </dl>

 


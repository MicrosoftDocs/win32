---
description: The get\_AddressType method gets the address type.
ms.assetid: b2ff6303-6beb-429c-ad1a-2f729749e5db
title: ITConnection::get_AddressType method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITConnection::get\_AddressType method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_AddressType** method gets the address type.

## Syntax


```C++
HRESULT get_AddressType(
  [out] BSTR *ppAddressType
);
```



## Parameters

<dl> <dt>

*ppAddressType* \[out\]
</dt> <dd>

Pointer to a **BSTR** containing the address type.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                     |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *ppAddressType* parameter is not a valid pointer.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>  |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                    |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                   |



 

## Remarks

The application must use [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) to free the memory allocated for the *ppAddressType* parameter.

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITConnection**](itconnection.md)
</dt> <dt>

[**ITConnection::put\_AddressType**](itconnection-put-addresstype.md)
</dt> </dl>

 


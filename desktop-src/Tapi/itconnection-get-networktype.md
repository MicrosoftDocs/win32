---
description: The get\_NetworkType method gets the network type.
ms.assetid: 5597284a-9cc6-422b-a064-cda25aa5964b
title: ITConnection::get_NetworkType method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITConnection::get\_NetworkType method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_NetworkType** method gets the network type.

## Syntax


```C++
HRESULT get_NetworkType(
  [out] BSTR *ppNetworkType
);
```



## Parameters

<dl> <dt>

*ppNetworkType* \[out\]
</dt> <dd>

Pointer to a **BSTR** containing the network type.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                     |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *ppNetworkType* parameter is not a valid pointer.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>  |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                    |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                   |



 

## Remarks

The application must use [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) to free the memory allocated for the *ppNetworkType* parameter.

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

[**ITConnection::put\_NetworkType**](itconnection-put-networktype.md)
</dt> </dl>

 


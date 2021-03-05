---
description: The SetAddressInfo method sets the address information.
ms.assetid: 100b96af-e6ba-4496-9978-4df133e1c2b5
title: ITConnection::SetAddressInfo method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITConnection::SetAddressInfo method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **SetAddressInfo** method sets the address information.

## Syntax


```C++
HRESULT SetAddressInfo(
  [in] BSTR          pStartAddress,
  [in] LONG          NumAddresses,
  [in] unsigned char Ttl
);
```



## Parameters

<dl> <dt>

*pStartAddress* \[in\]
</dt> <dd>

Pointer to a **BSTR** containing the start address.

</dd> <dt>

*NumAddresses* \[in\]
</dt> <dd>

Number of addresses to be used for the session.

</dd> <dt>

*Ttl* \[in\]
</dt> <dd>

[*time to live*](t-tapgloss.md) (TTL) scope for transmissions on the addresses.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                         | Meaning                                                                          |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *pStartAddress*, *NumAddresses*, or *Ttl* parameter is not valid.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                                    |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                                   |



 

## Remarks

The application must use [**SysAllocString**](/windows/win32/api/oleauto/nf-oleauto-sysallocstring) to allocate memory for the *pStartAddress* parameter and use [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) to free the memory when the variable is no longer needed.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITConnection**](itconnection.md)
</dt> </dl>

 


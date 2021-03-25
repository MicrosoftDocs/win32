---
description: The get\_MachineAddress method gets the machine address of the originating host.
ms.assetid: 8a67cc9f-f9fc-4ec3-86f9-ffe34d075830
title: ITSdp::get_MachineAddress method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITSdp::get\_MachineAddress method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_MachineAddress** method gets the machine address of the originating host.

## Syntax


```C++
HRESULT get_MachineAddress(
  [out] BSTR *ppMachineAddress
);
```



## Parameters

<dl> <dt>

*ppMachineAddress* \[out\]
</dt> <dd>

Pointer to a **BSTR** containing the machine address of the conference host.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                         |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                        |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *ppMachineAddres*s parameter is not a valid pointer.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>     |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                       |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                      |



 

## Remarks

The application must use [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) to free the memory allocated for the *ppMachineAddress* parameter.

The *ppMachineAddress* parameter can be returned as either a DNS name ("JohnSmith.workinghard.microsoft.com") or an IP address ("10.111.222.111").

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITSdp**](itsdp.md)
</dt> <dt>

[**ITSdp::put\_MachineAddress**](itsdp-put-machineaddress.md)
</dt> </dl>

 


---
Description: The put\_MachineAddress method sets the machine address of the originating host.
ms.assetid: f4af55b1-e20b-4fe8-a15e-a1a68d22f1b9
title: ITSdp::put\_MachineAddress method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ITSdp::put\_MachineAddress method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **put\_MachineAddress** method sets the machine address of the originating host.

## Syntax


```C++
);
```



## Parameters

<dl> <dt>

*pMachineAddress* \[in\]
</dt> <dd>

Pointer to a **BSTR** containing the machine address of the conference host.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                        |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                       |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pMachineAddress* parameter is not a valid pointer.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>    |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                      |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                     |



 

## Remarks

The application must use [**SysAllocString**](https://msdn.microsoft.com/en-us/library/ms221458(v=VS.71).aspx) to allocate memory for the *pMachineAddress* parameter and use [**SysFreeString**](https://msdn.microsoft.com/en-us/library/ms221481(v=VS.71).aspx) to free the memory when the variable is no longer needed.

The *pMachineAddress* parameter can be either a DNS name ("JohnSmith.workinghard.microsoft.com") or an IP address ("10.111.222.111").

This function may send data over the wire in unencrypted form; therefore, someone eavesdropping on the network may be able to read the data. The security risk of sending the data in clear text should be considered before using this method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITSdp**](itsdp.md)
</dt> <dt>

[**ITSdp::get\_MachineAddress**](itsdp-get-machineaddress.md)
</dt> </dl>

 

 





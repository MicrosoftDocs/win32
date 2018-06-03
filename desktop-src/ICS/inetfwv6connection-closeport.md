---
title: INetFwV6Connection ClosePort method
description: The ClosePort method modifies the firewall configuration for a connection to disallow inbound connection attempts for the specified port and protocol.
ms.assetid: c6e99869-6090-4c2e-90fb-cb143e746437
keywords:
- ClosePort method ICS/ICF
- ClosePort method ICS/ICF , INetFwV6Connection interface
- INetFwV6Connection interface ICS/ICF , ClosePort method
topic_type:
- apiref
api_name:
- INetFwV6Connection.ClosePort
api_location:
- Netfwv6.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# INetFwV6Connection::ClosePort method

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **ClosePort** method modifies the firewall configuration for a connection to disallow inbound connection attempts for the specified port and protocol. It is not an error to call **ClosePort** for a port and protocol pair that is already closed, even though such a call has no actual effect on the system.

This is a state-changing method, and thus is subject to the access control and confirmation UI mechanisms.

## Syntax


```C++
HRESULT ClosePort(
  [in] USHORT        usPort,
  [in] PORT_PROTOCOL Protocol
);
```



## Parameters

<dl> <dt>

*usPort* \[in\]
</dt> <dd>

Specifies the port ID in host byte order. Must be in the range 1   65535.

</dd> <dt>

*Protocol* \[in\]
</dt> <dd>

Specifies the port protocol type as defined in the [**PORT\_PROTOCOL**](port-protocol.md) enumeration.

</dd> </dl>

## Return value

If the method succeeds the return value is S\_OK.

If the method fails, the return value is one of the following error codes.



| Return code                                                                                   | Description                                                   |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>**E\_ABORT**</dt> </dl>       | The operation was aborted.<br/>                         |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | An unspecified error occurred.<br/>                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | One of the parameters is invalid.<br/>                  |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | A specified interface is not supported.<br/>            |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | A specified method is not implemented.<br/>             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The method was unable to allocate required memory.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A pointer passed as a parameter is not valid.<br/>      |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>  | The method failed for unknown reasons.<br/>             |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | None supported<br/>                                                              |
| End of client support<br/>    | Windows XP with SP1<br/>                                                         |
| Redistributable<br/>          | Advanced Networking Pack for Windows XP<br/>                                     |
| Header<br/>                   | <dl> <dt>Netfwv6.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Netfwv6.dll</dt> </dl> |



## See also

<dl> <dt>

[**INetFwV6Connection**](inetfwv6connection.md)
</dt> </dl>

 

 






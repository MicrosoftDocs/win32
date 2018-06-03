---
title: INetFwV6Connection OpenPorts property
description: Contains the set of port and protocol pairs for which inbound connection attempts are currently allowed at the time of the method call. It has the same semantics as EnumerateOpenPorts.
ms.assetid: 18cd494a-403d-4fc0-bee4-7016a65c43ec
keywords:
- OpenPorts property ICS/ICF
- OpenPorts property ICS/ICF , INetFwV6Connection interface
- INetFwV6Connection interface ICS/ICF , OpenPorts property
topic_type:
- apiref
api_name:
- INetFwV6Connection.OpenPorts
- INetFwV6Connection.get_OpenPorts
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

# INetFwV6Connection::OpenPorts property

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

Contains the set of port and protocol pairs for which inbound connection attempts are currently allowed at the time of the method call. It has the same semantics as [**EnumerateOpenPorts**](inetfwv6connection-enumerateopenports.md).

This property is read-only.

## Syntax


```C++
HRESULT get_OpenPorts(
  [out] INetFwV6OpenPortsCollection **pCollection
);
```



## Property value

Collection of open ports for this connection in host order.

## Error codes

If the method succeeds the return value is S\_OK.

If the method fails, the return value is one of the following error codes.



| Name                                                                                      | Meaning                                                       |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>E\_ABORT</dt> </dl>       | The operation was aborted.<br/>                         |
| <dl> <dt>E\_FAIL</dt> </dl>        | An unspecified error occurred.<br/>                     |
| <dl> <dt>E\_INVALIDARG</dt> </dl>  | The parameter is invalid.<br/>                          |
| <dl> <dt>E\_NOINTERFACE</dt> </dl> | A specified interface is not supported.<br/>            |
| <dl> <dt>E\_NOTIMPL</dt> </dl>     | A specified method is not implemented.<br/>             |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl> | The method was unable to allocate required memory.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>     | A pointer passed as a parameter is not valid.<br/>      |
| <dl> <dt>E\_UNEXPECTED</dt> </dl>  | The method failed for unknown reasons.<br/>             |



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

[INetFwV6Connection](https://msdn.microsoft.com/library/windows/desktop/aa365570)
</dt> <dt>

[**INetFwV6Connection**](inetfwv6connection.md)
</dt> </dl>

 

 






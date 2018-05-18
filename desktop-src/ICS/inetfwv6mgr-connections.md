---
title: INetFwV6Mgr Connections property
description: Specifies a scripting collection of the IPv6 connections present in the system at the time of the method call. It has the same semantics as EnumerateConnections.
ms.assetid: '5c31ea81-abeb-4b0e-b254-46179daa87cd'
keywords: ["Connections property ICS/ICF", "Connections property ICS/ICF , INetFwV6Mgr interface", "INetFwV6Mgr interface ICS/ICF , Connections property"]
topic_type:
- apiref
api_name:
- INetFwV6Mgr.Connections
- INetFwV6Mgr.get_Connections
api_location:
- Netfwv6.dll
api_type:
- COM
---

# INetFwV6Mgr::Connections property

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

Specifies a scripting collection of the IPv6 connections present in the system at the time of the method call. It has the same semantics as [**EnumerateConnections**](inetfwv6mgr-enumerateconnections.md).

This property is read-only.

## Syntax


```C++
HRESULT get_Connections(
  [out] INetFwV6ConnectionCollection **pCollection
);
```



## Property value

Pointer to collection of IPv6 connections.

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
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | None supported<br/>                                                              |
| End of client support<br/>    | Windows XP with SP1<br/>                                                         |
| Redistributable<br/>          | Advanced Networking Pack for Windows XP<br/>                                     |
| Header<br/>                   | <dl> <dt>Netfwv6.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Netfwv6.dll</dt> </dl> |



## See also

<dl> <dt>

[INetFwV6Mgr](https://msdn.microsoft.com/library/windows/desktop/aa365874)
</dt> <dt>

[**INetFwV6Mgr::EnumerateConnections**](inetfwv6mgr-enumerateconnections.md)
</dt> </dl>

 

 






---
title: INetFwV6Mgr GloballyOpenPorts property
description: Specifies the set of port and protocol pairs for which inbound connection attempts are currently allowed at the time of the method call.
ms.assetid: 50a8e41d-241f-4741-8004-a64a4e097f6d
keywords:
- GloballyOpenPorts property ICS/ICF
- GloballyOpenPorts property ICS/ICF , INetFwV6Mgr interface
- INetFwV6Mgr interface ICS/ICF , GloballyOpenPorts property
topic_type:
- apiref
api_name:
- INetFwV6Mgr.GloballyOpenPorts
- INetFwV6Mgr.get_GloballyOpenPorts
api_location:
- Netfwv6.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INetFwV6Mgr::GloballyOpenPorts property

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

Specifies the set of port and protocol pairs for which inbound connection attempts are currently allowed at the time of the method call.

This property is read-only.

## Syntax


```C++
HRESULT get_GloballyOpenPorts(
  [out] INetFwV6PortsCollection **pCollection
);
```



## Property value

References the collection.

## Error codes

If the method succeeds the return value is S\_OK.

If the method fails, the return value is one of the following error codes.



| Name                                                                                      | Meaning                                                      |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>E\_ABORT</dt> </dl>       | The operation was aborted.<br/>                        |
| <dl> <dt>E\_FAIL</dt> </dl>        | An unspecified error occurred.<br/>                    |
| <dl> <dt>E\_INVALIDARG</dt> </dl>  | One of the parameters is invalid.<br/>                 |
| <dl> <dt>E\_NOINTERFACE</dt> </dl> | A specified interface is not supported.<br/>           |
| <dl> <dt>E\_NOTIMPL</dt> </dl>     | A specified method is not implemented.<br/>            |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl> | The method is unable to allocate required memory.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>     | A pointer passed as a parameter is not valid.<br/>     |
| <dl> <dt>E\_UNEXPECTED</dt> </dl>  | The method failed for unknown reasons.<br/>            |



## Remarks

This interface has the same semantics as [**EnumerateGloballyOpenPorts**](inetfwv6mgr-enumerategloballyopenports.md)

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

[INetFwV6Mgr](https://msdn.microsoft.com/library/windows/desktop/aa365874)
</dt> <dt>


</dt> <dt>

[**INetFwV6Mgr**](inetfwv6mgr.md)
</dt> </dl>

 

 






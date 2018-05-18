---
title: INetFwV6OpenPort Protocol property
description: Returns the protocol for this port and protocol pair.
ms.assetid: '20ce24b1-11cd-48db-80d8-61882dcf5f05'
keywords: ["Protocol property ICS/ICF", "Protocol property ICS/ICF , INetFwV6OpenPort interface", "INetFwV6OpenPort interface ICS/ICF , Protocol property"]
topic_type:
- apiref
api_name:
- INetFwV6OpenPort.Protocol
- INetFwV6OpenPort.get_Protocol
api_location:
- Netfwv6.dll
api_type:
- COM
---

# INetFwV6OpenPort::Protocol property

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

Returns the protocol for this port and protocol pair.

This property is read-only.

## Syntax


```C++
HRESULT get_Protocol(
  [out] PORT_PROTOCOL *pProtocol
);
```



## Property value

The protocol for this pair.

## Error codes

If the method succeeds, the return value is S\_OK.

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

[INetFwV6OpenPort](https://msdn.microsoft.com/library/windows/desktop/aa365921)
</dt> <dt>

[**INetFwV6OpenPort**](inetfwv6openport.md)
</dt> </dl>

 

 






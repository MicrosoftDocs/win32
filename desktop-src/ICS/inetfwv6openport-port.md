---
title: INetFwV6Connection Port property
description: Returns the host-order port for this port and protocol pair.
ms.assetid: d886b0f1-4532-4a18-bed9-e18e6f23fae9
keywords:
- Port property ICS/ICF
- Port property ICS/ICF , INetFwV6Connection interface
- INetFwV6Connection interface ICS/ICF , Port property
topic_type:
- apiref
api_name:
- INetFwV6Connection.Port
- INetFwV6Connection.get_Port
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

# INetFwV6Connection::Port property

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

Returns the host-order port for this port and protocol pair.

This property is read-only.

## Syntax


```C++
HRESULT get_Port(
  [out] USHORT *usPort
);
```



## Property value

The port for this pair.

## Error codes

If the method succeeds, the return value is S\_OK.

If the method fails, the return value is one of the following error codes.



| Name                                                                                      | Meaning                                                       |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>E\_ABORT</dt> </dl>       | The operation was stopped.<br/>                         |
| <dl> <dt>E\_FAIL</dt> </dl>        | An unspecified error occurred.<br/>                     |
| <dl> <dt>E\_INVALIDARG</dt> </dl>  | The parameter is not valid.<br/>                        |
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

[**INetFwV6OpenPort**](inetfwv6openport.md)
</dt> </dl>

 

 






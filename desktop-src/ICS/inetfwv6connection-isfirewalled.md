---
title: INetFwV6Connection IsFirewalled property
description: Indicates whether the connection is currently firewalled.
ms.assetid: 4b900770-abef-474e-a0c9-6072b567b960
keywords:
- IsFirewalled property ICS/ICF
- IsFirewalled property ICS/ICF , INetFwV6Connection interface
- INetFwV6Connection interface ICS/ICF , IsFirewalled property
topic_type:
- apiref
api_name:
- INetFwV6Connection.IsFirewalled
- INetFwV6Connection.get_IsFirewalled
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

# INetFwV6Connection::IsFirewalled property

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

Indicates whether the connection is currently firewalled.

This property is read-only.

## Syntax


```C++
HRESULT get_IsFirewalled(
  [out] VARIANT_BOOL *pvbFirewalled
);
```



## Property value

Specifies whether the firewall is enabled.

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

 

 






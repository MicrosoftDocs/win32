---
title: INetFwV6Connection DisableFirewall method
description: The DisableFirewall method deactivates the IPv6 Firewall on this connection.
ms.assetid: '48640062-dce9-436c-b7fa-f0c70b4f7454'
keywords: ["DisableFirewall method ICS/ICF", "DisableFirewall method ICS/ICF , INetFwV6Connection interface", "INetFwV6Connection interface ICS/ICF , DisableFirewall method"]
topic_type:
- apiref
api_name:
- INetFwV6Connection.DisableFirewall
api_location:
- Netfwv6.dll
api_type:
- COM
---

# INetFwV6Connection::DisableFirewall method

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **DisableFirewall** method deactivates the IPv6 Firewall on this connection.

## Syntax


```C++
HRESULT DisableFirewall();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds the return value is S\_OK.

If the method fails, the return value is one of the following error codes.



| Return code                                                                                   | Description                                                   |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>**E\_ABORT**</dt> </dl>       | The operation was aborted.<br/>                         |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | An unspecified error occurred.<br/>                     |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | A specified interface is not supported.<br/>            |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | A specified method is not implemented.<br/>             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The method was unable to allocate required memory.<br/> |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>  | The method failed for unknown reasons.<br/>             |



 

## Remarks

It is not an error to call this method on a connection that is not currently firewalled, even though such a call has no actual effect on the system.

This is a state-changing method, and thus is subject to the access control and confirmation UI mechanisms.

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

[**INetFwV6Connection**](inetfwv6connection.md)
</dt> </dl>

 

 






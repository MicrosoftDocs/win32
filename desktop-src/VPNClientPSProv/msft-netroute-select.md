---
title: Select method of the MSFT\_NetRoute class
description: Selects the best local IP address and best route to reach the specified remote address.
audience: developer
ms.assetid: '4f3b3200-123c-4d7a-a1cf-86e328c397f4'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Select method", "Select method, MSFT_NetRoute class", "MSFT_NetRoute class, Select method"]
---

# Select method of the MSFT\_NetRoute class

Selects the best local IP address and best route to reach the specified remote address.

## Syntax


```mof
uint32 Select(
  [in]  uint32             InterfaceIndex,
  [in]  string             LocalIPAddress,
  [in]  string             RemoteIPAddress,
  [out] CIM_ManagedElement CmdletOutput[]
);
```



## Parameters

<dl> <dt>

*InterfaceIndex* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*LocalIPAddress* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*RemoteIPAddress* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*CmdletOutput* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetRoute**](msft-netroute.md)
</dt> </dl>

 

 






---
title: Reset method of the MSFT\_NetRoute class
description: Selects the best local IP address and best route to reach the specified remote address.
audience: developer
ms.assetid: 'c43af97c-52c7-42b1-8fc1-a23cbd77d3e8'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Reset method", "Reset method, MSFT_NetRoute class", "MSFT_NetRoute class, Reset method"]
topic_type:
- apiref
api_name:
- MSFT_NetRoute.Reset
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
---

# Reset method of the MSFT\_NetRoute class

Selects the best local IP address and best route to reach the specified remote address.

## Syntax


```mof
uint32 Reset(
  [in]  uint23        InterfaceIndex,
  [in]  string        LocalIPAddress,
  [in]  string        RemoteIPAddress,
  [out] MSFT_NetRoute CmdletOutput
);
```



## Parameters

<dl> <dt>

*InterfaceIndex* \[in\]
</dt> <dd>

The user-friendly interface index.

</dd> <dt>

*LocalIPAddress* \[in\]
</dt> <dd>

The local IP address of the route.

</dd> <dt>

*RemoteIPAddress* \[in\]
</dt> <dd>

The remote address of the route.

</dd> <dt>

*CmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object.

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

[**MSFT\_NetRoute**](msft-netroute-vpnclientpsprovider.md)
</dt> </dl>

 

 






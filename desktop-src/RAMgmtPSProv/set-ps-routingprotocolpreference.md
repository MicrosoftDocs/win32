---
title: Set method of the PS\_RoutingProtocolPreference class
description: Updates the preference level of the specified routing protocol.
audience: developer
ms.assetid: 457fe8ff-4523-4002-9c17-be6da4ba1232
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_RoutingProtocolPreference class
- PS_RoutingProtocolPreference class, Set method
topic_type:
- apiref
api_name:
- PS_RoutingProtocolPreference.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_RoutingProtocolPreference class

Updates the preference level of the specified routing protocol.

## Syntax


```mof
uint32 Set(
  [in]  string             Name,
  [in]  uint32             Level,
  [in]  boolean            PassThru,
  [out] ProtocolPreference cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The protocol name for the routing preference to update. You can set this parameter to one of the following values. The default value is static.

-   autostatic
-   local
-   netmgmt
-   nondod
-   BGP
-   rip
-   static

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The preference level of the routing protocol.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether the *cmdletOutput* parameter returns an object. **True** to return an object; otherwise **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**ProtocolPreference**](protocolpreference.md) object that receives the updated routing protocol preference.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RoutingProtocolPreference**](ps-routingprotocolpreference.md)
</dt> </dl>

 

 






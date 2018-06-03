---
title: Remove method of the PS\_VpnConnectionTriggerApplication class
description: Removes auto-trigger applications from a VPN connection profile.
audience: developer
ms.assetid: A46F35FE-67CB-42E4-BA3B-737305A0D31B
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_VpnConnectionTriggerApplication class
- PS_VpnConnectionTriggerApplication class, Remove method
topic_type:
- apiref
api_name:
- PS_VpnConnectionTriggerApplication.Remove
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_VpnConnectionTriggerApplication class

Removes auto-trigger applications from a VPN connection profile.

## Syntax


```mof
uint32 Remove(
  [in]  string                          ConnectionName,
  [in]  string                          ApplicationID[],
  [in]  boolean                         PassThru,
  [in]  boolean                         Force,
  [out] VpnConnectionTriggerApplication cmdletOutput
);
```



## Parameters

<dl> <dt>

*ConnectionName* \[in\]
</dt> <dd>

The name of the VPN connection profile to modify.

</dd> <dt>

*ApplicationID* \[in\]
</dt> <dd>

The identifiers of the applications to remove.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the [**VpnConnectionTriggerApplication**](vpnconnectiontriggerapplication.md) object that contains the trigger application settings; otherwise **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** to force the removal of the applications from the VPN profile; otherwise, **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**VpnConnectionTriggerApplication**](vpnconnectiontriggerapplication.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnConnectionTriggerApplication**](ps-vpnconnectiontriggerapplication.md)
</dt> </dl>

 

 






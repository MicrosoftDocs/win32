---
title: Add method of the PS\_VpnConnectionTriggerApplication class
description: Adds auto-trigger applications to a VPN connection profile. These applications, when launched, trigger a VPN connection.
audience: developer
ms.assetid: '47794659-6EC9-4375-A86F-BB385DCAD561'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Add method", "Add method, PS_VpnConnectionTriggerApplication class", "PS_VpnConnectionTriggerApplication class, Add method"]
topic_type:
- apiref
api_name:
- PS_VpnConnectionTriggerApplication.Add
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
---

# Add method of the PS\_VpnConnectionTriggerApplication class

Adds auto-trigger applications to a VPN connection profile. These applications, when launched, trigger a VPN connection.

## Syntax


```mof
uint32 Add(
  [in]  string                          ConnectionName,
  [in]  string                          ApplicationID[],
  [in]  boolean                         PassThru,
  [in]  boolean                         Force,
  [out] VpnConnectionTriggerApplication cmdletOutput
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

The identifiers of the applications to add.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the [**VpnConnectionTriggerApplication**](vpnconnectiontriggerapplication.md) object that contains the trigger application settings; otherwise **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** to force the addition of the application to the VPN profile; otherwise, **false**.

**Windows 8 and Windows Server 2012:** This parameter is not available until Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**VpnConnectionTriggerApplication**](vpnconnectiontriggerapplication.md) object. The **ApplicationID** field is populated.

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

[**PS\_VpnConnectionTriggerApplication**](ps-vpnconnectiontriggerapplication.md)
</dt> </dl>

 

 






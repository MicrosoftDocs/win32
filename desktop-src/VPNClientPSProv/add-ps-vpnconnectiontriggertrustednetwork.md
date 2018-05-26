---
title: Add method of the PS\_VpnConnectionTriggerTrustedNetwork class
description: Adds DNS suffixes to the trusted network list of the VPN connection profile.
audience: developer
ms.assetid: 71B4F04D-1B88-433D-BBB1-870D4781F70D
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_VpnConnectionTriggerTrustedNetwork class
- PS_VpnConnectionTriggerTrustedNetwork class, Add method
topic_type:
- apiref
api_name:
- PS_VpnConnectionTriggerTrustedNetwork.Add
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_VpnConnectionTriggerTrustedNetwork class

Adds DNS suffixes to the trusted network list of the VPN connection profile.

## Syntax


```mof
uint32 Add(
  [in]  string                             ConnectionName,
  [in]  string                             DnsSuffix[],
  [in]  boolean                            PassThru,
  [in]  boolean                            Force,
  [out] VpnConnectionTriggerTrustedNetwork cmdletOutput
);
```



## Parameters

<dl> <dt>

*ConnectionName* \[in\]
</dt> <dd>

The name of the VPN connection profile to modify.

</dd> <dt>

*DnsSuffix* \[in\]
</dt> <dd>

The list of DNS suffixes to add.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the [**VpnConnectionTriggerTrustedNetwork**](vpnconnectiontriggertrustednetwork.md) object that contains the trusted network list; otherwise **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** to force the addition of the DNS suffixes to the trusted network list; otherwise, **false**.

**Windows 8 and Windows Server 2012:** This parameter is not available until Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**VpnConnectionTriggerTrustedNetwork**](vpnconnectiontriggertrustednetwork.md) object that holds the trusted network list.

</dd> </dl>

## Remarks

When a trusted suffix is present on the client's physical interface, VPN auto-trigger is suppressed.

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

[**PS\_VpnConnectionTriggerTrustedNetwork**](ps-vpnconnectiontriggertrustednetwork.md)
</dt> </dl>

 

 






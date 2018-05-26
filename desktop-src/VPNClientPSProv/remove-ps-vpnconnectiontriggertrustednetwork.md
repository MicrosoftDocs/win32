---
title: Remove method of the PS\_VpnConnectionTriggerTrustedNetwork class
description: Removes DNS suffixes from the trusted network list of the VPN connection profile.
audience: developer
ms.assetid: 7ECAF198-384B-440F-9E5A-F005172D0C90
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_VpnConnectionTriggerTrustedNetwork class
- PS_VpnConnectionTriggerTrustedNetwork class, Remove method
topic_type:
- apiref
api_name:
- PS_VpnConnectionTriggerTrustedNetwork.Remove
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_VpnConnectionTriggerTrustedNetwork class

Removes DNS suffixes from the trusted network list of the VPN connection profile.

## Syntax


```mof
uint32 Remove(
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

The list of DNS suffixes to remove.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the [**VpnConnectionTriggerTrustedNetwork**](vpnconnectiontriggertrustednetwork.md) object that contains the trusted network list; otherwise **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** to force the removal of the DNS suffixes from the trusted network list; otherwise, **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**VpnConnectionTriggerTrustedNetwork**](vpnconnectiontriggertrustednetwork.md) object that holds the trusted network list.

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

[**PS\_VpnConnectionTriggerTrustedNetwork**](ps-vpnconnectiontriggertrustednetwork.md)
</dt> </dl>

 

 






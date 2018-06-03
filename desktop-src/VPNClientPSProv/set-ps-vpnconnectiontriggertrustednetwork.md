---
title: Set method of the PS\_VpnConnectionTriggerTrustedNetwork class
description: Sets the trusted network list with the Name Resolution Policy Table (NRPT) DNS suffixes that have been configured as part of triggering properties. The NRPT exemption entries are ignored.
audience: developer
ms.assetid: 0104FE64-294B-4C1A-99B0-8CAA8ACE5C59
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_VpnConnectionTriggerTrustedNetwork class
- PS_VpnConnectionTriggerTrustedNetwork class, Set method
topic_type:
- apiref
api_name:
- PS_VpnConnectionTriggerTrustedNetwork.Set
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_VpnConnectionTriggerTrustedNetwork class

Sets the trusted network list with the Name Resolution Policy Table (NRPT) DNS suffixes that have been configured as part of triggering properties. The NRPT exemption entries are ignored.

## Syntax


```mof
uint32 Set(
  [in]  string                             ConnectionName,
  [in]  boolean                            DefaultDnsSuffixes,
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

*DefaultDnsSuffixes* \[in\]
</dt> <dd>

**True** to copy all DNS suffixes in the [**VpnConnectionTriggerDnsConfiguration**](vpnconnectiontriggerdnsconfiguration.md) object into the DNS suffixes for [**VpnConnectionTriggerTrustedNetwork**](vpnconnectiontriggertrustednetwork.md); otherwise, **false**. Note that DNS suffixes without corresponding DNS servers will not be copied

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the [**VpnConnectionTriggerTrustedNetwork**](vpnconnectiontriggertrustednetwork.md) object that contains the trusted network list; otherwise **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** to replace the trusted network list with the DNS suffixes present in [**VpnConnectionTriggerDnsConfiguration**](vpnconnectiontriggerdnsconfiguration.md); otherwise, **false**. Note that only DNS suffixes with corresponding DNS server addresses are copied from **VpnConnectionTriggerDnsConfiguration**.

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

 

 






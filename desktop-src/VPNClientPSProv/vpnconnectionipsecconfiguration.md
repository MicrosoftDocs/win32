---
title: VpnConnectionIPsecConfiguration class
description: The VpnConnectionIPsecConfiguration class represents the IPsec configuration for a VPN connection.
audience: developer
ms.assetid: B993E97E-0E8F-42A6-8A0E-6794D1D90D88
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- VpnConnectionIPsecConfiguration class
- VpnConnectionIPsecConfiguration class, described
topic_type:
- apiref
api_name:
- VpnConnectionIPsecConfiguration
- VpnConnectionIPsecConfiguration.EncryptionMethod
- VpnConnectionIPsecConfiguration.IntegrityCheckMethod
- VpnConnectionIPsecConfiguration.CipherTransformConstants
- VpnConnectionIPsecConfiguration.DHGroup
- VpnConnectionIPsecConfiguration.AuthenticationTransformConstants
- VpnConnectionIPsecConfiguration.PfsGroup
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# VpnConnectionIPsecConfiguration class

The **VpnConnectionIPsecConfiguration** class represents the IPsec configuration for a VPN connection.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class VpnConnectionIPsecConfiguration
{
  uint32 EncryptionMethod;
  uint32 IntegrityCheckMethod;
  uint32 CipherTransformConstants;
  uint32 DHGroup;
  uint32 AuthenticationTransformConstants;
  uint32 PfsGroup;
};
```

## Members

The **VpnConnectionIPsecConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnConnectionIPsecConfiguration** class has these properties.

<dl> <dt>

**AuthenticationTransformConstants**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The authentication transform plumbed in IPsec policy.

</dd> <dt>

**CipherTransformConstants**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The cipher transform plumbed in IPsec policy.

</dd> <dt>

**DHGroup**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The DH group plumbed in IPsec policy.

</dd> <dt>

**EncryptionMethod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The encryption method plumbed in IKE policy.

</dd> <dt>

**IntegrityCheckMethod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The integrity method plumbed in IPsec policy.

</dd> <dt>

**PfsGroup**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The PFS group plumbed in IPsec policy.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



 

 






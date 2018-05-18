---
title: VpnServerIPsecCustomConfiguration class
description: Represents the VPN server custom IPsec configuration.
audience: developer
ms.assetid: '1241ec69-1581-4ccc-b4d2-31088e077309'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["VpnServerIPsecCustomConfiguration class", "VpnServerIPsecCustomConfiguration class, described"]
topic_type:
- apiref
api_name:
- VpnServerIPsecCustomConfiguration
- VpnServerIPsecCustomConfiguration.IdleDisconnect
- VpnServerIPsecCustomConfiguration.SALifeTime
- VpnServerIPsecCustomConfiguration.MMSALifeTime
- VpnServerIPsecCustomConfiguration.SADataSizeForRenegotiation
- VpnServerIPsecCustomConfiguration.Ikev2Ports
- VpnServerIPsecCustomConfiguration.L2tpPorts
- VpnServerIPsecCustomConfiguration.SstpPorts
- VpnServerIPsecCustomConfiguration.GrePorts
- VpnServerIPsecCustomConfiguration.TunnelType
- VpnServerIPsecCustomConfiguration.CustomPolicy
- VpnServerIPsecCustomConfiguration.EncryptionMethod
- VpnServerIPsecCustomConfiguration.IntegrityCheckMethod
- VpnServerIPsecCustomConfiguration.CipherTransformConstants
- VpnServerIPsecCustomConfiguration.PfsGroup
- VpnServerIPsecCustomConfiguration.AuthenticationTransformConstants
- VpnServerIPsecCustomConfiguration.DHGroup
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# VpnServerIPsecCustomConfiguration class

Represents the VPN server custom IPsec configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VpnServerIPsecCustomConfiguration : VpnServerIPsecConfiguration
{
  uint32  IdleDisconnect;
  uint32  SALifeTime;
  uint32  MMSALifeTime;
  uint32  SADataSizeForRenegotiation;
  uint32  Ikev2Ports;
  uint32  L2tpPorts;
  uint32  SstpPorts;
  uint32  GrePorts;
  uint32  TunnelType;
  boolean CustomPolicy;
  uint32  EncryptionMethod;
  uint32  IntegrityCheckMethod;
  uint32  CipherTransformConstants;
  uint32  PfsGroup;
  uint32  AuthenticationTransformConstants;
  uint32  DHGroup;
};
```

## Members

The **VpnServerIPsecCustomConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnServerIPsecCustomConfiguration** class has these properties.

<dl> <dt>

**AuthenticationTransformConstants**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Authentication transform plumbed in IPsec policy

</dd> <dt>

**CipherTransformConstants**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Cipher plumbed in IPsec policy

</dd> <dt>

**CustomPolicy**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Custom IKE and IPSEC policies, must be a separate parameter set

</dd> <dt>

**DHGroup**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

DH Group Plumbed in IPsec policy

</dd> <dt>

**EncryptionMethod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Encryption method plumbed in IKE policy

</dd> <dt>

**GrePorts**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of GRE ports created

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

This property is inherited from [**VpnServerIPsecConfiguration**](vpnserveripsecconfiguration.md).

</dd> <dt>

**IdleDisconnect**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The duration, in seconds, after which an idle connection is terminated

Unless the idle time-out is disabled, the entire connection is terminated if the connection is idle for the specified interval.

This property is inherited from [**VpnServerIPsecConfiguration**](vpnserveripsecconfiguration.md).

</dd> <dt>

**Ikev2Ports**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of IKEv2 ports created

This property is inherited from [**VpnServerIPsecConfiguration**](vpnserveripsecconfiguration.md).

</dd> <dt>

**IntegrityCheckMethod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Integrity method plumbed in IPsec policy

</dd> <dt>

**L2tpPorts**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of L2TP ports created

This property is inherited from [**VpnServerIPsecConfiguration**](vpnserveripsecconfiguration.md).

</dd> <dt>

**MMSALifeTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lifetime of main mode security association (SA) in seconds, after which the MM SA is no longer valid

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

This property is inherited from [**VpnServerIPsecConfiguration**](vpnserveripsecconfiguration.md).

</dd> <dt>

**PfsGroup**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

PFS Group plumbed in IPsec policy

</dd> <dt>

**SADataSizeForRenegotiation**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of kilobytes that can be transferred using a SA before the SA will be renegotiated

This property is inherited from [**VpnServerIPsecConfiguration**](vpnserveripsecconfiguration.md).

</dd> <dt>

**SALifeTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lifetime of a security association (SA), after which the SA is no longer valid, in seconds

This property is inherited from [**VpnServerIPsecConfiguration**](vpnserveripsecconfiguration.md).

</dd> <dt>

**SstpPorts**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of SSTP ports created

**Windows Server 2012:** This property is not supported before Windows Server 2012 R2.

This property is inherited from [**VpnServerIPsecConfiguration**](vpnserveripsecconfiguration.md).

</dd> <dt>

**TunnelType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The tunnel type to apply to custom policy

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

This property is inherited from [**VpnServerIPsecConfiguration**](vpnserveripsecconfiguration.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 






---
title: VpnServerIPsecDefaultConfiguration class
description: Represents the VPN server default IPsec configuration.
audience: developer
ms.assetid: 2429fa71-87bb-46a2-9df4-e3b3d0af1005
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- VpnServerIPsecDefaultConfiguration class
- VpnServerIPsecDefaultConfiguration class, described
topic_type:
- apiref
api_name:
- VpnServerIPsecDefaultConfiguration
- VpnServerIPsecDefaultConfiguration.IdleDisconnect
- VpnServerIPsecDefaultConfiguration.SALifeTime
- VpnServerIPsecDefaultConfiguration.MMSALifeTime
- VpnServerIPsecDefaultConfiguration.SADataSizeForRenegotiation
- VpnServerIPsecDefaultConfiguration.Ikev2Ports
- VpnServerIPsecDefaultConfiguration.L2tpPorts
- VpnServerIPsecDefaultConfiguration.SstpPorts
- VpnServerIPsecDefaultConfiguration.GrePorts
- VpnServerIPsecDefaultConfiguration.TunnelType
- VpnServerIPsecDefaultConfiguration.EncryptionType
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# VpnServerIPsecDefaultConfiguration class

Represents the VPN server default IPsec configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VpnServerIPsecDefaultConfiguration : VpnServerIPsecConfiguration
{
  uint32 IdleDisconnect;
  uint32 SALifeTime;
  uint32 MMSALifeTime;
  uint32 SADataSizeForRenegotiation;
  uint32 Ikev2Ports;
  uint32 L2tpPorts;
  uint32 SstpPorts;
  uint32 GrePorts;
  uint32 TunnelType;
  string EncryptionType;
};
```

## Members

The **VpnServerIPsecDefaultConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnServerIPsecDefaultConfiguration** class has these properties.

<dl> <dt>

**EncryptionType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the type of encryption.

The possible values are.

<dt>

<span id="NoEncryption"></span><span id="noencryption"></span><span id="NOENCRYPTION"></span>

**NoEncryption** ("NoEncryption")


</dt> <dd></dd> <dt>

<span id="RequireEncryption"></span><span id="requireencryption"></span><span id="REQUIREENCRYPTION"></span>

**RequireEncryption** ("RequireEncryption")


</dt> <dd></dd> <dt>

<span id="OptionalEncryption"></span><span id="optionalencryption"></span><span id="OPTIONALENCRYPTION"></span>

**OptionalEncryption** ("OptionalEncryption")


</dt> <dd></dd> <dt>

<span id="MaximumEncryption"></span><span id="maximumencryption"></span><span id="MAXIMUMENCRYPTION"></span>

**MaximumEncryption** ("MaximumEncryption")


</dt> <dd></dd> </dl>

</dd> <dt>

**GrePorts**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of GRE ports created

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

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

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

This property is inherited from [**VpnServerIPsecConfiguration**](vpnserveripsecconfiguration.md).

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

**Windows Server 2012:** This property is not supported before Windows Server 2012 R2.

This property is inherited from [**VpnServerIPsecConfiguration**](vpnserveripsecconfiguration.md).

</dd> <dt>

**TunnelType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The tunnel type to apply to custom policy

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

This property is inherited from [**VpnServerIPsecConfiguration**](vpnserveripsecconfiguration.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 






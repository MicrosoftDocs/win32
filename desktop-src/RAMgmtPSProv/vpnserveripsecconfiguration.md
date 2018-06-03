---
title: VpnServerIPsecConfiguration class
description: Represents a VPN server Internet Protocol Security (IPsec) configuration.
audience: developer
ms.assetid: 3cee426d-87f3-4ac9-88d7-f94bc375825b
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- VpnServerIPsecConfiguration class
- VpnServerIPsecConfiguration class, described
topic_type:
- apiref
api_name:
- VpnServerIPsecConfiguration
- VpnServerIPsecConfiguration.IdleDisconnect
- VpnServerIPsecConfiguration.SALifeTime
- VpnServerIPsecConfiguration.MMSALifeTime
- VpnServerIPsecConfiguration.SADataSizeForRenegotiation
- VpnServerIPsecConfiguration.Ikev2Ports
- VpnServerIPsecConfiguration.L2tpPorts
- VpnServerIPsecConfiguration.SstpPorts
- VpnServerIPsecConfiguration.GrePorts
- VpnServerIPsecConfiguration.TunnelType
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VpnServerIPsecConfiguration class

Represents a VPN server Internet Protocol Security (IPsec) configuration

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VpnServerIPsecConfiguration
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
};
```

## Members

The **VpnServerIPsecConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnServerIPsecConfiguration** class has these properties.

<dl> <dt>

**GrePorts**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of GRE ports created

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

</dd> <dt>

**IdleDisconnect**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The duration, in seconds, after which an idle connection is terminated

Unless the idle time-out is disabled, the entire connection is terminated if the connection is idle for the specified interval.

</dd> <dt>

**Ikev2Ports**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of IKEv2 ports created

</dd> <dt>

**L2tpPorts**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of L2TP ports created

</dd> <dt>

**MMSALifeTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lifetime of main mode security association (SA) in seconds, after which the MM SA is no longer valid

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

</dd> <dt>

**SADataSizeForRenegotiation**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of kilobytes that can be transferred using a SA before the SA will be renegotiated

</dd> <dt>

**SALifeTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lifetime of a security association (SA), after which the SA is no longer valid, in seconds

</dd> <dt>

**SstpPorts**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of SSTP ports created

**Windows Server 2012:** This property is not supported before Windows Server 2012 R2.

</dd> <dt>

**TunnelType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The tunnel type to apply to custom policy

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 






---
title: VpnTrafficSelector class
description: Describes the VPN traffic selector.
audience: developer
ms.assetid: 'F32347C5-BEF2-470F-AAC1-94E09DCB244E'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["VpnTrafficSelector class", "VpnTrafficSelector class, described"]
topic_type:
- apiref
api_name:
- VpnTrafficSelector
- VpnTrafficSelector.ProtocolId
- VpnTrafficSelector.IPAddressRange
- VpnTrafficSelector.PortRange
- VpnTrafficSelector.TsPayloadId
- VpnTrafficSelector.Type
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# VpnTrafficSelector class

Describes the VPN traffic selector

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VpnTrafficSelector
{
  uint32 ProtocolId;
  string IPAddressRange[];
  uint32 PortRange[];
  uint16 TsPayloadId;
  uint32 Type;
};
```

## Members

The **VpnTrafficSelector** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnTrafficSelector** class has these properties.

<dl> <dt>

**IPAddressRange**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address range for traffic selectors

</dd> <dt>

**PortRange**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port range of traffic selectors

</dd> <dt>

**ProtocolId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The protocol ID for traffic selectors

</dd> <dt>

**TsPayloadId**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The payload ID

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address family, IPv4 or IPv6

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 






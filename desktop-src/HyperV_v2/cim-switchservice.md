---
description: Represents a switch service.
ms.assetid: cf6319fa-7d69-4820-b0e0-775aad8b190c
title: CIM_SwitchService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_SwitchService
- CIM_SwitchService.BridgeAddress
- CIM_SwitchService.NumPorts
- CIM_SwitchService.BridgeType
- CIM_SwitchService.BridgeAddressType
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_SwitchService class

Represents a switch service.

## Syntax

``` syntax
[Abstract, Version("2.7.0"), UMLPackagePath("CIM::Network::SwitchingBridging")]
class CIM_SwitchService : CIM_ForwardingService
{
  string BridgeAddress;
  uint16 NumPorts;
  uint8  BridgeType;
  uint16 BridgeAddressType;
};
```

## Members

The **CIM\_SwitchService** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SwitchService** class has these properties.

<dl> <dt>

**BridgeAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (32), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIB.IETF\|BRIDGE-MIB.dot1dBaseBridgeAddress"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_SwitchService**.**BridgeAddressType**")
</dt> </dl>

The address of the switch service, which is a portion of the unique identifier of the service.

</dd> <dt>

**BridgeAddressType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_SwitchService**.**BridgeAddress**")
</dt> </dl>

The addressing format used for the bridge and the **BridgeAddress** property.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span>

**IPv4** (2)


</dt> <dd></dd> <dt>

<span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span>

**IPv6** (3)


</dt> <dd></dd> <dt>

<span id="MAC"></span><span id="mac"></span>

**MAC** (4)


</dt> <dd></dd> <dt>

<span id="MAC___Spanning_Tree_Priority"></span><span id="mac___spanning_tree_priority"></span><span id="MAC___SPANNING_TREE_PRIORITY"></span>

**MAC + Spanning Tree Priority** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**BridgeType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIB.IETF\|BRIDGE-MIB.dot1dBaseType")
</dt> </dl>

The type of switching service to perform.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (1)


</dt> <dd></dd> <dt>

<span id="Transparent-only"></span><span id="transparent-only"></span><span id="TRANSPARENT-ONLY"></span>

**Transparent-only** (2)


</dt> <dd></dd> <dt>

<span id="SourceRoute-only"></span><span id="sourceroute-only"></span><span id="SOURCEROUTE-ONLY"></span>

**SourceRoute-only** (3)


</dt> <dd></dd> <dt>

<span id="SRT"></span><span id="srt"></span>

**SRT** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**NumPorts**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIB.IETF\|BRIDGE-MIB.dot1dBaseNumPorts")
</dt> </dl>

The number of switch ports controlled by this switching service.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ForwardingService**](cim-forwardingservice.md)
</dt> </dl>

 


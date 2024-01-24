---
description: Represents a switch port that sends and receives data frames.
ms.assetid: 015eed2a-1393-40ef-a190-832ab48766f9
title: CIM_SwitchPort class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_SwitchPort
- CIM_SwitchPort.PortNumber
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_SwitchPort class

Represents a switch port that sends and receives data frames.

## Syntax

``` syntax
[Abstract, Version("2.7.0"), UMLPackagePath("CIM::Network::ProtocolEndpoints")]
class CIM_SwitchPort : CIM_ProtocolEndpoint
{
  uint16 PortNumber;
};
```

## Members

The **CIM\_SwitchPort** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SwitchPort** class has these properties.

<dl> <dt>

**PortNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIB.IETF\|BRIDGE-MIB.dot1dPort")
</dt> </dl>

The numeric identifier of the switch port.

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

[**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md)
</dt> </dl>

 


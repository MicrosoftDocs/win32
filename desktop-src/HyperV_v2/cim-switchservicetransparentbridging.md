---
description: Represents an association in which a bridge service is a component of a switch service.
ms.assetid: 737d5ba1-0759-40cf-bc46-a059d19902c8
title: CIM_SwitchServiceTransparentBridging class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_SwitchServiceTransparentBridging
- CIM_SwitchServiceTransparentBridging.GroupComponent
- CIM_SwitchServiceTransparentBridging.PartComponent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_SwitchServiceTransparentBridging class

Represents an association in which a bridge service is a component of a switch service.

## Syntax

``` syntax
[Association, Aggregation, Abstract, Version("2.6.0"), UMLPackagePath("CIM::Network::SwitchingBridging")]
class CIM_SwitchServiceTransparentBridging : CIM_ServiceComponent
{
  CIM_SwitchService              REF GroupComponent;
  CIM_TransparentBridgingService REF PartComponent;
};
```

## Members

The **CIM\_SwitchServiceTransparentBridging** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SwitchServiceTransparentBridging** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SwitchService**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](/windows/desktop/WmiSdk/standard-qualifiers), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("GroupComponent"), [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (1)
</dt> </dl>

A [**CIM\_SwitchService**](cim-switchservice.md) reference to the switch service.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_TransparentBridgingService**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("PartComponent")
</dt> </dl>

A [**CIM\_TransparentBridgingService**](cim-transparentbridgingservice.md) reference to the component bridging service.

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

[**CIM\_ServiceComponent**](cim-servicecomponent.md)
</dt> </dl>

 


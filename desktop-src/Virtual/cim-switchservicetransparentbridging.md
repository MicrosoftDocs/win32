---
title: CIM\_SwitchServiceTransparentBridging class
description: Represents an association in which a bridge service is a component of a switch service.
ms.assetid: 'dd726e70-1b60-4582-a726-38d88da08979'
keywords: ["CIM_SwitchServiceTransparentBridging class Hyper-V", "CIM_SwitchServiceTransparentBridging class Hyper-V , described"]
topic_type:
- apiref
api_name:
- CIM_SwitchServiceTransparentBridging
- CIM_SwitchServiceTransparentBridging.GroupComponent
- CIM_SwitchServiceTransparentBridging.PartComponent
api_location:
- Root\virtualization
api_type:
- Schema
---

# CIM\_SwitchServiceTransparentBridging class

Represents an association in which a bridge service is a component of a switch service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Aggregation, Version("2.6.0")]
class CIM_SwitchServiceTransparentBridging : CIM_ServiceComponent
{
  CIM_SwitchService              REF GroupComponent;
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

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A reference to the switch service.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_TransparentBridgingService**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

A reference to the component bridging service.

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ServiceComponent**](cim-servicecomponent.md)
</dt> </dl>

 

 






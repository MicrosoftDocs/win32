---
description: Represents a group of controllers that control the operation and function of devices that initiate protocols.
ms.assetid: fb6b65d4-3a1a-47b1-afc7-9b10e8eeaa32
title: CIM_ProtocolController class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ProtocolController
- CIM_ProtocolController.MaxUnitsControlled
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_ProtocolController class

Represents a group of controllers that control the operation and function of devices that initiate protocols.

## Syntax

``` syntax
[Abstract, Version("2.8.0"), UMLPackagePath("CIM::Device::ProtocolController"), AMENDMENT]
class CIM_ProtocolController : CIM_LogicalDevice
{
  uint32 MaxUnitsControlled;
};
```

## Members

The **CIM\_ProtocolController** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ProtocolController** class has these properties.

<dl> <dt>

**MaxUnitsControlled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of units that can be controlled by or accessed through the protocol controller.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_LogicalDevice**](cim-logicaldevice.md)
</dt> </dl>

 

 





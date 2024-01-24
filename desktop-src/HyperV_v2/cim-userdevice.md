---
description: Represents a logical device that allows a user to input, view or hear data on the computer system.
ms.assetid: 95f88a63-3a2a-4b8c-9849-564dac254933
title: CIM_UserDevice class (Hyper-V management)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_UserDevice
- CIM_UserDevice.IsLocked
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM_UserDevice class (Hyper-V management)

Represents a logical device that allows a user to input, view or hear data on the computer system.

## Syntax

``` syntax
[Abstract, Version("2.6.0"), UMLPackagePath("CIM::Device::UserDevices"), AMENDMENT]
class CIM_UserDevice : CIM_LogicalDevice
{
  boolean IsLocked;
};
```

## Members

The **CIM\_UserDevice** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_UserDevice** class has these properties.

<dl> <dt>

**IsLocked**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the device is locked, preventing user input or output; otherwise, **false**.

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

 

 





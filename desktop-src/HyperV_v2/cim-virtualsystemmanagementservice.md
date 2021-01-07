---
description: Represents a service that manages virtual systems.
ms.assetid: b2645546-3c04-4d3f-8d53-019a6db08e24
title: CIM_VirtualSystemManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_VirtualSystemManagementService
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_VirtualSystemManagementService class

Represents a service that manages virtual systems.

## Syntax

``` syntax
[Abstract, Version("2.22.0"), UMLPackagePath("CIM::Core::Virtualization"), AMENDMENT]
class CIM_VirtualSystemManagementService : CIM_Service
{
};
```

## Members

The **CIM\_VirtualSystemManagementService** class has these types of members:

-   [Methods](#methods)

### Methods

The **CIM\_VirtualSystemManagementService** class has these methods.



| Method                                                                                      | Description                                                                           |
|:--------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| [**AddResourceSettings**](cim-virtualsystemmanagementservice-addresourcesettings.md)       | Adds resources to a virtual system configuration.<br/>                          |
| [**DefineSystem**](cim-virtualsystemmanagementservice-definesystem.md)                     | Defines a virtual system.<br/>                                                  |
| [**DestroySystem**](cim-virtualsystemmanagementservice-destroysystem.md)                   | Deletes a virtual system.<br/>                                                  |
| [**ModifyResourceSettings**](cim-virtualsystemmanagementservice-modifyresourcesettings.md) | Modifies the virtual resource settings for a virtual system configuration.<br/> |
| [**ModifySystemSettings**](cim-virtualsystemmanagementservice-modifysystemsettings.md)     | Modifies virtual system settings.<br/>                                          |
| [**RemoveResourceSettings**](cim-virtualsystemmanagementservice-removeresourcesettings.md) | Removes virtual resource settings from a virtual system configuration.<br/>     |



 

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

[**CIM\_Service**](cim-service.md)
</dt> </dl>

 

 





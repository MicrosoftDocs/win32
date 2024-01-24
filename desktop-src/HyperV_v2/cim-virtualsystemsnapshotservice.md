---
description: Represents a service that can create, apply, and delete snapshots of virtual systems.
ms.assetid: 8d5d54a2-08f1-4f24-bca3-601dc698d018
title: CIM_VirtualSystemSnapshotService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_VirtualSystemSnapshotService
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_VirtualSystemSnapshotService class

Represents a service that can create, apply, and delete snapshots of virtual systems.

## Syntax

``` syntax
[Abstract, Version("2.22.0"), UMLPackagePath("CIM::Core::Virtualization"), AMENDMENT]
class CIM_VirtualSystemSnapshotService : CIM_Service
{
};
```

## Members

The **CIM\_VirtualSystemSnapshotService** class has these types of members:

-   [Methods](#methods)

### Methods

The **CIM\_VirtualSystemSnapshotService** class has these methods.



| Method                                                                      | Description                                                                                      |
|:----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| [**ApplySnapshot**](cim-virtualsystemsnapshotservice-applysnapshot.md)     | Applies a virtual system snapshot to the virtual system to the source virtual system.<br/> |
| [**CreateSnapshot**](cim-virtualsystemsnapshotservice-createsnapshot.md)   | Creates a snapshot of a virtual system.<br/>                                               |
| [**DestroySnapshot**](cim-virtualsystemsnapshotservice-destroysnapshot.md) | Deletes a virtual system snapshot.<br/>                                                    |



 

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

 

 





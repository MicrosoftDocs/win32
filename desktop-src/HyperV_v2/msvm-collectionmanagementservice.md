---
description: Manages the collections on the Hyper-V host.
ms.assetid: e895217e-352d-4d77-8f1d-7070012e6f60
title: Msvm_CollectionManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_CollectionManagementService
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_CollectionManagementService class

Manages the collections on the Hyper-V host.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_CollectionManagementService : CIM_Service
{
};
```

## Members

The **Msvm\_CollectionManagementService** class has these types of members:

-   [Methods](#methods)

### Methods

The **Msvm\_CollectionManagementService** class has these methods.



| Method                                                                          | Description                                                                                                                                                                                                                   |
|:--------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddMember**](msvm-collectionmanagementservice-addmember.md)                 | Adds the specified ManagedElement as a member of the given [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) object.<br/>                                                                                           |
| [**DefineCollection**](msvm-collectionmanagementservice-definecollection.md)   | Creates a new [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) object.<br/>                                                                                                                                        |
| [**DestroyCollection**](msvm-collectionmanagementservice-destroycollection.md) | Deletes the given [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) object.<br/>                                                                                                                                    |
| [**RemoveMember**](msvm-collectionmanagementservice-removemember.md)           | Removes the specified ManagedElement as a member of the given [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) object.<br/>                                                                                        |
| [**RemoveMemberById**](msvm-collectionmanagementservice-removememberbyid.md)   | Removes the specified ManagedElement as a member of the [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) with the given identifier. This will succeed even if the object with that identifier is not present.<br/> |
| [**RenameCollection**](msvm-collectionmanagementservice-renamecollection.md)   | Updates the ElementName the given [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) object.<br/>                                                                                                                    |
| [**StartService**](msvm-collectionmanagementservice-startservice.md)           | Starts the service.<br/>                                                                                                                                                                                                |
| [**StopService**](msvm-collectionmanagementservice-stopservice.md)             | Stops the service.<br/>                                                                                                                                                                                                 |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Service**](cim-service.md)
</dt> </dl>

 

 





---
description: Manages the configuration of resource pools by using jobs.
ms.assetid: cc0f0236-2335-4dd9-9132-51b3e6b9fcf4
title: CIM_ResourcePoolConfigurationService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ResourcePoolConfigurationService
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_ResourcePoolConfigurationService class

Manages the configuration of resource pools by using jobs.

## Syntax

``` syntax
[Abstract, Version("2.22.0"), UMLPackagePath("CIM::Core::Resource")]
class CIM_ResourcePoolConfigurationService : CIM_Service
{
};
```

## Members

The **CIM\_ResourcePoolConfigurationService** class has these types of members:

-   [Methods](#methods)

### Methods

The **CIM\_ResourcePoolConfigurationService** class has these methods.



| Method                                                                                                          | Description                                                                   |
|:----------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| [**AddResourcesToResourcePool**](cim-resourcepoolconfigurationservice-addresourcestoresourcepool.md)           | Starts a job to add resources to a resource pool.<br/>                  |
| [**ChangeParentResourcePool**](cim-resourcepoolconfigurationservice-changeparentresourcepool.md)               | Start a job to change the parent resource pool of a resource pool.<br/> |
| [**CreateChildResourcePool**](cim-resourcepoolconfigurationservice-createchildresourcepool.md)                 | Start a job to create a resource pool from a parent resource pool.<br/> |
| [**CreateResourcePool**](cim-resourcepoolconfigurationservice-createresourcepool.md)                           | Starts a job to create a root resource pool.<br/>                       |
| [**DeleteResourcePool**](cim-resourcepoolconfigurationservice-deleteresourcepool.md)                           | Start a job to delete a resource pool.<br/>                             |
| [**RemoveResourcesFromResourcePool**](cim-resourcepoolconfigurationservice-removeresourcesfromresourcepool.md) | Starts a job to remove resources from a resource pool.<br/>             |



 

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

[**CIM\_Service**](cim-service.md)
</dt> </dl>

 

 





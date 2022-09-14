---
description: Service to create, destroy and export reference points.
ms.assetid: 88a76319-b5a7-44a3-8a31-83ade999b255
title: Msvm_CollectionReferencePointService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_CollectionReferencePointService
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_CollectionReferencePointService class

Service to create, destroy and export reference points

of virtual system collections.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_CollectionReferencePointService : CIM_Service
{
};
```

## Members

The **Msvm\_CollectionReferencePointService** class has these types of members:

-   [Methods](#methods)

### Methods

The **Msvm\_CollectionReferencePointService** class has these methods.



| Method                                                                                      | Description                                                                                                                                                                                                     |
|:--------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateReferencePoint**](msvm-collectionreferencepointservice-createreferencepoint.md)   | Creates a reference point of a virtual system collection.<br/>                                                                                                                                            |
| [**DestroyReferencePoint**](msvm-collectionreferencepointservice-destroyreferencepoint.md) | Destroys an existing reference point collection. This method may as a side effect destroy other reference points that are dependent on the affected reference point collection.<br/>                      |
| [**ExportReferencePoint**](msvm-collectionreferencepointservice-exportreferencepoint.md)   | Exports a reference point collection to a file. The reference point collection, its associated configuration settings, and its associated resource settings will be preserved in the resulting file.<br/> |
| [**RemoveAssociatedData**](msvm-collectionreferencepointservice-removeassociateddata.md)   | Removes the data log associated with the reference point.<br/>                                                                                                                                            |



 

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

 

 





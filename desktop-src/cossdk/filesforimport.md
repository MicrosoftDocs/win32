---
description: Retrieves information for applications that are imported.
ms.assetid: 9ed4bc3f-3490-4c36-ba94-bc803886a4d2
title: FilesForImport collection
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FilesForImport
api_type: 
- COM
api_location: 
---

# FilesForImport collection

Retrieves information for applications that are imported.

This collection supports the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) and [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **FilesForImport** collection inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**Root**](root.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [ApplicationFileName](#applicationfilename)
-   [ApplicationName](#applicationname)
-   [Description](#partitiondescription)
-   [FileName](#applicationfilename)
-   [HasUsers](#hasusers)
-   [IsProxy](#isproxy)
-   [IsService](#isservice)
-   [PartitionDescription](#partitiondescription)
-   [PartitionID](#partitionid)
-   [PartitionName](#partitionname)

### ApplicationFileName



| Entry | Value |
|----------------|------------------------------------------------------------------------------|
| Description    | The name of the MSI file that contains the application that can be imported. |
| Access         | ReadOnly                                                                     |
| Type           | String                                                                       |
| Default        | N/A                                                                          |
| Minimum system | Windows XP                                                                   |



 

### ApplicationName



| Entry | Value |
|----------------|------------------------------|
| Description    | The name of the application. |
| Access         | ReadOnly                     |
| Type           | String                       |
| Default        | ""                           |
| Minimum system | Windows XP                   |



 

### Description



| Entry | Value |
|----------------|-----------------------------------|
| Description    | A description of the application. |
| Access         | ReadOnly                          |
| Type           | String                            |
| Default        | ""                                |
| Minimum system | Windows XP                        |



 

### FileName



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The name of the DLL or EXE file that contains the application. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) or [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                                                                                              |
| Type           | String                                                                                                                                                                                                                                |
| Default        | ""                                                                                                                                                                                                                                    |
| Minimum system | Windows XP                                                                                                                                                                                                                            |



 

### HasUsers



| Entry | Value |
|----------------|--------------------------------------------------|
| Description    | Indicates whether the application has any users. |
| Access         | ReadOnly                                         |
| Type           | Bool                                             |
| Default        | False                                            |
| Minimum system | Windows XP                                       |



 

### IsProxy



| Entry | Value |
|----------------|-----------------------------------------------|
| Description    | Indicates whether the application is a proxy. |
| Access         | ReadOnly                                      |
| Type           | Bool                                          |
| Default        | False                                         |
| Minimum system | Windows XP                                    |



 

### IsService



| Entry | Value |
|----------------|-------------------------------------------------|
| Description    | Indicates whether the application is a service. |
| Access         | ReadOnly                                        |
| Type           | Bool                                            |
| Default        | False                                           |
| Minimum system | Windows XP                                      |



 

### PartitionDescription



| Entry | Value |
|----------------|-----------------------------------------------|
| Description    | A description of the application's partition. |
| Access         | ReadOnly                                      |
| Type           | String                                        |
| Default        | ""                                            |
| Minimum system | Windows Server 2003                           |



 

### PartitionID



| Entry | Value |
|----------------|------------------------------------------|
| Description    | The GUID of the application's partition. |
| Access         | ReadOnly                                 |
| Type           | String                                   |
| Default        | ""                                       |
| Minimum system | Windows Server 2003                      |



 

### PartitionName



| Entry | Value |
|----------------|------------------------------------------|
| Description    | The name of the application's partition. |
| Access         | ReadOnly                                 |
| Type           | String                                   |
| Default        | ""                                       |
| Minimum system | Windows Server 2003                      |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 

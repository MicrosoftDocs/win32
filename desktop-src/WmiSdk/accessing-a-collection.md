---
description: A collection is a standard automation concept that provides a uniform interface to a set of objects over which you can perform iteration.
ms.assetid: c1ebe529-33cb-4158-923d-124d6328fc60
ms.tgt_platform: multiple
title: Accessing a WMI Collection
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Accessing a WMI Collection

A collection is a standard automation concept that provides a uniform interface to a set of objects over which you can perform iteration. The Scripting API for WMI exposes a number of interfaces that conform to the collection paradigm. In each case, use the **Item** method to identify the elements using a string containing the value.

The [**SWbemPropertySet**](swbempropertyset.md), [**SWbemQualifierSet**](swbemqualifierset.md), and [**SWbemMethodSet**](swbemmethodset.md) collections are mostly used to modify schema. An [**SWbemObjectSet**](swbemobjectset.md) object contains WMI objects, such as a [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) instance, that have been obtained through calls, such as [**SWbemServices.InstancesOf**](swbemservices-instancesof.md) or [**SWbemObject.Associators\_**](swbemobject-associators-.md). The [**SWbemRefresher**](swbemrefresher.md) object can only contain instances of WMI classes. The [**SWbemNamedValueSet**](swbemnamedvalueset.md) object may contain WMI objects or any other type of data that a provider requires for the method call.

> [!Note]  
> The following topics were written primarily for VBScript. C# uses the standard [IEnumerable](/dotnet/api/system.collections.ienumerable) interface to collate and enumerate objects. In contrast, PowerShell generally uses an implicit object collection whenever a return value contains more than one result.

 

The following table lists the collections in the Scripting API for WMI and the elements and parameters for each collection.



| Collection                                       | Element                                              | Item() Parameter                                                         |
|--------------------------------------------------|------------------------------------------------------|--------------------------------------------------------------------------|
| [**SWbemObjectSet**](swbemobjectset.md)         | [**SWbemObject**](swbemobject.md)                   | Object path                                                              |
| [**SWbemPropertySet**](swbempropertyset.md)     | [**SWbemProperty**](swbemproperty.md)               | Property name                                                            |
| [**SWbemQualifierSet**](swbemqualifierset.md)   | [**SWbemQualifier**](swbemqualifier.md)             | Qualifier name                                                           |
| [**SWbemMethodSet**](swbemmethodset.md)         | [**SWbemMethod**](swbemmethod.md)                   | Method name                                                              |
| [**SWbemNamedValueSet**](swbemnamedvalueset.md) | [**SWbemNamedValue**](swbemnamedvalue.md)           | Value name                                                               |
| [**SWbemPrivilegeSet**](swbemprivilegeset.md)   | [**SWbemPrivilege**](swbemprivilege.md)             | Privilege name                                                           |
| [**SWbemRefresher**](swbemrefresher.md)         | [**SWbemRefreshableItem**](swbemrefreshableitem.md) | Index of the item in the [**SWbemRefresher**](swbemrefresher.md) object |



 

For more information about and examples of adding and removing items from a collection, see [Removing a Single Item from a Collection](removing-a-single-item-from-a-collection.md) and [Removing Multiple Items from a Collection](removing-multiple-items-from-a-collection.md). For more information about working with classes, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md).

 

 

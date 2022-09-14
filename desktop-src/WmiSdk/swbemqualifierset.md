---
description: An SWbemQualifierSet object is a collection of SWbemQualifier objects.
ms.assetid: 7ac5469c-357b-499d-a558-30bf760c5311
ms.tgt_platform: multiple
title: SWbemQualifierSet object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemQualifierSet
- ISWbemQualifierSet
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemQualifierSet object

An **SWbemQualifierSet** object is a collection of [**SWbemQualifier**](swbemqualifier.md) objects. Items are added to the collection using the [**Add**](swbemqualifierset-add.md) method, retrieved from the collection using the [**Item**](swbemqualifierset-item.md) method, and removed from the collection using the [**Remove**](swbemqualifierset-remove.md) method. This object cannot be created by the VBScript [CreateObject](creating-an-object-using-vbscript.md) call.

For more information, see [Accessing a Collection](accessing-a-collection.md).

The [**SWbemQualifier**](swbemqualifier.md) objects that make up an **SWbemQualifierSet** collection describe the qualifiers attached to a WMI class, instance, method, or method parameter.

## Members

The **SWbemQualifierSet** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SWbemQualifierSet** object has these methods.



| Method                                     | Description                                                                                                 |
|:-------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**Add**](swbemqualifierset-add.md)       | Adds an [**SWbemQualifier**](swbemqualifier.md) object to the **SWbemQualifierSet** collection.<br/> |
| [**Item**](swbemqualifierset-item.md)     | Returns a named [**SWbemQualifier**](swbemqualifier.md) object from the collection.<br/>             |
| [**Remove**](swbemqualifierset-remove.md) | Deletes a named qualifier from the collection.<br/>                                                   |



 

### Properties

The **SWbemQualifierSet** object has these properties.



| Property                                            | Access type          | Description                                                                     |
|:----------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------|
| [**Count**](swbemqualifierset-count.md)<br/> | Read-only<br/> | Contains the number of items in an **SWbemQualifierSet** collection.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemQualifierSet<br/>                                                     |
| IID<br/>                      | IID\_ISWbemQualifierSet<br/>                                                      |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

 





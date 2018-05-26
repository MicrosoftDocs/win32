---
title: Properties Collection object
description: The Properties object is a collection of Property objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 40d3ebc4-5b91-4869-a6e2-6cc3b8d73b26
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Properties Collection object MMC
- Properties Collection object MMC , described
topic_type:
- apiref
api_name:
- Properties Collection
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# Properties Collection object

The **Properties** object is a collection of [**Property objects**](property-object.md).

## Members

The **Properties Collection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties-collection-object)

### Methods

The **Properties Collection** object has these methods.



| Method                              | Description                                                                                  |
|:------------------------------------|:---------------------------------------------------------------------------------------------|
| [**Item**](properties-item.md)     | Retrieves a [**Property**](property-object.md) object by name.<br/>                   |
| [**Remove**](properties-remove.md) | Removes the named [**Property**](property-object.md) object from the collection.<br/> |



 

### Properties

The **Properties Collection** object has these properties.



| Property                                     | Description                                                                                       |
|:---------------------------------------------|:--------------------------------------------------------------------------------------------------|
| [**Count**](properties-count.md)<br/> | Retrieves the number of [**Property**](property-object.md) objects in the collection.<br/> |



 

## Examples

The **Properties** collection supports the "**For Each**" enumeration syntax, as shown in the following example.


```VB
Dim objProp As MMC20.Property
' objProps is a Properties collection.
For Each objProp In objProps
    ' Use the Property object.
    MsgBox (objProp.Name)
Next
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |
| IID<br/>                      | IID\_Properties is defined as 2886ABC2-A425-42b2-91C6-E25C0E04581C<br/>           |



## See also

<dl> <dt>

[**Property object**](property-object.md)
</dt> </dl>

 

 






---
title: SnapIns Collection object
description: The SnapIns object is a collection of SnapIn objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 636478c5-ba14-4f18-a172-cb899d16bbc2
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- SnapIns Collection object MMC
- SnapIns Collection object MMC , described
topic_type:
- apiref
api_name:
- SnapIns Collection
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# SnapIns Collection object

The **SnapIns** object is a collection of [**SnapIn**](snapin-object.md) objects.

## Members

The **SnapIns Collection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SnapIns Collection** object has these methods.



| Method                           | Description                                                                                                            |
|:---------------------------------|:-----------------------------------------------------------------------------------------------------------------------|
| [**Add**](snapins-add.md)       | Adds a [**SnapIn**](snapin-object.md) object to the collection, given its name, CLSID, or ProgID.<br/>          |
| [**Item**](snapins-item.md)     | Retrieves the [**SnapIn**](snapin-object.md) object at a specified index.<br/>                                  |
| [**Remove**](snapins-remove.md) | Removes a [**SnapIn**](snapin-object.md) object from the collection, thereby removing it from the console.<br/> |



 

### Properties

The **SnapIns Collection** object has these properties.



| Property                                  | Description                                                                     |
|:------------------------------------------|:--------------------------------------------------------------------------------|
| [**Count**](snapins-count.md)<br/> | Number of [**SnapIn**](snapin-object.md) objects in the collection.<br/> |



 

## Examples

The **SnapIns** collection supports the "**For Each**" enumeration syntax, as shown in the following example.


```VB
Dim objSnap As MMC20.SnapIn
' objSnapIns is a SnapIns collection.
For Each objSnap In objSnapIns
    ' Use the SnapIn object.
    MsgBox (objSnap.Name)
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
| IID<br/>                      | IID\_SnapIns is defined as 2EF3DE1D-B12A-49D1-92C5-0B00798768F1<br/>              |



 

 






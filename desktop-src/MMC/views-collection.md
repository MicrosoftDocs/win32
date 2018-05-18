---
title: Views Collection object
description: The Views object is a collection of View objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '983da9be-8ed6-4bdf-bf09-a6c08b455a24'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Views Collection object MMC", "Views Collection object MMC , described"]
topic_type:
- apiref
api_name:
- Views Collection
api_location:
- MmcNdMgr.dll
api_type:
- COM
---

# Views Collection object

The **Views** object is a collection of [**View**](view-object.md) objects.

## Members

The **Views Collection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Views Collection** object has these methods.



| Method                     | Description                                                                         |
|:---------------------------|:------------------------------------------------------------------------------------|
| [**Add**](views-add.md)   | Adds a [**View**](view-object.md) object to the collection.<br/>             |
| [**Item**](views-item.md) | Retrieves the [**View**](view-object.md) object at the specified index.<br/> |



 

### Properties

The **Views Collection** object has these properties.



| Property                                | Description                                                                               |
|:----------------------------------------|:------------------------------------------------------------------------------------------|
| [**Count**](views-count.md)<br/> | Retrieves the number of [**View**](view-object.md) objects in the collection.<br/> |



 

## Examples

The **Views** collection supports the "**For Each**" enumeration syntax, as shown in the following example.


```VB
Dim objView As MMC20.View
' objViews is a Views collection.
For Each objView In objViews
    ' Use the View object.
    MsgBox (objView.Memento)
Next
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |
| IID<br/>                      | IID\_Views is defined as D6B8C29D-A1FF-4D72-AAB0-E381E9B9338D<br/>                |



 

 






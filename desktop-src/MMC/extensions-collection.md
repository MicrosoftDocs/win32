---
title: Extensions Collection object
description: The Extensions object is a collection of Extension objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ac49922e-5e13-4936-8f57-8901e4837fe3
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Extensions Collection object MMC
- Extensions Collection object MMC , described
topic_type:
- apiref
api_name:
- Extensions Collection
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# Extensions Collection object

The **Extensions** object is a collection of [**Extension**](extension-object.md) objects.

## Members

The **Extensions Collection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Extensions Collection** object has these methods.



| Method                          | Description                                                                                 |
|:--------------------------------|:--------------------------------------------------------------------------------------------|
| [**Item**](extensions-item.md) | Retrieves the [**Extension**](extension-object.md) object at a specified index.<br/> |



 

### Properties

The **Extensions Collection** object has these properties.



| Property                                     | Description                                                                           |
|:---------------------------------------------|:--------------------------------------------------------------------------------------|
| [**Count**](extensions-count.md)<br/> | Number of [**Extension**](extension-object.md) objects in the collection.<br/> |



 

## Examples

The **Extensions** collection supports the "For Each" enumeration syntax, as shown in the following example.


```VB
Dim objExt As MMC20.Extension
' objExts is an Extensions collection.
For Each objExt In objExts
    ' Use the Extension object.
    MsgBox (objExt.Name)
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
| IID<br/>                      | IID\_Extensions is defined as 82DBEA43-8CA4-44bc-A2CA-D18741059EC8<br/>           |



 

 






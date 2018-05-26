---
title: Nodes Collection object
description: The Nodes object is a collection of Node objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8318622b-d887-41b3-9c3a-8df031abb4d0
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Nodes Collection object MMC
- Nodes Collection object MMC , described
topic_type:
- apiref
api_name:
- Nodes Collection
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# Nodes Collection object

The **Nodes** object is a collection of [**Node**](node-object.md) objects.

## Members

The **Nodes Collection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Nodes Collection** object has these methods.



| Method                     | Description                                                                                   |
|:---------------------------|:----------------------------------------------------------------------------------------------|
| [**Item**](nodes-item.md) | Retrieves the result item [**Node**](node-object.md) object at a specified index.<br/> |



 

### Properties

The **Nodes Collection** object has these properties.



| Property                                | Description                                                                                           |
|:----------------------------------------|:------------------------------------------------------------------------------------------------------|
| [**Count**](nodes-count.md)<br/> | Retrieves the number of result item [**Node**](node-object.md) objects in the collection.<br/> |



 

## Examples

The **Nodes** collection supports the "**For Each**" enumeration syntax, as shown in the following code example.


```VB
' Retrieve the ListItems property
Dim objNodes As MMC20.Nodes
Set objNodes = objView.ListItems
' ...
' Use the ListItems.
' This code displays the count of items in the list.
MsgBox (objNodes.Count)
' Use objNodes for other processing.
' ...
 
' Free the object when done.
Set objNodes = Nothing


```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |
| IID<br/>                      | IID\_Nodes is defined as 313B01DF-B22F-4D42-B1B8-483CDCF51D35<br/>                |



 

 






---
title: Node Object object
description: The Node object is used to manage a scope (tree) or result (list or leaf) node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c504cb3f-8ec6-49fe-b0d3-05ea9cad61f4
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Node Object object MMC
- Node Object object MMC , described
topic_type:
- apiref
api_name:
- Node Object
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# Node Object object

The **Node** object is used to manage a scope (tree) or result (list or leaf) node.

## Members

The **Node Object** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Node Object** object has these methods.



| Method                                  | Description                                          |
|:----------------------------------------|:-----------------------------------------------------|
| [**IsScopeNode**](node-isscopenode.md) | Returns whether the node is a scope node.<br/> |



 

### Properties

The **Node Object** object has these properties.



| Property                                     | Access type          | Description                                                                                    |
|:---------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------|
| [**Bookmark**](node-bookmark.md)<br/> | Read-only<br/> | Returns a persistable bookmark for the node.<br/>                                        |
| [**Name**](node-name.md)<br/>         | Read-only<br/> | The name of the node.<br/>                                                               |
| [**Nodetype**](node-nodetype.md)<br/> | Read-only<br/> | Returns the globally unique identifier (GUID) that represents the type of the node.<br/> |
| [**Property**](node-property.md)<br/> | Read-only<br/> | Returns data for a specified clipboard format or property name.<br/>                     |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |
| IID<br/>                      | IID\_Node is defined as F81ED800-7839-4447-945D-8E15DA59CA55<br/>                 |



 

 






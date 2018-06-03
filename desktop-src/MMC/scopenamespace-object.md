---
title: ScopeNamespace Object object
description: The ScopeNamespace object is used to access the scope tree. Use the Document.ScopeNamespace property to retrieve the ScopeNamespace object for the MMC document.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 61cb4ced-7ceb-4a15-8fcb-9fb942eeae4c
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ScopeNamespace Object object MMC
- ScopeNamespace Object object MMC , described
topic_type:
- apiref
api_name:
- ScopeNamespace Object
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ScopeNamespace Object object

The **ScopeNamespace** object is used to access the scope tree. Use the [**Document.ScopeNamespace property**](document-scopenamespace.md) to retrieve the **ScopeNamespace** object for the MMC document.

## Members

The **ScopeNamespace Object** object has these types of members:

-   [Methods](#methods)

### Methods

The **ScopeNamespace Object** object has these methods.



| Method                                        | Description                                                       |
|:----------------------------------------------|:------------------------------------------------------------------|
| [**Expand**](scopenamespace-expand.md)       | Expands a node.<br/>                                        |
| [**GetChild**](scopenamespace-getchild.md)   | Returns the first child node of the scope node.<br/>        |
| [**GetNext**](scopenamespace-getnext.md)     | Returns the next child sibling node of the scope node.<br/> |
| [**GetParent**](scopenamespace-getparent.md) | Returns the parent of the scope node.<br/>                  |
| [**GetRoot**](scopenamespace-getroot.md)     | Returns the root node of the namespace.<br/>                |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |
| IID<br/>                      | IID\_ScopeNamespace is defined as EBBB48DC-1A3B-4D86-B786-C21B28389012<br/>       |



## See also

<dl> <dt>

[**Document.ScopeNamespace property**](document-scopenamespace.md)
</dt> </dl>

 

 






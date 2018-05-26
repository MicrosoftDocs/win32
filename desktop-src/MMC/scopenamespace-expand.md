---
title: ScopeNamespace Expand method
description: The Expand method causes the specified node to be expanded.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 63d77fb3-c9e2-4046-b8c8-8304913c9126
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Expand method MMC
- Expand method MMC , ScopeNamespace object
- ScopeNamespace object MMC , Expand method
- Expand method MMC , ScopeNamespace interface
- ScopeNamespace interface MMC , Expand method
topic_type:
- apiref
api_name:
- ScopeNamespace.Expand
- ScopeNamespace.Expand
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ScopeNamespace::Expand method

The **Expand** method causes the specified node to be expanded.

## Syntax


```VB
ScopeNamespace.Expand( _
  ByVal Node As Node _
)
```



## Parameters

<dl> <dt>

*Node* 
</dt> <dd>

The node that is to be expanded.

</dd> </dl>

## Return value

This method does not return a value.

## Examples


```VB
' Expand the node.
objScopeNS.Expand objNode
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mmcobj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>Mmcobj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl> |
| IID<br/>                      | IID\_ScopeNamespace is defined as EBBB48DC-1A3B-4D86-B786-C21B28389012<br/>       |



## See also

<dl> <dt>

[**ScopeNamespace.GetChild**](scopenamespace-getchild.md)
</dt> </dl>

 

 






---
title: ScopeNamespace GetRoot method
description: The GetRoot method returns the root node of the scope namespace.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bb50f59d-ff5d-457b-a1a1-6496e44fdfa9
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- GetRoot method MMC
- GetRoot method MMC , ScopeNamespace object
- ScopeNamespace object MMC , GetRoot method
- GetRoot method MMC , ScopeNamespace interface
- ScopeNamespace interface MMC , GetRoot method
topic_type:
- apiref
api_name:
- ScopeNamespace.GetRoot
- ScopeNamespace.GetRoot
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ScopeNamespace::GetRoot method

The **GetRoot** method returns the root node of the scope namespace.

## Syntax


```VB
ScopeNamespace.GetRoot() As Node
```



## Parameters

This method has no parameters.

## Examples


```VB
' Retrieve the Root of the ScopeNameSpace.
Dim objSNSRoot As Node
Set objSNSRoot = objScopeNS.GetRoot()
' Use the object; this code displays the Name property.
MsgBox (objSNSRoot.Name)
 
' Free the object when done.
Set objSNSRoot = Nothing
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

[**ScopeNamespace.GetParent**](scopenamespace-getparent.md)
</dt> <dt>

[**Node object**](node-object.md)
</dt> </dl>

 

 






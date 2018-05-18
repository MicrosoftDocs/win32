---
title: ScopeNamespace GetParent method
description: The GetParent method returns the parent node of the specified scope node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3b444d2f-41e6-45bc-8833-09d3ab4238de'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["GetParent method MMC", "GetParent method MMC , ScopeNamespace object", "ScopeNamespace object MMC , GetParent method", "GetParent method MMC , ScopeNamespace interface", "ScopeNamespace interface MMC , GetParent method"]
topic_type:
- apiref
api_name:
- ScopeNamespace.GetParent
- ScopeNamespace.GetParent
api_location:
- Mmcndmgr.dll
api_type:
- COM
---

# ScopeNamespace::GetParent method

The **GetParent** method returns the parent node of the specified scope node.

## Syntax


```VB
ScopeNamespace.GetParent( _
  ByVal Node As Node _
) As Node
```



## Parameters

<dl> <dt>

*Node* 
</dt> <dd>

The scope node being queried.

</dd> </dl>

## Examples


```VB
' Retrieve the parent of the scope node.
Dim objParent As MMC20.Node
Set objParent = objScopeNS.GetParent(objNode)
 
' This code displays the Parent's name.
MsgBox (objNode.Name & _
        "'s parent is " & objParent.Name)
 
' Free the object when done.
Set objParent = Nothing
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mmcobj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>Mmcobj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl> |
| IID<br/>                      | IID\_ScopeNamespace is defined as EBBB48DC-1A3B-4D86-B786-C21B28389012<br/>       |



## See also

<dl> <dt>

[**ScopeNamespace.GetRoot**](scopenamespace-getroot.md)
</dt> <dt>

[**ScopeNamespace.GetChild**](scopenamespace-getchild.md)
</dt> <dt>

[**Node object**](node-object.md)
</dt> </dl>

 

 






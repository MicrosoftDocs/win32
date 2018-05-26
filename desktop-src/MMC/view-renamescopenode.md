---
title: View RenameScopeNode method
description: The RenameScopeNode method renames a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b5034924-fa90-41ec-8d02-02a2c294eae9
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- RenameScopeNode method MMC
- RenameScopeNode method MMC , View object
- View object MMC , RenameScopeNode method
- RenameScopeNode method MMC , View interface
- View interface MMC , RenameScopeNode method
topic_type:
- apiref
api_name:
- View.RenameScopeNode
- View.RenameScopeNode
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# View::RenameScopeNode method

The **RenameScopeNode** method renames a node.

## Syntax


```VB
View.RenameScopeNode( _
  ByVal NewName As String, _
  ByVal ScopeNode As Variant _
)
```



## Parameters

<dl> <dt>

*NewName* 
</dt> <dd>

The new name for the node.

</dd> <dt>

*ScopeNode* 
</dt> <dd>

Optional. A value that specifies the node to be renamed; if this parameter is not specified, the active scope node is used.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Attempting to change a node name that cannot be changed results in a Windows Script Host error.

## Examples


```VB
' This example renames the Document object's RootNode.
' Retrieve the RootNode object.
Dim var1 As Variant
Set var1 = objDoc.RootNode
 
' Rename the scope node.
objView.RenameScopeNode "New Console Root", var1
 
' Free the Variant when done.
Set var1 = Nothing
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_View is defined as 6EFC2DA2-B38C-457E-9ABB-ED2D189B8C38<br/>               |



## See also

<dl> <dt>

[**View.RenameSelectedItem**](view-renameselecteditem.md)
</dt> </dl>

 

 






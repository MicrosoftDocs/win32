---
title: ScopeNamespace GetNext method
description: The GetNext method returns the next child sibling node for a given scope node. Before calling this method, the caller must retrieve the first child node by calling the ScopeNamespace.GetChild method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 21d06208-e84d-4f98-9a69-56ba06004c82
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- GetNext method MMC
- GetNext method MMC , ScopeNamespace object
- ScopeNamespace object MMC , GetNext method
- GetNext method MMC , ScopeNamespace interface
- ScopeNamespace interface MMC , GetNext method
topic_type:
- apiref
api_name:
- ScopeNamespace.GetNext
- ScopeNamespace.GetNext
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ScopeNamespace::GetNext method

The **GetNext** method returns the next child sibling node for a given scope node. Before calling this method, the caller must retrieve the first child node by calling the [**ScopeNamespace.GetChild method**](scopenamespace-getchild.md).

## Syntax


```VB
ScopeNamespace.GetNext( _
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
On Error Resume Next
Dim objNode As MMC20.Node
' Retrieve the child of the root node.
' objRoot was previously set to Document.RootNode.
Set objNode = objScopeNS.GetChild(objRoot)
If (objNode Is Nothing) Then
    MsgBox ("There are no child nodes")
Else
    ' There is at least one child node.
    Dim objSib As MMC20.Node
    Set objSib = objNode
    Dim objNext As MMC20.Node
    Do While True
        ' Display the Name of the sibling Node object.
        MsgBox ("Sibling: " & objSib.Name)
        ' Set objNext to Nothing, as it will be tested
        ' after the call to GetNext.
        Set objNext = Nothing
        ' Retrieve the next sibling Node.
        Set objNext = objSNS.GetNext(objSib)
        If (objNext Is Nothing) Then
            ' Free objects.
            Set objSib = Nothing
            Set objNode = Nothing
            Exit Do ' No more siblings.
        Else
            Set objSib = objNext
        End If
    Loop
End If
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
</dt> <dt>

[**ScopeNamespace.GetParent**](scopenamespace-getparent.md)
</dt> </dl>

 

 






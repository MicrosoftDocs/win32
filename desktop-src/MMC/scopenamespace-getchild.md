---
title: ScopeNamespace GetChild method
description: The GetChild method returns the first child node for a given scope node. Use the ScopeNamespace.GetNext method to retrieve the siblings of the node returned by the GetChild method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 955b35fb-4dbf-4e58-ba90-4dbc93367746
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- GetChild method MMC
- GetChild method MMC , ScopeNamespace object
- ScopeNamespace object MMC , GetChild method
- GetChild method MMC , ScopeNamespace interface
- ScopeNamespace interface MMC , GetChild method
topic_type:
- apiref
api_name:
- ScopeNamespace.GetChild
- ScopeNamespace.GetChild
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ScopeNamespace::GetChild method

The **GetChild** method returns the first child node for a given scope node. Use the [**ScopeNamespace.GetNext method**](scopenamespace-getnext.md) to retrieve the siblings of the node returned by the **GetChild** method.

## Syntax


```VB
ScopeNamespace.GetChild( _
  ByVal Node As Node _
) As Node
```



## Parameters

<dl> <dt>

*Node* 
</dt> <dd>

The scope node being queried.

</dd> </dl>

## Remarks

For an example of code that uses the **GetChild** method, see the [**ScopeNamespace.GetNext**](scopenamespace-getnext.md) method.

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

[**ScopeNamespace.GetNext**](scopenamespace-getnext.md)
</dt> <dt>

[**ScopeNamespace.GetParent**](scopenamespace-getparent.md)
</dt> <dt>

[**Node object**](node-object.md)
</dt> </dl>

 

 






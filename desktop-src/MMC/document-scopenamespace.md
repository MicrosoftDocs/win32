---
title: Document ScopeNamespace property
description: The ScopeNamespace property returns the ScopeNamespace object for the document. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c4a7d7ac-5378-4e22-a1a9-f1810849d55f'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["ScopeNamespace property MMC", "ScopeNamespace property MMC , Document object", "Document object MMC , ScopeNamespace property", "ScopeNamespace property MMC , Document interface", "Document interface MMC , ScopeNamespace property"]
topic_type:
- apiref
api_name:
- Document.ScopeNamespace
- Document.ScopeNamespace
api_location:
- Mmc.exe
api_type:
- COM
---

# Document::ScopeNamespace property

The **ScopeNamespace** property returns the [**ScopeNamespace**](scopenamespace-object.md) object for the document. This property is read-only.

## Syntax


```VB
Property ScopeNamespace As ScopeNamespace
```



## Property value

The [**ScopeNamespace**](scopenamespace-object.md) object for the document.

## Examples


```VB
' Retrieve the document's ScopeNamespace property.
Dim objScopeNS As MMC20.ScopeNamespace
Set objScopeNS = objDoc.ScopeNamespace
 
' Use the scopenamespace object.
' ...
 
' Free the object when done.
Set objScopeNS = Nothing
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Document<br/>                                                              |



## See also

<dl> <dt>

[**ScopeNamespace**](scopenamespace-object.md)
</dt> </dl>

 

 






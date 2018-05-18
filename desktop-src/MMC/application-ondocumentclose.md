---
title: AppEvents OnDocumentClose event
description: The OnDocumentClose event occurs when the document is being closed (prior to being destroyed).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8ff15be0-6069-4862-b89f-6bce1426ce8b'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["OnDocumentClose event MMC", "OnDocumentClose event MMC , Application object", "Application object MMC , OnDocumentClose event", "OnDocumentClose event MMC , AppEvents interface", "AppEvents interface MMC , OnDocumentClose event"]
topic_type:
- apiref
api_name:
- Application.OnDocumentClose
- AppEvents.OnDocumentClose
api_location:
- MmcNdMgr.dll
api_type:
- COM
---

# AppEvents::OnDocumentClose event

The **OnDocumentClose** event occurs when the document is being closed (prior to being destroyed).

## Syntax


```VB
Application.OnDocumentClose( _
  ByVal Document As Document _
)
```



## Parameters

<dl> <dt>

*Document* 
</dt> <dd>

The [**Document object**](document-object.md) being closed.

</dd> </dl>

## Return value

This event does not return a value.

## Examples


```VB
Private Sub g_AppMMC_OnDocumentClose( _
               ByVal Document As MMC20.Document)
    MsgBox ("OnDocumentClose Event: " & Document.Name)
End Sub
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_Application is defined as 49B2791A-B1AE-4C90-9B8E-E860BA07F889<br/>        |
| IID<br/>                      | DIID\_AppEvents is defined as FC7A4252-78AC-4532-8C5A-563CFE138863<br/>           |



 

 






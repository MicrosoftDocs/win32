---
title: AppEvents OnDocumentOpen event
description: The OnDocumentOpen event occurs when the document is opened.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '341ba51d-4d56-4206-9432-4e0eb1a9c1b3'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["OnDocumentOpen event MMC", "OnDocumentOpen event MMC , Application object", "Application object MMC , OnDocumentOpen event", "OnDocumentOpen event MMC , AppEvents interface", "AppEvents interface MMC , OnDocumentOpen event"]
topic_type:
- apiref
api_name:
- Application.OnDocumentOpen
- AppEvents.OnDocumentOpen
api_location:
- MmcNdMgr.dll
api_type:
- COM
---

# AppEvents::OnDocumentOpen event

The **OnDocumentOpen** event occurs when the document is opened.

## Syntax


```VB
Application.OnDocumentOpen( _
  ByVal Document As Document, _
  ByVal New As Long _
)
```



## Parameters

<dl> <dt>

*Document* 
</dt> <dd>

The [**Document object**](document-object.md) being opened.

</dd> <dt>

*New* 
</dt> <dd>

A value that specifies whether the document is new or being opened from a saved file.

</dd> </dl>

## Return value

This event does not return a value.

## Examples


```VB
Private Sub g_AppMMC_OnDocumentOpen( _
                ByVal Document As MMC20.Document, _
                ByVal lNew As Long)
    MsgBox ("OnDocumentOpen Event: " & Document.Name)
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



 

 






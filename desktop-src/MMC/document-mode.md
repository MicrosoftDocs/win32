---
title: Document Mode property
description: The Mode property sets or returns the documents mode. This property is read/write.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: eebc5a95-7464-49fb-aeca-b426f9b4aaec
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Mode property MMC
- Mode property MMC , Document object
- Document object MMC , Mode property
- Mode property MMC , Document interface
- Document interface MMC , Mode property
topic_type:
- apiref
api_name:
- Document.Mode
- Document.Mode
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Document::Mode property

The **Mode** property sets or returns the document's mode. This property is read/write.

## Syntax


```VB
Property Mode As DocumentMode
```



## Property value

The document's mode. This can be one of the following [**DocumentMode**](/windows/win32/MmcObj/ne-mmcobj-documentmode?branch=master) values.

<dt>

<span id="DocumentMode_Author"></span><span id="documentmode_author"></span><span id="DOCUMENTMODE_AUTHOR"></span>

<span id="DocumentMode_Author"></span><span id="documentmode_author"></span><span id="DOCUMENTMODE_AUTHOR"></span>**DocumentMode\_Author**


</dt> <dd>

The document is opened in Author Mode.

</dd> <dt>

<span id="DocumentMode_User"></span><span id="documentmode_user"></span><span id="DOCUMENTMODE_USER"></span>

<span id="DocumentMode_User"></span><span id="documentmode_user"></span><span id="DOCUMENTMODE_USER"></span>**DocumentMode\_User**


</dt> <dd>

The document is opened in Full-Access User Mode.

</dd> <dt>

<span id="DocumentMode_User_MDI"></span><span id="documentmode_user_mdi"></span><span id="DOCUMENTMODE_USER_MDI"></span>

<span id="DocumentMode_User_MDI"></span><span id="documentmode_user_mdi"></span><span id="DOCUMENTMODE_USER_MDI"></span>**DocumentMode\_User\_MDI**


</dt> <dd>

The document is opened in Limited-Access User Mode with multiple windows.

</dd> <dt>

<span id="DocumentMode_User_SDI"></span><span id="documentmode_user_sdi"></span><span id="DOCUMENTMODE_USER_SDI"></span>

<span id="DocumentMode_User_SDI"></span><span id="documentmode_user_sdi"></span><span id="DOCUMENTMODE_USER_SDI"></span>**DocumentMode\_User\_SDI**


</dt> <dd>

The document is opened in Limited-Access User Mode with a single window.

</dd> </dl>

## Examples


```VB
' Retrieve the document mode.
Dim docMode As MMC20.DocumentMode
docMode = objDoc.Mode
 
' Display a message box about the document mode.
Select Case docMode
    Case DocumentMode_Author
        MsgBox ("Author mode")
        
    Case DocumentMode_User
        MsgBox ("User full-access mode")
        
    Case DocumentMode_User_MDI
        MsgBox ("User MDI mode")
        
    Case DocumentMode_User_SDI
        MsgBox ("User SDI mode")
        
End Select
 
' Set the document mode.
objDoc.Mode = DocumentMode_User
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Document<br/>                                                              |



## See also

<dl> <dt>

[**DocumentMode**](/windows/win32/MmcObj/ne-mmcobj-documentmode?branch=master)
</dt> <dt>

[Console File and User Mode Changes](console-file-and-user-mode-changes.md)
</dt> </dl>

 

 






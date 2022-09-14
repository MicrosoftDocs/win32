---
description: Contains the Application object of the folder items collection.
ms.assetid: 2cd4243e-a5a6-4de4-b310-f74558ac0fbe
title: FolderItems.Application property (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FolderItems.Application
api_type: 
- COM
api_location: 
- Shell32.dll
---

# FolderItems.Application property

Contains the **Application** object of the folder items collection.

This property is read-only.

## Syntax


```JScript
objApplication = FolderItems.Application
```



## Property value

An object reference to the Application object.

## Remarks

The **Application** property returns the automation object supported by the application that contains the WebBrowser control, if that object is accessible. Otherwise, this property returns the WebBrowser control's automation object.

Use this property with the **Set** and **CreateObject** commands or with the **GetObject** command to create and manipulate an instance of the Windows Internet Explorer application.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 





---
description: ShellFolderView.Application property - Contains the object's Application object.
ms.assetid: 305766b1-a19f-4743-a9e3-6837b3f8ffe0
title: ShellFolderView.Application property (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellFolderView.Application
api_type: 
- COM
api_location: 
- Shell32.dll
---

# ShellFolderView.Application property

Contains the object's Application object.

This property is read-only.

## Syntax


```JScript
objApplication = ShellFolderView.Application
```



## Property value

A variable of type [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) that receives the Application object.

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



 

 

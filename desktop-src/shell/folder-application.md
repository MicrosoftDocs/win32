---
description: Contains the folder's Application object.
ms.assetid: 1dba83eb-1af6-42d9-b2c9-ab7767888efe
title: Folder.Application property (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Folder.Application
api_type: 
- COM
api_location: 
- Shldisp.h
---

# Folder.Application property

Contains the folder's Application object.

This property is read-only.

## Syntax


```JScript
Application = Folder.Application
```



## Property value

An object reference to the Application object.

## Remarks

The **Application** property returns the automation object supported by the application that contains the WebBrowser control, if that object is accessible. Otherwise, this property returns the WebBrowser control's automation object.

Use this property with the **Set** and **CreateObject** commands or with the **GetObject** command to create and manipulate an instance of the Internet Explorer application.

> [!Note]  
> Not all methods are implemented for all folders. For example, the [**ParseName**](folder-parsename.md) method is not implemented for the Control Panel folder (CSIDL\_CONTROLS). If you attempt to call an unimplemented method, a 0x800A01BD (decimal 445) error is raised.

 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                 |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl> |



 

 





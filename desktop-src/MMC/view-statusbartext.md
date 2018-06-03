---
title: View StatusBarText property
description: The StatusBarText property specifies the text in the status bar. This property is write-only; it cannot be retrieved.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7a673b2a-fc3f-4641-8844-9c0a81ee08d2
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- StatusBarText property MMC
- StatusBarText property MMC , View object
- View object MMC , StatusBarText property
- StatusBarText property MMC , View interface
- View interface MMC , StatusBarText property
topic_type:
- apiref
api_name:
- View.StatusBarText
- View.StatusBarText
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# View::StatusBarText property

The **StatusBarText** property specifies the text in the status bar. This property is write-only; it cannot be retrieved.

## Syntax


```VB
Property StatusBarText As String
```



## Property value

Text to display in the status bar.

## Remarks

The status bar has three sections, which are delineated by the pipe character ("\|"). For example, setting the text in the status bar to "Left\|Middle\|Right" places "Left" in the leftmost section of the status bar, "Middle" in the middle section, and "Right" in the rightmost section.

If more than three fields are delineated (that is, there are more than two pipes), then everything that would be placed in the fourth and higher fields is omitted.

In addition, the middle section is designed to function as a progress bar. This functionality is invoked by passing the "%" character as the first character in the middle section, followed by a number between 0 and 100. Instead of text, this section then displays a progress bar that is 0 to 100 percent complete. For example, passing "Working\|%75" places "Working" in the left section and a 75 percent complete progress bar in the middle section.

To display a string that begins with "%" in the middle section of the status bar, then begin the string with "%%". This causes the middle section to display text and removes the first "%". For example, "Today is\|%%Wednesday%" results in the left section that contains "Today is" and the middle section that contains "%Wednesday%". If an invalid number or non-numeric text is entered in the middle section following a "%", then the middle section is empty. If a "%" is the only character in the section, then it will be shown as text.

## Examples


```VB
' Set the View's StatusBarText property.
objView.StatusBarText = "left pane | middle pane | right pane"
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



 

 






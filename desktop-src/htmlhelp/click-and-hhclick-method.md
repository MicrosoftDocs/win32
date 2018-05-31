---
title: Click and HHClick Method
description: Use the Click method to invoke any command that supports the Button parameter.
ms.assetid: 101948CA-91F3-4ad5-A611-2683A9675DBE
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Click and HHClick Method

Use the **Click** method to invoke any command that supports the [Button](button-parameter.md) parameter.

Commands that do not support the **Button** parameter, such as [Splash](splash.md), are invoked as soon as your HTML file is loaded and, therefore, cannot be called from a method.

This method can be used with either a compiled help (.chm) file or uncompiled HTML files. However, not all [commands](about-commands.md) are supported in uncompiled HTML files.

Applies to: [Alink](alink.md) \| [Close](close.md) \| [HH Version](hh-version.md) \| [KLink](klink.md) \| [Related Topics](related-topics.md) \| [Shortcut](shortcut.md) \| [TCard](tcard.md) \| [WinHelp](winhelp.md)

## Syntax

``` syntax
Click() or HHClick() 
```

## Parameters

The **Click** method takes no parameters.

## Example

The following example shows how to use the **Click** method to invoke the [HH version](hh-version.md) command.

The code for the control:


```
<OBJECT
   id=test3
   type="application/x-oleobject"
   classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
   codebase="hhctrl.ocx#Version=5,02,3792,1194"
>
   <PARAM name="Command" value="HH Version">
</OBJECT>
```



The JavaScript code to invoke the control:


```
<a href=JavaScript:test3.Click()>On Click, do HH Version</a>
```



## Remarks

-   If you are using Microsoft Visual Basic Scripting Edition (VBScript), always use **HHClick**, which provides the same functionality as **Click**, but prevents a naming conflict with the VBScript **Click** method.

## Related topics

<dl> <dt>

[About the HTML Help ActiveX control Methods](about-methods.md)
</dt> </dl>

 

 





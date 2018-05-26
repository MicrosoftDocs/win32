---
title: TCard Method
description: Use the TCard method to send a WM\_TCARD message from a help window to a program. This method provides the same functionality as the TCard command with the exception that the method accepts only numeric arguments.
ms.assetid: 108A0299-7828-4cb7-BEFE-DA97E8BE0D92
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TCard Method

Use the [TCard](tcard.md) method to send a **WM\_TCARD** message from a help window to a program. This method provides the same functionality as the TCard command with the exception that the method accepts only numeric arguments.

Using the [TCard](tcard.md) method reduces the number of instances of the control in an HTML file. If you plan on using multiple TCard commands in a single HTML file, then you should insert a single &lt;OBJECT&gt; tag, and then call the TCard method.

The instance of the HTML Help ActiveX control that you reference using the [TCard](tcard.md) method must specify the TCard command.

This command can be used only with a compiled help (.chm) file.

Applies to: [TCard](tcard.md)

## Syntax

``` syntax
TCard(WPARAM <i>wPARAM</i>, LPARAM <i>lPARAM</i>) 
```

## Parameters

<dl> <dt>

<span id="wPARAM_"></span><span id="wparam_"></span><span id="WPARAM_"></span>*wPARAM* 
</dt> <dd>

Specifies the value to pass to the **WM\_TCARD** message. *wPARAM* usually identifies a user action.

This value must be numeric.

</dd> <dt>

<span id="lPARAM_"></span><span id="lparam_"></span><span id="LPARAM_"></span>*lPARAM* 
</dt> <dd>

Specifies the value to pass to the **WM\_TCARD** message. Contains additional data, depending on the value of *wPARAM*.

This value must be numeric.

</dd> </dl>

## Example

The code for the control:


```
<OBJECT
   id=test
   type="application/x-oleobject"
   classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
>
   <PARAM name="Command" value="TCard">
   <param name="Button" value="Call TCard command">
   <param name="Item1" value="123, MyText">
</OBJECT>
```



The JavaScript code to invoke the control:


```
<a href="JavaScript:test.TCard (5555, 10056)">TCard Example</a> 
```



## Remarks

The [TCard](tcard.md) method accepts only numeric arguments. To pass a string argument in *lPARAM*, use the TCard command.

## Related topics

<dl> <dt>

[About Methods](about-methods.md)
</dt> </dl>

 

 





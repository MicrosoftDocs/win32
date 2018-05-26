---
title: About Methods
description: About Methods
ms.assetid: BF2247BB-207F-4f94-9AF3-5EDE71BDA489
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About Methods

Methods enable you to access functionality within the HTML Help ActiveX control through the use of a scripting language, such as JavaScript or Visual Basic Scripting Edition. Generally, methods use the information specified in the [&lt;PARAM&gt;](html-help-activex-control-syntax.md) tags of the specified HTML Help ActiveX control to determine what functionality is actually to be invoked.

The following example uses the [Click](click-and-hhclick-method.md) method to invoke a [command](about-commands.md):


```
<A HREF=JavaScript:<i>related</i>.Click()<Example>/A> 
```



where JavaScript is the scripting language, related is the ID of the HTML Help ActiveX control being referenced, Click() is the method, and Example is the text link. The **Click()** method requires that the control contain &lt;PARAM&gt; tags that specify which command to invoke.

Some methods do not require any parameters to access functionality within the HTML Help ActiveX control. In these cases, if &lt;PARAM&gt; tags are present in a referenced control, they are ignored by the method being called. This lets you reuse an existing instance of the control in your HTML file.

In addition, you can call multiple methods from a single instance of the HTML Help ActiveX control. For example, if you are already using an instance of the control to call the [Related Topics](related-topics.md) command, you can reference the ID of that same control to call the [TextPopup](textpopup-method.md) method.

If you need to [insert](inserting-the-html-help-activex-control.md) a new instance of the control to call a method that does not require parameters, you can omit the &lt;PARAM&gt; tags from the &lt;OBJECT&gt; tag as shown in the following example:


```
<OBJECT
id=<i>for_script</i>
type="application/x-oleobject"
classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
>
</OBJECT>
```



where for\_script is the ID of the HTML Help ActiveX control that you will reference to call a method. Methods that do not require &lt;PARAM&gt; tags are listed in the table, below.

**Methods quick reference**



| Method                                  | Use with a compiled help file | Use with uncompiled HTML files | Does not require &lt;PARAM&gt; tags |
|-----------------------------------------|-------------------------------|--------------------------------|-------------------------------------|
| [Click](click-and-hhclick-method.md)   | **X**                         | **X**                          |                                     |
| [HHClick](click-and-hhclick-method.md) | **X**                         | **X**                          |                                     |
| [Print](print-method.md)               | **X**                         | **X**                          |                                     |
| [SyncURL](syncurl-method.md)           | **X**                         |                                |                                     |
| [TCard](tcard-method.md)               | **X**                         |                                |                                     |
| [TextPopup](textpopup-method.md)       | **X**                         | **X**                          | **X**                               |



 

## Related topics

<dl> <dt>

[About the HTML Help ActiveX Control](html-help-activex-control-overview.md)
</dt> </dl>

 

 





---
title: Inserting the HTML Help ActiveX Control
description: Inserting the HTML Help ActiveX Control
ms.assetid: '5F862AA3-D7C6-4085-A8E3-15440BD3816B'
---

# Inserting the HTML Help ActiveX Control

You can add the HTML Help ActiveX control to an HTML file by using the standard HTML &lt;OBJECT&gt; tag. The &lt;OBJECT&gt; tag includes a set of parameters that you use to specify which data the control should use, and to control the appearance and behavior of the control.

Whether you use the control in a compiled help (.chm) file or in uncompiled HTML files, you can insert the control using the HTML Help ActiveX Control Wizard, or you can insert it manually, by typing the appropriate [&lt;OBJECT&gt;](html-help-activex-control-syntax.md) tag code.

## Inserting the control using HTML Help Workshop

Use the HTML Help ActiveX Control Wizard, which is included in the HTML Help Workshop, to author any of the [commands](about-commands.md) in an HTML file.

To use the HTML Help ActiveX Control Wizard, start HTML Help Workshop, and then open an HTML file. Position your cursor anywhere between the &lt;BODY&gt; start and end tags, and then click **HTML Help ActiveX Control**.



|                        |                                                                                                                          |
|------------------------|--------------------------------------------------------------------------------------------------------------------------|
| ![](images/sb-wiz.gif) | Opens the HTML Help ActiveX Control Wizard, which enables you to insert or edit the control in an HTML file. <br/> |



 

To edit an existing instance of the control, position your cursor anywhere within the &lt;OBJECT&gt; start and end tags of the control, and then click **HTML Help ActiveX Control**.

## Inserting the control manually

The easiest way to work with the control is to insert it using the HTML Help ActiveX Control Wizard. However, you can also copy an existing instance of the control from one HTML file into another. You can then edit the [&lt;OBJECT&gt;](html-help-activex-control-syntax.md) tag code manually.

When you copy an existing control, make sure to copy all the text from the start &lt;OBJECT&gt; tag through the end &lt;/OBJECT&gt; tag. You should then paste the text anywhere between the &lt;BODY&gt; start and end tags of an HTML file.

## Note

Never omit the &lt;PARAM&gt; tag from the HTML Help ActiveX control &lt;OBJECT&gt; tag, as this may result in unexpected behavior.

## Related topics

<dl> <dt>

[About the HTML Help ActiveX Control](html-help-activex-control-overview.md)
</dt> </dl>

 

 






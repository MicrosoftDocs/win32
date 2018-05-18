---
title: HTML Help ActiveX Control Syntax
description: HTML Help ActiveX Control Syntax
ms.assetid: 'BD2CAA6F-0942-4ca6-AA45-9FC1F9022462'
---

# HTML Help ActiveX Control Syntax

All of the code required for an instance of the HTML Help ActiveX control is contained within the HTML &lt;OBJECT&gt; start and end tags. Use the &lt;OBJECT&gt; tag to specify a [command](about-commands.md), such as **Splash** or **Contents**, and to call a [method](about-methods.md), such as **Click** or [TextPopup](textpopup-method.md).

Using the HTML Help ActiveX Control Wizard in HTML Help Workshop, you can [insert](inserting-the-html-help-activex-control.md) the basic syntax automatically.

## Coding the HTML &lt;OBJECT&gt; tag

The &lt;OBJECT&gt; tag enables you to embed the HTML Help ActiveX control directly in a file. The attributes in the following table are required by the control.



| Attribute                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ID**                            | Specifies the name by which the HTML Help ActiveX control will be known to the HTML file. The default ID is **HHCTRL**, but you can specify any name you want. For example, if you entered **Test** as the ID, you would use that same ID to refer to the control from a script.<br/> If you use multiple instances of the HTML Help ActiveX control in a file, each instance must have a unique ID.<br/>                                                 |
| **TYPE**                          | Specifies the MIME type for the object. The HTML Help ActiveX control TYPE is **application/x-oleobject**.                                                                                                                                                                                                                                                                                                                                                            |
| **CLASSID**                       | Uniquely identifies the HTML Help ActiveX control from other ActiveX controls. The HTML Help ActiveX control identifier is the registry key number and is the same for every instance of the control that you use. The HTML Help ActiveX control **CLASSID** is:<br/> **clsid:52a2aaae-085d-4187-97ea-8c30db990436**.<br/>                                                                                                                                |
| **CODEBASE**                      | Specifies the version number of the HTML Help ActiveX control. Enables the automatic download mechanism of ActiveX controls and full version checking.                                                                                                                                                                                                                                                                                                                |
| [PARAM](coding-the-param-tag.md) | The PARAM attribute, which is also an HTML tag with attributes specific to it, lists a sequence of **NAME** and **VALUE** attribute pairs that are passed to the HTML Help ActiveX control to specify which HTML Help feature to provide and how to provide it. This attribute is required for all instances of the HTML Help ActiveX Control. Omitting the &lt;PARAM&gt; tag from an HTML Help ActiveX control &lt;OBJECT&gt; tag may result in unexpected behavior. |



 

## Notes

-   Several standard &lt;OBJECT&gt; tag attributes, such as **ALIGN**, **BORDER**, **CODETYPE**, **DECLARE**, **HEIGHT**, **HSPACE**, **NAME**, **SHAPES**, **STANDBY**, **USEMAP**, **VSPACE**, and **WIDTH**, can also be used to define the appearance and position of the HTML Help ActiveX control.
-   **WIDTH** and **HEIGHT** values can be expressed in percentage, followed by a percent sign, or in pixels (numeric value only).
-   The HTML Help ActiveX control does not support the &lt;OBJECT&gt; tag **DATA** attribute.

 

 






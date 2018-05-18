---
title: Button Parameter
description: Use the Button parameter to create a button that will invoke a command when clicked. You can select from several button styles.
ms.assetid: 'CB62D205-5B75-413d-9696-1DF38B92D368'
---

# Button Parameter

Use the **Button** parameter to create a button that will invoke a command when clicked. You can select from several button styles.

## Applies to

-   [ALink](alink.md)
-   [Close](close.md)
-   [HH Version](hh-version.md)
-   [KLink](klink.md)
-   [Related Topics](related-topics.md)
-   [Shortcut](shortcut.md)
-   [TCard](tcard.md)
-   [WinHelp](winhelp.md)

## Valid Values

The following table shows the syntax used to create various types of buttons.



| Syntax                                                         | Description                  | Notes                                                                                                              |
|----------------------------------------------------------------|------------------------------|--------------------------------------------------------------------------------------------------------------------|
| &lt;PARAM name="Button" value="Text:*button text*"&gt;         | Button with a text label.    | You can enter text of any length for the label. The text will not wrap.                                            |
| &lt;PARAM name="Button" value=""&gt;                           | "Chiclet" button.            | To specify a chiclet button, you can remove the Button parameter entirely or use empty quotation marks (value=""). |
| &lt;PARAM name="Button" value="Bitmap:shortcut"&gt;            | Button with a shortcut icon. | ...                                                                                                                |
| &lt;PARAM name="Button" value="Bitmap:*path to .bmp file*"&gt; | Button with a bitmap image.  | You can specify an absolute or relative path.                                                                      |
| &lt;PARAM name="Button" value="Icon:*path to .ico file*"&gt;   | Button with an icon.         | You can specify an absolute or relative path.                                                                      |



 

## Example

The following example uses a button with a bitmap image to call the [HH Version](hh-version.md) command.


```
<OBJECT
   id=bitmap
   type="application/x-oleobject"
   classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
   codebase="Hhctrl.ocx#Version=5,02,3790,1194"
   width=100
   height=100
>
   <PARAM name="Command" value="HH Version">
   <PARAM name="Button" value="Bitmap:bmpbutton.bmp">
</OBJECT>
```



## Remarks

-   You can invoke a command using the [Click](click-and-hhclick-method.md) method instead of a button.
-   Be sure to include all graphic files in the \[FILES\] section of your HTML Help project (.hhp) file.

## Related topics

<dl> <dt>

[About Parameters](parameters.md)
</dt> </dl>

 

 





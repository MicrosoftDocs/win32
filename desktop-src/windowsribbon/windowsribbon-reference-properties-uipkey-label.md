---
title: UI_PKEY_Label
description: Identifies the UI\_PKEY\_Label property.
ms.assetid: 4d704133-bba7-4c32-a552-d748b66455eb
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_Label

Identifies the UI\_PKEY\_Label property.

```
propertyDescription
   name = UI_PKEY_Label
   shellPKey = UI_PKEY_Label
   formatID = 00000004-7363-696e-8441798acf5aebb7
   propID = 4
   typeInfo
      type = VT_LPWSTR
```

## Remarks

UI\_PKEY\_Label is used by an application to query the label text of tabs, groups, buttons, gallery items, and other Ribbon controls.

> [!Note]  
> Windows 8 and newer: [Application Menu](windowsribbon-controls-applicationmenu.md) button image changed to label: **File**. We recommend that you do not use File as the label for any of your own tabs.

 

The property value is a string constrained to any sequence of characters, including white space and line-break characters.

> [!Note]  
> Use the Universal Character Set (UCS) XML character reference `&#xA;` to specify a line break.

 

Right alignment is not supported.

The maximum length of UI\_PKEY\_Label is unbounded.

If a Command is exposed through a menu item and the value of [**Command.LabelTitle**](windowsribbon-element-command-labeltitle.md) or UI\_PKEY\_Label contains a letter preceded by an ampersand, as shown in the following example, this letter is treated as both a keytip and a keyboard accelerator for that Command by the Ribbon framework.


```XML
<Command Name="cmdNew"
         Symbol="ID_FILE_NEW"
         Comment="New"
         Id="25001"
         LabelTitle="&amp;New"/>
```



To display an ampersand in a label, escape the special character designation with a double ampersand (`&&`) as shown in the following example.


```XML
<Command Name="cmdOpen"
         Symbol="ID_FILE_OPEN"
         Comment="Open"
         Id="25002"
         LabelTitle="&amp;&amp;Open"/>
```



## Related topics

<dl> <dt>

[Resource Properties](windowsribbon-reference-properties-resource.md)
</dt> <dt>

[**Command.LabelTitle**](windowsribbon-element-command-labeltitle.md)
</dt> <dt>

[UI\_PKEY\_LabelDescription](windowsribbon-reference-properties-uipkey-labeldescription.md)
</dt> </dl>

 

 





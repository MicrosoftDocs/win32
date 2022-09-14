---
title: UI_PKEY_Keytip
description: Identifies the UI\_PKEY\_Keytip property.
ms.assetid: 7af4abcb-abb0-466a-bc58-274fa18b79af
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_Keytip

Identifies the UI\_PKEY\_Keytip property.

```
propertyDescription
   name = UI_PKEY_Keytip
   shellPKey = UI_PKEY_Keytip
   formatID = 00000003-7363-696e-8441798acf5aebb7
   propID = 3
   typeInfo
      type = VT_LPWSTR
```

## Remarks

UI\_PKEY\_Keytip is used by an application to query the keyboard accelerator of a ribbon control.

This property value is a string, composed of any sequence of characters including white space.

The value of UI\_PKEY\_Keytip acts as the keyboard accelerator for a Command unless that Command is exposed through a menu item. In this case, the framework ignores the UI\_PKEY\_Keytip value and instead uses a character preceded by an ampersand as specified by [**Command.LabelTitle**](windowsribbon-element-command-labeltitle.md) or [UI\_PKEY\_Label](windowsribbon-reference-properties-uipkey-label.md). If no ampersand is specified by **Command.LabelTitle** or UI\_PKEY\_Label, no keytip or keyboard accelerator is exposed.

The maximum length of UI\_PKEY\_Keytip is unbounded.

## Related topics

<dl> <dt>

[Resource Properties](windowsribbon-reference-properties-resource.md)
</dt> <dt>

[**Command.Keytip**](windowsribbon-element-command-keytip.md)
</dt> </dl>

 

 





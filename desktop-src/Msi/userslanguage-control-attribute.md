---
description: If this bit flag is set, fonts are created using the user's default UI code page. If the bit flag is not set, fonts are created using the database code page.
ms.assetid: 6a3dbabe-6a14-4401-b46c-e8a0bd0cbe63
title: UsersLanguage Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# UsersLanguage Control Attribute

If this bit flag is set, fonts are created using the user's default UI code page. If the bit flag is not set, fonts are created using the database code page.

## Valid Controls

[Text](text-control.md)

 

[ListBox](listbox-control.md)

 

[ComboBox](combobox-control.md)

## Value



| Decimal | Hexadecimal | Constant                                |
|---------|-------------|-----------------------------------------|
| 1048576 | 0x00100000  | **msidbControlAttributesUsersLanguage** |



 

## Remarks

This control attribute can be used to display text that the user has entered into an [Edit](edit-control.md) or [PathEdit](pathedit-control.md) control.

The Edit control, PathEdit control, [DirectoryList control](directorylist-control.md) and [DirectoryCombo control](directorycombo-control.md) always use the fonts created in the user's default UI code page. This can cause problems if additional languages have been installed on the operating system. In this case, the fonts on the computer may not be able to represent all the characters in the added languages. To determine what fonts can be used, look up the values in **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\FontLink\\SystemLink**.

For more information, see [Control Attributes](control-attributes.md) and [Controls](controls.md).

 

 




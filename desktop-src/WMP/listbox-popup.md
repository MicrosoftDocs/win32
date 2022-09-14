---
title: LISTBOX.popUp
description: The popUp attribute specifies a value indicating whether the element represents a popup or list box control.
ms.assetid: b0ade23a-6164-4dd4-b599-43ea1fcd44e4
keywords:
- LISTBOX.popUp Windows Media Player
topic_type:
- apiref
api_name:
- LISTBOX.popUp
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# LISTBOX.popUp

The **popUp** attribute specifies a value indicating whether the element represents a popup or list box control.

``` syntax
<ELEMENT popUp="value">
```

## Possible Values

This attribute is a **Boolean** specified at design time only.



| Value | Description                                |
|-------|--------------------------------------------|
| true  | The element represents a popup control.    |
| false | The element represents a list box control. |



 

## Remarks

The **POPUP** element represents a list box control that is displayed only when needed. It is identical to the **LISTBOX** element except for the default value of this attribute, which changes the display behavior. For **LISTBOX** elements, the default value is false. For **POPUP** elements, the default value is true. Instead of specifying this attribute, the **LISTBOX** or **POPUP** element should be used to according to the desired behavior.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later<br/> |



## See also

<dl> <dt>

[**LISTBOX Element**](listbox-element.md)
</dt> <dt>

[**POPUP Element**](popup-element.md)
</dt> </dl>

 

 






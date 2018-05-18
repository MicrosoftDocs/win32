---
title: UiaNameLengthTooLong
description: UiaNameLengthTooLong
ms.assetid: '01AF3F1E-9A3F-48B4-8219-6E80BAFC82EE'
keywords: ["UIA_NamePropertyId identifier AutomationElement.NameProperty"]
---

# UiaNameLengthTooLong

## Text

Element's name should not return a string longer than {0} character

## Type

Error

## Description

The name of an element contains too many characters. For example, the [**IUIAutomationElement::CurrentName**](uiauto-iuiautomationelement-currentname.md) method used to retrieve the UIA name of an element returns a string greater than the limit.

This issue causes problems for people who rely on a screen-reader and keyboard for navigation because an element might have an unpronounceable, non-intuitive name.

## Possible causes

The element or its parent has an incorrectly assigned name or label.

## Related topics

<dl> <dt>

[**UIA\_NamePropertyId**](uiauto-automation-element-propids.md#uia-namepropertyid)
</dt> <dt>

[**IUIAutomationElement::CurrentName**](uiauto-iuiautomationelement-currentname.md)
</dt> </dl>

 

 





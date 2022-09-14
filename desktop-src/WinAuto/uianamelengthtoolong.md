---
title: UiaNameLengthTooLong
description: UiaNameLengthTooLong
ms.assetid: 01AF3F1E-9A3F-48B4-8219-6E80BAFC82EE
keywords:
- UIA_NamePropertyId identifier AutomationElement.NameProperty
ms.topic: article
ms.date: 05/31/2018
---

# UiaNameLengthTooLong

## Text

Element's name should not return a string longer than {0} character

## Type

Error

## Description

The name of an element contains too many characters. For example, the [**IUIAutomationElement::CurrentName**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentname) method used to retrieve the UIA name of an element returns a string greater than the limit.

This issue causes problems for people who rely on a screen-reader and keyboard for navigation because an element might have an unpronounceable, non-intuitive name.

## Possible causes

The element or its parent has an incorrectly assigned name or label.

## Related topics

<dl> <dt>

[**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)
</dt> <dt>

[**IUIAutomationElement::CurrentName**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentname)
</dt> </dl>

 

 





---
title: UiaNameShouldNotContainControlType
description: UiaNameShouldNotContainControlType
ms.assetid: 96F7A5FC-1879-4706-9E67-5B43D57F7281
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UiaNameShouldNotContainControlType

## Text

Element's Name ({0}) should not contain the text of the ControlType ({1})

## Type

Warning

## Description

The name of an element incorporates its UIA control type. For example, this warning can occur if the UIA Name property for an element with the Button control type is set to "My Button".

This issue causes problems for people who rely on a screen-reader and keyboard for navigation because the control type will be read twice, or it may be unpronounceable or non-intuitive for users.

## Possible causes

-   The element or its parent has an incorrectly assigned name or label.
-   The element or its parent has a default name that has not been revised to a friendly name. For example, button1.
-   A developer is not aware that screen readers read names and control types.

## Related topics

<dl> <dt>

[**UIA\_NamePropertyId**](uiauto-automation-element-propids.md#uia-namepropertyid)
</dt> <dt>

[**IUIAutomationElement::CurrentName**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentname?branch=master)
</dt> </dl>

 

 





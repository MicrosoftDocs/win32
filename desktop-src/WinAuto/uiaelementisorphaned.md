---
title: UiaElementIsOrphaned
description: UiaElementIsOrphaned
ms.assetid: 'F85F08E7-5A9C-4F08-B680-8B251D51168A'
---

# UiaElementIsOrphaned

## Text

Element is an orphaned AutomationElement in the tree

## Type

Error

## Description

The address of the object's [**IUIAutomationElement**](uiauto-iuiautomationelement.md) interface obtained for the given coordinates is a reference to an orphaned element in the element tree.

This issue is a problem for people who rely on a screen-reader and keyboard for navigation because elements will be treated as invisible and will not be announced to the user.

## Possible causes

-   User interaction during verification, such as moving focus to a non-target HWND, interfered with the verification process.
-   An incorrect or invalid UI Automation implementation.

## Related topics

<dl> <dt>

[**IUIAutomationElement.ElementFromPoint**](uiauto-iuiautomation-elementfrompoint.md)
</dt> </dl>

 

 





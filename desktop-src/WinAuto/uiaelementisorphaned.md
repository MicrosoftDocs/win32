---
title: UiaElementIsOrphaned
description: UiaElementIsOrphaned
ms.assetid: F85F08E7-5A9C-4F08-B680-8B251D51168A
ms.topic: article
ms.date: 05/31/2018
---

# UiaElementIsOrphaned

## Text

Element is an orphaned AutomationElement in the tree

## Type

Error

## Description

The address of the object's [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) interface obtained for the given coordinates is a reference to an orphaned element in the element tree.

This issue is a problem for people who rely on a screen-reader and keyboard for navigation because elements will be treated as invisible and will not be announced to the user.

## Possible causes

-   User interaction during verification, such as moving focus to a non-target HWND, interfered with the verification process.
-   An incorrect or invalid UI Automation implementation.

## Related topics

<dl> <dt>

[**IUIAutomationElement.ElementFromPoint**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfrompoint)
</dt> </dl>

 

 





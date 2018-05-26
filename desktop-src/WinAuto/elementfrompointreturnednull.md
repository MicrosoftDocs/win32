---
title: ElementFromPointReturnedNull
description: ElementFromPointReturnedNull
ms.assetid: DBCA6705-BDFD-4024-A505-4539F72A9421
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ElementFromPointReturnedNull

## Text

IUIAutomation.ElementFromPoint({0}, {1}) returned null

## Type

Error

## Description

The address of the UI element's [**IUIAutomationElement**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement?branch=master) object obtained for the given coordinates is NULL.

## Possible causes

-   User interaction during verification, such as moving focus to a non-target HWND, interfered with the verification process.
-   An incorrect or invalid UI Automation implementation.

## Related topics

<dl> <dt>

[**IUIAutomation::ElementFromPoint**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfrompoint?branch=master)
</dt> </dl>

 

 





---
title: AppearsToNotSupportTabbing
description: AppearsToNotSupportTabbing
ms.assetid: AA0A982E-A342-4B49-B159-A2683C8F5CC4
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AppearsToNotSupportTabbing

## Text

The application appears to not support tabbing.

## Type

Error

## Description

The application doesn't support standard keyboard navigation (Tab or Shift+Tab).

This issue causes usability problems for people who rely on a screen reader or the keyboard for navigation because none of the elements in the application are discoverable.

## Possible causes

-   The application's UI framework doesn't support MSAA.
-   MSAA is not implemented on any control in the application.

## Related topics

<dl> <dt>

[Guidelines for Keyboard User Interface Design](dnacc-guidelines_for_keyboard_user_interface_design)
</dt> </dl>

 

 





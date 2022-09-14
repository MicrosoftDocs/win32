---
title: TabbingNotCyclic
description: TabbingNotCyclic
ms.assetid: F6BCC613-1EA1-438C-AC09-8A282870E021
ms.topic: article
ms.date: 05/31/2018
---

# TabbingNotCyclic

## Text

The tabbing in this application is not cyclic. Tabbing forwards or backwards {0} times doesn't come back to the same control.

## Type

Error

## Description

When using standard keyboard navigation (Tab or Shift+Tab), it isn't possible to traverse the element tree of the verification target until the starting element becomes the ending element (using the same number of keystrokes) by reversing the direction of traversal. For example, tabbing forward (Tab) x times from element A(0) to element A(x) and then tabbing backward (Shift+Tab) x times does not result in element A(0) regaining focus.

This issue causes problems for people who rely on a screen-reader and keyboard for navigation because there is no predictable way to return to a control after it has been visited.

## Possible causes

-   The element or its parent is a custom control that doesn't implement tabbing correctly. For example, the MSAA State property isn't set correctly.
-   Some applications, such as the Notepad, exhibit this behavior innately.

## Related topics

<dl> <dt>

[Guidelines for Keyboard User Interface Design](/previous-versions/windows/desktop/dnacc/guidelines-for-keyboard-user-interface-design)
</dt> </dl>

 

 
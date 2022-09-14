---
title: TreeTooDeep
description: TreeTooDeep
ms.assetid: 3FD4A1BE-4710-4A1F-9ED7-98D7FCBCD304
ms.topic: article
ms.date: 05/31/2018
---

# TreeTooDeep

## Text

Tree is {0} levels deep.

## Type

Warning

## Description

The element tree might be too deep.

This issue causes problems for people who rely on a screen-reader and keyboard for navigation because traversing elements will seem to take a long time and may appear cyclic.

## Possible causes

-   Multiple elements or their parents are custom controls that do not implement tabbing correctly. For example, the MSAA State property is not updated correctly.
-   The application UI is overly complex.

## Related topics

<dl> <dt>

[Guidelines for Keyboard User Interface Design](/previous-versions/windows/desktop/dnacc/guidelines-for-keyboard-user-interface-design)
</dt> <dt>

[Windows User Experience Interaction Guidelines - Keyboard](/#guidelines)
</dt> </dl>

 

 
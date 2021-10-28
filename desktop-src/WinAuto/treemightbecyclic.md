---
title: TreeMightBeCyclic
description: TreeMightBeCyclic
ms.assetid: 9A997949-A1A2-448C-9739-BE176621F1B4
ms.topic: article
ms.date: 05/31/2018
---

# TreeMightBeCyclic

## Text

Tree is {0} levels deep. This might indicate that the accessibility tree is cyclic, and thus it would appear to be infinite.

## Type

Error

## Description

The element tree is cyclic and the tree depth might be infinite.

This issue causes problems for people who rely on a screen-reader and keyboard for navigation because there will be no apparent limit to the traversal of elements in the target application.

## Possible causes

Multiple elements, or their parents, are custom controls that do not implement tabbing correctly. For example, the MSAA [State](state-property.md) property is not updated correctly.

## Related topics

<dl> <dt>

[Guidelines for Keyboard User Interface Design](/previous-versions/windows/desktop/dnacc/guidelines-for-keyboard-user-interface-design)
</dt> <dt>

[Windows User Experience Interaction Guidelines - Keyboard](/#guidelines)
</dt> </dl>

 

 
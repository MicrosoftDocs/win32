---
title: TabbingNotSymmetric
description: TabbingNotSymmetric
ms.assetid: 1E14ED9F-27C1-4054-B0A6-702167222196
ms.topic: article
ms.date: 05/31/2018
---

# TabbingNotSymmetric

## Text

Tabbing backwards and forwards does not yield the same element. Expected {0} but received {1}

## Type

Error

## Description

When using standard keyboard navigation (Tab or Shift+Tab), it isn't possible to repeat the path of traversal through the element tree of the verification target if the direction of traversal is reversed. For example, tabbing forward (Tab) x times from element A(0) to element A(x) and then tabbing backward (Shift+Tab) x times results in element A(0) regaining focus through a different set of intermediate elements.

This issue causes problems for people who rely on a screen-reader and keyboard for navigation because traversing elements appears erratic and unpredictable.

## Possible causes

-   Multiple elements or their parents are custom controls that don't implement tabbing correctly. For example, the MSAA State property is not set correctly.

## Related topics

<dl> <dt>

[Guidelines for Keyboard User Interface Design](/previous-versions/windows/desktop/dnacc/guidelines-for-keyboard-user-interface-design)
</dt> </dl>

 

 
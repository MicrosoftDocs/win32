---
title: MissingItemInTabOrder
description: MissingItemInTabOrder
ms.assetid: 49DE892E-1B15-4F46-B316-217CC76AA1A9
ms.topic: article
ms.date: 05/31/2018
---

# MissingItemInTabOrder

## Text

This element appears to be tabbable but is not in the tab order.

## Type

Error

## Description

A focusable element is not accessible using standard keyboard navigation (Tab or Shift+Tab). For example, the element has not been marked as a tab stop or assigned a tab index. This issue causes problems for people who rely on a screen-reader and keyboard for navigation because:

-   The element is not discoverable.
-   If the element is a child of a custom list control, cues indicating the child element can be navigated using the Arrow or Page keys may be missing.

## Possible causes

-   The MSAA role of the element or its parent is not set correctly. For example, if all list items in a list view control are not exposed through MSAA as a ROLE\_SYSTEM\_LISTITEM, the verification fails because the list items are not accessible using the Tab key.
-   The element or its parent is a custom control that doesn't implement tabbing correctly. For example, the MSAA State property is never set to STATE\_SYSTEM\_FOCUSABLE.
-   An element that acts as a container for other elements was selected for verification but does not support keyboard navigation itself. For example, a toolbar and its child elements are not accessible using the TAB key.

## Related topics

<dl> <dt>

[Guidelines for Keyboard User Interface Design](/previous-versions/windows/desktop/dnacc/guidelines-for-keyboard-user-interface-design)
</dt> </dl>

 

 
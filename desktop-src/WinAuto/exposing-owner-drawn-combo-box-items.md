---
title: Exposing Owner-Drawn Combo Box Items
description: Application developers do not need to implement IAccessible to expose the items in an owner-drawn combo box that has the style CBS\_HASSTRINGS because Microsoft Active Accessibility exposes the items in combo boxes with this style.
ms.assetid: 9ff14b2f-ae09-4839-b281-fba46addaf5f
ms.topic: article
ms.date: 05/31/2018
---

# Exposing Owner-Drawn Combo Box Items

Application developers do not need to implement [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) to expose the items in an owner-drawn combo box that has the style **CBS\_HASSTRINGS** because Microsoft Active Accessibility exposes the items in combo boxes with this style. The items in an owner-drawn combo box with the **CBS\_HASSTRINGS** style are displayed as text. However, this style is also used with owner-drawn combo boxes that do not display text so that the combo box items are exposed by Microsoft Active Accessibility.

To allow Microsoft Active Accessibility to expose the items in an owner-drawn combo box that does not display text:

-   Use the **CBS\_HASSTRINGS** style when creating the combo box.
-   Create a textual counterpart that names or describes each item in the combo box.
-   When adding items to the owner-drawn combo box, use the CB\_ADDSTRING message to add the text that you want Microsoft Active Accessibility to expose. This text is not displayed, so it must not be part of the owner-drawn data. Add the owner-drawn item data using the CB\_SETITEMDATA message.

When using the above method, note the following:

-   If you use the **CBS\_SORT** style, the combo box is sorted using the supplied strings and not the [WM\_COMPAREITEM](../controls/wm-compareitem.md) callback procedure.
-   With owner-drawn variable combo boxes created with the style **CBS\_OWNERDRAWVARIABLE**, use a global variable or some other mechanism to keep track of when the **itemData** member of the [MEASUREITEMSTRUCT](/windows/win32/api/winuser/ns-winuser-measureitemstruct) is valid. The global variable is required because the system sends the [WM\_MEASUREITEM](../controls/wm-measureitem.md) message as soon as the string is added but before the item data is attached, and at this point the **itemData** member is not valid.
-   To change the string for an item in a combo box with the **CBS\_HASSTRINGS** style, delete the item with the [CB\_DELETESTRING](../controls/cb-deletestring.md) message and add the new string with the [CB\_ADDSTRING](../controls/cb-addstring.md) message.

 

 
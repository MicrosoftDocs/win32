---
title: Exposing Owner-Drawn List Box Items
description: Application developers do not need to implement IAccessible to expose the items in an owner-drawn list box that has the style LBS\_HASSTRINGS because Microsoft Active Accessibility exposes the items in list boxes with this style.
ms.assetid: d54ce297-ce8a-46c0-a86d-4acffa1eda27
ms.topic: article
ms.date: 05/31/2018
---

# Exposing Owner-Drawn List Box Items

Application developers do not need to implement [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) to expose the items in an owner-drawn list box that has the style **LBS\_HASSTRINGS** because Microsoft Active Accessibility exposes the items in list boxes with this style. The items in an owner-drawn list box with the **LBS\_HASSTRINGS** style are displayed as text. However, this style is also used with owner-drawn list boxes that do not display text so that the list box items are exposed by Microsoft Active Accessibility.

To allow Microsoft Active Accessibility to expose the items in an owner-drawn list box that does not display text:

-   Use the **LBS\_HASSTRINGS** style when creating the list box.
-   Create a textual counterpart that names or describes each item in the list box.
-   When adding items to the owner-drawn list box, use the [LB\_ADDSTRING](../controls/lb-addstring.md) message to add the text that you want Microsoft Active Accessibility to expose. This text is not displayed, so it is not part of the owner-drawn data. Add the owner-drawn item data using the [LB\_SETITEMDATA](../controls/lb-setitemdata.md) message.

When using the above method, note the following:

-   If you use the **LBS\_SORT** style, the list box is sorted using the supplied strings and not the [WM\_COMPAREITEM](../controls/wm-compareitem.md) callback procedure.
-   With owner-drawn variable list boxes created with the style **LBS\_OWNERDRAWVARIABLE**, use a global variable or some other mechanism to keep track of when the **itemData member** of the [MEASUREITEMSTRUCT](/windows/win32/api/winuser/ns-winuser-measureitemstruct) is valid. The global variable is needed because the system sends the [WM\_MEASUREITEM](../controls/wm-measureitem.md) message as soon as the string is added but before the item data is attached, and at this point the **itemData** member is not valid.
-   To change the string for an item in a list box with the **LBS\_HASSTRINGS** style, delete the item with the [LB\_DELETESTRING](../controls/lb-deletestring.md) message and add the new string with the LB\_ADDSTRING message.

 

 
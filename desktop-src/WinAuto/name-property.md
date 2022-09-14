---
title: Name Property
description: The Name property is a string used by clients to identify, find, or announce an object for the user. All objects support the Name property.
ms.assetid: 7533955a-9538-4ead-a6ca-f61dd1b4d5c5
ms.topic: article
ms.date: 05/31/2018
---

# Name Property

The **Name** property is a string used by clients to identify, find, or announce an object for the user. All objects support the **Name** property.

For example, the text on a button control is its name, while the name for a list box or edit control is the static text that immediately precedes the control in the tabbing order. Even graphic objects that do not display a name provide text when queried for the **Name** property.

The **Name** property is retrieved by calling [**IAccessible::get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname).

## Selecting Names

An object's name should be intuitive so that users understand the object's meaning or purpose. Also, the **Name** property should be unique relative to any sibling objects in the parent.

Navigation within tables presents especially difficult problems for some users. Therefore, server developers should make table cell names as descriptive as possible. For example, you could create a cell name by combining the names of the row and column it occupies, such as "A1." However, it is generally better to use more descriptive names, such as "Nancy, February" where "Nancy" is the current row and "February" is the current column.

## Delegating Requests

If an object does not have access to its **Name** property, it delegates requests to its parent, identifying itself by its child ID. For example, if a client calls an edit control's **Name** property, the edit control delegates the query to its parent, which returns the value of the static text control that labels the edit control.

 

 





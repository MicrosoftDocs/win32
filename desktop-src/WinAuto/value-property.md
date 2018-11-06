---
title: Value Property
description: The Value property provides a textual representation of the visual information contained in an object. Not all objects support the Value property.
ms.assetid: 89b99645-31f5-458a-ae61-a72bf1338195
ms.topic: article
ms.date: 05/31/2018
---

# Value Property

The **Value** property provides a textual representation of the visual information contained in an object. Not all objects support the **Value** property.

The **Value** property is retrieved by calling [**IAccessible::get\_accValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accvalue).

The **Value** property tells the client about the visual information contained in an object. For example, an edit control's value is the text it contains, whereas a menu item has no value.

## Providing Hierarchical Information

The **Value** property provides hierarchical information in cases such as a tree view control. Although the parent object in the tree view control does not provide information in the **Value** property, each item within the control has a zero-based value that represents its level within the hierarchy. Top-level items have a value of zero, second-level items have a value of one, and so on.

 

 





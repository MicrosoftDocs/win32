---
title: Viewing Containers as Leaf Nodes
description: Any object in Active Directory Domain Services can be a container of other objects.
ms.assetid: 38300ca5-745a-4640-9723-6052a9843f45
ms.tgt_platform: multiple
keywords:
- Viewing Containers as Leaf Nodes
- containers AD , viewing as leaf nodes
- leaf AD , viewing containers as leaf nodes
ms.topic: article
ms.date: 05/31/2018
---

# Viewing Containers as Leaf Nodes

Any object in Active Directory Domain Services can be a container of other objects. This can clutter the user interface, so it is possible to declare that an object of a specific class be only be displayed as a leaf in the user interface. The **treatAsLeaf** attribute is a single-valued display specifier attribute that determines if objects of that class should be only be displayed as leaf objects. This attribute is a Boolean value that, if **TRUE**, indicates that objects of the class should only be displayed as leaf elements. If **FALSE**, indicates that objects of the class can be displayed as a container or a leaf. Like all display specifier attributes, the **treatAsLeaf** attribute is set on a per-locale basis, so this attribute can be localized as required. For example, the **User-Display** for the English locale (0409) display specifier has the **treatAsLeaf** attribute set to **TRUE** by default. This causes the user interface to display all **User** objects as leaf objects.

**To set the value of the **treatAsLeaf** attribute**

1.  Bind to the desired display attribute in the desired locale. For more information and a code example, see [DisplaySpecifiers Container](displayspecifiers-container.md).
2.  Use the [**IADs::Put**](/windows/desktop/api/iads/nf-iads-iads-put) method to set the **treatAsLeaf** attribute to either **TRUE** or **FALSE**.
3.  To commit changes to the directory, call the [**IADs::SetInfo**](/windows/desktop/api/iads/nf-iads-iads-setinfo) method.

 

 
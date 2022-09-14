---
title: DefaultAction Property
description: An object's DefaultAction property describes the object's primary method of manipulation from the user's viewpoint. An object's DefaultAction property should be a verb or a short verb phrase.
ms.assetid: 8242c0af-b42e-44a4-8807-d6740fa1a24a
ms.topic: article
ms.date: 05/31/2018
---

# DefaultAction Property

An object's **DefaultAction** property describes the object's primary method of manipulation from the user's viewpoint. An object's **DefaultAction** property should be a verb or a short verb phrase.

The **DefaultAction** property is retrieved by calling [**IAccessible::get\_accDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction).

To perform an object's default action, clients call [**IAccessible::accDoDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accdodefaultaction).

Not all objects have default actions, and some objects have a default action that is related to its [**Value**](value-property.md) property, such as in the following examples:

-   A selected check box has a default action of "Uncheck" and a value of "Checked."
-   A cleared check box has a default action of "Check" and a value of "Unchecked."
-   A button labeled "Print" has a default action of "Press," with no value.
-   A static text control or an edit control that shows "Printer" has no default action, but has a value of "Printer."

 

 





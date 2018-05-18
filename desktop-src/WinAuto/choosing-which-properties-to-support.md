---
title: Choosing Which Properties to Support
description: The IAccessible properties provide a way for server developers to describe a wide variety of user interface elements.
ms.assetid: 'c51fd8a1-dc23-4d64-8921-e0a795c3ffb8'
---

# Choosing Which Properties to Support

The [**IAccessible**](iaccessible.md) properties provide a way for server developers to describe a wide variety of user interface elements. But not all of the properties are applicable for every kind of user interface element. Additionally, some properties provide descriptive information that is useful but not essential.

Servers must support the following properties and methods for every object:

-   [**Name**](name-property.md)
-   [**Role**](role-property.md)
-   [**State**](state-property.md)
-   [**Location**](iaccessible-iaccessible--acclocation.md) and [**IAccessible::accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**Parent**](iaccessible-iaccessible--get-accparent.md) and [**IAccessible::accNavigate**](iaccessible-iaccessible--accnavigate.md)

The following properties and method must be supported if they are applicable to the object:

-   [**KeyboardShortcut**](keyboardshortcut-property.md)
-   [**Value**](value-property.md)

The following properties and method must be supported if the object has children:

-   [**Child**](iaccessible-iaccessible--get-accchild.md) and [**ChildCount**](iaccessible-iaccessible--get-accchildcount.md)
-   [**Focus, Selection**](selection-and-focus-properties-and-methods.md), and [**IAccessible::accSelect**](iaccessible-iaccessible--accselect.md)

The following properties are optional, but provide useful descriptive information about the object. The [**Description**](description-property.md) property is implemented to describe bitmaps and other images.

-   [**Description**](description-property.md)
-   [**DefaultAction**](defaultaction-property.md) and [**IAccessible::accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md)
-   [**Help**](help-property.md)
-   [**HelpTopic**](helptopic-property.md)

 

 





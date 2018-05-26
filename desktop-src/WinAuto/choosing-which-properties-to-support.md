---
title: Choosing Which Properties to Support
description: The IAccessible properties provide a way for server developers to describe a wide variety of user interface elements.
ms.assetid: c51fd8a1-dc23-4d64-8921-e0a795c3ffb8
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Choosing Which Properties to Support

The [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties provide a way for server developers to describe a wide variety of user interface elements. But not all of the properties are applicable for every kind of user interface element. Additionally, some properties provide descriptive information that is useful but not essential.

Servers must support the following properties and methods for every object:

-   [**Name**](name-property.md)
-   [**Role**](role-property.md)
-   [**State**](state-property.md)
-   [**Location**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master) and [**IAccessible::accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)
-   [**Parent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master) and [**IAccessible::accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)

The following properties and method must be supported if they are applicable to the object:

-   [**KeyboardShortcut**](keyboardshortcut-property.md)
-   [**Value**](value-property.md)

The following properties and method must be supported if the object has children:

-   [**Child**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchild?branch=master) and [**ChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master)
-   [**Focus, Selection**](selection-and-focus-properties-and-methods.md), and [**IAccessible::accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)

The following properties are optional, but provide useful descriptive information about the object. The [**Description**](description-property.md) property is implemented to describe bitmaps and other images.

-   [**Description**](description-property.md)
-   [**DefaultAction**](defaultaction-property.md) and [**IAccessible::accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master)
-   [**Help**](help-property.md)
-   [**HelpTopic**](helptopic-property.md)

 

 





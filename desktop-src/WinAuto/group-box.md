---
title: Group Box (MSAA UI Element Reference)
description: A group box is a rectangle that surrounds a set of controls, such as check boxes or radio buttons, and contains an application-defined text (label).
ms.assetid: c6cd81a1-76c0-41c5-bb7f-4796ea7e3114
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Group Box (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Group Box** objects for purposes of MSAA UI Element Reference. How to create **Group Box** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A group box is a rectangle that surrounds a set of controls, such as check boxes or radio buttons, and contains an application-defined text (label).

The sole purpose of a group box is to organize controls related by a common purpose, indicated by the label.

The window class name for a group box is "BUTTON".

## IAccessible Methods

A group box supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:

-   [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)
-   [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)
-   [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)

## IAccessible Properties

A group box supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master)             | The **ChildCount** property is always zero.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accKeyboardShortcut**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut?branch=master) | Group boxes do not have keyboard shortcuts. However, if the window text for the group box contains an ampersand (&) character, Microsoft Active Accessibility returns a non-Null string as the **KeyboardShortcut** property.                                                                                                                                                                                                                                            |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)                         | The **Name** property is obtained from the control's window text (or caption), which is displayed with the group box.                                                                                                                                                                                                                                                                                                                                                    |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                              |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)                         | The **Role** property is [**ROLE\_SYSTEM\_GROUPING**](object-roles.md#role-system-grouping).                                                                                                                                                                                                                                                                                                                                                                            |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> </dl>

 

 






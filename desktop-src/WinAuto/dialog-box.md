---
title: Dialog Box (MSAA UI Element Reference)
description: A dialog box is a temporary window that an application creates to retrieve user input.
ms.assetid: 7d132c2c-eab1-4132-b2b6-fa1f8b142f58
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Dialog Box (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Dialog Box** objects for purposes of MSAA UI Element Reference. How to create **Dialog Box** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A dialog box is a temporary window that an application creates to retrieve user input. An application uses dialog boxes to prompt the user for additional information about commands that the user has chosen from a menu. A dialog box contains one or more controls (child windows) with which the user enters text, chooses options, or directs the action of the command.

The window class name for dialog boxes is "\#32770".

## IAccessible Methods

A dialog box supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:



| Method                                                                    | Comments                                                                                                                                                                                                                                                                               |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) | If the dialog box contains a default push button, the [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) method calls [**PostMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644944) with the [**BM\_CLICK**](https://msdn.microsoft.com/library/windows/desktop/bb775985) button message to click the default push button. |
| [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)                 |                                                                                                                                                                                                                                                                                        |
| [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)               |                                                                                                                                                                                                                                                                                        |
| [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)               |                                                                                                                                                                                                                                                                                        |
| [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)                   |                                                                                                                                                                                                                                                                                        |



 

## IAccessible Properties

A dialog box supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master)                 | The **ChildCount** property is equal to the number of child window controls on the dialog box.                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction?branch=master)           | If the dialog box contains a default push button, the **DefaultAction** property is "Press".                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accKeyboardShortcut**](https://msdn.microsoft.com/library/windows/desktop/dd318482) | Typically, dialog boxes do not have keyboard shortcuts. If the window text for the dialog box contains an ampersand (&) character, Microsoft Active Accessibility returns a non-Null string as the **KeyboardShortcut** property.                                                                                                                                                                                                                                        |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)                             | The **Name** property is the window text, or caption, that is displayed in the title bar of the dialog box.                                                                                                                                                                                                                                                                                                                                                              |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)                         | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the dialog box and has the same **Name** property and window class name as the dialog box.                                                                                                                                                                                                                                                        |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)                             | The **Role** property is [**ROLE\_SYSTEM\_DIALOG**](object-roles.md#role-system-dialog) or [**ROLE\_SYSTEM\_PROPERTYPAGE**](object-roles.md#role-system-propertypage).                                                                                                                                                                                                                                                                                                 |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)                           | The **State** property is a combination of one or more of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |



 

## Remarks

The dialog object does not support the [**get\_accChild**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchild?branch=master) method. To obtain an [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface pointer to a control on a dialog box, clients must obtain the window handle of the control and then call [**AccessibleObjectFromWindow**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromwindow?branch=master).

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> </dl>

 

 






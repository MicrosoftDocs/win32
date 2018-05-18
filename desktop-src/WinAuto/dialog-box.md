---
title: Dialog Box (MSAA UI Element Reference)
description: A dialog box is a temporary window that an application creates to retrieve user input.
ms.assetid: '7d132c2c-eab1-4132-b2b6-fa1f8b142f58'
---

# Dialog Box (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Dialog Box** objects for purposes of MSAA UI Element Reference. How to create **Dialog Box** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A dialog box is a temporary window that an application creates to retrieve user input. An application uses dialog boxes to prompt the user for additional information about commands that the user has chosen from a menu. A dialog box contains one or more controls (child windows) with which the user enters text, chooses options, or directs the action of the command.

The window class name for dialog boxes is "\#32770".

## IAccessible Methods

A dialog box supports the following [**IAccessible**](iaccessible.md) methods:



| Method                                                                    | Comments                                                                                                                                                                                                                                                                               |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) | If the dialog box contains a default push button, the [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) method calls [**PostMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644944) with the [**BM\_CLICK**](https://msdn.microsoft.com/library/windows/desktop/bb775985) button message to click the default push button. |
| [**accHitTest**](iaccessible-iaccessible--acchittest.md)                 |                                                                                                                                                                                                                                                                                        |
| [**accLocation**](iaccessible-iaccessible--acclocation.md)               |                                                                                                                                                                                                                                                                                        |
| [**accNavigate**](iaccessible-iaccessible--accnavigate.md)               |                                                                                                                                                                                                                                                                                        |
| [**accSelect**](iaccessible-iaccessible--accselect.md)                   |                                                                                                                                                                                                                                                                                        |



 

## IAccessible Properties

A dialog box supports the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)                 | The **ChildCount** property is equal to the number of child window controls on the dialog box.                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accDefaultAction**](iaccessible-iaccessible--get-accdefaultaction.md)           | If the dialog box contains a default push button, the **DefaultAction** property is "Press".                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accKeyboardShortcut**](https://msdn.microsoft.com/library/windows/desktop/dd318482) | Typically, dialog boxes do not have keyboard shortcuts. If the window text for the dialog box contains an ampersand (&) character, Microsoft Active Accessibility returns a non-Null string as the **KeyboardShortcut** property.                                                                                                                                                                                                                                        |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)                             | The **Name** property is the window text, or caption, that is displayed in the title bar of the dialog box.                                                                                                                                                                                                                                                                                                                                                              |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)                         | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the dialog box and has the same **Name** property and window class name as the dialog box.                                                                                                                                                                                                                                                        |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)                             | The **Role** property is [**ROLE\_SYSTEM\_DIALOG**](object-roles.md#role-system-dialog) or [**ROLE\_SYSTEM\_PROPERTYPAGE**](object-roles.md#role-system-propertypage).                                                                                                                                                                                                                                                                                                 |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)                           | The **State** property is a combination of one or more of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |



 

## Remarks

The dialog object does not support the [**get\_accChild**](iaccessible-iaccessible--get-accchild.md) method. To obtain an [**IAccessible**](iaccessible.md) interface pointer to a control on a dialog box, clients must obtain the window handle of the control and then call [**AccessibleObjectFromWindow**](accessibleobjectfromwindow.md).

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 






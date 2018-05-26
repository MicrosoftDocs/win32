---
title: Push Button (MSAA UI Element Reference)
description: A push button is a small, rectangular object used to perform an action. For example, the OK and CANCEL buttons on a dialog box are push buttons.
ms.assetid: 26dbe4a0-4110-4569-bac6-fa0a95c785dd
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Push Button (MSAA UI Element Reference)

A push button is a small, rectangular object used to perform an action. For example, the **OK** and **CANCEL** buttons on a dialog box are push buttons.

The window class name for a push button is "BUTTON".

## IAccessible Methods

A push button supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:



| Method                                                                    | Comments                                                                                                     |
|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) | The [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) method clicks the push button. |
| [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)                 |                                                                                                              |
| [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)               |                                                                                                              |
| [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)               |                                                                                                              |
| [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)                   |                                                                                                              |



 

## IAccessible Properties

A push button supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchild?branch=master)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master)             | The **ChildCount** property is zero or more.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [**get\_accDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction?branch=master)       | The **DefaultAction** property is "Press".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accDescription**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdescription?branch=master)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accKeyboardShortcut**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut?branch=master) | The **KeyboardShortcut** property is the button's access key, which is an underlined character in the text of the button's window text. For example, "Alt+o" is the **KeyboardShortcut** property for an **OK** button.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accHelp**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acchelp?branch=master)                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accHelpTopic**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acchelptopic?branch=master)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)                         | The **Name** property is obtained from the control's window text (or caption), which is displayed in the push button. For example, "OK" is the **Name** property for an **OK** button.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)                         | The **Role** property is [**ROLE\_SYSTEM\_PUSHBUTTON**](object-roles.md#role-system-pushbutton).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable) \| [**STATE\_SYSTEM\_PRESSED**](object-state-constants.md#state-system-pressed) \| [**STATE\_SYSTEM\_DEFAULT**](object-state-constants.md#state-system-default)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> <dt>

[**Check Box**](check-box.md)
</dt> <dt>

[**Group Box**](group-box.md)
</dt> <dt>

[**Radio Button**](radio-button.md)
</dt> </dl>

 

 






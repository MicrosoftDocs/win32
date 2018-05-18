---
title: Push Button (MSAA UI Element Reference)
description: A push button is a small, rectangular object used to perform an action. For example, the OK and CANCEL buttons on a dialog box are push buttons.
ms.assetid: '26dbe4a0-4110-4569-bac6-fa0a95c785dd'
---

# Push Button (MSAA UI Element Reference)

A push button is a small, rectangular object used to perform an action. For example, the **OK** and **CANCEL** buttons on a dialog box are push buttons.

The window class name for a push button is "BUTTON".

## IAccessible Methods

A push button supports the following [**IAccessible**](iaccessible.md) methods:



| Method                                                                    | Comments                                                                                                     |
|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) | The [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) method clicks the push button. |
| [**accHitTest**](iaccessible-iaccessible--acchittest.md)                 |                                                                                                              |
| [**accLocation**](iaccessible-iaccessible--acclocation.md)               |                                                                                                              |
| [**accNavigate**](iaccessible-iaccessible--accnavigate.md)               |                                                                                                              |
| [**accSelect**](iaccessible-iaccessible--accselect.md)                   |                                                                                                              |



 

## IAccessible Properties

A push button supports the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](iaccessible-iaccessible--get-accchild.md)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)             | The **ChildCount** property is zero or more.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [**get\_accDefaultAction**](iaccessible-iaccessible--get-accdefaultaction.md)       | The **DefaultAction** property is "Press".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accDescription**](iaccessible-iaccessible--get-accdescription.md)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md) | The **KeyboardShortcut** property is the button's access key, which is an underlined character in the text of the button's window text. For example, "Alt+o" is the **KeyboardShortcut** property for an **OK** button.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accHelp**](iaccessible-iaccessible--get-acchelp.md)                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accHelpTopic**](iaccessible-iaccessible--get-acchelptopic.md)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)                         | The **Name** property is obtained from the control's window text (or caption), which is displayed in the push button. For example, "OK" is the **Name** property for an **OK** button.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)                         | The **Role** property is [**ROLE\_SYSTEM\_PUSHBUTTON**](object-roles.md#role-system-pushbutton).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable) \| [**STATE\_SYSTEM\_PRESSED**](object-state-constants.md#state-system-pressed) \| [**STATE\_SYSTEM\_DEFAULT**](object-state-constants.md#state-system-default)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> <dt>

[**Check Box**](check-box.md)
</dt> <dt>

[**Group Box**](group-box.md)
</dt> <dt>

[**Radio Button**](radio-button.md)
</dt> </dl>

 

 






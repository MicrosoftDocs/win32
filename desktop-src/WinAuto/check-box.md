---
title: Check Box (MSAA UI Element Reference)
description: Check boxes are used to enable or disable one or more features or options from a set, usually within a dialog box. Typically, a check box contains a small box with adjoining text. When an option is selected, a check mark appears in the box.
ms.assetid: 'cdbaa152-82c2-4a5b-82a8-fed9b8ed63b4'
---

# Check Box (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Check Box** objects for purposes of MSAA UI Element Reference. How to create **Check Box** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Check boxes are used to enable or disable one or more features or options from a set, usually within a dialog box. Typically, a check box contains a small box with adjoining text. When an option is selected, a check mark appears in the box.

The window class name for a check box is "BUTTON".

## IAccessible Methods

Check boxes support the following [**IAccessible**](iaccessible.md) methods:



| Method                                                                    | Comments                                                                                                                                                                                                                         |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) | The [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) method calls [**PostMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644944) with the [**BM\_CLICK**](https://msdn.microsoft.com/library/windows/desktop/bb775985) button message to click the check box. |
| [**accHitTest**](iaccessible-iaccessible--acchittest.md)                 |                                                                                                                                                                                                                                  |
| [**accLocation**](iaccessible-iaccessible--acclocation.md)               |                                                                                                                                                                                                                                  |
| [**accNavigate**](iaccessible-iaccessible--accnavigate.md)               |                                                                                                                                                                                                                                  |
| [**accSelect**](iaccessible-iaccessible--accselect.md)                   |                                                                                                                                                                                                                                  |



 

## IAccessible Properties

Check boxes support the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                        | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](iaccessible-iaccessible--get-accchild.md)                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)        | The **ChildCount** property is zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accDefaultAction**](iaccessible-iaccessible--get-accdefaultaction.md)  | The **DefaultAction** property of a check box depends on whether it is selected. A check box that is not selected has "Check" as its **DefaultAction**, and a check box that is selected has "UnCheck" as its **DefaultAction**. The **DefaultAction** for a three-state check box is "Toggle".                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**get\_accDescription**](iaccessible-iaccessible--get-accdescription.md)      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**accFocus**](iaccessible-iaccessible--get-accfocus.md)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md) | The **KeyboardShortcut** property is the check box's access key, which is an underlined character in the control's window text. This string contains the access key character appended to the string "Alt+".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**accHelp**](iaccessible-iaccessible--get-acchelp.md)                         | The **Name** property is obtained from the control's window text (or caption), which is displayed with the check box.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**accHelpTopic**](iaccessible-iaccessible--get-acchelptopic.md)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**accName**](iaccessible-iaccessible--get-accname.md)                         | The **Name** property is obtained from the control's window text (or caption), which is displayed with the check box.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**accParent**](iaccessible-iaccessible--get-accparent.md)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name property and window class name as the control.**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**accRole**](iaccessible-iaccessible--get-accrole.md)                         | The **Role** property is [**ROLE\_SYSTEM\_CHECKBUTTON**](object-roles.md#role-system-checkbutton).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [**accState**](iaccessible-iaccessible--get-accstate.md)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable) \| [**STATE\_SYSTEM\_MIXED**](object-state-constants.md#state-system-mixed) \| [**STATE\_SYSTEM\_CHECKED**](object-state-constants.md#state-system-checked) \| [**STATE\_SYSTEM\_NORMAL**](object-state-constants.md#state-system-normal)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 






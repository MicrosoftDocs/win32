---
title: Check Box (MSAA UI Element Reference)
description: Check boxes are used to enable or disable one or more features or options from a set, usually within a dialog box. Typically, a check box contains a small box with adjoining text. When an option is selected, a check mark appears in the box.
ms.assetid: cdbaa152-82c2-4a5b-82a8-fed9b8ed63b4
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Check Box (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Check Box** objects for purposes of MSAA UI Element Reference. How to create **Check Box** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Check boxes are used to enable or disable one or more features or options from a set, usually within a dialog box. Typically, a check box contains a small box with adjoining text. When an option is selected, a check mark appears in the box.

The window class name for a check box is "BUTTON".

## IAccessible Methods

Check boxes support the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:



| Method                                                                    | Comments                                                                                                                                                                                                                         |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) | The [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) method calls [**PostMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644944) with the [**BM\_CLICK**](https://msdn.microsoft.com/library/windows/desktop/bb775985) button message to click the check box. |
| [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)                 |                                                                                                                                                                                                                                  |
| [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)               |                                                                                                                                                                                                                                  |
| [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)               |                                                                                                                                                                                                                                  |
| [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)                   |                                                                                                                                                                                                                                  |



 

## IAccessible Properties

Check boxes support the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                        | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchild?branch=master)                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master)        | The **ChildCount** property is zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction?branch=master)  | The **DefaultAction** property of a check box depends on whether it is selected. A check box that is not selected has "Check" as its **DefaultAction**, and a check box that is selected has "UnCheck" as its **DefaultAction**. The **DefaultAction** for a three-state check box is "Toggle".                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**get\_accDescription**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdescription?branch=master)      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**accKeyboardShortcut**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut?branch=master) | The **KeyboardShortcut** property is the check box's access key, which is an underlined character in the control's window text. This string contains the access key character appended to the string "Alt+".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**accHelp**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acchelp?branch=master)                         | The **Name** property is obtained from the control's window text (or caption), which is displayed with the check box.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**accHelpTopic**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acchelptopic?branch=master)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)                         | The **Name** property is obtained from the control's window text (or caption), which is displayed with the check box.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name property and window class name as the control.**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)                         | The **Role** property is [**ROLE\_SYSTEM\_CHECKBUTTON**](object-roles.md#role-system-checkbutton).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [**accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable) \| [**STATE\_SYSTEM\_MIXED**](object-state-constants.md#state-system-mixed) \| [**STATE\_SYSTEM\_CHECKED**](object-state-constants.md#state-system-checked) \| [**STATE\_SYSTEM\_NORMAL**](object-state-constants.md#state-system-normal)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> </dl>

 

 






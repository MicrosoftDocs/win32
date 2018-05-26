---
title: Hot Key Control (MSAA UI Element Reference)
description: Hot key controls allow users to enter a combination of keystrokes used as a hot key, which enables them to perform an action quickly. A hot key control displays the keystrokes entered by the user and ensures that the user selects a valid key combination.
ms.assetid: 56c9fee4-f3d3-4f61-8587-bf80186aa5b3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Hot Key Control (MSAA UI Element Reference)

Hot key controls allow users to enter a combination of keystrokes used as a hot key, which enables them to perform an action quickly. A hot key control displays the keystrokes entered by the user and ensures that the user selects a valid key combination.

The window class name for a hot key control is HOTKEY\_CLASS, which is defined as "msctls\_hotkey32" in Commctrl.h.

## IAccessible Methods

Hot key controls support the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:

-   [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)
-   [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)
-   [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)
-   [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)

## IAccessible Properties

The Hot key controls support the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master)             | The **ChildCount** property is always zero.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accKeyboardShortcut**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut?branch=master) | The **KeyboardShortcut** property is the hot key control's access key, which is an underlined character in the text of the hot key control's label. The returned string contains the access key character appended to the string "Alt+".                                                                                                                                                                                                                                 |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)                         | The **Name** property is the text from a static text control that labels the hot key control.                                                                                                                                                                                                                                                                                                                                                                            |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                              |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)                         | The **Role** property is [**ROLE\_SYSTEM\_HOTKEYFIELD**](object-roles.md#role-system-hotkeyfield).                                                                                                                                                                                                                                                                                                                                                                      |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |
| [**get\_accValue**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accvalue?branch=master)                       | The **Value** property is a string that contains the text in the hot key field.                                                                                                                                                                                                                                                                                                                                                                                          |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> </dl>

 

 






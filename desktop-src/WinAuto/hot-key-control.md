---
title: Hot Key Control (MSAA UI Element Reference)
description: Hot key controls allow users to enter a combination of keystrokes used as a hot key, which enables them to perform an action quickly. A hot key control displays the keystrokes entered by the user and ensures that the user selects a valid key combination.
ms.assetid: '56c9fee4-f3d3-4f61-8587-bf80186aa5b3'
---

# Hot Key Control (MSAA UI Element Reference)

Hot key controls allow users to enter a combination of keystrokes used as a hot key, which enables them to perform an action quickly. A hot key control displays the keystrokes entered by the user and ensures that the user selects a valid key combination.

The window class name for a hot key control is HOTKEY\_CLASS, which is defined as "msctls\_hotkey32" in Commctrl.h.

## IAccessible Methods

Hot key controls support the following [**IAccessible**](iaccessible.md) methods:

-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)
-   [**accNavigate**](iaccessible-iaccessible--accnavigate.md)
-   [**accSelect**](iaccessible-iaccessible--accselect.md)

## IAccessible Properties

The Hot key controls support the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)             | The **ChildCount** property is always zero.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md) | The **KeyboardShortcut** property is the hot key control's access key, which is an underlined character in the text of the hot key control's label. The returned string contains the access key character appended to the string "Alt+".                                                                                                                                                                                                                                 |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)                         | The **Name** property is the text from a static text control that labels the hot key control.                                                                                                                                                                                                                                                                                                                                                                            |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                              |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)                         | The **Role** property is [**ROLE\_SYSTEM\_HOTKEYFIELD**](object-roles.md#role-system-hotkeyfield).                                                                                                                                                                                                                                                                                                                                                                      |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |
| [**get\_accValue**](iaccessible-iaccessible--get-accvalue.md)                       | The **Value** property is a string that contains the text in the hot key field.                                                                                                                                                                                                                                                                                                                                                                                          |



 

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 






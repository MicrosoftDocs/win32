---
title: Progress Bar Control (MSAA UI Element Reference)
description: Progress bar controls indicate the progress of a lengthy operation such as downloading a file from the Internet. Usually the progress is expressed as a percentage from zero (0) to one hundred (100).
ms.assetid: '9165d00e-b3f3-41cd-812c-cd39313460fa'
---

# Progress Bar Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Progress Bar Control** objects for purposes of MSAA UI Element Reference. How to create **Progress Bar Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Progress bar controls indicate the progress of a lengthy operation such as downloading a file from the Internet. Usually the progress is expressed as a percentage from zero (0) to one hundred (100).

The window class name for a progress bar control is PROGRESS\_CLASS, which is defined as "msctls\_progress" in Commctrl.h.

## IAccessible Methods

Progress bar controls support the following [**IAccessible**](iaccessible.md) methods:

-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)
-   [**accNavigate**](iaccessible-iaccessible--accnavigate.md)
-   [**accSelect**](iaccessible-iaccessible--accselect.md)

## IAccessible Properties

Progress bar controls support the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)             | The **ChildCount** property is zero.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md) | The **KeyboardShortcut** property is the progress bar's access key, which is an underlined character in the text of the label for the progress bar. The returned string contains the access key character appended to the string "Alt+".                                                                                                                                                                                                                                 |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)                         | The **Name** property is the text from a static text control that labels the progress bar.                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                              |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)                         | The **Role** property is [**ROLE\_SYSTEM\_PROGRESSBAR**](object-roles.md#role-system-progressbar).                                                                                                                                                                                                                                                                                                                                                                      |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |
| [**get\_accValue**](iaccessible-iaccessible--get-accvalue.md)                       | The **Value** property is a string from "0%" to "100%" that describes the progress.                                                                                                                                                                                                                                                                                                                                                                                      |



 

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 






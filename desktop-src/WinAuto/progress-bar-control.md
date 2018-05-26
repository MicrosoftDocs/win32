---
title: Progress Bar Control (MSAA UI Element Reference)
description: Progress bar controls indicate the progress of a lengthy operation such as downloading a file from the Internet. Usually the progress is expressed as a percentage from zero (0) to one hundred (100).
ms.assetid: 9165d00e-b3f3-41cd-812c-cd39313460fa
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Progress Bar Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Progress Bar Control** objects for purposes of MSAA UI Element Reference. How to create **Progress Bar Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Progress bar controls indicate the progress of a lengthy operation such as downloading a file from the Internet. Usually the progress is expressed as a percentage from zero (0) to one hundred (100).

The window class name for a progress bar control is PROGRESS\_CLASS, which is defined as "msctls\_progress" in Commctrl.h.

## IAccessible Methods

Progress bar controls support the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:

-   [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)
-   [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)
-   [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)
-   [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)

## IAccessible Properties

Progress bar controls support the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master)             | The **ChildCount** property is zero.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accKeyboardShortcut**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut?branch=master) | The **KeyboardShortcut** property is the progress bar's access key, which is an underlined character in the text of the label for the progress bar. The returned string contains the access key character appended to the string "Alt+".                                                                                                                                                                                                                                 |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)                         | The **Name** property is the text from a static text control that labels the progress bar.                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                              |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)                         | The **Role** property is [**ROLE\_SYSTEM\_PROGRESSBAR**](object-roles.md#role-system-progressbar).                                                                                                                                                                                                                                                                                                                                                                      |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |
| [**get\_accValue**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accvalue?branch=master)                       | The **Value** property is a string from "0%" to "100%" that describes the progress.                                                                                                                                                                                                                                                                                                                                                                                      |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> </dl>

 

 






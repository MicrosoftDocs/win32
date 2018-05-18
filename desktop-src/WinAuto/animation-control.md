---
title: Animation Control (MSAA UI Element Reference)
description: Animation controls silently display an audio video interleaved (AVI) clip. Animation controls are usually displayed when files are being copied or when some other time-consuming task is being performed.
ms.assetid: '2a31d4ba-a1bd-478b-86a9-726fa93ab714'
---

# Animation Control (MSAA UI Element Reference)

Animation controls silently display an audio video interleaved (AVI) clip. Animation controls are usually displayed when files are being copied or when some other time-consuming task is being performed.

The window class name for an animation control is ANIMATE\_CLASS, which is defined as "SysAnimate32" in Commctrl.h.

## IAccessible Methods

Animation controls support the following [**IAccessible**](iaccessible.md) methods:

-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)
-   [**accNavigate**](iaccessible-iaccessible--accnavigate.md)
-   [**accSelect**](iaccessible-iaccessible--accselect.md)

## IAccessible Properties

Animation controls support the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)             | The **ChildCount** property is zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**get\_accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md) | Animation controls do not have keyboard shortcuts. However, if the label for the control contains an access key (an underlined character in the text of the control's label), [**get\_accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md) returns a non-NULL string. This string contains the access key character appended to the string "Alt+". For example, if the label is "Downloading Files", **KeyboardShortcut** is "Alt+d".                                                                                        |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)                         | The **Name** property is obtained from the static text control that labels the animation control. When creating controls, server developers must ensure that a static text control immediately precedes the control that it labels within the tab order.                                                                                                                                                                                                                                                                                             |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)                         | The **Role** property is [**ROLE\_SYSTEM\_ANIMATION**](object-roles.md#role-system-animation).                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)                       | The **State** property is a combination of one or more of the following object state constants: [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_ANIMATED**](object-state-constants.md#state-system-animated)<br/> For more information, see [Object State Constants](object-state-constants.md).<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 






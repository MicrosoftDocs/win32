---
title: Animation Control (MSAA UI Element Reference)
description: Animation controls silently display an audio video interleaved (AVI) clip. Animation controls are usually displayed when files are being copied or when some other time-consuming task is being performed.
ms.assetid: 2a31d4ba-a1bd-478b-86a9-726fa93ab714
ms.topic: article
ms.date: 05/31/2018
---

# Animation Control (MSAA UI Element Reference)

Animation controls silently display an audio video interleaved (AVI) clip. Animation controls are usually displayed when files are being copied or when some other time-consuming task is being performed.

The window class name for an animation control is ANIMATE\_CLASS, which is defined as "SysAnimate32" in Commctrl.h.

## IAccessible Methods

Animation controls support the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:

-   [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)
-   [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)
-   [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)
-   [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect)

## IAccessible Properties

Animation controls support the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount)             | The **ChildCount** property is zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**get\_accKeyboardShortcut**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut) | Animation controls do not have keyboard shortcuts. However, if the label for the control contains an access key (an underlined character in the text of the control's label), [**get\_accKeyboardShortcut**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut) returns a non-NULL string. This string contains the access key character appended to the string "Alt+". For example, if the label is "Downloading Files", **KeyboardShortcut** is "Alt+d".                                                                                        |
| [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)                         | The **Name** property is obtained from the static text control that labels the animation control. When creating controls, server developers must ensure that a static text control immediately precedes the control that it labels within the tab order.                                                                                                                                                                                                                                                                                             |
| [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)                         | The **Role** property is [**ROLE\_SYSTEM\_ANIMATION**](object-roles.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)                       | The **State** property is a combination of one or more of the following object state constants: [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md) \| [**STATE\_SYSTEM\_ANIMATED**](object-state-constants.md)<br/> For more information, see [Object State Constants](object-state-constants.md).<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> </dl>

 

 






---
title: Scroll Bar (MSAA UI Element Reference)
description: Scroll bars let a user choose the direction and distance to scroll through information in a related window or list box. The window class name for a scroll bar is \ 0034;SCROLLBAR \ 0034;.
ms.assetid: a4ec1708-d751-4526-bd69-9796c43872a0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Scroll Bar (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Scroll Bar** objects for purposes of MSAA UI Element Reference. How to create **Scroll Bar** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Scroll bars let a user choose the direction and distance to scroll through information in a related window or list box. The window class name for a scroll bar is "SCROLLBAR".

The contents of the [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties depends on whether the scroll bar is vertical or horizontal and on which of the following parts of the scroll bar is being queried by the client:

-   The scroll bar itself
-   The top or right arrow button
-   The bottom or left arrow button
-   The scroll box (thumb)
-   The page up or page right region
-   The page down or page left region

## IAccessible Methods

A scroll bar supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:

-   [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master)—The scroll bar object itself and the scroll thumb do not support the **accDoDefaultAction** method.

    For the other scroll bar parts on a vertical scroll bar, [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) calls [**PostMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644944) with the [**WM\_VSCROLL**](https://msdn.microsoft.com/library/windows/desktop/bb787577) message with *wParam* set to the following values.

    

    | Button/Region       | Vaule        |
    |---------------------|--------------|
    | Top arrow button    | SB\_LINEUP   |
    | Bottom arrow button | SB\_LINEDOWN |
    | Page up region      | SB\_PAGEUP   |
    | Page down region    | SB\_PAGEDOWN |

    

     

    For the other scroll bar parts on a horizontal scroll bar, [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) calls [**PostMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644944) with the [**WM\_HSCROLL**](https://msdn.microsoft.com/library/windows/desktop/bb787575) message with *wParam* set to the following values.

    

    | Button/Region      | Value         |
    |--------------------|---------------|
    | Left arrow button  | SB\_LINELEFT  |
    | Right arrow button | SB\_LINERIGHT |
    | Page left region   | SB\_PAGELEFT  |
    | Page right region  | SB\_PAGERIGHT |

    

     

-   [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)
-   [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)
-   [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)

## IAccessible Properties

A scroll bar supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:

-   [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master)—The **ChildCount** property for the scroll bar object is five. For the other scroll bar parts, the **ChildCount** property is zero.
-   [**get\_accDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction?branch=master)—The scroll bar object itself and the scroll thumb do not support the **DefaultAction** property. The **DefaultAction** property for the arrow buttons and the shaded areas on either side of the scroll thumb is "Press".
-   [**get\_accDescription**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdescription?branch=master)—The **Description** property depends on the part of the scroll bar that is queried.

    The parts of a vertical scroll bar have the following descriptions.

    

    | Part                | Description                                                                         |
    |---------------------|-------------------------------------------------------------------------------------|
    | Scroll bar itself   | "Used to change the vertical viewing area"                                          |
    | Top arrow button    | "Moves the vertical position up one line"                                           |
    | Bottom arrow button | "Moves the vertical position down one line"                                         |
    | Scroll thumb        | "Indicates the current vertical position, and can be dragged to change it directly" |
    | Page up region      | "Moves the vertical position up a couple of lines"                                  |
    | Page down region    | "Indicates the current vertical position, and can be dragged to change it directly" |

    

     

    The parts of a horizontal scroll bar have the following descriptions.

    

    | Part               | Description                                                                           |
    |--------------------|---------------------------------------------------------------------------------------|
    | Scroll bar itself  | "Used to change the horizontal viewing area"                                          |
    | Left arrow button  | "Moves the horizontal position left one column"                                       |
    | Right arrow button | 'Moves the horizontal position right one column"                                      |
    | Scroll thumb       | "Indicates the current horizontal position, and can be dragged to change it directly" |
    | Page left region   | "Moves the horizontal position left a couple of columns"                              |
    | Page right region  | "Indicates the current vertical position, and can be dragged to change it directly"   |

    

     

-   [**get\_accHelp**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acchelp?branch=master)
-   [**get\_accHelpTopic**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acchelptopic?branch=master)
-   [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)—The **Name** property depends on the part of the scroll bar that is queried.

    The parts of a vertical scroll bar have the following names.

    | Part                | Name        |
    |---------------------|-------------|
    | Scroll bar window   | "Vertical"  |
    | Top arrow button    | "Line up"   |
    | Bottom arrow button | "Line down" |
    | Scroll thumb        | "Position"  |
    | Page up region      | "Page up"   |
    | Page down region    | "Page down" |

    

     

    The parts of a horizontal scroll bar have the following names.

    

    | Part               | Name           |
    |--------------------|----------------|
    | Scroll bar window  | "Horizontal"   |
    | Left arrow button  | "Column left"  |
    | Right arrow button | "Column right" |
    | Scroll thumb       | "Position"     |
    | Page right region  | "Page right"   |
    | Page left region   | "Page left"    |

    

     

-   [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)—The **Parent** property of the arrow buttons, scroll thumb, and the shaded area on either side of the thumb is the scroll bar window. The **Parent** property of the scroll bar window is a window (ROLE\_SYSTEM\_WINDOW) that surrounds the control and has the same **Name** property and window class name.
-   [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)—The **Role** property depends on the part of the scroll bar that is queried. The parts of a scroll bar have the following roles. 

    | Part                                                  | Role                                                                    |
    |-------------------------------------------------------|-------------------------------------------------------------------------|
    | Scroll bar itself                                     | [**ROLE\_SYSTEM\_SCROLLBAR**](object-roles.md#role-system-scrollbar)   |
    | Top, down, left, and right arrow buttons              | [**ROLE\_SYSTEM\_PUSHBUTTON**](object-roles.md#role-system-pushbutton) |
    | Scroll thumb                                          | [**ROLE\_SYSTEM\_INDICATOR**](object-roles.md#role-system-indicator)   |
    | Page up, page down, page left, and page right regions | [**ROLE\_SYSTEM\_PUSHBUTTON**](object-roles.md#role-system-pushbutton) |

    

     

-   [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)—The **State** property of each scroll bar component includes a combination of the following [values](object-state-constants.md).

    | State                                                                                 | Value                                                                                                                                                                                                                       |
    |---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible)     | For the scroll bar itself, this indicates the specified vertical or horizontal scroll bar does not exist. For the page up or page down regions, this indicates the thumb is positioned such that the region does not exist. |
    | [**STATE\_SYSTEM\_OFFSCREEN**](object-state-constants.md#state-system-offscreen)     | For the scroll bar itself, this indicates the window is sized such that the specified vertical or horizontal scroll bar is not currently displayed.                                                                         |
    | [**STATE\_SYSTEM\_PRESSED**](object-state-constants.md#state-system-pressed)         | The arrow button or page region is pressed.                                                                                                                                                                                 |
    | [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) | The component is disabled.                                                                                                                                                                                                  |

    

     

-   [**get\_accValue**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accvalue?branch=master)—The **Value** property for the scroll bar window indicates the scroll bar position and is a string that contains an integer from "0" through "100".

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> </dl>

 

 





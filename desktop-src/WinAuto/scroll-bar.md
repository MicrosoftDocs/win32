---
title: Scroll Bar (MSAA UI Element Reference)
description: Scroll bars let a user choose the direction and distance to scroll through information in a related window or list box. The window class name for a scroll bar is \ 0034;SCROLLBAR \ 0034;.
ms.assetid: a4ec1708-d751-4526-bd69-9796c43872a0
ms.topic: article
ms.date: 05/31/2018
---

# Scroll Bar (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Scroll Bar** objects for purposes of MSAA UI Element Reference. How to create **Scroll Bar** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Scroll bars let a user choose the direction and distance to scroll through information in a related window or list box. The window class name for a scroll bar is "SCROLLBAR".

The contents of the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties depends on whether the scroll bar is vertical or horizontal and on which of the following parts of the scroll bar is being queried by the client:

-   The scroll bar itself
-   The top or right arrow button
-   The bottom or left arrow button
-   The scroll box (thumb)
-   The page up or page right region
-   The page down or page left region

## IAccessible Methods

A scroll bar supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:

-   [**accDoDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accdodefaultaction)—The scroll bar object itself and the scroll thumb do not support the **accDoDefaultAction** method.

    For the other scroll bar parts on a vertical scroll bar, [**accDoDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accdodefaultaction) calls [**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea) with the [**WM\_VSCROLL**](/windows/desktop/Controls/wm-vscroll) message with *wParam* set to the following values.

    

    | Button/Region       | Vaule        |
    |---------------------|--------------|
    | Top arrow button    | SB\_LINEUP   |
    | Bottom arrow button | SB\_LINEDOWN |
    | Page up region      | SB\_PAGEUP   |
    | Page down region    | SB\_PAGEDOWN |

    

     

    For the other scroll bar parts on a horizontal scroll bar, [**accDoDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accdodefaultaction) calls [**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea) with the [**WM\_HSCROLL**](/windows/desktop/Controls/wm-hscroll) message with *wParam* set to the following values.

    

    | Button/Region      | Value         |
    |--------------------|---------------|
    | Left arrow button  | SB\_LINELEFT  |
    | Right arrow button | SB\_LINERIGHT |
    | Page left region   | SB\_PAGELEFT  |
    | Page right region  | SB\_PAGERIGHT |

    

     

-   [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)
-   [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)
-   [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)

## IAccessible Properties

A scroll bar supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:

-   [**get\_accChildCount**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount)—The **ChildCount** property for the scroll bar object is five. For the other scroll bar parts, the **ChildCount** property is zero.
-   [**get\_accDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction)—The scroll bar object itself and the scroll thumb do not support the **DefaultAction** property. The **DefaultAction** property for the arrow buttons and the shaded areas on either side of the scroll thumb is "Press".
-   [**get\_accDescription**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdescription)—The **Description** property depends on the part of the scroll bar that is queried.

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

    

     

-   [**get\_accHelp**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acchelp)
-   [**get\_accHelpTopic**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acchelptopic)
-   [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)—The **Name** property depends on the part of the scroll bar that is queried.

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

    

     

-   [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent)—The **Parent** property of the arrow buttons, scroll thumb, and the shaded area on either side of the thumb is the scroll bar window. The **Parent** property of the scroll bar window is a window (ROLE\_SYSTEM\_WINDOW) that surrounds the control and has the same **Name** property and window class name.
-   [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)—The **Role** property depends on the part of the scroll bar that is queried. The parts of a scroll bar have the following roles. 

    | Part                                                  | Role                                                                    |
    |-------------------------------------------------------|-------------------------------------------------------------------------|
    | Scroll bar itself                                     | [**ROLE\_SYSTEM\_SCROLLBAR**](object-roles.md)   |
    | Top, down, left, and right arrow buttons              | [**ROLE\_SYSTEM\_PUSHBUTTON**](object-roles.md) |
    | Scroll thumb                                          | [**ROLE\_SYSTEM\_INDICATOR**](object-roles.md)   |
    | Page up, page down, page left, and page right regions | [**ROLE\_SYSTEM\_PUSHBUTTON**](object-roles.md) |

    

     

-   [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)—The **State** property of each scroll bar component includes a combination of the following [values](object-state-constants.md).

    | State                                                                                 | Value                                                                                                                                                                                                                       |
    |---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md)     | For the scroll bar itself, this indicates the specified vertical or horizontal scroll bar does not exist. For the page up or page down regions, this indicates the thumb is positioned such that the region does not exist. |
    | [**STATE\_SYSTEM\_OFFSCREEN**](object-state-constants.md)     | For the scroll bar itself, this indicates the window is sized such that the specified vertical or horizontal scroll bar is not currently displayed.                                                                         |
    | [**STATE\_SYSTEM\_PRESSED**](object-state-constants.md)         | The arrow button or page region is pressed.                                                                                                                                                                                 |
    | [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md) | The component is disabled.                                                                                                                                                                                                  |

    

     

-   [**get\_accValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accvalue)—The **Value** property for the scroll bar window indicates the scroll bar position and is a string that contains an integer from "0" through "100".

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> </dl>

 

 
---
title: Slider Control (MSAA UI Element Reference)
description: A slider control, also called a trackbar control, lets a user select from a range of values by moving a slider. The volume controls in the Windows operating system are slider controls.
ms.assetid: '8df4ed1d-d63c-49d7-94f1-df2113643484'
---

# Slider Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Slider Control** objects for purposes of MSAA UI Element Reference. How to create **Slider Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A slider control, also called a trackbar control, lets a user select from a range of values by moving a slider. The volume controls in the Windows operating system are slider controls.

The window class name for a slider control is TRACKBAR\_CLASS, which is defined as "msctls\_trackbar" in Commctrl.h.

The contents of the [**IAccessible**](iaccessible.md) properties depend on whether the slider is vertical or horizontal and on which of the following parts of the slider control is queried by the client:

-   Slider window
-   Slider thumb
-   Shaded area above (or to
-   Shaded area below (or to the right of) the slider thumb

## IAccessible Methods

A slider control supports the following [**IAccessible**](iaccessible.md) methods:

-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)
-   [**accNavigate**](iaccessible-iaccessible--accnavigate.md)
-   [**accSelect**](iaccessible-iaccessible--accselect.md)

## IAccessible Properties

A slider control supports the following [**IAccessible**](iaccessible.md) properties:

-   [**get\_accChild**](iaccessible-iaccessible--get-accchild.md)
-   [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)
-   [**get\_accDescription**](iaccessible-iaccessible--get-accdescription.md)
-   [**get\_accHelp**](iaccessible-iaccessible--get-acchelp.md)
-   [**get\_accHelpTopic**](iaccessible-iaccessible--get-acchelptopic.md)
-   [**get\_accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md)—The **KeyboardShortcut** property is the slider window's access key, which is an underlined character in the text of the label for the slider. The returned string contains the access key character appended to the string "Alt+".
-   [**get\_accName**](iaccessible-iaccessible--get-accname.md)—The **Name** property depends on the part of the slider that is queried.

    The parts of a vertical slider have the following names:

    

    | Slider part                    | Name                                |
    |--------------------------------|-------------------------------------|
    | Slider window                  | Static text control used as a label |
    | Slider thumb                   | "Position"                          |
    | Shaded area above slider thumb | "Page up"                           |
    | Shaded area below slider thumb | "Page down"                         |

    

     

    The parts of a horizontal slider have the following names:

    

    | Slider part                              | Name                                |
    |------------------------------------------|-------------------------------------|
    | Slider window                            | Static text control used as a label |
    | Slider thumb                             | "Position"                          |
    | Shaded area to the left of slider thumb  | "Page left"                         |
    | Shaded area to the right of slider thumb | "Page right"                        |

    

     

-   [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)—The **Parent** property of the arrow buttons, scroll thumb, and the shaded area on either side of the thumb is the slider window. The **Parent** property of the slider window is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name.
-   [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)—The **Role** property depends on the part of the slider that is queried. 

    | Slider part                                     | [Role](object-roles.md)                                                |
    |-------------------------------------------------|-------------------------------------------------------------------------|
    | Slider window                                   | [**ROLE\_SYSTEM\_SLIDER**](object-roles.md#role-system-slider)         |
    | Slider thumb                                    | [**ROLE\_SYSTEM\_INDICATOR**](object-roles.md#role-system-indicator)   |
    | Shaded areas on either side of the slider thumb | [**ROLE\_SYSTEM\_PUSHBUTTON**](object-roles.md#role-system-pushbutton) |

    

     

-   [**get\_accState**](iaccessible-iaccessible--get-accstate.md)—[Values](object-state-constants.md) for the **State** property depend on the part of the slider that is queried. 

    | Slider Part                                     | Possible state values                                                                                                                                                                                                                                                                                                                                                                                                           |
    |-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Slider window                                   | [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable) \| [**STATE\_SYSTEM\_NORMAL**](object-state-constants.md#state-system-normal) |
    | Slider thumb                                    | Zero (0), which means the object is visible, or [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_NORMAL**](object-state-constants.md#state-system-normal)                                                                                                                       |
    | Shaded areas on either side of the slider thumb | Zero (0), which means the object is visible, or [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_NORMAL**](object-state-constants.md#state-system-normal)                                                                                                                       |

    

     

-   [**get\_accValue**](iaccessible-iaccessible--get-accvalue.md)—The **Value** property for the slider window indicates the position of the thumb and is a string that contains an integer from "0" through "100".

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> <dt>

[**Scroll Bar**](scroll-bar.md)
</dt> </dl>

 

 





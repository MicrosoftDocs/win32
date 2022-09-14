---
title: Design Considerations for Proxy Objects
description: Proxy and accessible object design depends on the design of the server UI elements. Regardless of the design, a UI element must notify its proxy object right before it is destroyed so that the proxy object handles calls from clients appropriately.
ms.assetid: 83a9ff66-2fe6-4589-a187-cdaf207b02b8
ms.topic: article
ms.date: 05/31/2018
---

# Design Considerations for Proxy Objects

Proxy and accessible object design depends on the design of the server UI elements. Regardless of the design, a UI element must notify its proxy object right before it is destroyed so that the proxy object handles calls from clients appropriately.

The following list describes two design possibilities:

-   Place the code that implements the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface in the same module as the code that implements the user interface element if the user interface code is easily extensible. In this case, the proxy is "lightweight" in the sense that all it does is monitor the life span of the accessible object, forward calls to the accessible object, and return the results.
-   Place the code that implements [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) in the same module as the code that implements the proxy object. In this case, the accessible object uses internal functions to obtain information about the UI element.

## Trackbar Controls

When implementing trackbar controls, use the trackbar style **TBS\_REVERSED** to provide more meaningful information. This style reverses the scale used by [**IAccessible::get\_accValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accvalue).

For vertical trackbars without this style, [**IAccessible::get\_accValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accvalue) returns zero (0) when the trackbar thumb is at the top of the control; the values increase as you slide the thumb toward the bottom. With the **TBS\_REVERSED** style, **IAccessible::get\_accValue** returns one hundred (100) when the trackbar thumb is at the top; the numbers decrease as you move the trackbar thumb toward the bottom.

For horizontal trackbars without this style, zero (0) is returned when the trackbar thumb is at the left end of the control; the values increase as you move the trackbar thumb to the right. With the **TBS\_REVERSED** style, [**IAccessible::get\_accValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accvalue) returns one hundred (100) when the trackbar thumb is at the left; the values decrease as you move the trackbar thumb to the right.

 

 





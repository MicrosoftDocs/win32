---
title: Cursor (MSAA UI Element Reference)
description: A cursor is a small picture whose location on the screen is controlled by a pointing device, such as a mouse, pen, or trackball. When the user moves the pointing device, the Windows operating system moves the cursor.
ms.assetid: ff97d474-7c96-4f89-bc34-2cf320381ce0
ms.topic: article
ms.date: 05/31/2018
---

# Cursor (MSAA UI Element Reference)

> [!Note]  
> This topic describes cursors for purposes of MSAA UI Element Reference. How to use cursors in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A cursor is a small picture whose location on the screen is controlled by a pointing device, such as a mouse, pen, or trackball. When the user moves the pointing device, the Windows operating system moves the cursor.

## IAccessible Methods

A cursor supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:

-   [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)
-   [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)

## IAccessible Properties

A cursor supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:

-   [**get\_accChildCount**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount)—The **ChildCount** property is zero.
-   [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)—Developers can create custom cursors or use the predefined cursors that are identified by their cursor ID. The **Name** property of the cursor depends on its shape and is one of the following: 

    | Cursor shape     | Name              |
    |------------------|-------------------|
    | Custom cursor    | "Unknown"         |
    | IDC\_ARROW       | "Normal"          |
    | IDC\_IBEAM       | "Edit"            |
    | IDC\_WAIT        | "Wait"            |
    | IDC\_CROSS       | "Graphic"         |
    | IDC\_UPARROW     | "Up"              |
    | IDC\_SIZENWSE    | "NWSE size"       |
    | IDC\_SIZENESW    | "NESW size"       |
    | IDC\_SIZEWE      | "Horizontal size" |
    | IDC\_SIZENS      | "Vertical size"   |
    | IDC\_SIZEALL     | "Move"            |
    | IDC\_NO          | "Forbidden"       |
    | IDC\_APPSTARTING | "App start"       |
    | IDC\_HELP        | "Help"            |

    

     

-   [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)—The **Role** property is [**ROLE\_SYSTEM\_CURSOR**](object-roles.md).
-   [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)—The **State** property is a combination of one or more of the following [values](object-state-constants.md):

    [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_FLOATING**](object-state-constants.md)

## Notes

-   Unlike other UI elements, the cursor object does not have an associated window handle. To obtain access to the cursor object, clients must set a [*WinEventProc*](/windows/desktop/api/Winuser/nc-winuser-wineventproc) and wait for the cursor object to generate events.

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> </dl>

 

 





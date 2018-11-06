---
title: Sample Resource-Definition File
description: Example script file that defines the resources for an application named Shapes.
ms.assetid: 0362b1be-7671-4685-8eb8-bff502224939
ms.topic: article
ms.date: 05/31/2018
---

# Sample Resource-Definition File

The following example shows a script file that defines the resources for an application named Shapes:

``` syntax
#include "shapes.h"

ShapesCursor  CURSOR  SHAPES.CUR
ShapesIcon    ICON    SHAPES.ICO

ShapesMenu MENU
{
    POPUP "&Shape"
    {
        MENUITEM "&Clear", ID_CLEAR
        MENUITEM "&Rectangle", ID_RECT
        MENUITEM "&Triangle", ID_TRIANGLE
        MENUITEM "&Star", ID_STAR
        MENUITEM "&Ellipse", ID_ELLIPSE
    }
}
```

The [**CURSOR**](cursor-resource.md) statement names the application's cursor resource ShapesCursor and specifies the cursor file SHAPES.CUR, which contains the image for that cursor.

The [**ICON**](icon-resource.md) statement names the application's icon resource ShapesIcon and specifies the icon file SHAPES.ICO, which contains the image for that icon.

The [**MENU**](menu-resource.md) statement defines an application menu named **ShapesMenu**, a pop-up menu with five menu items.

The body of the menu definition, enclosed by the curly braces, or the **BEGIN** and **END** keywords, specifies each menu item and the menu identifier that is returned when the user selects that item. For example, the first item on the menu, **Clear**, returns the menu identifier ID\_CLEAR when the user selects it. The menu identifiers are defined in the application header file, SHAPES.H.

 

 





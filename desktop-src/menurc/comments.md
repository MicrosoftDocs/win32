---
title: Comments (Menus and Other Resources)
description: RC supports C-style syntax for both single-line comments and block comments. Single-line comments begin with two forward slashes (//) and run to the end of the line. The following is an example of a resource statement followed by a single-line comment.
ms.assetid: 045268fb-2d6e-446c-8b95-90e42baeb282
ms.topic: article
ms.date: 05/31/2018
---

# Comments (Menus and Other Resources)

RC supports C-style syntax for both single-line comments and block comments. Single-line comments begin with two forward slashes (//) and run to the end of the line. The following is an example of a resource statement followed by a single-line comment.

``` syntax
NewCursor  CURSOR  NEW.CUR  // a new cursor for the application.
```

Block comments begin with an opening delimiter (/\*) and run to a closing delimiter (\*/). Comments do not nest. The following is an example of a block comment at the beginning of a .rc file.

``` syntax
/* 
    Resources.Rc

    Contains the resource definitions for the application.
    Control identifiers are defined in Resources.h.
*/

#include "resources.h"
//...
```

 

 





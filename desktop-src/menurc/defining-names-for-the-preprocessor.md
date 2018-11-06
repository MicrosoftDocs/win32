---
title: Defining Names for the Preprocessor
description: You can specify conditional compilation in a script, based on whether a name is defined on the RC command line with the /d option, or in the file or an include file with the \ define directive.
ms.assetid: bc72911e-2aca-46a4-b6c1-60cc8ed7d82f
ms.topic: article
ms.date: 05/31/2018
---

# Defining Names for the Preprocessor

You can specify conditional compilation in a script, based on whether a name is defined on the RC command line with the **/d** option, or in the file or an include file with the [**\#define**](-define.md) directive.

For example, suppose your application has a pop-up menu that should appear only with debugging versions of the application. When you compile the application for normal use, the menu is not included. The following example shows the statements that can be added to the resource-definition file to define a Debug menu:

``` syntax
#include <windows.h>

MainMenu MENU
{
    //. . .
#ifdef DEBUG
    POPUP "&Debug"
    {
        MENUITEM "&Memory usage", ID_MEMORY
        MENUITEM "&Walk data heap", ID_WALK_HEAP
    }
#endif
}
```

When compiling resources for a debugging version of the application, you could include the Debug menu by using the following command:

**rc -d DEBUG myapp.rc**

To compile resources for a normal version of the application?one that does not include the Debug menu?you could use the following command:

**rc myapp.rc**

 

 





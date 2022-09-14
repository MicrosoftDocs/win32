---
title: Using COM in Your Windows app
description: Module 1 of this series showed how to create a window and respond to window messages such as WM\_PAINT and WM\_CLOSE. Module 2 introduces the Component Object Model (COM).
ms.assetid: 6e867618-4d02-4c17-b7ea-dc7290507689
ms.topic: article
ms.date: 05/31/2018
---

# Module 2. Using COM in Your Windows-Based Program

[Module 1](your-first-windows-program.md) of this series showed how to create a window and respond to window messages such as [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) and [**WM\_CLOSE**](/windows/desktop/winmsg/wm-close). Module 2 introduces the Component Object Model (COM).

COM is a specification for creating reusable software components. Many of the features that you will use in a modern Windows-based program rely on COM, such as the following:

-   Graphics (Direct2D)
-   Text (DirectWrite)
-   The Windows Shell
-   The Ribbon control
-   UI animation

(Some technologies on this list use a subset of COM and are therefore not "pure" COM.)

COM has a reputation for being difficult to learn. And it is true that writing a new software module to support COM can be tricky. But if your program is strictly a *consumer* of COM, you may find that COM is easier to understand than you expect.

This module shows how to call COM-based APIs in your program. It also describes some of the reasoning behind the design of COM. If you understand why COM is designed as it is, you can program with it more effectively. The second part of the module describes some recommended programming practices for COM.

COM was introduced in 1993 to support Object Linking and Embedding (OLE) 2.0. People sometimes think that COM and OLE are the same thing. This may be another reason for the perception that COM is difficult to learn. OLE 2.0 is built on COM, but you do not have to know OLE to understand COM.

COM is a *binary standard*, not a language standard: It defines the binary interface between an application and a software component. As a binary standard, COM is language-neutral, although it maps naturally to certain C++ constructs. This module will focus on three major goals of COM:

-   Separating the implementation of an object from its interface.
-   Managing the lifetime of an object.
-   Discovering the capabilities of an object at run time.

## In this section

-   [What Is a COM Interface?](what-is-a-com-interface-.md)
-   [Initializing the COM Library](initializing-the-com-library.md)
-   [Error Codes in COM](error-codes-in-com.md)
-   [Creating an Object in COM](creating-an-object-in-com.md)
-   [Example: The Open Dialog Box](example--the-open-dialog-box.md)
-   [Managing the Lifetime of an Object](managing-the-lifetime-of-an-object.md)
-   [Asking an Object for an Interface](asking-an-object-for-an-interface.md)
-   [Memory Allocation in COM](memory-allocation-in-com.md)
-   [COM Coding Practices](com-coding-practices.md)
-   [Error Handling in COM](error-handling-in-com.md)

## Related topics

<dl> <dt>

[Learn to Program for Windows in C++](learn-to-program-for-windows.md)
</dt> </dl>

 

 
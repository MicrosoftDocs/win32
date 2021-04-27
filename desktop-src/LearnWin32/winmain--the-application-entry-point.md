---
title: WinMain The Application Entry Point
description: WinMain: The Application Entry Point
ms.assetid: 389da5d4-d0f9-4339-be6c-0f4fecc59316
ms.topic: article
ms.date: 05/31/2018
---

# WinMain: The Application Entry Point

Every Windows program includes an entry-point function that is named either **WinMain** or **wWinMain**. Here is the signature for **wWinMain**.


```C++
int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PWSTR pCmdLine, int nCmdShow);
```



The four parameters are:

-   *hInstance* is something called a "handle to an instance" or "handle to a module." The operating system uses this value to identify the executable (EXE) when it is loaded in memory. The instance handle is needed for certain Windows functions—for example, to load icons or bitmaps.
-   *hPrevInstance* has no meaning. It was used in 16-bit Windows, but is now always zero.
-   *pCmdLine* contains the command-line arguments as a Unicode string.
-   *nCmdShow* is a flag that says whether the main application window will be minimized, maximized, or shown normally.

The function returns an **int** value. The return value is not used by the operating system, but you can use the return value to convey a status code to some other program that you write.

**WINAPI** is the calling convention. A *calling convention* defines how a function receives parameters from the caller. For example, it defines the order that parameters appear on the stack. Just make sure to declare your **wWinMain** function as shown.

The **WinMain** function is identical to **wWinMain**, except the command-line arguments are passed as an ANSI string. The Unicode version is preferred. You can use the ANSI **WinMain** function even if you compile your program as Unicode. To get a Unicode copy of the command-line arguments, call the [**GetCommandLine**](/windows/desktop/api/processenv/nf-processenv-getcommandlinea) function. This function returns all of the arguments in a single string. If you want the arguments as an *argv*-style array, pass this string to [**CommandLineToArgvW**](/windows/desktop/api/shellapi/nf-shellapi-commandlinetoargvw).

How does the compiler know to invoke **wWinMain** instead of the standard **main** function? What actually happens is that the Microsoft C runtime library (CRT) provides an implementation of **main** that calls either **WinMain** or **wWinMain**.

> [!Note]  
> The CRT does some additional work inside **main**. For example, any static initializers are called before **wWinMain**. Although you can tell the linker to use a different entry-point function, use the default if you link to the CRT. Otherwise, the CRT initialization code will be skipped, with unpredictable results. (For example, global objects will not be initialized correctly.)

 

Here is an empty **WinMain** function.


```C++
INT WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
    PSTR lpCmdLine, INT nCmdShow)
{
    return 0;
}
```



Now that you have the entry point and understand some of the basic terminology and coding conventions, you are ready to create a complete Window program.

## Next

[Module 1. Your First Windows Program](your-first-windows-program.md).

 

 

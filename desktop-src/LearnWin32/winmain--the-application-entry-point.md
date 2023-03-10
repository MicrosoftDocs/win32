---
title: The WinMain application entry point
description: Learn about the function named WinMain or wWinMain that every Windows program includes, and its parameters.
ms.assetid: 389da5d4-d0f9-4339-be6c-0f4fecc59316
ms.topic: article
ms.date: 02/08/2023
---

# The WinMain application entry point

Every Windows program includes an entry-point function named either **WinMain** or **wWinMain**. The following code shows the signature for **wWinMain**:

```cpp
int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PWSTR pCmdLine, int nCmdShow);
```

The four **wWinMain** parameters are as follows:

- *hInstance* is the *handle to an instance* or handle to a module. The operating system uses this value to identify the executable or EXE when it's loaded in memory. Certain Windows functions need the instance handle, for example to load icons or bitmaps.
- *hPrevInstance* has no meaning. It was used in 16-bit Windows, but is now always zero.
- *pCmdLine* contains the command-line arguments as a Unicode string.
- *nCmdShow* is a flag that indicates whether the main application window is minimized, maximized, or shown normally.

The function returns an `int` value. The operating system doesn't use the return value, but you can use the value to pass a status code to another program.

A *calling convention*, such as `WINAPI`, defines how a function receives parameters from the caller. For example, the calling convention defines the order that parameters appear on the stack. Make sure to declare your **wWinMain** function as shown in the preceding example.

The **WinMain** function is the same as **wWinMain**, except the command-line arguments are passed as an ANSI string. The Unicode string is preferred. You can use the ANSI **WinMain** function even if you compile your program as Unicode. To get a Unicode copy of the command-line arguments, call the [GetCommandLine](/windows/desktop/api/processenv/nf-processenv-getcommandlinea) function. This function returns all of the arguments in a single string. If you want the arguments as an *argv*-style array, pass this string to [CommandLineToArgvW](/windows/desktop/api/shellapi/nf-shellapi-commandlinetoargvw).

How does the compiler know to invoke **wWinMain** instead of the standard **main** function? What actually happens is that the Microsoft C runtime library (CRT) provides an implementation of **main** that calls either **WinMain** or **wWinMain**.

The CRT does some more work inside **main**. For example, it calls any static initializers before **wWinMain**. Although you can tell the linker to use a different entry-point function, you should use the default if you link to the CRT. Otherwise, the CRT initialization code is skipped, with unpredictable results such as global objects not being initialized correctly.

The following code shows an empty **WinMain** function:

```cpp
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
    PSTR lpCmdLine, int nCmdShow)
{
    return 0;
}
```

Now that you have the entry point and understand some of the basic terminology and coding conventions, you're ready to [Create your first Windows program](your-first-windows-program.md).


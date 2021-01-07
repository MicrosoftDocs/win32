---
description: This section describes how to print from a native Windows desktop program.
ms.assetid: C1EDBE38-9D18-41BB-961C-12CF2283C639
title: Desktop App Printing
ms.topic: article
ms.date: 05/31/2018
---

# Desktop App Printing

This section describes how to print from a native Windows desktop program.

## Overview

To provide the best user experience when you print from a native Windows program, the program must be designed to print from a dedicated thread. In a native Windows program, the program is responsible for managing user interface events and messages. Printing operations can require periods of intense computation as the application content is rendered for the printer, which can prevent the program from responding to user interaction if this processing is performed in the same thread as event processing of the user interaction.

If you are already familiar with how to write a multi-threaded native Windows program, you go directly to [How to print from a Windows application](how-to--print-from-a-windows-application.md) and learn how to add printing functionality to your program.

### Basic Windows Program Requirements

For best performance and program responsiveness, do not perform a program's print job processing in the thread that processes user interaction.

This separation of printing from user interaction will influence how the program manages the application data. You should thoroughly understand these implications before you start writing the application. The following topics describe the basic requirements of handling printing in a separate thread of a program.

### Windows Program Basics

A native Windows program must provide the main window procedure to process the window messages that it receives from the operating system. Every window in a Windows program has a corresponding **WndProc** function that processes these window messages. The thread in which this function runs is called the user interface, or UI, thread.

**Use resources for strings.**  
Use string resources from the program's resource file instead of string constants for strings that might need to be changed when you support another language. Before a program can use a string resource as a string, the program must retrieve the resource from the resource file and copy it to a local memory buffer. This requires some additional programming in the beginning, but allows for easier modification, translation, and localization of the program in the future.  
**Process data in steps.**  
Process the print job in steps that can be interrupted. This design makes it possible for the user to cancel a long processing operation before it completes and prevents the program from blocking other programs that might be running at the same time.  
**Use window user data.**  
Printing applications often have several windows and threads. To keep the data available between threads and processing steps without using static, global variables, reference the data structures by a data pointer that is part of the window in which they are used.  


The following code example shows a main entry point for a printing application. This example shows how to use string resources instead of string constants and also shows the main message loop that processes the program's window messages.


```C++
int APIENTRY 
wWinMain(
        HINSTANCE hInstance, 
        HINSTANCE hPrevInstance, 
        LPWSTR lpCmdLine, 
        int nCmdShow
)
{
    UNREFERENCED_PARAMETER(hPrevInstance);
    UNREFERENCED_PARAMETER(lpCmdLine);

    MSG msg;
    HACCEL hAccelTable;
    HRESULT hr = S_OK;

    // Register the main window class name
    WCHAR szWindowClass[MAXIMUM_RESOURCE_STRING_LENGTH];            
    LoadString(
        hInstance, 
        IDC_PRINTSAMPLE, 
        szWindowClass, 
        MAXIMUM_RESOURCE_STRING_LENGTH);
    MyRegisterClass(hInstance, szWindowClass);

    // Perform application initialization:
    if (!InitInstance (hInstance, nCmdShow))
    {
        // Unable to initialize this instance of the application
        //  so display error message and exit
        MessageBoxWithResourceString (
            hInstance, 
            GetDesktopWindow(), 
            IDS_ERROR_INSTINITFAIL, 
            IDS_CAPTION_ERROR, 
            (MB_OK | MB_ICONEXCLAMATION));
        return FALSE;
    }    
    
    // Init COM for printing interfaces
    if (FAILED(hr = CoInitializeEx(0, COINIT_MULTITHREADED)))
    {
        // Unable to initialize COM
        //  so display error message and exit
        MessageBoxWithResourceString (
            hInstance, 
            GetDesktopWindow(), 
            IDS_ERROR_COMINITFAIL, 
            IDS_CAPTION_ERROR, 
            (MB_OK | MB_ICONEXCLAMATION));
        return FALSE;
    }

    hAccelTable = LoadAccelerators(
                    hInstance, 
                    MAKEINTRESOURCE(IDC_PRINTSAMPLE));

    // Main message handling loop
    while (GetMessage(&msg, NULL, 0, 0))
    {
        if (!TranslateAccelerator(msg.hwnd, hAccelTable, &msg))
        {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
    }

    // Uninitialize (close) the COM interface
    CoUninitialize();

    return (int) msg.wParam;
}
```



### Document Information

Native Windows programs that print should be designed for multi-threaded processing. One of the requirements of a multi-threaded design is to protect the program's data elements so that they are safe for multiple threads to use at the same time. You can protect data elements by using synchronization objects and organizing the data to avoid conflicts between the threads. At the same time, the program must prevent changes to the program data while it is being printed. The sample program uses several different multi-threaded programming techniques.

 **Synchronization Events**  
The sample program uses events, thread handles, and wait functions to synchronize the processing between the print thread and the main program and to indicate that the data is in use.  
**Application-Specific Windows Messages**  
The sample program uses application-specific window messages to make the program more compatible with other native Windows programs. Breaking the processing into smaller steps and queuing those steps in the window message loop makes it easier for Windows to manage the processing without blocking other applications that might also be running on the computer.  
**Data Structures**  
The sample program is not written in an object-oriented style using objects and classes, although it does group data elements into data structures. The sample does not use an object-oriented approach to avoid implying that one approach is better or worse than another.  
You can use the functions and data structures of the sample program as a starting point when you design your program. Whether you decide to design an object-oriented program or not, the important design consideration to remember is to group the related data elements so that you can use them safely in different threads as necessary.  


### Printer Device Context

When printing, you might want to render the content to be printed to a device context. [How To: Retrieve a Printer Device Context](retrieving-a-printer-device-context.md) describes the different ways that you can obtain a printer device context.

## Related topics



[How to print from a Windows application](how-to--print-from-a-windows-application.md)


 

 




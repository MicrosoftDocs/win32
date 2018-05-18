---
Description: Microsoft Corporation
ms.assetid: '641156c4-774e-49fd-b790-f5a83ea22268'
title: Console Accessibility
---

# Console Accessibility

Microsoft Corporation

October 2001

**Summary:** This paper outlines the requirements for console accessibility in Microsoft Windows XP. (25 printed pages)

-   [Overview](#overview)
-   [Backward Compatibility](#backward-compatibility)
-   [Definition of Terms](#definition-of-terms)
    -   [API](#api)
    -   [Console](#console-accessibility)
    -   [SDK](#sdk)
    -   [WinEvents](#winevents)
-   [Assumptions](#assumptions)
-   [Accessibility through APIs and Events](#accessibility-through-apis-and-events)
    -   [To determine when an application currently in use is a console](#to-determine-when-an-application-currently-in-use-is-a-console)
    -   [To gather information about the application running under the console](#to-gather-information-about-the-application-running-under-the-console)
    -   [To track user interactions with the console](#to-track-user-interactions-with-the-console)
-   [Example Scenarios](#example-scenarios)
    -   [How To Determine if the Current Application is a Console](#how-to-determine-if-the-current-application-is-a-console)
    -   [How To Extract Console Information](#how-to-extract-console-information)
    -   [Console Specific Events](#console-specific-events)
-   [Additional Information](#additional-information)

## Overview

Many people with vision, hearing, or motion disabilities are unable to use the mainstream applications running on Microsoft Windows operating systems without the assistance of accessibility aids. Thus, accessibility aids allow people with these disabilities to gain or improve their access to the computing world.

In 1988, Microsoft became involved in accessibility issues and, since then, has worked hard to improve the accessibility of products as well as create new and better technologies that others can use.

This white paper is intended to show how the console Application Programming Interfaces (APIs) can be used to programmatically access information about the console and applications running under the console. It also seeks to show how the console APIs and events can be used by assistive technologies to work with applications running within a console. This paper outlines the requirements for console accessibility in the Windows XP version of the Windows operating system, but does not address the console as a whole.

To make a console more accessible to individuals with certain disabilities, Microsoft provides a programmatic way to expose the user interface. This lets third-party software and hardware developers expose the PC interface through other methods (for example, Braille displays and verbal descriptions of the user interface). The console provides mechanisms that can keep applications informed of changes to the console and its contents. This document outlines the APIs and events used to expose the console.

## Backward Compatibility

In the past, information about the console was gathered using real-mode drivers. Real-mode drivers are drivers that run under the operating system of the console and understand how to interact with MS-DOS applications by examining specific portions of the system memory. The Windows XP version does not support real-mode drivers in any form. For any aids relying on real-mode drivers to support the console, developers will have to rewrite their applications to use the new WinEvents and APIs. Most of these APIs applied to applications that were creating a console themselves. Several new APIs have been added that allow applications to attach themselves to a console on the system. The WinEvents associated with the console are new and have never existed on any previous version of the Windows operating system.

## Definition of Terms

### API

Application Programming Interface is an interface exposed by a software module as a means for other software modules to interact with it. For example, applications generally interact with an operating system by way of the APIs that the operating system exposes. In the case of the Windows XP operating system, the APIs consist of functions that an application uses to request operating system services such as screen management, keyboard input, printer output, and console accessibility. Microsoft Active Accessibility provides functions (such as [**AccessibleObjectFromWindow**](https://msdn.microsoft.com/library/windows/desktop/dd317978) and [**AccessibleObjectFromPoint**](https://msdn.microsoft.com/library/windows/desktop/dd317977)) that allow clients to retrieve information about accessible objects in an application.

### Console

A console is an interface that provides input and output to character-mode applications. Consoles manage input and output (I/O) for *character-mode applications* (applications that do not provide their own graphical user interface). This processor-independent mechanism makes it easy to port existing character-mode applications or to create new character-mode tools and applications.

### SDK

A Software Development Kit (SDK) is a set of tools and libraries for creating software applications for Windows operating systems.

### WinEvents

Active Accessibility provides a mechanism called WinEvents that allows servers and the operating system to notify clients when an accessible object changes in some manner.

The system generates events for:

-   System-wide notifications about focus changes. WinEvents can signal when an object receives or loses focus.
-   Activation changes. WinEvents can signal when an object is created or destroyed, or when an object's state or location changes.
-   Events regarding system-provided objects, such as common controls.

## Assumptions

This paper is written for accessibility aid developers. It contains several assumptions in respect to this audience, including:

-   The developer has at least intermediate-level programming skills and is familiar with Windows software development.
-   The developer is familiar with C and Visual C++ programming concepts.
-   The developer is familiar with the Windows API.
-   The developer is familiar with WinEvents.

## Accessibility through APIs and Events

In the past, accessibility aids have relied on real-mode drivers to interrogate well-known areas of the system memory. This worked because the MS-DOS operating system allowed applications to interrogate its memory and it always used well-known addresses to store information. With the security constraints of Windows NT, these techniques were no longer supported. Since then, accessibility aids have been looking for other ways to support the console effectively within the operating system.

Microsoft has built the console APIs and events so that developers can accomplish the tasks necessary for accessibility aids to support the console effectively. The goals of these APIs and events were to allow accessibility aids to accomplish the following:

-   Determine when the application currently being used is a console.
-   Gather information about the application running under the console.
-   Track user interactions with the console.

Each of these scenarios may be accomplished using a variety of the events and APIs provided within the Windows XP operating system. By allowing an application to track user interactions with the console and providing APIs to access the current state of information contained within the console, the accessibility aids can accurately represent applications running under the console.

This section describes the three scenarios in which aids use the APIs and events. The section following this one, [Example Scenarios](#example-scenarios), provides samples of these scenarios.

### To determine when an application currently in use is a console

Consoles are managed under the Microsoft Windows architecture. This means that most of the WinEvents associated with standard operating systems apply to consoles as well. It is recommended that you follow the OBJECT\_FOCUS\_EVENT to determine when a particular window has the input focus. To determine if that application is the console, you can do one of two things:

-   Call the [**AttachConsole**](https://msdn.microsoft.com/library/windows/desktop/ms681952) function and check to see if it returns **TRUE**.
-   Read the name property of the **IAccessible** associated with the window and look for the word Command Prompt.

If an application is interested in knowing when a console window is created and destroyed, track the WinEvents EVENT\_OBJECT\_CREATE and EVENT\_OBJECT\_DESTROY.

### To gather information about the application running under the console

The console provides an assortment of function that allows applications to programmatically access its internal buffer and current state. An application may call these functions after attaching itself to the console through the [**AttachConsole**](https://msdn.microsoft.com/library/windows/desktop/ms681952) function. An application may only be attached to one console at a time. An application will have to detach itself from any console prior to attaching itself to a new console. Specific information on the console functions is contained in [Console Reference](https://msdn.microsoft.com/library/windows/desktop/ms682087).

### To track user interactions with the console

Several new WinEvents have been added to provide information about user interactions within the console. These events are geared toward providing specific information about user interactions with console applications. The new events are as follows:

<dl> <dt>

<span id="EVENT_CONSOLE_CARET"></span><span id="event_console_caret"></span>EVENT\_CONSOLE\_CARET
</dt> <dd>

Provides notification when the caret within the console changes position.

</dd> <dt>

<span id="EVENT_CONSOLE_UPDATE_REGION"></span><span id="event_console_update_region"></span>EVENT\_CONSOLE\_UPDATE\_REGION
</dt> <dd>

Provides information on when a section of text is updated within the console.

</dd> <dt>

<span id="EVENT_CONSOLE_UPDATE_SIMPLE"></span><span id="event_console_update_simple"></span>EVENT\_CONSOLE\_UPDATE\_SIMPLE
</dt> <dd>

Notifies aids of when a single character has been changed in the buffer.

</dd> <dt>

<span id="EVENT_CONSOLE_UPDATE_SCROLL"></span><span id="event_console_update_scroll"></span>EVENT\_CONSOLE\_UPDATE\_SCROLL
</dt> <dd>

Notifies aids when the console has been scrolled.

</dd> <dt>

<span id="EVENT_CONSOLE_LAYOUT"></span><span id="event_console_layout"></span>EVENT\_CONSOLE\_LAYOUT
</dt> <dd>

Notifies aids that the console's layout has changed. The console's layout changes from window to full-screen.

</dd> <dt>

<span id="EVENT_CONSOLE_START_APPLICATION"></span><span id="event_console_start_application"></span>EVENT\_CONSOLE\_START\_APPLICATION
</dt> <dd>

Triggered when a new console process has started.

</dd> <dt>

<span id="EVENT_CONSOLE_END_APPLICATION"></span><span id="event_console_end_application"></span>EVENT\_CONSOLE\_END\_APPLICATION
</dt> <dd>

Triggered when a console process is terminated.

</dd> </dl>

## Example Scenarios

Following are scenarios intended to provide information to the user about the interaction between the console and the user.

### How To Determine if the Current Application is a Console

Use [**AttachConsole**](https://msdn.microsoft.com/library/windows/desktop/ms681952) to determine if the current window is a console.


```
// Track and Find Consoles

#include <stdio.h>
#include <tchar.h>
#include <windows.h>
#include <Strsafe.h> 

#define BUFFSIZE  128

PROCESS_INFORMATION hConsole1, hConsole2;
typedef BOOL (WINAPI* PFN_AttachConsole)(DWORD);
typedef HWND (WINAPI* PFN_GetConsoleWindow)(VOID);

PFN_AttachConsole fpAttachConsole;
PFN_GetConsoleWindow fpGetConsoleWindow;
DWORD g_dwCurrentProc;
void createConsoles(void);

// Main entry point (the function arguments are ignored).
int _tmain(int argc, _TCHAR* argv[])
{

    createConsoles();
    return 0;
}


void createConsoles(void)
{
    int iResponse;
    iResponse = IDOK;
    LPTSTR lpstrMyprompt;
    LPTSTR lpstrEditcmd;
    LPTSTR lpstrSysDir;
    DWORD cWritten;
    TCHAR buffer[BUFFSIZE];
    TCHAR buffer2[BUFFSIZE];
    TCHAR buffer3[BUFFSIZE];
    HINSTANCE hInst;
    STARTUPINFO hStartUp;
    RECT   rcConsole2;
   
    // Check for AttachConsole
    hInst = ::LoadLibrary(L"kernel32.dll");
    fpAttachConsole = (BOOL (_stdcall*)(DWORD))GetProcAddress(hInst,"AttachConsole");
    fpGetConsoleWindow = (HWND (_stdcall *)(VOID))GetProcAddress(hInst,"GetConsoleWindow");
   
    memset(&amp;hStartUp, 0, sizeof(hStartUp));   
    hStartUp.cb = sizeof(hStartUp);  
    lpstrMyprompt = &amp;buffer[0];
    lpstrEditcmd = &amp;buffer2[0];
    lpstrSysDir = &amp;buffer3[0];
   
    GetSystemDirectory(lpstrSysDir,BUFFSIZE);

    size_t cb = sizeof(TCHAR) * BUFFSIZE;
    StringCbPrintf(lpstrEditcmd, cb, L"%s\\edit.com", lpstrSysDir);
    StringCbCopy(lpstrMyprompt, cb, L"Console #1");

    // First, we have to create two consoles
    if (FALSE == CreateProcess(lpstrEditcmd, NULL, NULL, NULL, FALSE,
            CREATE_NEW_CONSOLE | NORMAL_PRIORITY_CLASS, NULL, 
            NULL, &amp;hStartUp, &amp;hConsole1))
    {
        StringCbPrintf(lpstrMyprompt, cb, L"Error, couldn't create a new console: %d.", 
            GetLastError());
        MessageBox(NULL, lpstrMyprompt, L"Track and Find Consoles", 
            MB_OK | MB_SYSTEMMODAL);

        return;
    }

    StringCbPrintf(lpstrEditcmd, cb, L"\nAttached\n"); 

    Sleep(5000);
    BOOL bRet = fpAttachConsole(hConsole1.dwProcessId);
    if (bRet)
    {
        HANDLE hStdOut = GetStdHandle( STD_OUTPUT_HANDLE );

        if (FALSE == WriteConsole( hStdOut, lpstrEditcmd, lstrlen(lpstrMyprompt),
                &amp;cWritten, NULL))
        {
            StringCbPrintf(lpstrMyprompt, cb, L"Error, couldn't attach to the console: %d.", 
                GetLastError()); 
            MessageBox(NULL,lpstrMyprompt, L"Track and Find Consoles", MB_OK | MB_SYSTEMMODAL);
        }

        SetConsoleTitle (lpstrMyprompt);
        MessageBox (NULL, L"Successfully attached to console #1", 
            L"Track and Find Consoles", MB_OK | MB_SYSTEMMODAL);
        HWND hWnd = fpGetConsoleWindow();
        GetWindowRect(hWnd,&amp;rcConsole2);
      
        hStartUp.dwX = rcConsole2.left + 10;
        hStartUp.dwY = rcConsole2.bottom + 10;
        hStartUp.dwXSize = rcConsole2.right - rcConsole2.left;
        hStartUp.dwYSize = rcConsole2.bottom - rcConsole2.top;
        hStartUp.dwFlags = STARTF_USEPOSITION;
        g_dwCurrentProc = hConsole1.dwProcessId;
    }
    else
    {
        StringCbPrintf(lpstrMyprompt, cb, L"Error, couldn't attach to the console: %d.", 
                GetLastError()); 
        MessageBox(NULL,lpstrMyprompt, L"Track and Find Consoles", 
                MB_OK | MB_SYSTEMMODAL);
    }

    FreeConsole();

    StringCbPrintf(lpstrEditcmd, cb, L"%s\\edit.com", lpstrSysDir);
    StringCbCopy(lpstrMyprompt, cb, L"Console #2");

    // First, we have to create two consoles
    if (FALSE == CreateProcess(lpstrEditcmd, NULL, NULL, NULL, FALSE,
                CREATE_NEW_CONSOLE | NORMAL_PRIORITY_CLASS,
                NULL, NULL, &amp;hStartUp, &amp;hConsole2))
    {
        StringCbPrintf(lpstrMyprompt, cb, L"Error, couldn't create a new console: %d.", 
                GetLastError()); 
        MessageBox(NULL,lpstrMyprompt, L"Track and Find Consoles", 
                MB_OK | MB_SYSTEMMODAL);
        return;
    }

    Sleep(5000);
    bRet = fpAttachConsole(hConsole2.dwProcessId);
    if (FALSE == bRet)
    {
        StringCbPrintf(buffer, cb, L"Error, couldn't attach to the console: %d.", 
                GetLastError()); 
        MessageBox(NULL,buffer, L"Track and Find Consoles", 
                MB_OK | MB_SYSTEMMODAL);
      return;
   }
   
   SetConsoleTitle (lpstrMyprompt);

   FreeConsole();

}
```



### How To Extract Console Information

An application will have to attach itself to the console by using the [**AttachConsole**](https://msdn.microsoft.com/library/windows/desktop/ms681952) function. You can then use any of the console functions to gather information about the console. The following three illustrations may be of interest to a developer:

1.  When the EVENT\_CONSOLE\_UPDATE\_REGION event is triggered, notify the user that this event was received and then display the portion of the buffer that was changed. The [**ReadConsoleOutput**](https://msdn.microsoft.com/library/windows/desktop/ms684965) and [**WriteConsoleOutput**](https://msdn.microsoft.com/library/windows/desktop/ms687404) functions can be used. The following sample demonstrates one method for retrieving the region data and writing it to a new console.

    ```
    // Extracting Console Information

    void DisplayRegion()
    {
       int i;
       HANDLE hStdout;
       LPTSTR lpstrMyprompt;
       DWORD cWritten;
       TCHAR buffer[BUFFSIZE];
       lpstrMyprompt = &amp;buffer[0];
       size_t cb = sizeof(TCHAR) * BUFFSIZE;

       CHAR_INFO chiBuffer[3200];
       COORD coordBufSize, coordBufCoord;
       SMALL_RECT srctReadRect, srctWriteRect;

       FreeConsole();

       BOOL bRet = fpAttachConsole(hConsole1.dwProcessId);
       if (FALSE == bRet)
       {
          StringCbPrintf(buffer, cb, L"Error, couldn't attach to the console: %d.", 
                GetLastError());
          MessageBox(NULL, buffer, L"Track and Find Consoles", 
                MB_OK | MB_SYSTEMMODAL);
          return;
       }

       hStdout = GetStdHandle(STD_OUTPUT_HANDLE); 

       for (i = 1; i < 10; i++)
       {

          StringCbPrintf(buffer, cb, L"\nLine %d to copy over...\n", i);
          WriteConsole(
             hStdout,
             buffer,
             lstrlen(buffer),
             &amp;cWritten,
             NULL
             );
       }
       srctReadRect.Top=0;
       srctReadRect.Left=0;
       srctReadRect.Bottom=50;
       srctReadRect.Right=40;

       coordBufSize.X=40;
       coordBufSize.Y=50;

       coordBufCoord.X=0;
       coordBufCoord.Y=0;

       ReadConsoleOutput(
          hStdout,
          chiBuffer,
          coordBufSize,
          coordBufCoord,
          &amp;srctReadRect
          );

       srctWriteRect.Left=0;
       srctWriteRect.Top=0;
       srctWriteRect.Right=40;
       srctWriteRect.Bottom=50;

       FreeConsole();

       bRet = fpAttachConsole(hConsole2.dwProcessId);
       if (FALSE == bRet)
       {
          StringCbPrintf(buffer, cb, L"Error, couldn't attach to the console: %d.", 
              GetLastError());
          MessageBox(NULL,buffer, L"Track and Find Consoles", 
                MB_OK | MB_SYSTEMMODAL);
          return;
       }

       hStdout = GetStdHandle(STD_OUTPUT_HANDLE); 

       WriteConsoleOutput(
          hStdout,
          chiBuffer,
          coordBufSize,
          coordBufCoord,
          &amp;srctWriteRect
          );

       FreeConsole();

    return;

    }
    ```

    

2.  When the EVENT\_CONSOLE\_UPDATE\_SCROLL event is triggered, notify the user that this event was received and then display the region of the buffer that is currently visible in the console window. The [**ReadConsoleOutput**](https://msdn.microsoft.com/library/windows/desktop/ms684965) and [**WriteConsoleOutput**](https://msdn.microsoft.com/library/windows/desktop/ms687404) functions can be used. The following sample demonstrates one method for retrieving the region data and writing it to a new console.

    ```
    // Extracting Console Information

    void CopyDisplayedText(void) 
    {
       int i;
       HANDLE hStdout;
       DWORD cWritten;
       TCHAR buffer[BUFFSIZE];
       size_t cb = sizeof(TCHAR) * BUFFSIZE;

       CHAR_INFO chiBuffer[3200];
       COORD coordBufSize, coordBufCoord;
       SMALL_RECT srctReadRect, srctWriteRect;
       CONSOLE_SCREEN_BUFFER_INFO lConsoleScreenBufferInfo;

       FreeConsole();
       
       BOOL bRet = fpAttachConsole(hConsole1.dwProcessId);
       if (FALSE == bRet)
       {
          StringCbPrintf(buffer, cb, L"Error, couldn't attach to the console: %d.", 
              GetLastError());
          MessageBox(NULL,buffer, L"Track and Find Consoles", 
                MB_OK | MB_SYSTEMMODAL);
          return;
       }
       
       hStdout = GetStdHandle(STD_OUTPUT_HANDLE); 

       for (i = 1; i < 30; i++)
       {
          StringCbPrintf(buffer, cb, L"CopyDisplayedText: Line to ignore %d\n", i);
          WriteConsole(
             hStdout,
             buffer,
             lstrlen(buffer),
             &amp;cWritten,
             NULL
             );
       }

       StringCbPrintf(buffer, cb, L"\n\n");
       for (i = 1; i < 10; i++)
       {
          WriteConsole(
             hStdout,
             buffer,
             lstrlen(buffer),
             &amp;cWritten,
             NULL
             );
       }


       for (i = 1; i < 20; i++)
       {
          StringCbPrintf(buffer, cb, L"CopyDisplayedText:Copy Line %d\n", i);
          WriteConsole(
             hStdout,
             buffer,
             lstrlen(buffer),
             &amp;cWritten,
             NULL
             );
       }

       MessageBox (NULL, L"Copy to new window", L"APIs", MB_OK);

       // Get the screen buffer information and set the rectangles
       GetConsoleScreenBufferInfo(
          hStdout, &amp;lConsoleScreenBufferInfo
          );
       srctReadRect.Top=lConsoleScreenBufferInfo.srWindow.Top;
       srctReadRect.Left=lConsoleScreenBufferInfo.srWindow.Left;
       srctReadRect.Bottom=lConsoleScreenBufferInfo.srWindow.Bottom;
       srctReadRect.Right = lConsoleScreenBufferInfo.srWindow.Right;

       coordBufSize.X=lConsoleScreenBufferInfo.srWindow.Right;
       coordBufSize.Y=lConsoleScreenBufferInfo.srWindow.Bottom;
       coordBufCoord.X=lConsoleScreenBufferInfo.srWindow.Left;
       coordBufCoord.Y=lConsoleScreenBufferInfo.srWindow.Top;

       // Read the window
       ReadConsoleOutput(
          hStdout,
          chiBuffer,
          coordBufSize,
          coordBufCoord,
          &amp;srctReadRect
          );

       srctWriteRect.Left=lConsoleScreenBufferInfo.srWindow.Left;
       srctWriteRect.Top=lConsoleScreenBufferInfo.srWindow.Top;
       srctWriteRect.Right=lConsoleScreenBufferInfo.srWindow.Right;
       srctWriteRect.Bottom=lConsoleScreenBufferInfo.srWindow.Bottom;

       FreeConsole();

       bRet = fpAttachConsole(hConsole2.dwProcessId);
       if (FALSE == bRet)
       {
          StringCbPrintf(buffer, cb, L"Error, couldn't attach to the console: %d.", 
              GetLastError());
          MessageBox(NULL,buffer, L"Track and Find Consoles", 
                MB_OK | MB_SYSTEMMODAL);
          return;
       }

       hStdout = GetStdHandle(STD_OUTPUT_HANDLE); 
       
       // Display the buffer in the new window
       WriteConsoleOutput(
          hStdout,
          chiBuffer,
          coordBufSize,
          coordBufCoord,
          &amp;srctWriteRect
          );
       FreeConsole();

       MessageBox (NULL, L"Return to original console.",
           L"APIs", MB_OK);
    return;
    }
    ```

    

### Console Specific Events

The console triggers several WinEvents to provide more comprehensive information about the interactions between the user and console applications. Following are scenarios for each event:

-   When the WinEvent EVENT\_CONSOLE\_CARET is triggered, inform the user that the caret position has changed and whether the caret is selecting text or is visible.
-   When the WinEvent EVENT\_CONSOLE\_UPDATE\_SIMPLE is triggered, inform the user that this event was received and then display the character that was just entered.
-   When the WinEvent EVENT\_CONSOLE\_LAYOUT is triggered, inform the user that this event was received.
-   When the WinEvent EVENT\_CONSOLE\_START\_ APPLICATION is triggered, inform the user that this event was received. This event determines when an application is started from within a DOS box.
-   When the WinEvent EVENT\_CONSOLE\_END\_ APPLICATION is triggered, inform the user that this event was received.
-   When the WinEvent EVENT\_OBJECT\_CREATE is triggered, track the event to determine when a console is created.
-   When the WinEvent EVENT\_OBJECT\_FOCUS is triggered, you can determine when a console has focus or not.


```
HWINEVENTHOOK   hEventHook;

#define  EVENT_CONSOLE_CARET              0x4001
#define  EVENT_CONSOLE_UPDATE_REGION      0x4002
#define  EVENT_CONSOLE_UPDATE_SIMPLE      0x4003
#define  EVENT_CONSOLE_UPDATE_SCROLL      0x4004
#define  EVENT_CONSOLE_LAYOUT             0x4005
#define  EVENT_CONSOLE_START_APPLICATION  0x4006
#define  EVENT_CONSOLE_END_APPLICATION    0x4007

#define WINEVENTDLL_API __declspec(dllexport)

/*******************************************************************
WinEventProc() - Callback function handles events
*******************************************************************/
WINEVENTDLL_API VOID CALLBACK WinEventProc( HWINEVENTHOOK 
      hWinEventHook, DWORD event, HWND hwnd, 
                  LONG idObject, LONG idChild, 
                  DWORD dwEventThread, DWORD dwmsEventTime )
{

   DWORD dwProcessId;
   GetWindowThreadProcessId(hwnd,&amp;dwProcessId);

   if (((dwProcessId == hConsole1.dwProcessId) || 
      (dwProcessId == hConsole2.dwProcessId)) &amp;&amp;
      (dwProcessId == g_dwCurrentProc))
      return;

   TCHAR Buf[BUFFSIZE];
   size_t cb = sizeof(TCHAR) * BUFFSIZE;
   size_t len = 0;
   HANDLE hStdOut = GetStdHandle( STD_OUTPUT_HANDLE );
   DWORD cWritten;

   switch (event)
   {

   case EVENT_CONSOLE_CARET:
   {

         if( 1 == idObject )      //CONSOLE_CARET_SELECTION
            StringCbCopy(Buf, cb, L"idObject: CONSOLE CARET SELECTION - ");
         else if( 2 == idObject ) //CONSOLE_CARET_VISIBLE
            StringCbCopy(Buf, cb, L"idObject: CONSOLE CARET VISIBLE - ");
         else
            StringCbPrintf(Buf, cb, L" idObject: %d - INVALID VALUE!! - ", 
                    idObject );

         StringCbPrintf(Buf, cb, L"\r\nEvent Console CARET!\r\nX: \
                                  %d - Y: %d \r\n\r\n", 
                                  LOWORD(idChild), HIWORD(idChild) );
         StringCbLength(Buf, cb, &amp;len); 
         if (FALSE == WriteConsole(hStdOut, Buf, len, &amp;cWritten, NULL))
         {
            StringCbPrintf(Buf, cb, L"Error, couldn't write to the console: %d.", 
                    GetLastError());
            MessageBox(NULL, Buf, L"Track and Find Consoles", MB_OK | MB_SYSTEMMODAL);
         }
   }
      break;


   case EVENT_CONSOLE_UPDATE_REGION:
   {
         StringCbPrintf(Buf, cb, L"Event Console UPDATE REGION!\r\n \
                                  Left: %d - Top: %d - Right: %d - Bottom:%d \r\n\r\n", 
                                  LOWORD(idObject), HIWORD(idObject), LOWORD(idChild), 
                                  HIWORD(idChild) );
         StringCbLength(Buf, cb, &amp;len); 
         if (FALSE == WriteConsole(hStdOut, Buf, len, &amp;cWritten, NULL))
         {
            StringCbPrintf(Buf, cb, L"Error, couldn't write to the console: %d.", 
                    GetLastError());
            MessageBox(NULL,Buf, L"Track and Find Consoles", MB_OK | MB_SYSTEMMODAL);
         }

   }
      break;

   
   case EVENT_CONSOLE_UPDATE_SIMPLE:
      {
         StringCbPrintf(Buf, cb, L"\r\nEvent Console UPDATE SIMPLE!\r\n \
                                  X: %d - Y: %d\t Char: %d Attr: %d\r\n\r\n", 
                                  LOWORD(idObject), HIWORD(idObject), 
                                  LOWORD(idChild), HIWORD(idChild) );
         StringCbLength(Buf, cb, &amp;len); 
         if (FALSE == WriteConsole( hStdOut, Buf, len, &amp;cWritten, NULL))
         {
            StringCbPrintf(Buf, cb, L"Error, couldn't write to the console: %d.", 
                    GetLastError());
            MessageBox(NULL, Buf, L"Track and Find Consoles", MB_OK | MB_SYSTEMMODAL);
         }

      }
      break;

    
   case EVENT_CONSOLE_UPDATE_SCROLL:
      {
         StringCbPrintf(Buf, cb, L"Event Console UPDATE SCROLL!\r\ndx: \
                                  %d  -  dy: %d\r\n\r\n", idObject, idChild );
         StringCbLength(Buf, cb, &amp;len);                     
         if (FALSE == WriteConsole( hStdOut, Buf, len, &amp;cWritten, NULL))
         {
            StringCbPrintf(Buf, cb, L"Error, couldn't write to the console: %d.", 
                    GetLastError());
            MessageBox(NULL, Buf, L"Track and Find Consoles", MB_OK | MB_SYSTEMMODAL);
         }
      }
      break;

   
   case EVENT_CONSOLE_LAYOUT:
      {
         StringCbPrintf(Buf, cb, L"Event Console LAYOUT!\r\n", idObject, idChild );
         StringCbLength(Buf, cb, &amp;len);                     
         if (FALSE == WriteConsole( hStdOut, Buf, len, &amp;cWritten, NULL))
         {
            StringCbPrintf(Buf, cb, L"Error, couldn't write to the console: %d.", 
                    GetLastError());
            MessageBox(NULL, Buf, L"Track and Find Consoles", MB_OK | MB_SYSTEMMODAL);
         }

      }
      break;

   
   case EVENT_CONSOLE_START_APPLICATION:
      {
         StringCbPrintf(Buf, cb, L"Event Console START APPLICATION!\r\n \
                                  Process ID: %d - Child ID: %d\r\n\r\n", 
                                  idObject, idChild );
         StringCbLength(Buf, cb, &amp;len);                     
         if (FALSE == WriteConsole(hStdOut, Buf, len, &amp;cWritten, NULL))
         {
            StringCbPrintf(Buf, cb, L"Error, couldn't write to the console: %d.", 
                    GetLastError());
            MessageBox(NULL, Buf, L"Track and Find Consoles", MB_OK | MB_SYSTEMMODAL);
         }
      }
      break;

   
   case EVENT_CONSOLE_END_APPLICATION:
      {
         StringCbPrintf(Buf, cb, L"Event Console END APPLICATION!\r\n \
                                  Process ID: %d - Child ID: %d\r\n\r\n", 
                                  idObject, idChild );
         StringCbLength(Buf, cb, &amp;len);                     
         if (FALSE == WriteConsole(hStdOut, Buf, len, &amp;cWritten, NULL ))
         {
            StringCbPrintf(Buf, cb, L"Error, couldn't write to the console: %d.", 
                    GetLastError());
            MessageBox(NULL, Buf, L"Track and Find Consoles", MB_OK | MB_SYSTEMMODAL);
         }

      }
      break;
   }

    return;

}


/*************************************************************************
InstallWinEventsHook() - Initalize the Active Accessibility subsystem
*************************************************************************/
WINEVENTDLL_API BOOL InstallWinEventsHook()
{

   TCHAR buffer[BUFFSIZE];
   LPTSTR lpstrMyprompt;
   size_t cb = sizeof(TCHAR) * BUFFSIZE;
   size_t len = 0;

   lpstrMyprompt = &amp;buffer[0];

   // Set up event call back
    hEventHook = SetWinEventHook(EVENT_CONSOLE_CARET,               
   // We want all events
                                 EVENT_CONSOLE_END_APPLICATION,     
                                 NULL,         // Use our own module
                                 WinEventProc, // Our callback function
                                 0,            // All processes
                                 0,            // All threads
                                 WINEVENT_SKIPOWNPROCESS | 
                                 WINEVENT_OUTOFCONTEXT); 

    // Did we install correctly? 
    if (hEventHook)
   {
      BOOL bRet = fpAttachConsole(hConsole1.dwProcessId);
      if (bRet)
      {
         HANDLE hStdout = GetStdHandle( STD_OUTPUT_HANDLE );
         DWORD cWritten;

         StringCbPrintf(buffer, cb, 
             L"\nPlease start typing to see event information\n");
         StringCbLength(buffer, cb, &amp;len);                     
         if (FALSE == WriteConsole(hStdout, buffer, len, &amp;cWritten, NULL))
         {
            StringCbPrintf(buffer, cb, L"Error, couldn't write to the console: %d.", 
                    GetLastError());
            MessageBox(NULL, buffer, L"Track and Find Consoles", MB_OK | MB_SYSTEMMODAL);
         }
         
         g_dwCurrentProc = hConsole1.dwProcessId;
         return TRUE;
      }
   }

    // Did not install properly - fail
   StringCbPrintf(buffer, cb, L"Error, couldn't set windows hook: %d.", 
        GetLastError());
   MessageBox(NULL, lpstrMyprompt, L"Track and Find Consoles", 
         MB_OK | MB_SYSTEMMODAL);
    return FALSE;
}

/*************************************************************************
UninstallWinEventsHook() - Shuts down the Active Accessibility subsystem
*************************************************************************/
WINEVENTDLL_API BOOL UninstallWinEventsHook(void)
{
    
    // Remove the WinEvent hook    
    UnhookWinEvent(hEventHook);
    
    return(TRUE);
}
```



## Additional Information

[Microsoft Accessibility](http://go.microsoft.com/fwlink/p/?linkid=202480): A website delineating many features for developers of accessibility aids.

 

 




---
title: Registering for device notification
description: Applications can use the RegisterDeviceNotification function to register to receive notification messages from the system.
ms.date: 08/28/2020
ms.assetid: f3a4477a-7b09-4943-8b06-f252f8f9fed8
ms.topic: article
ms.custom: contperf-fy21q1
---

# Registering for device notification

The operating system can send notification messages that represent the events raised by a device. The system sends those notifications either to a window or to a Windows service. And you can register to receive those notifications by calling the [**RegisterDeviceNotification**](/windows/win32/api/winuser/nf-winuser-registerdevicenotificationw) function.

This topic provides a code example that shows you how to register for device notifications. You can identify the device to receive notifications about by specifying a device class when you call **RegisterDeviceNotification**. And you identify that device class by its GUID.

## Source code listing

If you want to build and run this source code example as an app, then begin by creating a new project in Microsoft Visual Studio. Create a new project based on the **Windows Desktop Application** project template. Name the project *RegisterDeviceNotification*.

Open `RegisterDeviceNotification.cpp`, delete its entire contents, and paste in the listing below.

```cpp
// RegisterDeviceNotification.cpp
#include <windows.h>
#include <stdio.h>
#include <tchar.h>
#include <strsafe.h>
#include <dbt.h>

// This GUID is for all USB serial host PnP drivers, but you can replace it 
// with any valid device class guid.
GUID WceusbshGUID = { 0x25dbce51, 0x6c8f, 0x4a72,
                      0x8a,0x6d,0xb5,0x4c,0x2b,0x4f,0xc8,0x35 };

// For informational messages and window titles.
PWSTR g_pszAppName;

void OutputMessage(
    HWND hOutWnd,
    WPARAM wParam,
    LPARAM lParam
)
// Routine Description:
//     Support routine.
//     Send text to the output window, scrolling if necessary.

// Parameters:
//     hOutWnd - Handle to the output window.
//     wParam  - Standard windows message code, not used.
//     lParam  - String message to send to the window.

// Return Value:
//     None

// Note:
//     This routine assumes the output window is an edit control
//     with vertical scrolling enabled.

//     This routine has no error-checking.
{
    LRESULT   lResult;
    LONG      bufferLen;
    LONG      numLines;
    LONG      firstVis;

    // Make writable and turn off redraw.
    lResult = SendMessage(hOutWnd, EM_SETREADONLY, FALSE, 0L);
    lResult = SendMessage(hOutWnd, WM_SETREDRAW, FALSE, 0L);

    // Obtain current text length in the window.
    bufferLen = SendMessage(hOutWnd, WM_GETTEXTLENGTH, 0, 0L);
    numLines = SendMessage(hOutWnd, EM_GETLINECOUNT, 0, 0L);
    firstVis = SendMessage(hOutWnd, EM_GETFIRSTVISIBLELINE, 0, 0L);
    lResult = SendMessage(hOutWnd, EM_SETSEL, bufferLen, bufferLen);

    // Write the new text.
    lResult = SendMessage(hOutWnd, EM_REPLACESEL, 0, lParam);

    // See whether scrolling is necessary.
    if (numLines > (firstVis + 1))
    {
        int        lineLen = 0;
        int        lineCount = 0;
        int        charPos;

        // Find the last nonblank line.
        numLines--;
        while (!lineLen)
        {
            charPos = SendMessage(
                hOutWnd, EM_LINEINDEX, (WPARAM)numLines, 0L);
            lineLen = SendMessage(
                hOutWnd, EM_LINELENGTH, charPos, 0L);
            if (!lineLen)
                numLines--;
        }
        // Prevent negative value finding min.
        lineCount = numLines - firstVis;
        lineCount = (lineCount >= 0) ? lineCount : 0;

        // Scroll the window.
        lResult = SendMessage(
            hOutWnd, EM_LINESCROLL, 0, (LPARAM)lineCount);
    }

    // Done, make read-only and allow redraw.
    lResult = SendMessage(hOutWnd, WM_SETREDRAW, TRUE, 0L);
    lResult = SendMessage(hOutWnd, EM_SETREADONLY, TRUE, 0L);
}

void ErrorHandler(
    LPCTSTR lpszFunction
)
// Routine Description:
//     Support routine.
//     Retrieve the system error message for the last-error code
//     and pop a modal alert box with usable info.

// Parameters:
//     lpszFunction - String containing the function name where 
//     the error occurred plus any other relevant data you'd 
//     like to appear in the output. 

// Return Value:
//     None

// Note:
//     This routine is independent of the other windowing routines
//     in this application and can be used in a regular console
//     application without modification.
{

    LPVOID lpMsgBuf;
    LPVOID lpDisplayBuf;
    DWORD dw = GetLastError();

    FormatMessage(
        FORMAT_MESSAGE_ALLOCATE_BUFFER |
        FORMAT_MESSAGE_FROM_SYSTEM |
        FORMAT_MESSAGE_IGNORE_INSERTS,
        NULL,
        dw,
        MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
        (LPTSTR)&lpMsgBuf,
        0, NULL);

    // Display the error message and exit the process.

    lpDisplayBuf = (LPVOID)LocalAlloc(LMEM_ZEROINIT,
        (lstrlen((LPCTSTR)lpMsgBuf)
            + lstrlen((LPCTSTR)lpszFunction) + 40)
        * sizeof(TCHAR));
    if (!lpDisplayBuf) return;
    StringCchPrintf((LPTSTR)lpDisplayBuf,
        LocalSize(lpDisplayBuf) / sizeof(TCHAR),
        TEXT("%s failed with error %d: %s"),
        lpszFunction, dw, (LPCTSTR)lpMsgBuf);
    MessageBox(NULL, (LPCTSTR)lpDisplayBuf, g_pszAppName, MB_OK);

    LocalFree(lpMsgBuf);
    LocalFree(lpDisplayBuf);
}

BOOL DoRegisterDeviceInterfaceToHwnd(
    IN GUID InterfaceClassGuid,
    IN HWND hWnd,
    OUT HDEVNOTIFY* hDeviceNotify
)
// Routine Description:
//     Registers an HWND for notification of changes in the device interfaces
//     for the specified interface class GUID. 

// Parameters:
//     InterfaceClassGuid - The interface class GUID for the device 
//         interfaces. 

//     hWnd - Window handle to receive notifications.

//     hDeviceNotify - Receives the device notification handle. On failure, 
//         this value is NULL.

// Return Value:
//     If the function succeeds, the return value is TRUE.
//     If the function fails, the return value is FALSE.

// Note:
//     RegisterDeviceNotification also allows a service handle be used,
//     so a similar wrapper function to this one supporting that scenario
//     could be made from this template.
{
    DEV_BROADCAST_DEVICEINTERFACE NotificationFilter;

    ZeroMemory(&NotificationFilter, sizeof(NotificationFilter));
    NotificationFilter.dbcc_size = sizeof(DEV_BROADCAST_DEVICEINTERFACE);
    NotificationFilter.dbcc_devicetype = DBT_DEVTYP_DEVICEINTERFACE;
    NotificationFilter.dbcc_classguid = InterfaceClassGuid;

    *hDeviceNotify = RegisterDeviceNotification(
        hWnd,                       // events recipient
        &NotificationFilter,        // type of device
        DEVICE_NOTIFY_WINDOW_HANDLE // type of recipient handle
    );

    if (NULL == *hDeviceNotify)
    {
        ErrorHandler(L"RegisterDeviceNotification");
        return FALSE;
    }

    return TRUE;
}

void MessagePump(
    HWND hWnd
)
// Routine Description:
//     Simple main thread message pump.
//

// Parameters:
//     hWnd - handle to the window whose messages are being dispatched

// Return Value:
//     None.
{
    MSG msg;
    int retVal;

    // Get all messages for any window that belongs to this thread,
    // without any filtering. Potential optimization could be
    // obtained via use of filter values if desired.

    while ((retVal = GetMessage(&msg, NULL, 0, 0)) != 0)
    {
        if (retVal == -1)
        {
            ErrorHandler(L"GetMessage");
            break;
        }
        else
        {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
    }
}

INT_PTR WINAPI WinProcCallback(
    HWND hWnd,
    UINT message,
    WPARAM wParam,
    LPARAM lParam
)
// Routine Description:
//     Simple Windows callback for handling messages.
//     This is where all the work is done because the example
//     is using a window to process messages. This logic would be handled 
//     differently if registering a service instead of a window.

// Parameters:
//     hWnd - the window handle being registered for events.

//     message - the message being interpreted.

//     wParam and lParam - extended information provided to this
//          callback by the message sender.

//     For more information regarding these parameters and return value,
//     see the documentation for WNDCLASSEX and CreateWindowEx.
{
    LRESULT lRet = 1;
    static HDEVNOTIFY hDeviceNotify;
    static HWND hEditWnd;
    static ULONGLONG msgCount = 0;

    switch (message)
    {
    case WM_CREATE:
        //
        // This is the actual registration., In this example, registration 
        // should happen only once, at application startup when the window
        // is created.
        //
        // If you were using a service, you would put this in your main code 
        // path as part of your service initialization.
        //
        if (!DoRegisterDeviceInterfaceToHwnd(
            WceusbshGUID,
            hWnd,
            &hDeviceNotify))
        {
            // Terminate on failure.
            ErrorHandler(L"DoRegisterDeviceInterfaceToHwnd");
            ExitProcess(1);
        }


        //
        // Make the child window for output.
        //
        hEditWnd = CreateWindow(TEXT("EDIT"),// predefined class 
            NULL,        // no window title 
            WS_CHILD | WS_VISIBLE | WS_VSCROLL |
            ES_LEFT | ES_MULTILINE | ES_AUTOVSCROLL,
            0, 0, 0, 0,  // set size in WM_SIZE message 
            hWnd,        // parent window 
            (HMENU)1,    // edit control ID 
            (HINSTANCE)GetWindowLong(hWnd, GWL_HINSTANCE),
            NULL);       // pointer not needed 

        if (hEditWnd == NULL)
        {
            // Terminate on failure.
            ErrorHandler(L"CreateWindow: Edit Control");
            ExitProcess(1);
        }
        // Add text to the window. 
        SendMessage(hEditWnd, WM_SETTEXT, 0,
            (LPARAM)TEXT("Registered for USB device notification...\n"));

        break;

    case WM_SETFOCUS:
        SetFocus(hEditWnd);

        break;

    case WM_SIZE:
        // Make the edit control the size of the window's client area. 
        MoveWindow(hEditWnd,
            0, 0,                  // starting x- and y-coordinates 
            LOWORD(lParam),        // width of client area 
            HIWORD(lParam),        // height of client area 
            TRUE);                 // repaint window 

        break;

    case WM_DEVICECHANGE:
    {
        //
        // This is the actual message from the interface via Windows messaging.
        // This code includes some additional decoding for this particular device type
        // and some common validation checks.
        //
        // Note that not all devices utilize these optional parameters in the same
        // way. Refer to the extended information for your particular device type 
        // specified by your GUID.
        //
        PDEV_BROADCAST_DEVICEINTERFACE b = (PDEV_BROADCAST_DEVICEINTERFACE)lParam;
        TCHAR strBuff[256];

        // Output some messages to the window.
        switch (wParam)
        {
        case DBT_DEVICEARRIVAL:
            msgCount++;
            StringCchPrintf(
                strBuff, 256,
                TEXT("Message %d: DBT_DEVICEARRIVAL\n"), (int)msgCount);
            break;
        case DBT_DEVICEREMOVECOMPLETE:
            msgCount++;
            StringCchPrintf(
                strBuff, 256,
                TEXT("Message %d: DBT_DEVICEREMOVECOMPLETE\n"), (int)msgCount);
            break;
        case DBT_DEVNODES_CHANGED:
            msgCount++;
            StringCchPrintf(
                strBuff, 256,
                TEXT("Message %d: DBT_DEVNODES_CHANGED\n"), (int)msgCount);
            break;
        default:
            msgCount++;
            StringCchPrintf(
                strBuff, 256,
                TEXT("Message %d: WM_DEVICECHANGE message received, value %d unhandled.\n"),
                (int)msgCount, wParam);
            break;
        }
        OutputMessage(hEditWnd, wParam, (LPARAM)strBuff);
    }
    break;
    case WM_CLOSE:
        if (!UnregisterDeviceNotification(hDeviceNotify))
        {
            ErrorHandler(L"UnregisterDeviceNotification");
        }
        DestroyWindow(hWnd);
        break;

    case WM_DESTROY:
        PostQuitMessage(0);
        break;

    default:
        // Send all other messages on to the default windows handler.
        lRet = DefWindowProc(hWnd, message, wParam, lParam);
        break;
    }

    return lRet;
}

#define WND_CLASS_NAME TEXT("SampleAppWindowClass")

BOOL InitWindowClass()
// Routine Description:
//      Simple wrapper to initialize and register a window class.

// Parameters:
//     None

// Return Value:
//     TRUE on success, FALSE on failure.

// Note: 
//     wndClass.lpfnWndProc and wndClass.lpszClassName are the
//     important unique values used with CreateWindowEx and the
//     Windows message pump.
{
    WNDCLASSEX wndClass;

    wndClass.cbSize = sizeof(WNDCLASSEX);
    wndClass.style = CS_OWNDC | CS_HREDRAW | CS_VREDRAW;
    wndClass.hInstance = reinterpret_cast<HINSTANCE>(GetModuleHandle(0));
    wndClass.lpfnWndProc = reinterpret_cast<WNDPROC>(WinProcCallback);
    wndClass.cbClsExtra = 0;
    wndClass.cbWndExtra = 0;
    wndClass.hIcon = LoadIcon(0, IDI_APPLICATION);
    wndClass.hbrBackground = CreateSolidBrush(RGB(192, 192, 192));
    wndClass.hCursor = LoadCursor(0, IDC_ARROW);
    wndClass.lpszClassName = WND_CLASS_NAME;
    wndClass.lpszMenuName = NULL;
    wndClass.hIconSm = wndClass.hIcon;


    if (!RegisterClassEx(&wndClass))
    {
        ErrorHandler(L"RegisterClassEx");
        return FALSE;
    }
    return TRUE;
}

int __stdcall _tWinMain(
    _In_ HINSTANCE hInstanceExe,
    _In_opt_ HINSTANCE, // should not reference this parameter
    _In_ PTSTR lpstrCmdLine,
    _In_ int nCmdShow)
{
    //
    // To enable a console project to compile this code, set
    // Project->Properties->Linker->System->Subsystem: Windows.
    //

    int nArgC = 0;
    PWSTR* ppArgV = CommandLineToArgvW(lpstrCmdLine, &nArgC);
    g_pszAppName = ppArgV[0];

    if (!InitWindowClass())
    {
        // InitWindowClass displays any errors
        return -1;
    }

    // Main app window

    HWND hWnd = CreateWindowEx(
        WS_EX_CLIENTEDGE | WS_EX_APPWINDOW,
        WND_CLASS_NAME,
        g_pszAppName,
        WS_OVERLAPPEDWINDOW, // style
        CW_USEDEFAULT, 0,
        640, 480,
        NULL, NULL,
        hInstanceExe,
        NULL);

    if (hWnd == NULL)
    {
        ErrorHandler(L"CreateWindowEx: main appwindow hWnd");
        return -1;
    }

    // Actually draw the window.

    ShowWindow(hWnd, SW_SHOWNORMAL);
    UpdateWindow(hWnd);

    // The message pump loops until the window is destroyed.

    MessagePump(hWnd);

    return 1;
}
```

You can now build and run the project.

## About the code example

The code example uses a window handle for device change notifications, and it contains a large amount of code just to manage the windowing infrastructure. An application intended to be installed as a Windows service would contain different infrastructure code.

The application will receive the [**WM_DEVICECHANGE**](./wm-devicechange.md) message whenever a USB device interface event notification is sent.

The system broadcasts a set of default device change events to all applications and services. You don't need to register to receive those default events. For details, see the **Remarks** section in [**RegisterDeviceNotification**](/windows/win32/api/winuser/nf-winuser-registerdevicenotificationw).

## Related topics

* [Device notifications](./device-notifications.md)
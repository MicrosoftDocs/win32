---
description: The following code examples demonstrate how to perform the following tasks associated with Windows messages and message queues.
ms.assetid: 62b4616c-37bf-4d9f-8891-7010c7035d18
title: Using Messages and Message Queues
ms.topic: article
ms.date: 05/31/2018
---

# Using Messages and Message Queues

The following code examples demonstrate how to perform the following tasks associated with Windows messages and message queues.

-   [Creating a Message Loop](#creating-a-message-loop)
-   [Examining a Message Queue](#examining-a-message-queue)
-   [Posting a Message](#posting-a-message)
-   [Sending a Message](#sending-a-message)

## Creating a Message Loop

The system does not automatically create a message queue for each thread. Instead, the system creates a message queue only for threads that perform operations which require a message queue. If the thread creates one or more windows, a message loop must be provided; this message loop retrieves messages from the thread's message queue and dispatches them to the appropriate window procedures.

Because the system directs messages to individual windows in an application, a thread must create at least one window before starting its message loop. Most applications contain a single thread that creates windows. A typical application registers the window class for its main window, creates and shows the main window, and then starts its message loop — all in the [**WinMain**](/windows/win32/api/winbase/nf-winbase-winmain) function.

You create a message loop by using the [**GetMessage**](/windows/win32/api/winuser/nf-winuser-getmessage) and [**DispatchMessage**](/windows/win32/api/winuser/nf-winuser-dispatchmessage) functions. If your application must obtain character input from the user, include the [**TranslateMessage**](/windows/win32/api/winuser/nf-winuser-translatemessage) function in the loop. **TranslateMessage** translates virtual-key messages into character messages. The following example shows the message loop in the [**WinMain**](/windows/win32/api/winbase/nf-winbase-winmain) function of a simple Windows-based application.

```cpp
HINSTANCE hinst; 
HWND hwndMain; 
 
int PASCAL WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, 
    LPSTR lpszCmdLine, int nCmdShow) 
{ 
    MSG msg;
    BOOL bRet; 
    WNDCLASS wc; 
    UNREFERENCED_PARAMETER(lpszCmdLine); 
 
    // Register the window class for the main window. 
 
    if (!hPrevInstance) 
    { 
        wc.style = 0; 
        wc.lpfnWndProc = (WNDPROC) WndProc; 
        wc.cbClsExtra = 0; 
        wc.cbWndExtra = 0; 
        wc.hInstance = hInstance; 
        wc.hIcon = LoadIcon((HINSTANCE) NULL, 
            IDI_APPLICATION); 
        wc.hCursor = LoadCursor((HINSTANCE) NULL, 
            IDC_ARROW); 
        wc.hbrBackground = GetStockObject(WHITE_BRUSH); 
        wc.lpszMenuName =  "MainMenu"; 
        wc.lpszClassName = "MainWndClass"; 
 
        if (!RegisterClass(&wc)) 
            return FALSE; 
    } 
 
    hinst = hInstance;  // save instance handle 
 
    // Create the main window. 
 
    hwndMain = CreateWindow("MainWndClass", "Sample", 
        WS_OVERLAPPEDWINDOW, CW_USEDEFAULT, CW_USEDEFAULT, 
        CW_USEDEFAULT, CW_USEDEFAULT, (HWND) NULL, 
        (HMENU) NULL, hinst, (LPVOID) NULL); 
 
    // If the main window cannot be created, terminate 
    // the application. 
 
    if (!hwndMain) 
        return FALSE; 
 
    // Show the window and paint its contents. 
 
    ShowWindow(hwndMain, nCmdShow); 
    UpdateWindow(hwndMain); 
 
    // Start the message loop. 
 
    while( (bRet = GetMessage( &msg, NULL, 0, 0 )) != 0)
    { 
        if (bRet == -1)
        {
            // handle the error and possibly exit
        }
        else
        {
            TranslateMessage(&msg); 
            DispatchMessage(&msg); 
        }
    } 
 
    // Return the exit code to the system. 
 
    return msg.wParam; 
} 
```

The following example shows a message loop for a thread that uses accelerators and displays a modeless dialog box. When [**TranslateAccelerator**](/windows/win32/api/winuser/nf-winuser-translateacceleratora) or [**IsDialogMessage**](/windows/win32/api/winuser/nf-winuser-isdialogmessagea) returns **TRUE** (indicating that the message has been processed), [**TranslateMessage**](/windows/win32/api/winuser/nf-winuser-translatemessage) and [**DispatchMessage**](/windows/win32/api/winuser/nf-winuser-dispatchmessage) are not called. The reason for this is that **TranslateAccelerator** and **IsDialogMessage** perform all necessary translating and dispatching of messages.

```cpp
HWND hwndMain; 
HWND hwndDlgModeless = NULL; 
MSG msg;
BOOL bRet; 
HACCEL haccel; 
// 
// Perform initialization and create a main window. 
// 
 
while( (bRet = GetMessage( &msg, NULL, 0, 0 )) != 0)
{ 
    if (bRet == -1)
    {
        // handle the error and possibly exit
    }
    else
    {
        if (hwndDlgModeless == (HWND) NULL || 
                !IsDialogMessage(hwndDlgModeless, &msg) && 
                !TranslateAccelerator(hwndMain, haccel, 
                    &msg)) 
        { 
            TranslateMessage(&msg); 
            DispatchMessage(&msg); 
        }
    } 
} 
```

## Examining a Message Queue

Occasionally, an application needs to examine the contents of a thread's message queue from outside the thread's message loop. For example, if an application's window procedure performs a lengthy drawing operation, you may want the user to be able to interrupt the operation. Unless your application periodically examines the message queue during the operation for mouse and keyboard messages, it will not respond to user input until after the operation has completed. The reason for this is that the [**DispatchMessage**](/windows/win32/api/winuser/nf-winuser-dispatchmessage) function in the thread's message loop does not return until the window procedure finishes processing a message.

You can use the [**PeekMessage**](/windows/win32/api/winuser/nf-winuser-peekmessagea) function to examine a message queue during a lengthy operation. **PeekMessage** is similar to the [**GetMessage**](/windows/win32/api/winuser/nf-winuser-getmessage) function; both check a message queue for a message that matches the filter criteria and then copy the message to an [**MSG**](/windows/win32/api/winuser/ns-winuser-msg) structure. The main difference between the two functions is that **GetMessage** does not return until a message matching the filter criteria is placed in the queue, whereas **PeekMessage** returns immediately regardless of whether a message is in the queue.

The following example shows how to use [**PeekMessage**](/windows/win32/api/winuser/nf-winuser-peekmessagea) to examine a message queue for mouse clicks and keyboard input during a lengthy operation.

```cpp
HWND hwnd; 
BOOL fDone; 
MSG msg; 
 
// Begin the operation and continue until it is complete 
// or until the user clicks the mouse or presses a key. 
 
fDone = FALSE; 
while (!fDone) 
{ 
    fDone = DoLengthyOperation(); // application-defined function 
 
    // Remove any messages that may be in the queue. If the 
    // queue contains any mouse or keyboard 
    // messages, end the operation. 
 
    while (PeekMessage(&msg, hwnd,  0, 0, PM_REMOVE)) 
    { 
        switch(msg.message) 
        { 
            case WM_LBUTTONDOWN: 
            case WM_RBUTTONDOWN: 
            case WM_KEYDOWN: 
                // 
                // Perform any required cleanup. 
                // 
                fDone = TRUE; 
        } 
    } 
} 
```

Other functions, including [**GetQueueStatus**](/windows/win32/api/winuser/nf-winuser-getqueuestatus) and [**GetInputState**](/windows/win32/api/winuser/nf-winuser-getinputstate), also allow you to examine the contents of a thread's message queue. **GetQueueStatus** returns an array of flags that indicates the types of messages in the queue; using it is the fastest way to discover whether the queue contains any messages. **GetInputState** returns **TRUE** if the queue contains mouse or keyboard messages. Both of these functions can be used to determine whether the queue contains messages that need to be processed.

## Posting a Message

You can post a message to a message queue by using the [**PostMessage**](/windows/win32/api/winuser/nf-winuser-postmessagea) function. **PostMessage** places a message at the end of a thread's message queue and returns immediately, without waiting for the thread to process the message. The function's parameters include a window handle, a message identifier, and two message parameters. The system copies these parameters to an [**MSG**](/windows/win32/api/winuser/ns-winuser-msg) structure, fills the **time** and **pt** members of the structure, and places the structure in the message queue.

The system uses the window handle passed with the [**PostMessage**](/windows/win32/api/winuser/nf-winuser-postmessagea) function to determine which thread message queue should receive the message. If the handle is **HWND\_TOPMOST**, the system posts the message to the thread message queues of all top-level windows.

You can use the [**PostThreadMessage**](/windows/win32/api/winuser/nf-winuser-postthreadmessagea) function to post a message to a specific thread message queue. **PostThreadMessage** is similar to [**PostMessage**](/windows/win32/api/winuser/nf-winuser-postmessagea), except the first parameter is a thread identifier rather than a window handle. You can retrieve the thread identifier by calling the [**GetCurrentThreadId**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentthreadid) function.

Use the [**PostQuitMessage**](/windows/win32/api/winuser/nf-winuser-postquitmessage) function to exit a message loop. **PostQuitMessage** posts the [**WM\_QUIT**](wm-quit.md) message to the currently executing thread. The thread's message loop terminates and returns control to the system when it encounters the **WM\_QUIT** message. An application usually calls **PostQuitMessage** in response to the [**WM\_DESTROY**](wm-destroy.md) message, as shown in the following example.


```cpp
case WM_DESTROY: 
 
    // Perform cleanup tasks. 
 
    PostQuitMessage(0); 
    break; 
```



## Sending a Message

The [**SendMessage**](/windows/win32/api/winuser/nf-winuser-sendmessage) function is used to send a message directly to a window procedure. **SendMessage** calls a window procedure and waits for that procedure to process the message and return a result.

A message can be sent to any window in the system; all that is required is a window handle. The system uses the handle to determine which window procedure should receive the message.

Before processing a message that may have been sent from another thread, a window procedure should first call the [**InSendMessage**](/windows/win32/api/winuser/nf-winuser-insendmessage) function. If this function returns **TRUE**, the window procedure should call [**ReplyMessage**](/windows/win32/api/winuser/nf-winuser-replymessage) before any function that causes the thread to yield control, as shown in the following example.


```cpp
case WM_USER + 5: 
    if (InSendMessage()) 
        ReplyMessage(TRUE); 
 
    DialogBox(hInst, "MyDialogBox", hwndMain, (DLGPROC) MyDlgProc); 
    break; 
```



A number of messages can be sent to controls in a dialog box. These control messages set the appearance, behavior, and content of controls or retrieve information about controls. For example, the [**CB\_ADDSTRING**](../controls/cb-addstring.md) message can add a string to a combo box, and the [**BM\_SETCHECK**](../controls/bm-setcheck.md) message can set the check state of a check box or radio button.

Use the [**SendDlgItemMessage**](/windows/win32/api/winuser/nf-winuser-senddlgitemmessagea) function to send a message to a control, specifying the identifier of the control and the handle of the dialog box window that contains the control. The following example, taken from a dialog box procedure, copies a string from a combo box's edit control into its list box. The example uses **SendDlgItemMessage** to send a [**CB\_ADDSTRING**](../controls/cb-addstring.md) message to the combo box.


```cpp
HWND hwndCombo; 
int cTxtLen; 
PSTR pszMem; 
 
switch (uMsg) 
{ 
    case WM_COMMAND: 
        switch (LOWORD(wParam)) 
        { 
            case IDD_ADDCBITEM: 
                // Get the handle of the combo box and the 
                // length of the string in the edit control 
                // of the combo box. 
 
                hwndCombo = GetDlgItem(hwndDlg, IDD_COMBO); 
                cTxtLen = GetWindowTextLength(hwndCombo); 
 
                // Allocate memory for the string and copy 
                // the string into the memory. 
 
                pszMem = (PSTR) VirtualAlloc((LPVOID) NULL, 
                    (DWORD) (cTxtLen + 1), MEM_COMMIT, 
                    PAGE_READWRITE); 
                GetWindowText(hwndCombo, pszMem, 
                    cTxtLen + 1); 
 
                // Add the string to the list box of the 
                // combo box and remove the string from the 
                // edit control of the combo box. 
 
                if (pszMem != NULL) 
                { 
                    SendDlgItemMessage(hwndDlg, IDD_COMBO, 
                        CB_ADDSTRING, 0, 
                        (DWORD) ((LPSTR) pszMem)); 
                    SetWindowText(hwndCombo, (LPSTR) NULL); 
                } 
 
                // Free the memory and return. 
 
                VirtualFree(pszMem, 0, MEM_RELEASE); 
                return TRUE; 
            // 
            // Process other dialog box commands. 
            // 
 
        } 
    // 
    // Process other dialog box messages. 
    // 
 
}
```

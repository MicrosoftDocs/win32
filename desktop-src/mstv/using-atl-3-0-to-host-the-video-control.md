---
title: Using ATL 3.0 to Host the Video Control
description: Using ATL 3.0 to Host the Video Control
ms.assetid: 83955cdb-f6f0-47f8-8470-d7505a7a1602
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using ATL 3.0 to Host the Video Control

This topic applies to Windows XP or later.

This article shows how to host the Video Control using ATL 3.0. The application hosts the Video Control inside a composite control. (A composite control is a type of ActiveX object that contains other controls.) To create the application, you must perform the following steps:

-   Create the framework with the ATL AppWizard.
-   Add the composite control, using the ATL **CComCompositeControl** class.
-   Add the Video Control to the composite control.
-   Add code for showing the composite control.

The remainder of this article describes these steps in more detail.

**Create the Framework**

Create a new project using the ATL COM AppWizard. Select **Executable (EXE)** for the server type. Include the header file Msvidctl.h, and link to the Strmiids.lib library.

**Add the Composite Control**

Use the ATL Object Wizard to create a composite control. For this example, the default attributes are fine. Give the control a name; for example, MyComposite.

**Add the Video Control**

Use the Dialog Editor to add the Video Control to the composite control, by doing the following:

1.  Right click the dialog box.
2.  Choose **Insert ActiveX Control**.
3.  Select **MS TV Video Control**. It should appear in the list if Msvidctl.dll is registered on your system.

Also, check **Visible** in the dialog properties. Otherwise, the control will not be visible.

**Show the Composite Control**

The ATL Object Wizard creates a generic **WinMain** function. Inside this function, add code before the message loop that creates and displays the composite control. The following code snippet shows the code that you need to add, in bold:


```C++
extern "C" int WINAPI _tWinMain(HINSTANCE hInstance, 
    HINSTANCE /*hPrevInstance*/, LPTSTR lpCmdLine, int /*nShowCmd*/)
{
    /* ... */

    //Create the window and show the composite control.
    AtlAxWinInit();
    HWND hWnd = ::CreateWindow(TEXT("AtlAxWin"), 
        Text("
Your Control's ProgID Here"
),
 
        // Example: TEXT("MyTVApp.MyComposite")
        NULL,
        CW_USEDEFAULT, CW_USEDEFAULT,
        CW_USEDEFAULT, CW_USEDEFAULT,
        NULL, NULL,
        ::GetModuleHandle(NULL), NULL);

    MSG msg;
    while (GetMessage(&amp;msg, 0, 0, 0))
    {
        TranslateMessage(&amp;msg);
        DispatchMessage(&amp;msg);
    }
    /* ... */
}
```



Also, add a message handler for the WM\_CLOSE message. In it, destroy the window and post a quit message:


```C++
LRESULT MyComposite::OnClose(
    UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL&amp; bHandled)
{
    DestroyWindow();
    PostQuitMessage(0);
    return 0;
}
```



Now you can get a pointer to the Video Control from within the control class as follows:


```C++
CComPtr<IMSVidCtl> pVidControl;
hr = GetDlgControl(IDC_MSVIDCTL1, __uuidof(IMSVidCtl), 
        reinterpret_cast<void **>(&amp;pVidControl));
```



 

 





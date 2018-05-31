---
title: Using ATL 7.0 to Host the Video Control
description: Using ATL 7.0 to Host the Video Control
ms.assetid: 83f561e2-8eca-4e40-b353-63c33ef9dbd3
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using ATL 7.0 to Host the Video Control

This topic applies to Windows XP or later.

This article shows how to host the Video Control using ATL 7.0 and Visual Studio.NET. The application hosts the Video Control inside a composite control, which is a type of ActiveX object that contains other controls. To create the application, you must perform the following steps:

-   Create the framework with the ATL AppWizard.
-   Add the composite control, using the ATL **CComCompositeControl** class.
-   Add the Video Control to the composite control.
-   Add code for showing the composite control.

The remainder of this article describes these steps in more detail.

**Create the Framework**

Create a new project and select **ATL Project** from the project types. In the application settings, select **Executable (EXE)**.

Include the header file Msvidctl.h, and link to the Strmiids.lib library.

**Add the Composite Control**

Add a composite control class to the project:

1.  From the **Project** menu, choose **Add Class**.
2.  Select **ATL Control** and click **Open**.
3.  Give the control a name, such as MyControl.
4.  Under **Options**, select **Composite Control**. For this example, the default values for the remaining options are fine.

**Add the Video Control**

Use the Dialog Editor to add the Video Control to the composite control, by doing the following:

1.  Right click the dialog box.
2.  Choose **Insert ActiveX Control**.
3.  Select **MS TV Video Control**. It should appear in the list if Msvidctl.dll is registered on your system.

Also, set the **Visible** property to true. Otherwise, the control will not be visible.

**Show the Composite Control**

In your module class that derives from **CAtlExeModuleT**, override the **PreMessageLoop** method to show the control window:


```C++
class CMyControlModule : public CAtlExeModuleT< CMyControlModule >
{
public :
    HRESULT PreMessageLoop(int nCmdShow)
    {
        HRESULT hr;
        hr = CAtlExeModuleT< CMyControlModule >::PreMessageLoop(nCmdShow);
        if (FAILED(hr))
        {
            return hr;
        }
    
        //Create the window and show the composite control.
        AtlAxWinInit();
        HWND hWnd = ::CreateWindow(TEXT("AtlAxWin7"), 
            TEXT("Your Control's ProgID Here"), 
            // Example: TEXT("MyTVApp.MyComposite")
            WS_OVERLAPPED | WS_SYSMENU | WS_CAPTION,
            CW_USEDEFAULT, CW_USEDEFAULT,
            CW_USEDEFAULT, CW_USEDEFAULT,
            NULL, NULL,
            ::GetModuleHandle(NULL), NULL);
        if (hWnd == 0)
        {
            ::MessageBox(0, TEXT("Cannot create window"), 0, MB_OK);
            return E_FAIL;
        }
        ShowWindow(hWnd, nCmdShow);
        return S_OK;
    }
};
```



Now you can get a pointer to the Video Control from within the control class as follows:


```C++
CComPtr<IMSVidCtl> pVidControl;
hr = GetDlgControl(IDC_MSVIDCTL1, __uuidof(IMSVidCtl), 
        reinterpret_cast<void **>(&amp;pVidControl));
```



 

 





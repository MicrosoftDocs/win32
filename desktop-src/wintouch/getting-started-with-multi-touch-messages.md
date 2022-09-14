---
title: Getting Started with Windows Touch Messages
description: This section explains the tasks associated with getting Windows Touch input to function in your application.
ms.assetid: cd4e140e-a0b8-494f-82d9-bc0bfba55ecd
keywords:
- Windows Touch,messages
- Windows Touch,registering for touch input
- Windows Touch,testing input digitizers
ms.topic: article
ms.date: 05/31/2018
---

# Getting Started with Windows Touch Messages

This section explains the tasks associated with getting Windows Touch input to function in your application.

The following steps are typically performed when working with Windows Touch messages:

1.  Test the capabilities of the input digitizer.
2.  Register to receive Windows Touch messages.
3.  Handle the messages.

The message used for Windows Touch is [**WM\_TOUCH**](wm-touchdown.md). This message indicates the various states of contact with a digitizer.

## Testing the Capabilities of the Input Digitizer

The [GetSystemMetrics](/windows/win32/api/winuser/nf-winuser-getsystemmetrics) function can be used to query the capabilities of the input digitizer by passing in the *nIndex* value of **SM\_DIGITIZER**. [GetSystemMetrics](/windows/win32/api/winuser/nf-winuser-getsystemmetrics) returns a bit field that indicates whether the device is ready, whether the device supports pen or touch, whether the input device is integrated or external, and whether the device supports multiple inputs (Windows Touch). The following table shows the bits for the various fields.



| Bit   | 8           | 7           | 6        | 5        | 4            | 3              | 2              | 1                |
|-------|-------------|-------------|----------|----------|--------------|----------------|----------------|------------------|
| Value | Stack Ready | Multi-input | Reserved | Reserved | External Pen | Integrated Pen | External Touch | Integrated Touch |



 

To test the result from the command for a particular feature, you can use the bitwise & operator and the particular bit you are testing. For example, to test for Windows Touch, you would test that the seventh-order bit is set (0x40 in hex). The following code example shows how these values could be tested.


```C++
#include <windows.h>
```




```C++
// test for touch
int value = GetSystemMetrics(SM_DIGITIZER);
if (value & NID_READY){ /* stack ready */}
if (value  & NID_MULTI_INPUT){
    /* digitizer is multitouch */ 
    MessageBoxW(hWnd, L"Multitouch found", L"IsMulti!", MB_OK);
}
if (value & NID_INTEGRATED_TOUCH){ /* Integrated touch */}
```



The following table lists the constants defined in windows.h for testing touch capabilities of the input digitizer.



| Name                   | Value      | Description                                                                                                                                                                                   |
|------------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TABLET\_CONFIG\_NONE   | 0x00000000 | The input digitizer does not have touch capabilities.                                                                                                                                         |
| NID\_INTEGRATED\_TOUCH | 0x00000001 | An integrated touch digitizer is used for input.                                                                                                                                              |
| NID\_EXTERNAL\_TOUCH   | 0x00000002 | An external touch digitizer is used for input.                                                                                                                                                |
| NID\_INTEGRATED\_PEN   | 0x00000004 | An integrated pen digitizer is used for input.                                                                                                                                                |
| NID\_EXTERNAL\_PEN     | 0x00000008 | An external pen digitizer is used for input.                                                                                                                                                  |
| NID\_MULTI\_INPUT      | 0x00000040 | An input digitizer with support for multiple inputs is used for input.                                                                                                                        |
| NID\_READY             | 0x00000080 | The input digitizer is ready for input. If this value is unset, it may mean that the tablet service is stopped, the digitizer is not supported, or digitizer drivers have not been installed. |



 

Checking the NID\_\* values is a useful way of checking the capabilities of a user's computer to configure your application for touch, pen, or non-tablet input. For example, if you have a dynamic user interface (UI) and want to automatically configure some of it, you could check for NID\_INTEGRATED\_TOUCH, NID\_MULTITOUCH, and could get the maximum number of touches the first time that a user runs your application.

> [!Note]  
> There are some inherent limitations for SM\_GETSYSTEMMETRICS. For example, there is no support for plug and play. For this reason, use caution when using this function as a means for permanent configuration.

 

## Registering to Receive Windows Touch Input

Before receiving Windows Touch input, applications must first register to receive Windows Touch input. By registering the application window, the application indicates that it is touch compatible. After the application registers its window, notifications from the Windows Touch driver are forwarded to the application when input is made on the window. When the application shuts down, it unregisters its window to disable notifications.

> [!Note]  
> [**WM\_TOUCH**](wm-touchdown.md) messages are currently "greedy." After the first touch message is received on a window, all touch messages are sent to that window until another window receives focus.

 

> [!Note]  
> By default, you receive [**WM\_GESTURE**](wm-gesture.md) messages instead of [**WM\_TOUCH**](wm-touchdown.md) messages. If you call [**RegisterTouchWindow**](/windows/desktop/api/winuser/nf-winuser-registertouchwindow), you will stop receiving **WM\_GESTURE** messages.

 

The following code demonstrates how an application could register to receive Windows Touch messages in a Win32 application.


```C++
RegisterTouchWindow(hWnd, 0);
```



## Handling Windows Touch Messages

You can handle the Windows Touch messages from applications in Windows operating systems in many ways. If you are programming a GUI application, you add code within the `WndProc` function to handle the messages of interest. If you are programming a Microsoft Foundation Class (MFC) or managed application, you add handlers for the messages of interest. The following code example shows how touch messages could be handled from WndProc in a Windows-based application.


```C++
  LRESULT OnTouch(HWND hWnd, WPARAM wParam, LPARAM lParam ){
    BOOL bHandled = FALSE;
    UINT cInputs = LOWORD(wParam);
    PTOUCHINPUT pInputs = new TOUCHINPUT[cInputs];
    if (pInputs){
        if (GetTouchInputInfo((HTOUCHINPUT)lParam, cInputs, pInputs, sizeof(TOUCHINPUT))){
            for (UINT i=0; i < cInputs; i++){
                TOUCHINPUT ti = pInputs[i];
                //do something with each touch input entry
            }            
            bHandled = TRUE;
        }else{
             /* handle the error here */
        }
        delete [] pInputs;
    }else{
        /* handle the error here, probably out of memory */
    }
    if (bHandled){
        // if you handled the message, close the touch input handle and return
        CloseTouchInputHandle((HTOUCHINPUT)lParam);
        return 0;
    }else{
        // if you didn't handle the message, let DefWindowProc handle it
        return DefWindowProc(hWnd, WM_TOUCH, wParam, lParam);
    }
  }


LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    int wmId, wmEvent;
    PAINTSTRUCT ps;
    HDC hdc;

    switch (message)
    {
      // pass touch messages to the touch handler 
      case WM_TOUCH:
        OnTouch(hWnd, wParam, lParam);
        break;
```





The following code shows how you can implement the message map and a message handler. Note that the messages must be declared in the message map and then the handler for the message should be implemented. For example, in an MFC application, this could be declared in the dialog code. Note also, that the `OnInitDialog` function for your dialog window would have to include a call to [**RegisterTouchWindow**](/windows/desktop/api/winuser/nf-winuser-registertouchwindow) such as `RegisterTouchWindow(m_hWnd, 0)`.


```C++
  // Class implementations within a dialog
  LRESULT TestDlg::OnTouch( WPARAM wParam, LPARAM lParam ){
    //Insert handler code here to do something with the message or uncomment the following line to test
    //MessageBox(L"touch!", L"touch!", MB_OK);
    return 0;
  }
  // The message map
  BEGIN_MESSAGE_MAP()
    ON_WM_CREATE()
    ... ... ...
    ON_MESSAGE(WM_TOUCH, OnTouch)
  END_MESSAGE_MAP()  
 
  BOOL TestDlg::OnInitDialog()
  {
    CDialog::OnInitDialog();    

    RegisterTouchWindow(m_hWnd, 0);
     ... ... ...
  }  
  
```



Touching the window will indicate touches from a pop-up window.

## Related topics

<dl> <dt>

[Windows Touch Input](guide-multi-touch-input.md)
</dt> </dl>

 

 
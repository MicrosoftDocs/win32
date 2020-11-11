---
title: How to Create Rich Edit Controls
description: To create a rich edit control, call the CreateWindowEx function, specifying the rich edit window class.
ms.assetid: E0F3E458-7907-42BD-841A-CB3D12628AA8
ms.topic: article
ms.date: 05/31/2018
---

# How to Create Rich Edit Controls

To create a rich edit control, call the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function, specifying the rich edit window class. For Microsoft Rich Edit 4.1 (Msftedit.dll), specify MSFTEDIT\_CLASS as the window class. For all previous versions, specify RICHEDIT\_CLASS. For more information, see [Versions of Rich Edit](about-rich-edit-controls.md).

Rich edit controls support most of the window styles used with edit controls as well as additional styles. You should specify the [**ES\_MULTILINE**](edit-control-styles.md) window style if you want to allow more than one line of text in the control. For more information, see [Rich Edit Control Styles](rich-edit-control-styles.md).

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Create a Rich Edit Control

The following example function creates a rich edit control and initializes it with some text.


```C++
HWND CreateRichEdit(HWND hwndOwner,        // Dialog box handle.
                    int x, int y,          // Location.
                    int width, int height, // Dimensions.
                    HINSTANCE hinst)       // Application or DLL instance.
{
    LoadLibrary(TEXT("Msftedit.dll"));
    
    HWND hwndEdit= CreateWindowEx(0, MSFTEDIT_CLASS, TEXT("Type here"),
        ES_MULTILINE | WS_VISIBLE | WS_CHILD | WS_BORDER | WS_TABSTOP, 
        x, y, width, height, 
        hwndOwner, NULL, hinst, NULL);
        
    return hwndEdit;
}
```



In Microsoft Visual Studio 2005 and later, it is possible to add a rich edit control into a dialog template by dragging the control from the toolbox. However, doing this in the dialog editor does not ensure that the required library will be loaded before the control is created. It is necessary to call the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) function to load Riched32.dll, Riched20.dll, or Msftedit.dll before the dialog is created.

## Remarks

To use visual styles with these controls, an application must include a manifest and must call the [**InitCommonControls**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrols) function at the beginning of the program. For information on visual styles, see [Visual Styles](themes-overview.md). For information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

## Related topics

<dl> <dt>

[Using Rich Edit Controls](using-rich-edit-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 
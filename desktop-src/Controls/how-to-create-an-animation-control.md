---
title: How to Create an Animation Control
description: This topic demonstrates how to create an animation control.
ms.assetid: 5852B636-F3D0-47A4-82F6-8BE570013E1B
ms.topic: article
ms.date: 05/31/2018
---

# How to Create an Animation Control

This topic demonstrates how to create an animation control. The accompanying C++ code example creates an animation control in a dialog box. It positions the animation control below a specified control, and sets the dimensions of the animation control based on the dimensions of a frame in the Audio-Video Interleaved (AVI) clip.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming
-   AVI files

## Instructions

### Step 1: Create an instance of the animation control.

Use the [**Animate\_Create**](/windows/desktop/api/Commctrl/nf-commctrl-animate_create) macro to create an instance of the animation control.


```C++
// IDC_ANIMATE - identifier of the animation control. 
// hwndDlg - handle to the dialog box.
RECT rc;
hwndAnim = Animate_Create(hwndDlg, IDC_ANIMATE, 
    WS_BORDER | WS_CHILD, g_hinst); 
```



### Step 2: Position the animation control.

Get the screen coordinates of the specified control button.


```C++
// nIDCtl - identifier of the control below which the animation control is to be positioned.
GetWindowRect(GetDlgItem(hwndDlg, nIDCtl), &rc); 
```



Convert the coordinates of the lower-left corner to client coordinates.


```C++
POINT pt;
pt.x = rc.left; 
pt.y = rc.bottom; 
ScreenToClient(hwndDlg, &pt); 
```



Position the animation control below the specified control button.


```C++
// CX_FRAME, CY_FRAME - width and height of the frames in the AVI clip.      
SetWindowPos(hwndAnim, 0, pt.x, pt.y + 20, 
    CX_FRAME, CY_FRAME, 
    SWP_NOZORDER | SWP_DRAWFRAME);
```



### Step 3: Open the AVI clip.

Call the [**Animate\_Open**](/windows/desktop/api/Commctrl/nf-commctrl-animate_open) macro to open the AVI clip and display the first frame in the animation control. Call the **ShowWindow** function to make the animation control visible.


```C++
Animate_Open(hwndAnim, "SEARCH.AVI"); 
ShowWindow(hwndAnim, SW_SHOW); 
```



## Complete example


```C++
// CreateAnimationCtrl - creates an animation control, positions it 
//                       below the specified control in a dialog box, 
//                       and opens the AVI clip for the animation control. 
// Returns the handle to the animation control. 
// hwndDlg             - handle to the dialog box. 
// nIDCtl              - identifier of the control below which the animation control 
//                       is to be positioned. 
// 
// Constants 
//     IDC_ANIMATE - identifier of the animation control. 
//     CX_FRAME, CY_FRAME - width and height of the frames 
//     in the AVI clip. 

HWND CreateAnimationCtrl(HWND hwndDlg, int nIDCtl) 
{ 
    HWND hwndAnim = NULL;    
    
    // Create the animation control.
    // IDC_ANIMATE - identifier of the animation control. 
    // hwndDlg - handle to the dialog box.
    RECT rc;
    hwndAnim = Animate_Create(hwndDlg, IDC_ANIMATE, 
        WS_BORDER | WS_CHILD, g_hinst); 

    // Get the screen coordinates of the specified control button.
    // nIDCtl - identifier of the control below which the animation control is to be positioned.
    GetWindowRect(GetDlgItem(hwndDlg, nIDCtl), &rc); 

    // Convert the coordinates of the lower-left corner to 
    // client coordinates.
    POINT pt;
    pt.x = rc.left; 
    pt.y = rc.bottom; 
    ScreenToClient(hwndDlg, &pt); 

    // Position the animation control below the Stop button.
    // CX_FRAME, CY_FRAME - width and height of the frames in the AVI clip.      
    SetWindowPos(hwndAnim, 0, pt.x, pt.y + 20, 
        CX_FRAME, CY_FRAME, 
        SWP_NOZORDER | SWP_DRAWFRAME);

    // Open the AVI clip, and show the animation control.
    Animate_Open(hwndAnim, "SEARCH.AVI"); 
    ShowWindow(hwndAnim, SW_SHOW); 

    return hwndAnim; 
} 
```



## Related topics

<dl> <dt>

[About Animation Controls](animation-control-overview.md)
</dt> <dt>

[Animation Control Reference](bumper-animation-animation-control-reference.md)
</dt> <dt>

[Using Animation Controls](using-animation-control.md)
</dt> <dt>

[Animation](animation-control-reference.md)
</dt> </dl>

 

 





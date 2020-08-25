---
title: How to Create a Tabbed Dialog Box
description: The example in this section demonstrates how to create a dialog box that uses tabs to provide multiple pages of controls.
ms.assetid: DBF7FBDF-AADC-45CE-833E-F893C1129FC0
ms.topic: article
ms.date: 05/31/2018
---

# How to Create a Tabbed Dialog Box

The example in this section demonstrates how to create a dialog box that uses tabs to provide multiple pages of controls. The main dialog box is a modal dialog box. Each page of controls is defined by a dialog box template that has the [**WS\_CHILD**](/windows/desktop/winmsg/window-styles) style. When a tab is selected, a modeless dialog box is created for the incoming page and the dialog box for the outgoing page is destroyed.

> [!Note]  
> In many cases, you can implement multiple-page dialog boxes more easily by using property sheets. For more information about property sheets, see [About Property Sheets](property-sheets.md).

 

The template for the main dialog box simply defines two button controls. When processing the [**WM\_INITDIALOG**](/windows/desktop/dlgbox/wm-initdialog) message, the dialog box procedure creates a tab control and loads the dialog box template resources for each of the child dialog boxes.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Create a Tabbed Dialog Box

The information is saved in an application-defined structure called DLGHDR. A pointer to this structure is associated with the dialog box window by using the [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) function. The structure is defined in the application's header file, as follows.


```C++
#define C_PAGES 3 

typedef struct tag_dlghdr { 
    HWND hwndTab;       // tab control 
    HWND hwndDisplay;   // current child dialog box 
    RECT rcDisplay;     // display rectangle for the tab control 
    DLGTEMPLATEEX *apRes[C_PAGES]; 
} DLGHDR; 
```



The following function processes the [**WM\_INITDIALOG**](/windows/desktop/dlgbox/wm-initdialog) message for the main dialog box. The function allocates the `DLGHDR` structure, loads the dialog box template resources for the child dialog boxes, and creates the tab control.

The size of each child dialog box is specified by the [**DLGTEMPLATEEX**](/windows/desktop/dlgbox/dlgtemplateex) structure. The function examines the size of each dialog box and uses the macro for the [**TCM\_ADJUSTRECT**](tcm-adjustrect.md) message to calculate an appropriate size for the tab control. Then it sizes the dialog box and positions the two buttons accordingly. This example sends **TCM\_ADJUSTRECT** by using the [**TabCtrl\_AdjustRect**](/windows/desktop/api/Commctrl/nf-commctrl-tabctrl_adjustrect) macro.


```C++
// Handles the WM_INITDIALOG message for a dialog box that contains 
//   a tab control used to select among three child dialog boxes.
// Returns a result code.
// hwndDlg - handle of the dialog box.
// 
HRESULT OnTabbedDialogInit(HWND hwndDlg) 
{ 
    INITCOMMONCONTROLSEX iccex;
    DWORD dwDlgBase = GetDialogBaseUnits();
    int cxMargin = LOWORD(dwDlgBase) / 4; 
    int cyMargin = HIWORD(dwDlgBase) / 8; 

    TCITEM tie; 
    RECT rcTab; 
    HWND hwndButton; 
    RECT rcButton; 
    int i; 

    // Initialize common controls.
    iccex.dwSize = sizeof(INITCOMMONCONTROLSEX);
    iccex.dwICC = ICC_TAB_CLASSES;
    InitCommonControlsEx(&iccex); 

    // Allocate memory for the DLGHDR structure. Remember to 
    // free this memory before the dialog box is destroyed.
    DLGHDR *pHdr = (DLGHDR *) LocalAlloc(LPTR, sizeof(DLGHDR)); 

    // Save a pointer to the DLGHDR structure in the window
    // data of the dialog box. 
    SetWindowLongPtr(hwndDlg, GWLP_USERDATA, (LONG_PTR) pHdr); 
 
    // Create the tab control. Note that g_hInst is a global 
    // instance handle. 
    pHdr->hwndTab = CreateWindow( 
        WC_TABCONTROL, L"", 
        WS_CHILD | WS_CLIPSIBLINGS | WS_VISIBLE, 
        0, 0, 100, 100, 
        hwndDlg, NULL, g_hInst, NULL 
        ); 
    if (pHdr->hwndTab == NULL) 
    {
        return HRESULT_FROM_WIN32(GetLastError());
    }
 
    // Add a tab for each of the three child dialog boxes. 
    tie.mask = TCIF_TEXT | TCIF_IMAGE; 
    tie.iImage = -1; 
    tie.pszText = L"First"; 
    TabCtrl_InsertItem(pHdr->hwndTab, 0, &tie); 
    tie.pszText = L"Second"; 
    TabCtrl_InsertItem(pHdr->hwndTab, 1, &tie); 
    tie.pszText = L"Third"; 
    TabCtrl_InsertItem(pHdr->hwndTab, 2, &tie); 

    // Lock the resources for the three child dialog boxes. 
    pHdr->apRes[0] = DoLockDlgRes(MAKEINTRESOURCE(IDD_FIRSTDLG)); 
    pHdr->apRes[1] = DoLockDlgRes(MAKEINTRESOURCE(IDD_SECONDDLG)); 
    pHdr->apRes[2] = DoLockDlgRes(MAKEINTRESOURCE(IDD_THIRDDLG)); 

    // Determine a bounding rectangle that is large enough to 
    // contain the largest child dialog box. 
    SetRectEmpty(&rcTab); 
    for (i = 0; i < C_PAGES; i++) 
    { 
        if (pHdr->apRes[i]->cx > rcTab.right) 
            rcTab.right = pHdr->apRes[i]->cx; 
        if (pHdr->apRes[i]->cy > rcTab.bottom) 
            rcTab.bottom = pHdr->apRes[i]->cy; 
    }

    // Map the rectangle from dialog box units to pixels.
    MapDialogRect(hwndDlg, &rcTab);
    
    // Calculate how large to make the tab control, so 
    // the display area can accommodate all the child dialog boxes. 
    TabCtrl_AdjustRect(pHdr->hwndTab, TRUE, &rcTab); 
    OffsetRect(&rcTab, cxMargin - rcTab.left, cyMargin - rcTab.top); 
 
    // Calculate the display rectangle. 
    CopyRect(&pHdr->rcDisplay, &rcTab); 
    TabCtrl_AdjustRect(pHdr->hwndTab, FALSE, &pHdr->rcDisplay); 
 
    // Set the size and position of the tab control, buttons, 
    // and dialog box. 
    SetWindowPos(pHdr->hwndTab, NULL, rcTab.left, rcTab.top, 
            rcTab.right - rcTab.left, rcTab.bottom - rcTab.top, 
            SWP_NOZORDER); 
 
    // Move the first button below the tab control. 
    hwndButton = GetDlgItem(hwndDlg, IDB_CLOSE); 
    SetWindowPos(hwndButton, NULL, 
            rcTab.left, rcTab.bottom + cyMargin, 0, 0, 
            SWP_NOSIZE | SWP_NOZORDER); 
 
    // Determine the size of the button. 
    GetWindowRect(hwndButton, &rcButton); 
    rcButton.right -= rcButton.left; 
    rcButton.bottom -= rcButton.top; 
 
    // Move the second button to the right of the first. 
    hwndButton = GetDlgItem(hwndDlg, IDB_TEST); 
    SetWindowPos(hwndButton, NULL, 
        rcTab.left + rcButton.right + cxMargin, 
        rcTab.bottom + cyMargin, 0, 0, 
        SWP_NOSIZE | SWP_NOZORDER); 
 
    // Size the dialog box. 
    SetWindowPos(hwndDlg, NULL, 0, 0, 
        rcTab.right + cyMargin + (2 * GetSystemMetrics(SM_CXDLGFRAME)), 
        rcTab.bottom + rcButton.bottom + (2 * cyMargin)
        + (2 * GetSystemMetrics(SM_CYDLGFRAME)) 
        + GetSystemMetrics(SM_CYCAPTION), 
        SWP_NOMOVE | SWP_NOZORDER); 
 
    // Simulate selection of the first item. 
    OnSelChanged(hwndDlg); 

    return S_OK;
} 

// Loads and locks a dialog box template resource. 
// Returns the address of the locked dialog box template resource. 
// lpszResName - name of the resource. 
//
DLGTEMPLATEEX* DoLockDlgRes(LPCTSTR lpszResName) 
{ 
    HRSRC hrsrc = FindResource(NULL, lpszResName, RT_DIALOG); 

    // Note that g_hInst is the global instance handle
    HGLOBAL hglb = LoadResource(g_hInst, hrsrc);  
    return (DLGTEMPLATEEX *) LockResource(hglb); 
} 
```



The following function processes the [TCN\_SELCHANGE](tcn-selchange.md) notification code for the main dialog box. The function destroys the dialog box for the outgoing page, if any. Then it uses the [**CreateDialogIndirect**](/windows/desktop/api/winuser/nf-winuser-createdialogindirecta) function to create a modeless dialog box for the incoming page.


```C++
// Processes the TCN_SELCHANGE notification. 
// hwndDlg - handle to the parent dialog box. 
//
VOID OnSelChanged(HWND hwndDlg) 
{ 
    // Get the dialog header data.
    DLGHDR *pHdr = (DLGHDR *) GetWindowLongPtr( 
        hwndDlg, GWLP_USERDATA); 

    // Get the index of the selected tab.
    int iSel = TabCtrl_GetCurSel(pHdr->hwndTab); 
 
    // Destroy the current child dialog box, if any. 
    if (pHdr->hwndDisplay != NULL) 
        DestroyWindow(pHdr->hwndDisplay); 
 
    // Create the new child dialog box. Note that g_hInst is the
    // global instance handle.
    pHdr->hwndDisplay = CreateDialogIndirect(g_hInst, 
        (DLGTEMPLATE *)pHdr->apRes[iSel], hwndDlg, ChildDialogProc); 

    return;
} 
```



The following function processes the [**WM\_INITDIALOG**](/windows/desktop/dlgbox/wm-initdialog) message for each of the child dialog boxes. You cannot specify the position of a dialog box that is created using the [**CreateDialogIndirect**](/windows/desktop/api/winuser/nf-winuser-createdialogindirecta) function. This function uses the [**SetWindowPos**](/windows/desktop/api/winuser/nf-winuser-setwindowpos) function to position the child dialog within the tab control's display area.


```C++
// Positions the child dialog box to occupy the display area of the 
//   tab control. 
// hwndDlg - handle of the dialog box.
//
VOID WINAPI OnChildDialogInit(HWND hwndDlg) 
{ 
    HWND hwndParent = GetParent(hwndDlg);
    DLGHDR *pHdr = (DLGHDR *) GetWindowLongPtr( 
        hwndParent, GWLP_USERDATA); 
    SetWindowPos(hwndDlg, NULL, pHdr->rcDisplay.left,
        pHdr->rcDisplay.top,//-2,
        (pHdr->rcDisplay.right - pHdr->rcDisplay.left),
        (pHdr->rcDisplay.bottom - pHdr->rcDisplay.top),
        SWP_SHOWWINDOW);
        
    return;
}
```



## Related topics

<dl> <dt>

[Using Tab Controls](using-tab-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 
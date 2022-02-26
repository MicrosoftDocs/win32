---
title: Using the Clipboard
description: This section has code samples for the following tasks
ms.assetid: 377fb2cc-5b46-481a-8222-9291e504ae2c
keywords:
- clipboard,cutting data
- clipboard,copying data
- clipboard,pasting data
- clipboard,selecting data
- clipboard,Edit menu commands
- clipboard,viewers
- clipboard,viewer windows
ms.topic: article
ms.date: 02/11/2022
---

# Using the Clipboard

This section has code samples for the following tasks:

-   [Implementing the Cut, Copy, and Paste Commands](#implementing-the-cut-copy-and-paste-commands)
    -   [Selecting Data](#selecting-data)
    -   [Creating an Edit Menu](#creating-an-edit-menu)
    -   [Processing the `WM_INITMENUPOPUP` Message](#processing-the-wm_initmenupopup-message)
    -   [Processing the `WM_COMMAND` Message](#processing-the-wm_command-message)
    -   [Copying Information to the Clipboard](#copying-information-to-the-clipboard)
    -   [Pasting Information from the Clipboard](#pasting-information-from-the-clipboard)
    -   [Registering a Clipboard Format](#registering-a-clipboard-format)
    -   [Processing the `WM_RENDERFORMAT` and `WM_RENDERALLFORMATS` Messages](#processing-the-wm_renderformat-and-wm_renderallformats-messages)
    -   [Processing the `WM_DESTROYCLIPBOARD` Message](#processing-the-wm_destroyclipboard-message)
    -   [Using the Owner-Display Clipboard Format](#using-the-owner-display-clipboard-format)
-   [Monitoring Clipboard Contents](#monitoring-clipboard-contents)
-   [Querying the Clipboard Sequence Number](#querying-the-clipboard-sequence-number)
-   [Creating a Clipboard Format Listener](#creating-a-clipboard-format-listener)
-   [Creating a Clipboard Viewer Window](#creating-a-clipboard-viewer-window)
-   [Adding a Window to the Clipboard Viewer Chain](#adding-a-window-to-the-clipboard-viewer-chain)
    -   [Processing the `WM_CHANGECBCHAIN` Message](#processing-the-wm_changecbchain-message)
    -   [Removing a Window from the Clipboard Viewer Chain](#removing-a-window-from-the-clipboard-viewer-chain)
    -   [Processing the `WM_DRAWCLIPBOARD` Message](#processing-the-wm_drawclipboard-message)
    -   [Example of a Clipboard Viewer](#example-of-a-clipboard-viewer)

## Implementing the Cut, Copy, and Paste Commands

This section describes how standard **Cut**, **Copy**, and **Paste** commands are implemented in an application. The example in this section uses these methods to place data on the clipboard using a registered clipboard format, the `CF_OWNERDISPLAY` format, and the `CF_TEXT` format. The registered format is used to represent rectangular or elliptical text windows, called labels.

### Selecting Data

Before information can be copied to the clipboard, the user must select specific information to be copied or cut. An application should provide a means for the user to select information within a document and some kind of visual feedback to indicate selected data.

### Creating an Edit Menu

An application should load an accelerator table containing the standard keyboard accelerators for the **Edit** menu commands. The [`TranslateAccelerator`](/windows/desktop/api/winuser/nf-winuser-translateacceleratora) function must be added to the application's message loop for the accelerators to take effect. For more information about keyboard accelerators, see [Keyboard Accelerators](/windows/desktop/menurc/keyboard-accelerators).

### Processing the `WM_INITMENUPOPUP` Message

Not all clipboard commands are available to the user at any given time. An application should process the [`WM_INITMENUPOPUP`](/windows/desktop/menurc/wm-initmenupopup) message to enable the menu items for available commands and disable unavailable commands.

Following is the [`WM_INITMENUPOPUP`](/windows/desktop/menurc/wm-initmenupopup) case for an application named Label.

```cpp
case WM_INITMENUPOPUP:
    InitMenu((HMENU) wParam);
    break;
```

The `InitMenu` function is defined as follows.

```cpp
void WINAPI InitMenu(HMENU hmenu) 
{ 
    int  cMenuItems = GetMenuItemCount(hmenu); 
    int  nPos; 
    UINT id; 
    UINT fuFlags; 
    PLABELBOX pbox = (hwndSelected == NULL) ? NULL : 
        (PLABELBOX) GetWindowLong(hwndSelected, 0); 
 
    for (nPos = 0; nPos < cMenuItems; nPos++) 
    { 
        id = GetMenuItemID(hmenu, nPos); 
 
        switch (id) 
        { 
            case IDM_CUT: 
            case IDM_COPY: 
            case IDM_DELETE: 
                if (pbox == NULL || !pbox->fSelected) 
                    fuFlags = MF_BYCOMMAND | MF_GRAYED; 
                else if (pbox->fEdit) 
                    fuFlags = (id != IDM_DELETE && pbox->ichSel 
                            == pbox->ichCaret) ? 
                        MF_BYCOMMAND | MF_GRAYED : 
                        MF_BYCOMMAND | MF_ENABLED; 
                else 
                    fuFlags = MF_BYCOMMAND | MF_ENABLED; 
 
                EnableMenuItem(hmenu, id, fuFlags); 
                break; 
 
            case IDM_PASTE: 
                if (pbox != NULL && pbox->fEdit) 
                    EnableMenuItem(hmenu, id, 
                        IsClipboardFormatAvailable(CF_TEXT) ? 
                            MF_BYCOMMAND | MF_ENABLED : 
                            MF_BYCOMMAND | MF_GRAYED 
                    ); 
                else 
                    EnableMenuItem(hmenu, id, 
                        IsClipboardFormatAvailable( 
                                uLabelFormat) ? 
                            MF_BYCOMMAND | MF_ENABLED : 
                            MF_BYCOMMAND | MF_GRAYED 
                    ); 
 
        } 
    } 
}
```

### Processing the `WM_COMMAND` Message

To process menu commands, add the [`WM_COMMAND`](/windows/desktop/menurc/wm-command) case to your application's main window procedure. Following is the `WM_COMMAND` case for the Label application's window procedure.

```cpp
case WM_COMMAND: 
    switch (LOWORD(wParam)) 
    { 
        case IDM_CUT: 
            if (EditCopy()) 
                EditDelete(); 
            break; 
 
        case IDM_COPY: 
            EditCopy(); 
            break; 
 
        case IDM_PASTE: 
            EditPaste(); 
            break; 
 
        case IDM_DELETE: 
            EditDelete(); 
            break; 
 
        case IDM_EXIT: 
            DestroyWindow(hwnd); 
    } 
    break; 
```

To carry out the **Copy** and **Cut** commands, the window procedure calls the application-defined `EditCopy` function. For more information, see [Copying Information to the Clipboard](#copying-information-to-the-clipboard). To carry out the **Paste** command, the window procedure calls the application-defined `EditPaste` function. For more information about the `EditPaste` function, see [Pasting Information from the Clipboard](#pasting-information-from-the-clipboard).

### Copying Information to the Clipboard

In the Label application, the application-defined EditCopy function copies the current selection to the clipboard. This function does the following:

1.  Opens the clipboard by calling the [`OpenClipboard`](/windows/desktop/api/Winuser/nf-winuser-openclipboard) function.
2.  Empties the clipboard by calling the [`EmptyClipboard`](/windows/desktop/api/Winuser/nf-winuser-emptyclipboard) function.
3.  Calls the [`SetClipboardData`](/windows/desktop/api/Winuser/nf-winuser-setclipboarddata) function once for each clipboard format the application provides.
4.  Closes the clipboard by calling the [`CloseClipboard`](/windows/desktop/api/Winuser/nf-winuser-closeclipboard) function.

Depending on the current selection, the EditCopy function either copies a range of text or copies an application-defined structure representing an entire label. The structure, called `LABELBOX`, is defined as follows.

```cpp
#define BOX_ELLIPSE  0 
#define BOX_RECT     1 
 
#define CCH_MAXLABEL 80 
#define CX_MARGIN    12 
 
typedef struct tagLABELBOX {  // box 
    RECT rcText;    // coordinates of rectangle containing text 
    BOOL fSelected; // TRUE if the label is selected 
    BOOL fEdit;     // TRUE if text is selected 
    int nType;      // rectangular or elliptical 
    int ichCaret;   // caret position 
    int ichSel;     // with ichCaret, delimits selection 
    int nXCaret;    // window position corresponding to ichCaret 
    int nXSel;      // window position corresponding to ichSel 
    int cchLabel;   // length of text in atchLabel 
    TCHAR atchLabel[CCH_MAXLABEL]; 
} LABELBOX, *PLABELBOX;
```

Following is the `EditCopy` function.

```cpp
BOOL WINAPI EditCopy(VOID) 
{ 
    PLABELBOX pbox; 
    LPTSTR  lptstrCopy; 
    HGLOBAL hglbCopy; 
    int ich1, ich2, cch; 
 
    if (hwndSelected == NULL) 
        return FALSE; 
 
    // Open the clipboard, and empty it. 
 
    if (!OpenClipboard(hwndMain)) 
        return FALSE; 
    EmptyClipboard(); 
 
    // Get a pointer to the structure for the selected label. 
 
    pbox = (PLABELBOX) GetWindowLong(hwndSelected, 0); 
 
    // If text is selected, copy it using the CF_TEXT format. 
 
    if (pbox->fEdit) 
    { 
        if (pbox->ichSel == pbox->ichCaret)     // zero length
        {   
            CloseClipboard();                   // selection 
            return FALSE; 
        } 
 
        if (pbox->ichSel < pbox->ichCaret) 
        { 
            ich1 = pbox->ichSel; 
            ich2 = pbox->ichCaret; 
        } 
        else 
        { 
            ich1 = pbox->ichCaret; 
            ich2 = pbox->ichSel; 
        } 
        cch = ich2 - ich1; 
 
        // Allocate a global memory object for the text. 
 
        hglbCopy = GlobalAlloc(GMEM_MOVEABLE, 
            (cch + 1) * sizeof(TCHAR)); 
        if (hglbCopy == NULL) 
        { 
            CloseClipboard(); 
            return FALSE; 
        } 
 
        // Lock the handle and copy the text to the buffer. 
 
        lptstrCopy = GlobalLock(hglbCopy); 
        memcpy(lptstrCopy, &pbox->atchLabel[ich1], 
            cch * sizeof(TCHAR)); 
        lptstrCopy[cch] = (TCHAR) 0;    // null character 
        GlobalUnlock(hglbCopy); 
 
        // Place the handle on the clipboard. 
 
        SetClipboardData(CF_TEXT, hglbCopy); 
    } 
 
    // If no text is selected, the label as a whole is copied. 
 
    else 
    { 
        // Save a copy of the selected label as a local memory 
        // object. This copy is used to render data on request. 
        // It is freed in response to the WM_DESTROYCLIPBOARD 
        // message. 
 
        pboxLocalClip = (PLABELBOX) LocalAlloc( 
            LMEM_FIXED, 
            sizeof(LABELBOX) 
        ); 
        if (pboxLocalClip == NULL) 
        { 
            CloseClipboard(); 
            return FALSE; 
        } 
        memcpy(pboxLocalClip, pbox, sizeof(LABELBOX)); 
        pboxLocalClip->fSelected = FALSE; 
        pboxLocalClip->fEdit = FALSE; 
 
        // Place a registered clipboard format, the owner-display 
        // format, and the CF_TEXT format on the clipboard using 
        // delayed rendering. 
 
        SetClipboardData(uLabelFormat, NULL); 
        SetClipboardData(CF_OWNERDISPLAY, NULL); 
        SetClipboardData(CF_TEXT, NULL); 
    } 
 
    // Close the clipboard. 
 
    CloseClipboard(); 
 
    return TRUE; 
}
```

### Pasting Information from the Clipboard

In the Label application, the application-defined `EditPaste` function pastes the content of the clipboard. This function does the following:

1. Opens the clipboard by calling the [`OpenClipboard`](/windows/desktop/api/Winuser/nf-winuser-openclipboard) function.
2. Determines which of the available clipboard formats to retrieve.
3. Retrieves the handle to the data in the selected format by calling the [`GetClipboardData`](/windows/desktop/api/Winuser/nf-winuser-getclipboarddata) function.
4. Inserts a copy of the data into the document. The handle returned by [`GetClipboardData`](/windows/desktop/api/Winuser/nf-winuser-getclipboarddata) is still owned by the clipboard, so an application must not free it or leave it locked.
5. Closes the clipboard by calling the [`CloseClipboard`](/windows/desktop/api/Winuser/nf-winuser-closeclipboard) function.

If a label is selected and contains an insertion point, the EditPaste function inserts the text from the clipboard at the insertion point. If there is no selection or if a label is selected, the function creates a new label, using the application-defined `LABELBOX` structure on the clipboard. The `LABELBOX` structure is placed on the clipboard by using a registered clipboard format.

The structure, called `LABELBOX`, is defined as follows.

```cpp
#define BOX_ELLIPSE  0 
#define BOX_RECT     1 
 
#define CCH_MAXLABEL 80 
#define CX_MARGIN    12 
 
typedef struct tagLABELBOX {  // box 
    RECT rcText;    // coordinates of rectangle containing text 
    BOOL fSelected; // TRUE if the label is selected 
    BOOL fEdit;     // TRUE if text is selected 
    int nType;      // rectangular or elliptical 
    int ichCaret;   // caret position 
    int ichSel;     // with ichCaret, delimits selection 
    int nXCaret;    // window position corresponding to ichCaret 
    int nXSel;      // window position corresponding to ichSel 
    int cchLabel;   // length of text in atchLabel 
    TCHAR atchLabel[CCH_MAXLABEL]; 
} LABELBOX, *PLABELBOX;
```

Following is the `EditPaste` function.

```cpp
VOID WINAPI EditPaste(VOID) 
{ 
    PLABELBOX pbox; 
    HGLOBAL   hglb; 
    LPTSTR    lptstr; 
    PLABELBOX pboxCopy; 
    int cx, cy; 
    HWND hwnd; 
 
    pbox = hwndSelected == NULL ? NULL : 
        (PLABELBOX) GetWindowLong(hwndSelected, 0); 
 
    // If the application is in edit mode, 
    // get the clipboard text. 
 
    if (pbox != NULL && pbox->fEdit) 
    { 
        if (!IsClipboardFormatAvailable(CF_TEXT)) 
            return; 
        if (!OpenClipboard(hwndMain)) 
            return; 
 
        hglb = GetClipboardData(CF_TEXT); 
        if (hglb != NULL) 
        { 
            lptstr = GlobalLock(hglb); 
            if (lptstr != NULL) 
            { 
                // Call the application-defined ReplaceSelection 
                // function to insert the text and repaint the 
                // window. 
 
                ReplaceSelection(hwndSelected, pbox, lptstr); 
                GlobalUnlock(hglb); 
            } 
        } 
        CloseClipboard(); 
 
        return; 
    } 
 
    // If the application is not in edit mode, 
    // create a label window. 
 
    if (!IsClipboardFormatAvailable(uLabelFormat)) 
        return; 
    if (!OpenClipboard(hwndMain)) 
        return; 
 
    hglb = GetClipboardData(uLabelFormat); 
    if (hglb != NULL) 
    { 
        pboxCopy = GlobalLock(hglb); 
        if (pboxCopy != NULL) 
        { 
            cx = pboxCopy->rcText.right + CX_MARGIN; 
            cy = pboxCopy->rcText.top * 2 + cyText; 
 
            hwnd = CreateWindowEx( 
                WS_EX_NOPARENTNOTIFY | WS_EX_TRANSPARENT, 
                atchClassChild, NULL, WS_CHILD, 0, 0, cx, cy, 
                hwndMain, NULL, hinst, NULL 
            ); 
            if (hwnd != NULL) 
            { 
                pbox = (PLABELBOX) GetWindowLong(hwnd, 0); 
                memcpy(pbox, pboxCopy, sizeof(LABELBOX)); 
                ShowWindow(hwnd, SW_SHOWNORMAL); 
                SetFocus(hwnd); 
            } 
            GlobalUnlock(hglb); 
        } 
    } 
    CloseClipboard(); 
}
```

### Registering a Clipboard Format

To register a clipboard format, add a call to the [`RegisterClipboardFormat`](/windows/desktop/api/Winuser/nf-winuser-registerclipboardformata) function to your application's instance initialization function, as follows.

```cpp
// Register a clipboard format. 
 
// We assume that atchTemp can contain the format name and
// a null-terminator, otherwise it is truncated.
//
LoadString(hinstCurrent, IDS_FORMATNAME, atchTemp, 
    sizeof(atchTemp)/sizeof(TCHAR)); 
uLabelFormat = RegisterClipboardFormat(atchTemp); 
if (uLabelFormat == 0) 
    return FALSE;
```

### Processing the `WM_RENDERFORMAT` and `WM_RENDERALLFORMATS` Messages

If a window passes a `NULL` handle to the [`SetClipboardData`](/windows/desktop/api/Winuser/nf-winuser-setclipboarddata) function, it must process the [`WM_RENDERFORMAT`](wm-renderformat.md) and [`WM_RENDERALLFORMATS`](wm-renderallformats.md) messages to render data upon request.

If a window delays rendering a specific format and then another application requests data in that format, then a [`WM_RENDERFORMAT`](wm-renderformat.md) message is sent to the window. In addition, if a window delays rendering one or more formats, and if some of those formats remain unrendered when the window is about to be destroyed, then a [`WM_RENDERALLFORMATS`](wm-renderallformats.md) message is sent to the window before its destruction.

To render a clipboard format, the window procedure should place a non-`NULL` data handle on the clipboard using the [`SetClipboardData`](/windows/desktop/api/Winuser/nf-winuser-setclipboarddata) function. If the window procedure is rendering a format in response to the [`WM_RENDERFORMAT`](wm-renderformat.md) message, it must not open the clipboard before calling `SetClipboardData`. But if it is rendering one or more formats in response to the [`WM_RENDERALLFORMATS`](wm-renderallformats.md) message, it must open the clipboard and check that the window still owns the clipboard before calling `SetClipboardData`, and it must close the clipboard before returning.

The Label application processes the [`WM_RENDERFORMAT`](wm-renderformat.md) and [`WM_RENDERALLFORMATS`](wm-renderallformats.md) messages as follows.

```cpp
case WM_RENDERFORMAT: 
    RenderFormat((UINT) wParam); 
    break; 
 
case WM_RENDERALLFORMATS:
    if (OpenClipboard(hwnd))
    {
        if (GetClipboardOwner() == hwnd)
        {
            RenderFormat(uLabelFormat);
            RenderFormat(CF_TEXT);
        }
        CloseClipboard();
    }
    break;
```

In both cases, the window procedure calls the application-defined `RenderFormat` function, defined as follows.

The structure, called `LABELBOX`, is defined as follows.


```cpp
#define BOX_ELLIPSE  0 
#define BOX_RECT     1 
 
#define CCH_MAXLABEL 80 
#define CX_MARGIN    12 
 
typedef struct tagLABELBOX {  // box 
    RECT rcText;    // coordinates of rectangle containing text 
    BOOL fSelected; // TRUE if the label is selected 
    BOOL fEdit;     // TRUE if text is selected 
    int nType;      // rectangular or elliptical 
    int ichCaret;   // caret position 
    int ichSel;     // with ichCaret, delimits selection 
    int nXCaret;    // window position corresponding to ichCaret 
    int nXSel;      // window position corresponding to ichSel 
    int cchLabel;   // length of text in atchLabel 
    TCHAR atchLabel[CCH_MAXLABEL]; 
} LABELBOX, *PLABELBOX;
```

```cpp
void WINAPI RenderFormat(UINT uFormat) 
{ 
    HGLOBAL hglb; 
    PLABELBOX pbox; 
    LPTSTR  lptstr; 
    int cch; 
 
    if (pboxLocalClip == NULL) 
        return; 
 
    if (uFormat == CF_TEXT) 
    { 
        // Allocate a buffer for the text. 
 
        cch = pboxLocalClip->cchLabel; 
        hglb = GlobalAlloc(GMEM_MOVEABLE, 
            (cch + 1) * sizeof(TCHAR)); 
        if (hglb == NULL) 
            return; 
 
        // Copy the text from pboxLocalClip. 
 
        lptstr = GlobalLock(hglb); 
        memcpy(lptstr, pboxLocalClip->atchLabel, 
            cch * sizeof(TCHAR)); 
        lptstr[cch] = (TCHAR) 0; 
        GlobalUnlock(hglb); 
 
        // Place the handle on the clipboard. 
 
        SetClipboardData(CF_TEXT, hglb); 
    } 
    else if (uFormat == uLabelFormat) 
    { 
        hglb = GlobalAlloc(GMEM_MOVEABLE, sizeof(LABELBOX)); 
        if (hglb == NULL) 
            return; 
        pbox = GlobalLock(hglb); 
        memcpy(pbox, pboxLocalClip, sizeof(LABELBOX)); 
        GlobalUnlock(hglb); 
 
        SetClipboardData(uLabelFormat, hglb); 
    } 
}
```

### Processing the `WM_DESTROYCLIPBOARD` Message

A window can process the [`WM_DESTROYCLIPBOARD`](wm-destroyclipboard.md) message in order to free any resources that it set aside to support delayed rendering. For example the Label application, when copying a label to the clipboard, allocates a local memory object. It then frees this object in response to the `WM_DESTROYCLIPBOARD` message, as follows.

```cpp
case WM_DESTROYCLIPBOARD: 
    if (pboxLocalClip != NULL) 
    { 
        LocalFree(pboxLocalClip); 
        pboxLocalClip = NULL; 
    } 
    break;
```

### Using the Owner-Display Clipboard Format

If a window places information on the clipboard by using the `CF_OWNERDISPLAY` clipboard format, it must do the following:

- Process the [`WM_PAINTCLIPBOARD`](wm-paintclipboard.md) message. This message is sent to the clipboard owner when a portion of the clipboard viewer window must be repainted.
- Process the [`WM_SIZECLIPBOARD`](wm-sizeclipboard.md) message. This message is sent to the clipboard owner when the clipboard viewer window has been resized or its content has changed. Typically, a window responds to this message by setting the scroll positions and ranges for the clipboard viewer window. In response to this message, the Label application also updates a [`SIZE`](/previous-versions//dd145106(v=vs.85)) structure for the clipboard viewer window.
- Process the [`WM_HSCROLLCLIPBOARD`](wm-hscrollclipboard.md) and [`WM_VSCROLLCLIPBOARD`](wm-vscrollclipboard.md) messages. These messages are sent to the clipboard owner when a scroll bar event occurs in the clipboard viewer window.
- Process the [`WM_ASKCBFORMATNAME`](wm-askcbformatname.md) message. The clipboard viewer window sends this message to an application to retrieve the name of the owner-display format.

The window procedure for the Label application processes these messages, as follows.

```cpp
LRESULT CALLBACK MainWindowProc(hwnd, msg, wParam, lParam) 
HWND hwnd; 
UINT msg; 
WPARAM wParam; 
LPARAM lParam; 
{ 
    static RECT rcViewer; 
 
    RECT rc; 
    LPRECT lprc; 
    LPPAINTSTRUCT lpps; 
 
    switch (msg) 
    { 
        //
        // Handle other messages.
        //
        case WM_PAINTCLIPBOARD: 
            // Determine the dimensions of the label. 
 
            SetRect(&rc, 0, 0, 
                pboxLocalClip->rcText.right + CX_MARGIN, 
                pboxLocalClip->rcText.top * 2 + cyText 
            ); 
 
            // Center the image in the clipboard viewer window. 
 
            if (rc.right < rcViewer.right) 
            { 
                rc.left = (rcViewer.right - rc.right) / 2; 
                rc.right += rc.left; 
            } 
            if (rc.bottom < rcViewer.bottom) 
            { 
                rc.top = (rcViewer.bottom - rc.bottom) / 2; 
                rc.bottom += rc.top; 
            } 
 
            // Paint the image, using the specified PAINTSTRUCT 
            // structure, by calling the application-defined 
            // PaintLabel function. 
 
            lpps = (LPPAINTSTRUCT) GlobalLock((HGLOBAL) lParam); 
            PaintLabel(lpps, pboxLocalClip, &rc); 
            GlobalUnlock((HGLOBAL) lParam); 
            break; 
 
        case WM_SIZECLIPBOARD: 
            // Save the dimensions of the window in a static 
            // RECT structure. 
 
            lprc = (LPRECT) GlobalLock((HGLOBAL) lParam); 
            memcpy(&rcViewer, lprc, sizeof(RECT)); 
            GlobalUnlock((HGLOBAL) lParam); 
 
            // Set the scroll ranges to zero (thus eliminating 
            // the need to process the WM_HSCROLLCLIPBOARD and 
            // WM_VSCROLLCLIPBOARD messages). 
 
            SetScrollRange((HWND) wParam, SB_HORZ, 0, 0, TRUE); 
            SetScrollRange((HWND) wParam, SB_VERT, 0, 0, TRUE); 
 
            break; 
 
        case WM_ASKCBFORMATNAME: 
            LoadString(hinst, IDS_OWNERDISPLAY, 
                (LPSTR) lParam, wParam); 
            break; 
 
        default: 
            return DefWindowProc(hwnd, msg, wParam, lParam); 
    } 
    return 0; 
}
```

## Monitoring Clipboard Contents

There are three ways of monitoring changes to the clipboard. The oldest method is to create a clipboard viewer window. Windows 2000 added the ability to query the clipboard sequence number, and Windows Vista added support for clipboard format listeners. Clipboard viewer windows are supported for backward compatibility with earlier versions of Windows. New programs should use clipboard format listeners or the clipboard sequence number.

## Querying the Clipboard Sequence Number

Each time the contents of the clipboard change, a 32-bit value known as the clipboard sequence number is incremented. A program can retrieve the current clipboard sequence number by calling the [`GetClipboardSequenceNumber`](/windows/desktop/api/Winuser/nf-winuser-getclipboardsequencenumber) function. By comparing the value returned against a value returned by a previous call to `GetClipboardSequenceNumber`, a program can determine whether the clipboard contents have changed. This method is more suitable to programs which cache results based on the current clipboard contents and need to know whether the calculations are still valid before using the results from that cache. Note that this is a not a notification method and should not be used in a polling loop. To be notified when clipboard contents change, use a clipboard format listener or a clipboard viewer.

## Creating a Clipboard Format Listener

A clipboard format listener is a window which has registered to be notified when the contents of the clipboard has changed. This method is recommended over creating a clipboard viewer window because it is simpler to implement and avoids problems if programs fail to maintain the clipboard viewer chain properly or if a window in the clipboard viewer chain stops responding to messages.

A window registers as a clipboard format listener by calling the [`AddClipboardFormatListener`](/windows/desktop/api/Winuser/nf-winuser-addclipboardformatlistener) function. When the contents of the clipboard change, the window is posted a [`WM_CLIPBOARDUPDATE`](wm-clipboardupdate.md) message. The registration remains valid until the window unregister itself by calling the [`RemoveClipboardFormatListener`](/windows/desktop/api/Winuser/nf-winuser-removeclipboardformatlistener) function.

## Creating a Clipboard Viewer Window

A clipboard viewer window displays the current content of the clipboard, and receives messages when the clipboard content changes. To create a clipboard viewer window, your application must do the following:

-   Add the window to the clipboard viewer chain.
-   Process the [`WM_CHANGECBCHAIN`](wm-changecbchain.md) message.
-   Process the [`WM_DRAWCLIPBOARD`](wm-drawclipboard.md) message.
-   Remove the window from the clipboard viewer chain before it is destroyed.

## Adding a Window to the Clipboard Viewer Chain

A window adds itself to the clipboard viewer chain by calling the [`SetClipboardViewer`](/windows/desktop/api/Winuser/nf-winuser-setclipboardviewer) function. The return value is the handle to the next window in the chain. A window must keep track of this value — for example, by saving it in a static variable named `hwndNextViewer`.

The following example adds a window to the clipboard viewer chain in response to the [`WM_CREATE`](/windows/desktop/winmsg/wm-create) message.

```cpp
case WM_CREATE: 
 
    // Add the window to the clipboard viewer chain. 
 
    hwndNextViewer = SetClipboardViewer(hwnd); 
    break;
```

Code snippets are shown for the following tasks:

-   [Processing the `WM_CHANGECBCHAIN` Message](/windows)
-   [Removing a Window from the Clipboard Viewer Chain](#removing-a-window-from-the-clipboard-viewer-chain)
-   [Processing the `WM_DRAWCLIPBOARD` Message](/windows)
-   [Example of a Clipboard Viewer](#example-of-a-clipboard-viewer)

### Processing the `WM_CHANGECBCHAIN` Message

A clipboard viewer window receives the [`WM_CHANGECBCHAIN`](wm-changecbchain.md) message when another window is removing itself from the clipboard viewer chain. If the window being removed is the next window in the chain, the window receiving the message must unlink the next window from the chain. Otherwise, this message should be passed to the next window in the chain.

The following example shows the processing of the [`WM_CHANGECBCHAIN`](wm-changecbchain.md) message.

```cpp
case WM_CHANGECBCHAIN: 
 
    // If the next window is closing, repair the chain. 
 
    if ((HWND) wParam == hwndNextViewer) 
        hwndNextViewer = (HWND) lParam; 
 
    // Otherwise, pass the message to the next link. 
 
    else if (hwndNextViewer != NULL) 
        SendMessage(hwndNextViewer, uMsg, wParam, lParam); 
 
    break;
```

### Removing a Window from the Clipboard Viewer Chain

To remove itself from the clipboard viewer chain, a window calls the [`ChangeClipboardChain`](/windows/desktop/api/Winuser/nf-winuser-changeclipboardchain) function. The following example removes a window from the clipboard viewer chain in response to the [`WM_DESTROY`](/windows/desktop/winmsg/wm-destroy) message.

```cpp
case WM_DESTROY: 
    ChangeClipboardChain(hwnd, hwndNextViewer); 
    PostQuitMessage(0); 
    break;
```

### Processing the `WM_DRAWCLIPBOARD` Message

The [`WM_DRAWCLIPBOARD`](wm-drawclipboard.md) message notifies a clipboard viewer window that the content of the clipboard has changed. A window should do the following when processing the `WM_DRAWCLIPBOARD` message:

1.  Determine which of the available clipboard formats to display.
2.  Retrieve the clipboard data and display it in the window. Or if the clipboard format is `CF_OWNERDISPLAY`, send a [`WM_PAINTCLIPBOARD`](wm-paintclipboard.md) message to the clipboard owner.
3.  Send the message to the next window in the clipboard viewer chain.

For an example of processing the [`WM_DRAWCLIPBOARD`](wm-drawclipboard.md) message, see the example listing in [Example of a Clipboard Viewer](#example-of-a-clipboard-viewer).

### Example of a Clipboard Viewer

The following example shows a simple clipboard viewer application.

```cpp
HINSTANCE hinst; 
UINT uFormat = (UINT)(-1); 
BOOL fAuto = TRUE; 
 
LRESULT APIENTRY MainWndProc(hwnd, uMsg, wParam, lParam) 
HWND hwnd; 
UINT uMsg; 
WPARAM wParam; 
LPARAM lParam; 
{ 
    static HWND hwndNextViewer; 
 
    HDC hdc; 
    HDC hdcMem; 
    PAINTSTRUCT ps; 
    LPPAINTSTRUCT lpps; 
    RECT rc; 
    LPRECT lprc; 
    HGLOBAL hglb; 
    LPSTR lpstr; 
    HBITMAP hbm; 
    HENHMETAFILE hemf; 
    HWND hwndOwner; 
 
    switch (uMsg) 
    { 
        case WM_PAINT: 
            hdc = BeginPaint(hwnd, &ps); 
 
            // Branch depending on the clipboard format. 
 
            switch (uFormat) 
            { 
                case CF_OWNERDISPLAY: 
                    hwndOwner = GetClipboardOwner(); 
                    hglb = GlobalAlloc(GMEM_MOVEABLE, 
                        sizeof(PAINTSTRUCT)); 
                    lpps = GlobalLock(hglb);
                    memcpy(lpps, &ps, sizeof(PAINTSTRUCT)); 
                    GlobalUnlock(hglb); 
 
                    SendMessage(hwndOwner, WM_PAINTCLIPBOARD, 
                        (WPARAM) hwnd, (LPARAM) hglb); 
 
                    GlobalFree(hglb); 
                    break; 
 
                case CF_BITMAP: 
                    hdcMem = CreateCompatibleDC(hdc); 
                    if (hdcMem != NULL) 
                    { 
                        if (OpenClipboard(hwnd)) 
                        { 
                            hbm = (HBITMAP) 
                                GetClipboardData(uFormat); 
                            SelectObject(hdcMem, hbm); 
                            GetClientRect(hwnd, &rc); 
 
                            BitBlt(hdc, 0, 0, rc.right, rc.bottom, 
                                hdcMem, 0, 0, SRCCOPY); 
                            CloseClipboard(); 
                        } 
                        DeleteDC(hdcMem); 
                    } 
                    break; 
 
                case CF_TEXT: 
                    if (OpenClipboard(hwnd)) 
                    { 
                        hglb = GetClipboardData(uFormat); 
                        lpstr = GlobalLock(hglb); 
 
                        GetClientRect(hwnd, &rc); 
                        DrawText(hdc, lpstr, -1, &rc, DT_LEFT); 
 
                        GlobalUnlock(hglb); 
                        CloseClipboard(); 
                    } 
                    break; 
 
                case CF_ENHMETAFILE: 
                    if (OpenClipboard(hwnd)) 
                    { 
                        hemf = GetClipboardData(uFormat); 
                        GetClientRect(hwnd, &rc); 
                        PlayEnhMetaFile(hdc, hemf, &rc); 
                        CloseClipboard(); 
                    } 
                    break; 
 
                case 0: 
                    GetClientRect(hwnd, &rc); 
                    DrawText(hdc, "The clipboard is empty.", -1, 
                        &rc, DT_CENTER | DT_SINGLELINE | 
                        DT_VCENTER); 
                    break; 
 
                default: 
                    GetClientRect(hwnd, &rc); 
                    DrawText(hdc, "Unable to display format.", -1, 
                        &rc, DT_CENTER | DT_SINGLELINE | 
                        DT_VCENTER); 
            } 
            EndPaint(hwnd, &ps); 
            break; 
 
        case WM_SIZE: 
            if (uFormat == CF_OWNERDISPLAY) 
            { 
                hwndOwner = GetClipboardOwner(); 
                hglb = GlobalAlloc(GMEM_MOVEABLE, sizeof(RECT)); 
                lprc = GlobalLock(hglb); 
                GetClientRect(hwnd, lprc); 
                GlobalUnlock(hglb); 
 
                SendMessage(hwndOwner, WM_SIZECLIPBOARD, 
                    (WPARAM) hwnd, (LPARAM) hglb); 
 
                GlobalFree(hglb); 
            } 
            break; 
 
        case WM_CREATE: 
 
            // Add the window to the clipboard viewer chain. 
 
            hwndNextViewer = SetClipboardViewer(hwnd); 
            break; 
 
        case WM_CHANGECBCHAIN: 
 
            // If the next window is closing, repair the chain. 
 
            if ((HWND) wParam == hwndNextViewer) 
                hwndNextViewer = (HWND) lParam; 
 
            // Otherwise, pass the message to the next link. 
 
            else if (hwndNextViewer != NULL) 
                SendMessage(hwndNextViewer, uMsg, wParam, lParam); 
 
            break; 
 
        case WM_DESTROY: 
            ChangeClipboardChain(hwnd, hwndNextViewer); 
            PostQuitMessage(0); 
            break; 
 
        case WM_DRAWCLIPBOARD:  // clipboard contents changed. 
 
            // Update the window by using Auto clipboard format. 
 
            SetAutoView(hwnd); 
 
            // Pass the message to the next window in clipboard 
            // viewer chain. 
 
            SendMessage(hwndNextViewer, uMsg, wParam, lParam); 
            break; 
 
        case WM_INITMENUPOPUP: 
            if (!HIWORD(lParam)) 
                InitMenu(hwnd, (HMENU) wParam); 
            break; 
 
        case WM_COMMAND: 
            switch (LOWORD(wParam)) 
            { 
                case IDM_EXIT: 
                    DestroyWindow(hwnd); 
                    break; 
 
                case IDM_AUTO: 
                    SetAutoView(hwnd); 
                    break; 
 
                default: 
                    fAuto = FALSE; 
                    uFormat = LOWORD(wParam); 
                    InvalidateRect(hwnd, NULL, TRUE); 
            } 
            break; 
 
        default: 
            return DefWindowProc(hwnd, uMsg, wParam, lParam); 
    } 
    return (LRESULT) NULL; 
} 
 
void WINAPI SetAutoView(HWND hwnd) 
{ 
    static UINT auPriorityList[] = { 
        CF_OWNERDISPLAY, 
        CF_TEXT, 
        CF_ENHMETAFILE, 
        CF_BITMAP 
    }; 
 
    uFormat = GetPriorityClipboardFormat(auPriorityList, 4); 
    fAuto = TRUE; 
 
    InvalidateRect(hwnd, NULL, TRUE); 
    UpdateWindow(hwnd); 
} 
 
void WINAPI InitMenu(HWND hwnd, HMENU hmenu) 
{ 
    UINT uFormat; 
    char szFormatName[80]; 
    LPCSTR lpFormatName; 
    UINT fuFlags; 
    UINT idMenuItem; 
 
    // If a menu is not the display menu, no initialization is necessary. 
 
    if (GetMenuItemID(hmenu, 0) != IDM_AUTO) 
        return; 
 
    // Delete all menu items except the first. 
 
    while (GetMenuItemCount(hmenu) > 1) 
        DeleteMenu(hmenu, 1, MF_BYPOSITION); 
 
    // Check or uncheck the Auto menu item. 
 
    fuFlags = fAuto ? MF_BYCOMMAND | MF_CHECKED : 
        MF_BYCOMMAND | MF_UNCHECKED; 
    CheckMenuItem(hmenu, IDM_AUTO, fuFlags); 
 
    // If there are no clipboard formats, return. 
 
    if (CountClipboardFormats() == 0) 
        return; 
 
    // Open the clipboard. 
 
    if (!OpenClipboard(hwnd)) 
        return; 
 
    // Add a separator and then a menu item for each format. 
 
    AppendMenu(hmenu, MF_SEPARATOR, 0, NULL); 
    uFormat = EnumClipboardFormats(0); 
 
    while (uFormat) 
    { 
        // Call an application-defined function to get the name 
        // of the clipboard format. 
 
        lpFormatName = GetPredefinedClipboardFormatName(uFormat); 
 
        // For registered formats, get the registered name. 
 
        if (lpFormatName == NULL) 
        {

        // Note that, if the format name is larger than the
        // buffer, it is truncated. 
            if (GetClipboardFormatName(uFormat, szFormatName, 
                    sizeof(szFormatName))) 
                lpFormatName = szFormatName; 
            else 
                lpFormatName = "(unknown)"; 
        } 
 
        // Add a menu item for the format. For displayable 
        // formats, use the format ID for the menu ID. 
 
        if (IsDisplayableFormat(uFormat)) 
        { 
            fuFlags = MF_STRING; 
            idMenuItem = uFormat; 
        } 
        else 
        { 
            fuFlags = MF_STRING | MF_GRAYED; 
            idMenuItem = 0; 
        } 
        AppendMenu(hmenu, fuFlags, idMenuItem, lpFormatName); 
 
        uFormat = EnumClipboardFormats(uFormat); 
    } 
    CloseClipboard(); 
 
} 
 
BOOL WINAPI IsDisplayableFormat(UINT uFormat) 
{ 
    switch (uFormat) 
    { 
        case CF_OWNERDISPLAY: 
        case CF_TEXT: 
        case CF_ENHMETAFILE: 
        case CF_BITMAP: 
            return TRUE; 
    } 
    return FALSE; 
} 
```

---
title: Subclassing Controls
description: If a control does almost everything you want, but you need a few more features, you can change or add features to the original control by subclassing it.
ms.assetid: 7f558674-c8b2-4461-96ba-e139416b7a1c
ms.topic: article
ms.date: 05/31/2018
---

# Subclassing Controls

If a control does almost everything you want, but you need a few more features, you can change or add features to the original control by subclassing it. A subclass can have all the features of an existing class as well as any additional features you want to give it.

This document discusses how subclasses are created and includes the following topics.

-   [Subclassing Controls Prior to ComCtl32.dll version 6](#subclassing-controls-prior-to-comctl32dll-version-6)
    -   [Storing User Data](#storing-user-data)
    -   [Disadvantages of the Old Subclassing Approach](#disadvantages-of-the-old-subclassing-approach)
-   [Subclassing Controls Using ComCtl32.dll version 6](#subclassing-controls-using-comctl32dll-version-6)
    -   [SetWindowSubclass](#setwindowsubclass)
    -   [GetWindowSubclass](#getwindowsubclass)
    -   [RemoveWindowSubclass](#removewindowsubclass)
    -   [DefSubclassProc](#defsubclassproc)

## Subclassing Controls Prior to ComCtl32.dll version 6

You can put a control in a subclass and store user data within a control. You do this when you use versions of ComCtl32.dll prior to version 6. There are some disadvantages in creating subclasses with earlier versions of ComCtl32.dll.

To make a new control, it is best to start with one of the Windows common controls and extend it to fit a particular need. To extend a control, create a control and replace its existing window procedure with a new one. The new procedure intercepts the control's messages and either acts on them or passes them to the original procedure for default processing. Use the [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) or [**SetWindowLongPtr**](/windows/desktop/api/winuser/nf-winuser-setwindowlongptra) function to replace the WNDPROC of the control. The following code sample shows how to replace a WNDPROC.


```
OldWndProc = (WNDPROC)SetWindowLongPtr (hButton,
GWLP_WNDPROC, (LONG_PTR)NewWndProc);
```



### Storing User Data

You might want to store user data with an individual window. This data can be used by the new window procedure to determine how to draw the control or where to send certain messages. For example, you might use data to store a C++ class pointer to the class that represents the control. The following code sample shows how to use [**SetProp**](/windows/desktop/api/winuser/nf-winuser-setpropa) to store data with a window.


```
SetProp (hwnd, TEXT("MyData"), (HANDLE)pMyData);
```



### Disadvantages of the Old Subclassing Approach

The following list points out some of the disadvantages of using the previously described approach to subclassing a control.

-   The window procedure can only be replaced once.
-   It is difficult to remove a subclass after it is created.
-   Associating private data with a window is inefficient.
-   To call the next procedure in a subclass chain, you cannot cast the old window procedure and call it, you must call it by using the [**CallWindowProc**](/windows/desktop/api/winuser/nf-winuser-callwindowproca) function.

## Subclassing Controls Using ComCtl32.dll version 6

> [!Note]  
> ComCtl32.dll version 6 is Unicode only. The common controls supported by ComCtl32.dll version 6 should not be subclassed (or superclassed) with ANSI window procedures.

 

ComCtl32.dll version 6 contains four functions that make creating subclasses easier and eliminate the disadvantages previously discussed. The new functions encapsulate the management involved with multiple sets of reference data, therefore the developer can focus on programming features and not on managing subclasses. The subclassing functions are:

-   [**SetWindowSubclass**](/windows/desktop/api/commctrl/nf-commctrl-setwindowsubclass)
-   [**GetWindowSubclass**](/windows/desktop/api/commctrl/nf-commctrl-getwindowsubclass)
-   [**RemoveWindowSubclass**](/windows/desktop/api/commctrl/nf-commctrl-removewindowsubclass)
-   [**DefSubclassProc**](/windows/desktop/api/commctrl/nf-commctrl-defsubclassproc)

### SetWindowSubclass

This function is used to initially subclass a window. Each subclass is uniquely identified by the address of the *pfnSubclass* and its *uIdSubclass*. Both of these are parameters of the [**SetWindowSubclass**](/windows/desktop/api/commctrl/nf-commctrl-setwindowsubclass) function. Several subclasses can share the same subclass procedure and the ID can identify each call. To change reference data you can make subsequent calls to **SetWindowSubclass**. The important advantage is that each subclass instance has its own reference data.

The declaration of a subclass procedure is slightly different from a regular window procedure because it has two additional pieces of data: the subclass ID and the reference data. The last two parameters of the following function declaration show this.


```
LRESULT CALLBACK MyWndProc (HWND hWnd, UINT msg,
WPARAM wParam, LPARAM lParam, UINT_PTR uIdSubclass,
DWORD_PTR dwRefData);
```



Every time a message is received by the new window procedure, a subclass ID and reference data are included.

> [!Note]  
> All strings passed to the procedure are Unicode strings even if Unicode is not specified as a preprocessor definition.

 

The following example shows a skeleton implementation of a window procedure for a subclassed control.


```
LRESULT CALLBACK OwnerDrawButtonProc(HWND hWnd, UINT uMsg, WPARAM wParam,
                               LPARAM lParam, UINT_PTR uIdSubclass, DWORD_PTR dwRefData)
{
    switch (uMsg)
    {
    case WM_PAINT:
        .
        .
        .
        return TRUE;
    // Other cases...
    } 
    return DefSubclassProc(hWnd, uMsg, wParam, lParam);
}
```



The window procedure can be attached to the control in the [**WM\_INITDIALOG**](/windows/desktop/dlgbox/wm-initdialog) handler of the dialog procedure, as shown in the following example.


```
case WM_INITDIALOG:
{
    HWND button = GetDlgItem(hDlg, IDC_OWNERDRAWBUTTON);
    SetWindowSubclass(button, OwnerDrawButtonProc, 0, 0);
    return TRUE;
}
```



### GetWindowSubclass

This function retrieves information about a subclass. For example, you can use [**GetWindowSubclass**](/windows/desktop/api/commctrl/nf-commctrl-getwindowsubclass) to access the reference data.

### RemoveWindowSubclass

This function removes subclasses. [**RemoveWindowSubclass**](/windows/desktop/api/commctrl/nf-commctrl-removewindowsubclass) in combination with [**SetWindowSubclass**](/windows/desktop/api/commctrl/nf-commctrl-setwindowsubclass) allows you to dynamically add and remove subclasses.

### DefSubclassProc

The [**DefSubclassProc**](/windows/desktop/api/commctrl/nf-commctrl-defsubclassproc) function calls the next handler in the subclass chain. The function also retrieves the proper ID and reference data and passes the information to the next window procedure.

 

 
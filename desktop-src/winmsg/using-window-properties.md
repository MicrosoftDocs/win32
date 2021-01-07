---
description: This section explains how to perform the following tasks associated with window properties.
ms.assetid: cdf196ec-300c-4c7b-8a4f-68088c4a2507
title: Using Window Properties
ms.topic: article
ms.date: 05/31/2018
---

# Using Window Properties

This section explains how to perform the following tasks associated with window properties.

-   [Adding a Window Property](#adding-a-window-property)
-   [Retrieving a Window Property](#retrieving-a-window-property)
-   [Listing Window Properties for a Given Window](#listing-window-properties-for-a-given-window)
-   [Deleting a Window Property](#deleting-a-window-property)

## Adding a Window Property

The following example loads an icon and then a cursor and allocates memory for a buffer. The example then uses the [**SetProp**](/windows/win32/api/winuser/nf-winuser-setpropa) function to assign the resulting icon, cursor, and memory handles as window properties for the window identified by the application-defined hwndSubclass variable. The properties are identified by the strings PROP\_ICON, PROP\_CURSOR, and PROP\_BUFFER.


```
#define BUFFER 4096 
 
HINSTANCE hinst;       // handle of current instance 
HWND hwndSubclass;     // handle of a subclassed window 
HANDLE hIcon, hCursor; 
HGLOBAL hMem; 
char *lpMem; 
TCHAR tchPath[] = "c:\\winnt\\samples\\winprop.c";
HRESULT hResult; 
 
// Load resources. 
 
hIcon = LoadIcon(hinst, MAKEINTRESOURCE(400)); 
hCursor = LoadCursor(hinst, MAKEINTRESOURCE(220)); 
 
// Allocate and fill a memory buffer. 
 
hMem = GlobalAlloc(GPTR, BUFFER); 
lpMem = GlobalLock(hMem);
if (lpMem == NULL)
{
// TODO: write error handler
}
hResult = StringCchCopy(lpMem, STRSAFE_MAX_CCH, tchPath);
if (FAILED(hResult))
{
// TO DO: write error handler if function fails.
} 
GlobalUnlock(hMem); 
 
// Set the window properties for hwndSubclass. 
 
SetProp(hwndSubclass, "PROP_ICON", hIcon); 
SetProp(hwndSubclass, "PROP_CURSOR", hCursor); 
SetProp(hwndSubclass, "PROP_BUFFER", hMem); 
```



## Retrieving a Window Property

A window can create handles to its window property data and use the data for any purpose. The following example uses [**GetProp**](/windows/win32/api/winuser/nf-winuser-getpropa) to obtain handles to the window properties identified by PROP\_ICON, PROP\_CURSOR, and PROP\_BUFFER. The example then displays the contents of the newly obtained memory buffer, cursor, and icon in the window's client area.


```
#define PATHLENGTH 256 
 
HWND hwndSubclass;     // handle of a subclassed window 
HANDLE hIconProp, hCursProp; 
HGLOBAL hMemProp; 
char *lpFilename; 
TCHAR tchBuffer[PATHLENGTH]; 
size_t * nSize; 
HDC hdc;
HRESULT hResult; 
 
// Get the window properties, then use the data. 
 
hIconProp = (HICON) GetProp(hwndSubclass, "PROP_ICON"); 
TextOut(hdc, 10, 40, "PROP_ICON", 9); 
DrawIcon(hdc, 90, 40, hIconProp); 
 
hCursProp = (HCURSOR) GetProp(hwndSubclass, "PROP_CURSOR"); 
TextOut(hdc, 10, 85, "PROP_CURSOR", 9); 
DrawIcon(hdc, 110, 85, hCursProp); 
 
hMemProp = (HGLOBAL) GetProp(hwndSubclass, "PROP_BUFFER"); 
lpFilename = GlobalLock(hMemProp);
hResult = StringCchPrintf(tchBuffer, PATHLENGTH, 
    "Path to file:  %s", lpFilename);
if (FAILED(hResult))
{
// TODO: write error handler if function fails.
}
hResult = StringCchLength(tchBuffer, PATHLENGTH, nSize)
if (FAILED(hResult))
{
// TODO: write error handler if function fails.
}
TextOut(hdc, 10, 10, tchBuffer, *nSize); 
```



## Listing Window Properties for a Given Window

In the following example, the [**EnumPropsEx**](/windows/win32/api/winuser/nf-winuser-enumpropsexa) function lists the string identifiers of the window properties for the window identified by the application-defined hwndSubclass variable. This function relies on the application-defined callback function WinPropProc to display the strings in the window's client area.


```
EnumPropsEx(hwndSubclass, WinPropProc, NULL); 
 
// WinPropProc is an application-defined callback function 
// that lists a window property. 
 
BOOL CALLBACK WinPropProc( 
    HWND hwndSubclass,  // handle of window with property 
    LPCSTR lpszString,  // property string or atom 
    HANDLE hData)       // data handle 
{ 
    static int nProp = 1;    // property counter 
    TCHAR tchBuffer[BUFFER]; // expanded-string buffer 
    size_t * nSize;          // size of string in buffer 
    HDC hdc;                 // device-context handle
    HRESULT hResult; 
 
    hdc = GetDC(hwndSubclass); 
 
    // Display window property string in client area.
    hResult = StringCchPrintf(tchBuffer, BUFFER, "WinProp %d:  %s", nProp++, lpszString);
    if (FAILED(hResult))
    {
    // TO DO: write error handler if function fails.
    }
    hResult = StringCchLength(tchBuffer, BUFFER, nSize);
    if (FAILED(hResult))
    {
    // TO DO: write error handler if function fails.
    } 
    TextOut(hdc, 10, nProp * 20, tchBuffer, *nSize); 
 
    ReleaseDC(hwndSubclass, hdc); 
 
    return TRUE; 
} 
```



## Deleting a Window Property

When a window is destroyed, it must destroy any window properties it set. The following example uses the [**EnumPropsEx**](/windows/win32/api/winuser/nf-winuser-enumpropsexa) function and the application-defined callback function DelPropProc to destroy the properties associated with the window identified by the application-defined hwndSubclass variable. The callback function, which uses the [**RemoveProp**](/windows/win32/api/winuser/nf-winuser-removepropa) function, is also shown.


```
case WM_DESTROY: 
 
    EnumPropsEx(hwndSubclass, DelPropProc, NULL); 
 
    PostQuitMessage(0); 
    break; 
 
// DelPropProc is an application-defined callback function 
// that deletes a window property. 
 
BOOL CALLBACK DelPropProc( 
    HWND hwndSubclass,  // handle of window with property 
    LPCSTR lpszString,  // property string or atom 
    HANDLE hData)       // data handle 
{ 
    hData = RemoveProp(hwndSubclass, lpszString); 
//
// if appropriate, free the handle hData
//
 
    return TRUE; 
}
```



 

 

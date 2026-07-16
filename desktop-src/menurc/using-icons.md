---
title: Using Icons
description: This section provides code samples that show how to perform tasks related to icons.
ms.assetid: 5021d59a-7aae-4ddc-be66-9abdc75ad316
keywords:
- resources,icons
- icons,creating
- icons,displaying
- icons,sharing resources
- creating icons
- displaying icons
- sharing icon resources
ms.topic: concept-article
ms.date: 05/31/2018
---

# Using Icons

The following topics describe how to perform certain tasks related to icons:

-   [Creating an Icon](#creating-an-icon)
-   [Getting the Icon size](#getting-the-icon-size)
-   [Displaying an Icon](#displaying-an-icon)
-   [Sharing Icon Resources](#sharing-icon-resources)

## Creating an Icon

The following example creates two icon handles: one for the standard question icon and one for a custom icon included as a resource in the application's resource-definition file.

```c
HICON hIcon1 = LoadIcon(NULL, IDI_QUESTION);
HICON hIcon2 = LoadIcon(hInstance, MAKEINTRESOURCE(IDI_MYICON));
```

Applications should implement custom icons as resources and use [**LoadIcon**](/windows/win32/api/winuser/nf-winuser-loadiconw) or [**LoadImage**](/windows/win32/api/winuser/nf-winuser-loadimagew) rather than create the icon at run time. Using icon resources avoids device dependence, simplifies localization, and enables applications to share icon designs.

[**CreateIcon**](/windows/win32/api/winuser/nf-winuser-createicon) can be used to create a custom monochrome icon at run time. The technique is identical to the [Creating a Cursor](/windows/win32/menurc/using-cursors#creating-a-cursor) example — use the same `PackCursorMasks` helper and symbol map, replace [**CreateCursor**](/windows/win32/api/winuser/nf-winuser-createcursor) with [**CreateIcon**](/windows/win32/api/winuser/nf-winuser-createicon), and omit the hotspot parameters.

To create an alpha blended icon at run time, see [Creating an Alpha Blended Cursor](/windows/win32/menurc/using-cursors#creating-an-alpha-blended-cursor) — pass `TRUE` for `fIcon` in [**ICONINFO**](/windows/win32/api/winuser/ns-winuser-iconinfo) to create an icon instead of a cursor.

Before closing, your application must use [**DestroyIcon**](/windows/win32/api/winuser/nf-winuser-destroyicon) to destroy any icon obtained from [**CreateIcon**](/windows/win32/api/winuser/nf-winuser-createicon), [**CreateIconIndirect**](/windows/win32/api/winuser/nf-winuser-createiconindirect), or [**LoadImage**](/windows/win32/api/winuser/nf-winuser-loadimagew) without the `LR_SHARED` flag. Icons loaded with [**LoadIcon**](/windows/win32/api/winuser/nf-winuser-loadiconw) or `LoadImage` with `LR_SHARED` are shared system resources and must not be destroyed.

## Getting the Icon size

See [Getting a Cursor size](/windows/win32/menurc/using-cursors#getting-a-cursor-size). The example works identically for icons — pass an `HICON` in place of `HCURSOR`.

## Displaying an Icon

Your application can load and create icons to display in the application's client area or child windows. The following example demonstrates how to draw an icon in the client area of the window whose device context (DC) is identified by the *hdc* parameter.

```c
DrawIcon(hdc, 10, 20, hIcon1);
```

The system automatically displays the class icon(s) for a window. Your application can assign class icons while registering a window class. Your application can replace a class icon by using the [**SetClassLongPtr**](/windows/win32/api/winuser/nf-winuser-setclasslongptrw) function. This function changes the default window settings for all windows of a given class. The following example replaces a class icon with the icon whose resource identifier is 480.

```c
SetClassLongPtr(hWnd, GCLP_HICON,
    (LONG_PTR)LoadIcon(hInstance, MAKEINTRESOURCE(IDI_MYICON)));
```

For more information about window classes, see [Window Classes](/windows/win32/winmsg/window-classes).

## Sharing Icon Resources

The following code uses the functions [**CreateIconFromResourceEx**](/windows/win32/api/winuser/nf-winuser-createiconfromresourceex), [**DrawIcon**](/windows/win32/api/winuser/nf-winuser-drawicon), and [**LookupIconIdFromDirectoryEx**](/windows/win32/api/winuser/nf-winuser-lookupiconidfromdirectoryex), and several of the resource functions, to create an icon handle based on icon data from another executable file. Then, it displays the icon in a window.

**Security Warning:** Using [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryw) incorrectly can compromise the security of your application by loading the wrong DLL. Refer to the **LoadLibrary** documentation for information on how to correctly load DLLs with different versions of Windows.

```c
int cx = GetSystemMetrics(SM_CXICON);
int cy = GetSystemMetrics(SM_CYICON);

// LoadLibraryExW with LOAD_LIBRARY_AS_DATAFILE avoids running the DLL/EXE.
// Always use a fully qualified path to prevent DLL planting.
HINSTANCE hExe = LoadLibraryEx(TEXT("C:\\path\\to\\myapp.exe"), NULL,
                               LOAD_LIBRARY_AS_DATAFILE);
if (hExe == NULL)
    return;

HRSRC hResource = FindResource(hExe, MAKEINTRESOURCE(440), RT_GROUP_ICON);
HGLOBAL hMem    = LoadResource(hExe, hResource);
BYTE *lpResource = LockResource(hMem);

int nID = LookupIconIdFromDirectoryEx(lpResource, TRUE, cx, cy, LR_DEFAULTCOLOR);

hResource  = FindResource(hExe, MAKEINTRESOURCE(nID), RT_ICON);
hMem       = LoadResource(hExe, hResource);
lpResource = LockResource(hMem);

HICON hIcon1 = CreateIconFromResourceEx(lpResource,
    SizeofResource(hExe, hResource), TRUE, 0x00030000,
    cx, cy, LR_DEFAULTCOLOR);

DrawIcon(hdc, 10, 20, hIcon1);

FreeLibrary(hExe);
```

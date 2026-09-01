---
title: About Icons
description: This topic discusses icons.
ms.assetid: 67867460-07f6-460f-9263-05bbf3474744
keywords:
- resources,icons
- icons,standard
- standard icons
- icons,custom
- custom icons
- icons,sizes
- creating icons
- icons,displaying
- icons,destroying
- icons,duplicating
- icons,creating
- displaying icons
- destroying icons
- duplicating icons
- IDI_APPLICATION, IDI_ASTERISK, IDI_ERROR, IDI_EXCLAMATION, IDI_HAND, IDI_INFORMATION, IDI_QUESTION, IDI_SHIELD, IDI_WARNING, IDI_WINLOGO
ms.topic: concept-article
ms.date: 05/31/2018
---

# About Icons

The system uses icons throughout the user interface to represent objects such as files, folders, shortcuts, applications, and documents. The icon functions enable applications to create, load, display, copy, and destroy icons. For information on specifying icons for file types, see [**ExtractIcon**](/windows/win32/api/shellapi/nf-shellapi-extracticonw).

This overview provides information on the following topics:

-   [Icon Types](#icon-types)
-   [Icon Sizes](#icon-sizes)
    -   [System icon sizes](#system-icon-sizes)
    -   [Shell icon sizes](#shell-icon-sizes)
-   [Icon Creation](#icon-creation)
-   [The Window Class Icon](#the-window-class-icon)
-   [Icon Display](#icon-display)
-   [Icon Destruction](#icon-destruction)
-   [Icon Duplication](#icon-duplication)

## Icon Types

The operating system provides a set of standard icons that are available for any application to use at any time. The software development kit (SDK) header files contain identifiers for the **system icons** - the identifiers begin with the **IDI\_** prefix.

| Value | Meaning |
|---|---|
| **IDI\_APPLICATION**<br/>MAKEINTRESOURCE(32512) | :::image type="icon" source="./images/IDI_APPLICATION.png"::: Default application icon |
| **IDI\_ERROR**<br/>MAKEINTRESOURCE(32513) | :::image type="icon" source="./images/IDI_ERROR.png"::: Error icon |
| **IDI\_QUESTION**<br/>MAKEINTRESOURCE(32514) | :::image type="icon" source="./images/IDI_QUESTION.png"::: Question mark icon |
| **IDI\_WARNING**<br/>MAKEINTRESOURCE(32515) | :::image type="icon" source="./images/IDI_WARNING.png"::: Warning icon |
| **IDI\_INFORMATION**<br/>MAKEINTRESOURCE(32516) | :::image type="icon" source="./images/IDI_INFORMATION.png"::: Information icon |
| **IDI\_WINLOGO**<br/>MAKEINTRESOURCE(32517) | :::image type="icon" source="./images/IDI_WINLOGO.png"::: Windows logo icon |
| **IDI\_SHIELD**<br/>MAKEINTRESOURCE(32518) | :::image type="icon" source="./images/IDI_SHIELD.png"::: Security shield icon |

See [Guidelines](/windows/win32/uxguide/vis-std-icons) for information on recommended usage of standard icons.

Also, starting with Windows Vista, an additional set of **standard system shell icons** is available through the [SHGetStockIconInfo](/windows/win32/api/shellapi/nf-shellapi-shgetstockiconinfo) method.

*Custom icons* are designed for use in a particular application and can be any design. User can load custom icons from files or create them at run-time. Following are several custom icons.

![several custom icons](images/csicn-02.png)

## Icon Sizes

See [Icon scaling](/windows/apps/design/style/iconography/app-icon-construction#icon-scaling) for recommendations on preferred icon sizes for your application.

### System icon sizes

System icon sizes are reported by [**GetSystemMetrics**](/windows/win32/api/winuser/nf-winuser-getsystemmetrics) and scale linearly with DPI - unlike cursor sizes, which change in discrete steps.

| Size | Metric | 96 DPI (100%) | 384 DPI (400%) | Description |
|---|---|---|---|---|
| System small | **SM\_CXSMICON** / **SM\_CYSMICON** | 16x16 | 64x64 | Menus, notification area, Explorer list view |
| System large | **SM\_CXICON** / **SM\_CYICON** | 32x32 | 128x128 | ICON\_BIG (WM\_SETICON / WM\_GETICON), Alt+Tab (legacy/fallback) |

The [**CreateIconFromResource**](/windows/win32/api/winuser/nf-winuser-createiconfromresource), [**DrawIcon**](/windows/win32/api/winuser/nf-winuser-drawicon), [**ExtractAssociatedIcon**](/windows/win32/api/shellapi/nf-shellapi-extractassociatediconw), [**ExtractIcon**](/windows/win32/api/shellapi/nf-shellapi-extracticonw), [**ExtractIconEx**](/windows/win32/api/shellapi/nf-shellapi-extracticonexw), and [**LoadIcon**](/windows/win32/api/winuser/nf-winuser-loadiconw) functions all use the system large icon size. The [**CreateIcon**](/windows/win32/api/winuser/nf-winuser-createicon), [**CreateIconFromResourceEx**](/windows/win32/api/winuser/nf-winuser-createiconfromresourceex), [**CreateIconIndirect**](/windows/win32/api/winuser/nf-winuser-createiconindirect), and [**LoadImage**](/windows/win32/api/winuser/nf-winuser-loadimagew) functions can work with icons at any size.

To retrieve system icon sizes, call [**GetSystemMetrics**](/windows/win32/api/winuser/nf-winuser-getsystemmetrics) with **SM\_CXSMICON** / **SM\_CYSMICON** for the small size, or **SM\_CXICON** / **SM\_CYICON** for the large size. In per-monitor DPI-aware applications, use [**GetSystemMetricsForDpi**](/windows/win32/api/winuser/nf-winuser-getsystemmetricsfordpi) with the DPI of the target monitor instead, so the returned size reflects the correct display. The baseline DPI value of 96 is available as **USER\_DEFAULT\_SCREEN\_DPI** in winuser.h, useful when computing scaled sizes with **MulDiv**. For code examples, see [Getting System Icon Sizes](using-icons.md#getting-system-icon-sizes). For more information, see [High DPI Desktop Application Development on Windows](/windows/win32/hidpi/high-dpi-desktop-application-development-on-windows).

### Shell icon sizes

The shell uses a separate set of sizes for Explorer views and the system image lists, accessible via [**SHGetImageList**](/windows/win32/api/shellapi/nf-shellapi-shgetimagelistw). Call **SHGetImageList** with the appropriate **SHIL\_\*** constant, then call [**ImageList\_GetIconSize**](/windows/win32/api/commctrl/nf-commctrl-imagelist_geticonsize) on the returned image list.

| SHIL constant | 96 DPI (100%) | 384 DPI (400%) | Description |
|---|---|---|---|
| **SHIL\_SMALL** (1) | 16x16 | 64x64 | Explorer list/details view, common dialogs, window title bar icon |
| **SHIL\_SYSSMALL** (3) | 16x16 | 64x64 | Shell toolbars, status bars; tracks caption button size; may differ from **SHIL\_SMALL** when the user customizes window border and caption size |
| **SHIL\_LARGE** (0) | 32x32 | 128x128 | Explorer medium icons view, dialogs |
| **SHIL\_EXTRALARGE** (2) | 48x48 | 192x192 | Explorer large icons view, desktop |
| **SHIL\_JUMBO** (4) | 256x256 | 256x256 | Explorer extra large icons view (Vista+); always 256 physical pixels |

## Icon Creation

An icon resource (.ico file or **RT\_ICON** / **RT\_GROUP\_ICON** in a PE file) stores multiple images - typically at standard sizes 16, 32, 48, and 256 pixels, optionally at different color depths including 32bpp ARGB for per-pixel alpha transparency. Each image is optimized for its size; providing all standard sizes avoids the quality loss that results from scaling a single image up or down.

To load an icon from a resource, call [**LoadIcon**](/windows/win32/api/winuser/nf-winuser-loadiconw) or [**LoadImage**](/windows/win32/api/winuser/nf-winuser-loadimagew). The system automatically selects the best-matching image for the requested size and display color depth using the same algorithm as [**LookupIconIdFromDirectoryEx**](/windows/win32/api/winuser/nf-winuser-lookupiconidfromdirectoryex). To load directly from an .ico file, pass **LR\_LOADFROMFILE** to **LoadImage**. To load at a non-standard size with high-quality scaling, use [**LoadIconWithScaleDown**](/windows/win32/api/commctrl/nf-commctrl-loadiconwithscaledown) - it selects the nearest larger standard image (16, 32, 48, or 256) and scales it down to the requested size.

An application can also create a custom icon at run-time by using the [**CreateIconIndirect**](/windows/win32/api/winuser/nf-winuser-createiconindirect) function, which creates an icon based on the contents of an [**ICONINFO**](/windows/win32/api/winuser/ns-winuser-iconinfo) structure. Note that for icons the hotspot fields in **ICONINFO** are ignored by the system - the hotspot is always the center of the image. The [**CreateIconFromResourceEx**](/windows/win32/api/winuser/nf-winuser-createiconfromresourceex) function creates an icon from binary resource data from other executable files or DLLs; use [**LookupIconIdFromDirectoryEx**](/windows/win32/api/winuser/nf-winuser-lookupiconidfromdirectoryex) first to identify the most appropriate image for the current display size and color depth. For examples, see [Creating an Icon](using-icons.md#creating-an-icon).

Applications should implement custom icons as resources and use **LoadIcon** or **LoadImage** rather than create icons at run-time. Using icon resources avoids device dependence, simplifies localization, and enables applications to share icon shapes.

## The Window Class Icon

When you register a window class using the [**RegisterClassEx**](/windows/win32/api/winuser/nf-winuser-registerclassexw) function, set the **hIcon** field of [**WNDCLASSEX**](/windows/win32/api/winuser/ns-winuser-wndclassexa) to the large icon (**SM\_CXICON** x **SM\_CYICON**) and **hIconSm** to the small icon (**SM\_CXSMICON** x **SM\_CYSMICON**). Every window of that class uses these icons by default. For more information, see [Class Icons](/windows/win32/winmsg/about-window-classes).

To set or update a specific window's icon at run time, send [**WM\_SETICON**](/windows/win32/winmsg/wm-seticon) with **ICON\_BIG** or **ICON\_SMALL**. To retrieve the current icon handle, send [**WM\_GETICON**](/windows/win32/winmsg/wm-geticon) with the same wParam value. To replace the class icon for all windows of a class, use [**SetClassLongPtr**](/windows/win32/api/winuser/nf-winuser-setclasslongptrw) with **GCLP\_HICON** or **GCLP\_HICONSM**.

## Icon Display

You can retrieve the image and size of an icon by using the [**GetIconInfo**](/windows/win32/api/winuser/nf-winuser-geticoninfo) function - see [Getting Icon Size from Handle](using-icons.md#getting-icon-size-from-handle) for an example. You can draw the icon by using the [**DrawIconEx**](/windows/win32/api/winuser/nf-winuser-drawiconex) function.

To display an icon in a static control, send [**STM\_SETIMAGE**](/windows/win32/controls/stm-setimage) with **IMAGE\_ICON** and the icon handle:

```c
HICON hIcon = LoadIcon(hInstance, MAKEINTRESOURCE(IDI_MYICON));
SendMessage(hStatic, STM_SETIMAGE, IMAGE_ICON, (LPARAM)hIcon);
```

## Icon Destruction

When an application no longer needs an icon, destroy it by calling [**DestroyIcon**](/windows/win32/api/winuser/nf-winuser-destroyicon). The only exceptions are shared handles, which must **not** be destroyed:

- [**LoadIcon**](/windows/win32/api/winuser/nf-winuser-loadiconw) - always uses **LR\_SHARED** internally regardless of the instance parameter; use **LoadImage** without **LR\_SHARED** if you need an owned handle
- [**LoadImage**](/windows/win32/api/winuser/nf-winuser-loadimagew) with **LR\_SHARED**
- [**CopyImage**](/windows/win32/api/winuser/nf-winuser-copyimage) with **LR\_COPYRETURNORG** when the size already matches - returns the original handle, which may be shared

## Icon Duplication

The [**CopyIcon**](/windows/win32/api/winuser/nf-winuser-copyicon) function creates a new independent icon object with the same image as the original. This enables an application or DLL to obtain an icon that outlives the module it was loaded from - if the original module is freed, the copy remains valid. The copy is owned by the caller.

The [**CopyImage**](/windows/win32/api/winuser/nf-winuser-copyimage) function creates a new icon based on an existing icon handle, optionally at a different size - useful when you already hold a handle and need a resized copy without reloading the original resource.

For information about adding, removing, or replacing icon resources in executable (.exe) files, see [Resources](resources.md).

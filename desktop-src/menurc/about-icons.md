---
title: About Icons
description: This topic discusses icons.
ms.assetid: 67867460-07f6-460f-9263-05bbf3474744
keywords:
- resources,icons
- icons,hot spots
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
ms.topic: article
ms.date: 05/31/2018
---

# About Icons

The system uses icons throughout the user interface to represent objects such as files, folders, shortcuts, applications, and documents. The icon functions enable applications to create, load, display, arrange, animate, and destroy icons. For information on specifying icons for file types, see [**ExtractIcon**](/windows/desktop/api/Shellapi/nf-shellapi-extracticonw).

## Icon Types

The operating system provides a set of standard icons that are available for any application to use at any time. The software development kit (SDK) header files contain identifiers for the **system icons** — the identifiers begin with the **IDI\_** prefix.

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

The system uses four icon sizes:

-   System small (usually 16x16 pixels size)
-   System large (usually 32x32 pixels size)
-   Shell small (usually 16x16 pixels size)
-   Shell large (usually 32x32 pixels size)
-   Shell extra-large (usually 48x48 pixels size)
-   **Starting Windows Vista:** Jumbo (256x256 pixels size)

The *system small* icon is displayed in the window caption.
The *system large* icon is mainly used by applications, but it is also displayed in the classic Alt+Tab dialog. 
The *shell* and *jumbo* icons are used in the Windows Explorer and the common dialogs.

When filling in the [**WNDCLASSEX**](/windows/win32/api/winuser/ns-winuser-wndclassexw) structure to be used in registering your window class, set the `hIcon` member to the system large icon and the `hIconSm` member to the system small icon. For more information about class icons, see [Class Icons](/windows/desktop/winmsg/about-window-classes#class-icons).

As of Windows Vista, *shell small*, *shell large*, and *extra large* scale with dots per inch (dpi) if the process is [marked as dpi-aware](/windows/win32/hidpi/high-dpi-desktop-application-development-on-windows). *Jumbo* icon is fixed at 256 pixels regardless of the dpi-aware setting.

See [Icon scaling](/windows/apps/design/style/iconography/app-icon-construction#icon-scaling) for recommendations on preferred icon sizes for your application.

### To retrieve the size of the system icon

-   Call the [**GetSystemMetrics**](/windows/desktop/api/winuser/nf-winuser-getsystemmetrics) function with `SM_CXICON`/`SM_CYICON` or `SM_CXSMICON`/`SM_CYSMICON`.

The [**CreateIconFromResource**](/windows/desktop/api/Winuser/nf-winuser-createiconfromresource), [**DrawIcon**](/windows/desktop/api/Winuser/nf-winuser-drawicon), [**ExtractAssociatedIcon**](/windows/desktop/api/shellapi/nf-shellapi-extractassociatediconw), [**ExtractIcon**](/windows/desktop/api/Shellapi/nf-shellapi-extracticonw), [**ExtractIconEx**](/windows/desktop/api/Shellapi/nf-shellapi-extracticonexw), and [**LoadIcon**](/windows/desktop/api/Winuser/nf-winuser-loadiconw) functions all use *system large* icons.

The [**CreateIcon**](/windows/desktop/api/Winuser/nf-winuser-createicon), [**LoadImage**](/windows/win32/api/winuser/nf-winuser-loadimagew), [**CreateIconFromResourceEx**](/windows/desktop/api/Winuser/nf-winuser-createiconfromresourceex), [**CreateIconIndirect**](/windows/desktop/api/Winuser/nf-winuser-createiconindirect), and [**SHGetFileInfo**](/windows/win32/api/shellapi/nf-shellapi-shgetfileinfow) functions can be used to work with icons in sizes *other than system large*.

### To retrieve the size of the shell icon

1.  Use the [**SHGetImageList**](/windows/win32/api/shellapi/nf-shellapi-shgetimagelist) function with `SHIL_SMALL`/`SHIL_LARGE`/`SHIL_EXTRALARGE`/`SHIL_JUMBO` to retrieve a handle to the system image list.
2.  Then call the [**ImageList\_GetIconSize**](/windows/win32/api/commctrl/nf-commctrl-imagelist_geticonsize) function to get the icon size.

## Icon Creation

Standard icons are predefined, so it is not necessary to create them. To use a standard icon, an application can obtain its handle by using the [**LoadImage**](/windows/desktop/api/Winuser/nf-winuser-loadimagew) function. An *icon handle* is a unique value of the **HICON** type that identifies a standard or custom icon.

To create a custom icon for an application, you would typically use a graphics application and include the [ICON Resource](./icon-resource.md) in the application's resource-definition file. At run-time, you can call [**LoadIcon**](/windows/desktop/api/Winuser/nf-winuser-loadiconw) or [**LoadImage**](/windows/desktop/api/Winuser/nf-winuser-loadimagew) to retrieve a handle to the icon. An icon resource can contain a group of images for several different display devices. **LoadIcon** and **LoadImage** automatically select the most appropriate icon from the group for the current display device.

An application can also create a custom icon at run-time by using the [**CreateIconIndirect**](/windows/desktop/api/Winuser/nf-winuser-createiconindirect) function, which creates an icon based on the contents of an [**ICONINFO**](/windows/desktop/api/Winuser/ns-winuser-iconinfo) structure. The [**GetIconInfo**](/windows/desktop/api/Winuser/nf-winuser-geticoninfo) function fills the structure with the information about the bitmask bitmap and color bitmap for the icon.

Applications should implement custom icons as resources and should use [**LoadIcon**](/windows/desktop/api/Winuser/nf-winuser-loadiconw) or [**LoadImage**](/windows/desktop/api/Winuser/nf-winuser-loadimagew), rather than create the icon at run-time. Using icon resources avoids device dependence, simplifies localization, and enables applications to share icon shapes.

The [**CreateIconFromResourceEx**](/windows/desktop/api/Winuser/nf-winuser-createiconfromresourceex) function enables an application to browse through the system's resources and create icons and cursors based on resource data. **CreateIconFromResourceEx** creates an icon based on binary resource data from other executable files or DLLs. An application must precede this function with calls to the [**LookupIconIdFromDirectoryEx**](/windows/desktop/api/Winuser/nf-winuser-lookupiconidfromdirectoryex) function and several of the resource functions. **LookupIconIdFromDirectoryEx** returns the identifier of the most appropriate icon data for the current display device.

## Icon Display

You can retrieve the image for an icon by using the [**GetIconInfo**](/windows/desktop/api/Winuser/nf-winuser-geticoninfo) function, and can draw it by using the [**DrawIconEx**](/windows/desktop/api/Winuser/nf-winuser-drawiconex) function.

When the system displays an icon, it must extract the appropriate icon image from the .exe or .dll file. The system uses the following steps to select the icon image:

1.  Select the `RT_GROUP_ICON` resource. If more than one such resource exists, the system uses the first resource listed in the resource scrip.
2.  Select the appropriate `RT_ICON` image from the `RT_GROUP_ICON` resource. If more than one image exists, the system uses the following criteria to choose an image:
    -   The image closest in size to the requested size is chosen.
    -   If two or more images of that size are present, the one that matches the color depth of the display is chosen.
    -   If no images exactly match the color depth of the display, the image with the greatest color depth that does not exceed the color depth of the display is chosen. If all exceed the color depth, the one with the lowest color depth is chosen.

> [!Note]  
> The system treats all color depths of 8 or more bpp as equal. Therefore, there is no advantage of including a 16x16 256-color image and a 16x16 16-color image in the same resource—the system will simply choose the first one it encounters. When the display is in 8-bpp mode, the system will choose a 16-color icon over a 256-color icon, and will display all icons using the system default palette.

To display an animated icon, use a static control as shown in the following code fragment.

```cpp
hIcon = LoadImage(NULL, "ico.ani", IMAGE_ICON, 0, 0, LR_LOADFROMFILE);
SendMessage(hStatic, STM_SETIMAGE, IMAGE_ICON, (LPARAM)(UINT)hIcon);
```

## Icon Destruction

When an application no longer needs an icon it created by using the [**CreateIconIndirect**](/windows/desktop/api/Winuser/nf-winuser-createiconindirect) function, it should destroy the icon. The [**DestroyIcon**](/windows/desktop/api/Winuser/nf-winuser-destroyicon) function destroys the icon handle and frees any memory used by the icon. Applications should use this function only for icons created with **CreateIconIndirect**; it is not necessary to destroy other icons.

## Icon Duplication

The [**CopyIcon**](/windows/desktop/api/Winuser/nf-winuser-copyicon) function copies an icon handle. This enables an application or DLL to get its own handle to an icon owned by another module. Then, if the other module is freed, the application that copied the icon will still be able to use the icon.

The [**CopyImage**](/windows/desktop/api/Winuser/nf-winuser-copyimage) function creates a new icon based on the specified source icon. The new icon can be larger or smaller than the source icon.

For information about adding, removing, or replacing icon resources in executable (.exe) files, see [Resources](resources.md).

The [**DuplicateIcon**](/windows/desktop/api/Shellapi/nf-shellapi-duplicateicon) function makes an actual copy of the icon.

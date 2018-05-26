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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About Icons

The system uses icons throughout the user interface to represent objects such as files, folders, shortcuts, applications, and documents. The icon functions enable applications to create, load, display, arrange, animate, and destroy icons. For information on specifying icons for file types, see [**ExtractIcon**](/windows/win32/Shellapi/nf-shellapi-extracticona?branch=master).

This overview provides information on the following topics:

-   [Icon Hot Spot](#icon-hot-spot)
-   [Icon Types](#icon-types)
-   [Icon Sizes](#icon-sizes)
    -   [To change the size of the system small icon](#to-change-the-size-of-the-system-small-icon)
    -   [To retrieve the size of the system small icon](#to-retrieve-the-size-of-the-system-small-icon)
    -   [To retrieve the size of the system large icon](#to-retrieve-the-size-of-the-system-large-icon)
    -   [To retrieve the size of the shell small icon](#to-retrieve-the-size-of-the-shell-small-icon)
    -   [To change the size of the large icon](#to-change-the-size-of-the-large-icon)
    -   [To retrieve the size of the shell large icon](#to-retrieve-the-size-of-the-shell-large-icon)
-   [Icon Creation](#icon-creation)
-   [Icon Display](#icon-display)
-   [Icon Destruction](#icon-destruction)
-   [Icon Duplication](#icon-duplication)

## Icon Hot Spot

One of the pixels in an icon is designated as the [hot spot](#icon-hot-spot), which is the point the system tracks and recognizes as the position of the icon. An icon's hot spot is typically the pixel located at the center of the icon. If you use the [**CreateIconIndirect**](/windows/win32/Winuser/nf-winuser-createiconindirect?branch=master) function to create an icon, you can specify any pixel to be the hot spot.

## Icon Types

The operating system provides a set of *standard icons* that are available for any application to use at any time. The software development kit (SDK) header files contain identifiers for the standard icons—the identifiers begin with the **IDI\_** prefix.

Each standard icon has a corresponding default image associated with it. The user can replace the default image associated with any standard cursor at any time.

*Custom icons* are designed for use in a particular application and can be any design. Following are several custom icons.

![several custom icons](images/csicn-02.png)

## Icon Sizes

The system uses four icon sizes:

-   System small
-   System large
-   Shell small
-   Shell large

The *system small icon* is displayed in the window caption.

### To change the size of the system small icon

1.  From Control Panel, click **Display**, then click the **Appearance** tab.
2.  Select **Caption Buttons** from the **Item** list, then set the **Size** field.

### To retrieve the size of the system small icon

-   Call the [**GetSystemMetrics**](https://msdn.microsoft.com/library/windows/desktop/ms724385) function with **SM\_CXSMICON** and **SM\_CYSMICON**.

The *system large icon* is mainly used by applications, but it is also displayed in the Alt+Tab dialog. The [**CreateIconFromResource**](/windows/win32/Winuser/nf-winuser-createiconfromresource?branch=master), [**DrawIcon**](/windows/win32/Winuser/nf-winuser-drawicon?branch=master), [**ExtractAssociatedIcon**](/windows/win32/Shellapi/nf-shellapi-extractassociatedicona?branch=master), [**ExtractIcon**](/windows/win32/Shellapi/nf-shellapi-extracticona?branch=master), [**ExtractIconEx**](/windows/win32/Shellapi/nf-shellapi-extracticonexa?branch=master), and [**LoadIcon**](/windows/win32/Winuser/nf-winuser-loadicona?branch=master) functions all use system large icons. The size of the system large icon is defined by the video driver, therefore it cannot be changed.

### To retrieve the size of the system large icon

-   Call [**GetSystemMetrics**](https://msdn.microsoft.com/library/windows/desktop/ms724385) with **SM\_CXICON** and **SM\_CYICON**.

The [**CreateIcon**](/windows/win32/Winuser/nf-winuser-createicon?branch=master), [**CreateIconFromResourceEx**](/windows/win32/Winuser/nf-winuser-createiconfromresourceex?branch=master), [**CreateIconIndirect**](/windows/win32/Winuser/nf-winuser-createiconindirect?branch=master), and [**SHGetFileInfo**](_win32_SHGetFileInfo) functions can be used to work with icons in sizes other than system large.

The *shell small icon* is used in the Windows Explorer and the common dialogs. Currently, this defaults to the system small size.

### To retrieve the size of the shell small icon

1.  Use the [SHGetFileInfo](http://msdn.microsoft.com/library/Bb762179(VS.85).aspx) function with `SHGFI_SHELLICONSIZE | SHGFI_SMALLICON` to retrieve a handle to the system image list.
2.  Then call the [**ImageList\_GetIconSize**](_win32_ImageList_GetIconSize) function to get the icon size.

The shell large icon is used on the desktop.

### To change the size of the large icon

1.  From Control Panel , click **Display**, then click the **Appearance** tab,
2.  Select **Icon** from the **Item** list, then set the **Size** field (this size is stored in the registry, under **HKEY\_CURRENT\_USER\\Control Panel, Desktop\\WindowMetrics\\Shell Icon Size**).
3.  Click the **Plus!** tab and then select the **Use Large Icons** check box.

### To retrieve the size of the shell large icon

1.  Use the [**SHGetFileInfo**](_win32_SHGetFileInfo) function with **SHGFI\_SHELLICONSIZE** to retrieve a handle to the system image list.
2.  Then call the [**ImageList\_GetIconSize**](_win32_ImageList_GetIconSize) function to get the icon size.

The Start menu uses either shell small icons or shell large icons, depending on whether the **Use Large Icons** check box is selected.

Your application should supply groups of icon images in the following sizes:

-   48x48, 256 color
-   32x32, 16 color
-   16x16 pixels, 16 color

When filling in the [**WNDCLASSEX**](https://msdn.microsoft.com/library/windows/desktop/ms633577) structure to be used in registering your window class, set the **hIcon** member to the 32x32 icon and the **hIconSm** member to the 16x16 icon. For more information about class icons, see [Class Icons](https://msdn.microsoft.com/library/windows/desktop/ms633574#class-icons).

## Icon Creation

Standard icons are predefined, so it is not necessary to create them. To use a standard icon, an application can obtain its handle by using the [**LoadImage**](/windows/win32/Winuser/nf-winuser-loadimagea?branch=master) function. An *icon handle* is a unique value of the **HICON** type that identifies a standard or custom icon.

To create a custom icon for an application, you would typically use a graphics application and include the [ICON Resource](_Tools_ICON_Resource) in the application's resource-definition file. At run-time, you can call [**LoadIcon**](/windows/win32/Winuser/nf-winuser-loadicona?branch=master) or [**LoadImage**](/windows/win32/Winuser/nf-winuser-loadimagea?branch=master) to retrieve a handle to the icon. An icon resource can contain a group of images for several different display devices. **LoadIcon** and **LoadImage** automatically select the most appropriate icon from the group for the current display device.

An application can also create a custom icon at run-time by using the [**CreateIconIndirect**](/windows/win32/Winuser/nf-winuser-createiconindirect?branch=master) function, which creates an icon based on the contents of an [**ICONINFO**](/windows/win32/Winuser/ns-winuser-_iconinfo?branch=master) structure. The [**GetIconInfo**](/windows/win32/Winuser/nf-winuser-geticoninfo?branch=master) function fills the structure with the hot-spot coordinates and information about the bitmask bitmap and color bitmap for the icon.

Applications should implement custom icons as resources and should use [**LoadIcon**](/windows/win32/Winuser/nf-winuser-loadicona?branch=master) or [**LoadImage**](/windows/win32/Winuser/nf-winuser-loadimagea?branch=master), rather than create the icon at run-time. Using icon resources avoids device dependence, simplifies localization, and enables applications to share icon shapes.

The [**CreateIconFromResourceEx**](/windows/win32/Winuser/nf-winuser-createiconfromresourceex?branch=master) function enables an application to browse through the system's resources and create icons and cursors based on resource data. **CreateIconFromResourceEx** creates an icon based on binary resource data from other executable files or DLLs. An application must precede this function with calls to the [**LookupIconIdFromDirectoryEx**](/windows/win32/Winuser/nf-winuser-lookupiconidfromdirectoryex?branch=master) function and several of the resource functions. **LookupIconIdFromDirectoryEx** returns the identifier of the most appropriate icon data for the current display device.

## Icon Display

You can retrieve the image for an icon by using the [**GetIconInfo**](/windows/win32/Winuser/nf-winuser-geticoninfo?branch=master) function, and can draw it by using the [**DrawIconEx**](/windows/win32/Winuser/nf-winuser-drawiconex?branch=master) function. To draw the default image for a icon, specify the **DI\_COMPAT** flag in the call to **DrawIconEx**. If you do not specify the **DI\_COMPAT** flag, **DrawIconEx** draws the icon using the image that the user specified.

When the system displays an icon, it must extract the appropriate icon image from the .exe or .dll file. The system uses the following steps to select the icon image:

1.  Select the **RT\_GROUP\_ICON** resource. If more than one such resource exists, the system uses the first resource listed in the resource scrip.
2.  Select the appropriate **RT\_ICON** image from the **RT\_GROUP\_ICON** resource. If more than one image exists, the system uses the following criteria to choose an image:
    -   -   The image closest in size to the requested size is chosen.
        -   If two or more images of that size are present, the one that matches the color depth of the display is chosen.
        -   If no images exactly match the color depth of the display, the image with the greatest color depth that does not exceed the color depth of the display is chosen. If all exceed the color depth, the one with the lowest color depth is chosen.

> [!Note]  
> The system treats all color depths of 8 or more bpp as equal. Therefore, there is no advantage of including a 16x16 256-color image and a 16x16 16-color image in the same resource—the system will simply choose the first one it encounters. When the display is in 8-bpp mode, the system will choose a 16-color icon over a 256-color icon, and will display all icons using the system default palette.

 

To display an animated icon, use a static control as shown in the following code fragment.


```
hIcon = LoadImage(NULL, "ico.ani", IMAGE_ICON, 0, 0, LR_LOADFROMFILE);
SendMessage( hStatic, STM_SETIMAGE, IMAGE_ICON, (LPARAM)(UINT)hIcon);
```



## Icon Destruction

When an application no longer needs an icon it created by using the [**CreateIconIndirect**](/windows/win32/Winuser/nf-winuser-createiconindirect?branch=master) function, it should destroy the icon. The [**DestroyIcon**](/windows/win32/Winuser/nf-winuser-destroyicon?branch=master) function destroys the icon handle and frees any memory used by the icon. Applications should use this function only for icons created with **CreateIconIndirect**; it is not necessary to destroy other icons.

## Icon Duplication

The [**CopyIcon**](/windows/win32/Winuser/nf-winuser-copyicon?branch=master) function copies an icon handle. This enables an application or DLL to get its own handle to an icon owned by another module. Then, if the other module is freed, the application that copied the icon will still be able to use the icon.

The [**CopyImage**](/windows/win32/Winuser/nf-winuser-copyimage?branch=master) function creates a new icon based on the specified source icon. The new icon can be larger or smaller than the source icon.

For information about adding, removing, or replacing icon resources in executable (.exe) files, see [Resources](resources.md).

The [**DuplicateIcon**](/windows/win32/Shellapi/nf-shellapi-duplicateicon?branch=master) function makes an actual copy of the icon.

 

 





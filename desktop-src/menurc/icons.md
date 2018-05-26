---
title: Icons
description: This section discusses icons which are bitmap images combined with a mask to create transparent areas in the picture.
ms.assetid: 67867460-07f6-460f-9263-05bbf3474744
keywords:
- resources,icons
- icons,about
- RT_ICON resource
- RT_GROUP_ICON resource
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Icons

An *icon* is a picture that consists of a bitmap image combined with a mask to create transparent areas in the picture. The term icon can refer to either of the following:

-   A single icon image. This is a resource of type **RT\_ICON**.
-   A group of images, from which the system or an application can choose the most appropriate icon based on size and color depth. This is a resource of type **RT\_GROUP\_ICON**.

### In This Section



| Name                                 | Description                                                 |
|--------------------------------------|-------------------------------------------------------------|
| [About Icons](about-icons.md)       | Discusses icons.<br/>                                 |
| [Using Icons](using-icons.md)       | Discusses how to perform tasks related to icons.<br/> |
| [Icon Reference](icon-reference.md) | Contains the API reference.<br/>                      |



 

### Icon Functions



| Name                                                               | Description                                                                                                                                                                                                           |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CopyIcon**](/windows/win32/Winuser/nf-winuser-copyicon?branch=master)                                       | Copies the specified icon from another module to the current module. <br/>                                                                                                                                      |
| [**CreateIcon**](/windows/win32/Winuser/nf-winuser-createicon?branch=master)                                   | Creates an icon that has the specified size, colors, and bit patterns. <br/>                                                                                                                                    |
| [**CreateIconFromResource**](/windows/win32/Winuser/nf-winuser-createiconfromresource?branch=master)           | Creates an icon or cursor from resource bits describing the icon.<br/>                                                                                                                                          |
| [**CreateIconFromResourceEx**](/windows/win32/Winuser/nf-winuser-createiconfromresourceex?branch=master)       | Creates an icon or cursor from resource bits describing the icon. <br/>                                                                                                                                         |
| [**CreateIconIndirect**](/windows/win32/Winuser/nf-winuser-createiconindirect?branch=master)                   | Creates an icon or cursor from an [**ICONINFO**](/windows/win32/Winuser/ns-winuser-_iconinfo?branch=master) structure. <br/>                                                                                                                                 |
| [**DestroyIcon**](/windows/win32/Winuser/nf-winuser-destroyicon?branch=master)                                 | Destroys an icon and frees any memory the icon occupied. <br/>                                                                                                                                                  |
| [**DrawIcon**](/windows/win32/Winuser/nf-winuser-drawicon?branch=master)                                       | Draws an icon or cursor into the specified device context.<br/>                                                                                                                                                 |
| [**DrawIconEx**](/windows/win32/Winuser/nf-winuser-drawiconex?branch=master)                                   | Draws an icon or cursor into the specified device context, performing the specified raster operations, and stretching or compressing the icon or cursor as specified. <br/>                                     |
| [**DuplicateIcon**](/windows/win32/Shellapi/nf-shellapi-duplicateicon?branch=master)                             | Creates a duplicate of a specified icon.<br/>                                                                                                                                                                   |
| [**ExtractAssociatedIcon**](/windows/win32/Shellapi/nf-shellapi-extractassociatedicona?branch=master)             | Retrieves a handle to an indexed icon found in a file or an icon found in an associated executable file. <br/>                                                                                                  |
| [**ExtractIcon**](/windows/win32/Shellapi/nf-shellapi-extracticona?branch=master)                                 | Retrieves a handle to an icon from the specified executable file,DLL, or icon file.<br/>                                                                                                                        |
| [**ExtractIconEx**](/windows/win32/Shellapi/nf-shellapi-extracticonexa?branch=master)                             | Creates an array of handles to large or small icons extracted from the specified executable file, DLL, or icon file. <br/>                                                                                      |
| [**GetIconInfo**](/windows/win32/Winuser/nf-winuser-geticoninfo?branch=master)                                 | Retrieves information about the specified icon or cursor. <br/>                                                                                                                                                 |
| [**GetIconInfoEx**](/windows/win32/Winuser/nf-winuser-geticoninfoexa?branch=master)                             | Retrieves information about the specified icon or cursor. [**GetIconInfoEx**](/windows/win32/Winuser/nf-winuser-geticoninfoexa?branch=master) extends [**GetIconInfo**](/windows/win32/Winuser/nf-winuser-geticoninfo?branch=master) by using the newer [**ICONINFOEX**](/windows/win32/Winuser/ns-winuser-_iconinfoexa?branch=master) structure.<br/> |
| [**LoadIcon**](/windows/win32/Winuser/nf-winuser-loadicona?branch=master)                                       | Loads the specified icon resource from the executable (.exe) file associated with an application instance.<br/>                                                                                                 |
| [**LookupIconIdFromDirectory**](/windows/win32/Winuser/nf-winuser-lookupiconidfromdirectory?branch=master)     | Searches through icon or cursor data for the icon or cursor that best fits the current display device.<br/>                                                                                                     |
| [**LookupIconIdFromDirectoryEx**](/windows/win32/Winuser/nf-winuser-lookupiconidfromdirectoryex?branch=master) | Searches through icon or cursor data for the icon or cursor that best fits the current display device. <br/>                                                                                                    |
| [**PrivateExtractIcons**](/windows/win32/Winuser/nf-winuser-privateextracticonsa?branch=master)                 | Creates an array of handles to icons that are extracted from a specified file.<br/>                                                                                                                             |



 

### Icon Structures



| Name                               | Description                                                                                                                                                                                                                                     |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICONINFO**](/windows/win32/Winuser/ns-winuser-_iconinfo?branch=master)       | Contains information about an icon or a cursor. <br/>                                                                                                                                                                                     |
| [**ICONINFOEX**](/windows/win32/Winuser/ns-winuser-_iconinfoexa?branch=master)   | Contains information about an icon or a cursor. Extends [**ICONINFO**](/windows/win32/Winuser/ns-winuser-_iconinfo?branch=master). Used by [**GetIconInfoEx**](/windows/win32/Winuser/nf-winuser-geticoninfoexa?branch=master).<br/>                                                                                                |
| [**ICONMETRICS**](/windows/win32/Winuser/ns-winuser-tagiconmetricsa?branch=master) | Contains the scalable metrics associated with icons. This structure is used with the [**SystemParametersInfo**](https://msdn.microsoft.com/library/windows/desktop/ms724947) function when the **SPI\_GETICONMETRICS** or **SPI\_SETICONMETRICS** action is specified.<br/> |



 

 

 






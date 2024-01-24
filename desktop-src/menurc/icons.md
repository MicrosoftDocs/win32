---
title: Icons (Menus and Other Resources)
description: This section discusses icons which are bitmap images combined with a mask to create transparent areas in the picture.
ms.assetid: 'vs|winui|~\winui\windowsuserinterface\resources\icons.htm'
keywords:
- resources,icons
- icons,about
- RT_ICON resource
- RT_GROUP_ICON resource
ms.topic: article
ms.date: 05/31/2018
---

# Icons (Menus and Other Resources)

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
| [**CopyIcon**](/windows/desktop/api/Winuser/nf-winuser-copyicon)                                       | Copies the specified icon from another module to the current module. <br/>                                                                                                                                      |
| [**CreateIcon**](/windows/desktop/api/Winuser/nf-winuser-createicon)                                   | Creates an icon that has the specified size, colors, and bit patterns. <br/>                                                                                                                                    |
| [**CreateIconFromResource**](/windows/desktop/api/Winuser/nf-winuser-createiconfromresource)           | Creates an icon or cursor from resource bits describing the icon.<br/>                                                                                                                                          |
| [**CreateIconFromResourceEx**](/windows/desktop/api/Winuser/nf-winuser-createiconfromresourceex)       | Creates an icon or cursor from resource bits describing the icon. <br/>                                                                                                                                         |
| [**CreateIconIndirect**](/windows/desktop/api/Winuser/nf-winuser-createiconindirect)                   | Creates an icon or cursor from an [**ICONINFO**](/windows/desktop/api/Winuser/ns-winuser-iconinfo) structure. <br/>                                                                                                                                 |
| [**DestroyIcon**](/windows/desktop/api/Winuser/nf-winuser-destroyicon)                                 | Destroys an icon and frees any memory the icon occupied. <br/>                                                                                                                                                  |
| [**DrawIcon**](/windows/desktop/api/Winuser/nf-winuser-drawicon)                                       | Draws an icon or cursor into the specified device context.<br/>                                                                                                                                                 |
| [**DrawIconEx**](/windows/desktop/api/Winuser/nf-winuser-drawiconex)                                   | Draws an icon or cursor into the specified device context, performing the specified raster operations, and stretching or compressing the icon or cursor as specified. <br/>                                     |
| [**DuplicateIcon**](/windows/desktop/api/Shellapi/nf-shellapi-duplicateicon)                             | Creates a duplicate of a specified icon.<br/>                                                                                                                                                                   |
| [**ExtractAssociatedIcon**](/windows/desktop/api/Shellapi/nf-shellapi-extractassociatedicona)             | Retrieves a handle to an indexed icon found in a file or an icon found in an associated executable file. <br/>                                                                                                  |
| [**ExtractIcon**](/windows/desktop/api/Shellapi/nf-shellapi-extracticona)                                 | Retrieves a handle to an icon from the specified executable file,DLL, or icon file.<br/>                                                                                                                        |
| [**ExtractIconEx**](/windows/desktop/api/Shellapi/nf-shellapi-extracticonexa)                             | Creates an array of handles to large or small icons extracted from the specified executable file, DLL, or icon file. <br/>                                                                                      |
| [**GetIconInfo**](/windows/desktop/api/Winuser/nf-winuser-geticoninfo)                                 | Retrieves information about the specified icon or cursor. <br/>                                                                                                                                                 |
| [**GetIconInfoEx**](/windows/desktop/api/Winuser/nf-winuser-geticoninfoexa)                             | Retrieves information about the specified icon or cursor. [**GetIconInfoEx**](/windows/desktop/api/Winuser/nf-winuser-geticoninfoexa) extends [**GetIconInfo**](/windows/desktop/api/Winuser/nf-winuser-geticoninfo) by using the newer [**ICONINFOEX**](/windows/desktop/api/Winuser/ns-winuser-iconinfoexa) structure.<br/> |
| [**LoadIcon**](/windows/desktop/api/Winuser/nf-winuser-loadicona)                                       | Loads the specified icon resource from the executable (.exe) file associated with an application instance.<br/>                                                                                                 |
| [**LookupIconIdFromDirectory**](/windows/desktop/api/Winuser/nf-winuser-lookupiconidfromdirectory)     | Searches through icon or cursor data for the icon or cursor that best fits the current display device.<br/>                                                                                                     |
| [**LookupIconIdFromDirectoryEx**](/windows/desktop/api/Winuser/nf-winuser-lookupiconidfromdirectoryex) | Searches through icon or cursor data for the icon or cursor that best fits the current display device. <br/>                                                                                                    |
| [**PrivateExtractIcons**](/windows/desktop/api/Winuser/nf-winuser-privateextracticonsa)                 | Creates an array of handles to icons that are extracted from a specified file.<br/>                                                                                                                             |



 

### Icon Structures



| Name                               | Description                                                                                                                                                                                                                                     |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICONINFO**](/windows/desktop/api/Winuser/ns-winuser-iconinfo)       | Contains information about an icon or a cursor. <br/>                                                                                                                                                                                     |
| [**ICONINFOEX**](/windows/desktop/api/Winuser/ns-winuser-iconinfoexa)   | Contains information about an icon or a cursor. Extends [**ICONINFO**](/windows/desktop/api/Winuser/ns-winuser-iconinfo). Used by [**GetIconInfoEx**](/windows/desktop/api/Winuser/nf-winuser-geticoninfoexa).<br/>                                                                                                |
| [**ICONMETRICS**](/windows/win32/api/winuser/ns-winuser-iconmetricsa) | Contains the scalable metrics associated with icons. This structure is used with the [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) function when the **SPI\_GETICONMETRICS** or **SPI\_SETICONMETRICS** action is specified.<br/> |



 

 


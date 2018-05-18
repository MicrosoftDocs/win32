---
title: Icons
description: This section discusses icons which are bitmap images combined with a mask to create transparent areas in the picture.
ms.assetid: '67867460-07f6-460f-9263-05bbf3474744'
keywords: ["resources,icons", "icons,about", "RT_ICON resource", "RT_GROUP_ICON resource"]
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
| [**CopyIcon**](copyicon.md)                                       | Copies the specified icon from another module to the current module. <br/>                                                                                                                                      |
| [**CreateIcon**](createicon.md)                                   | Creates an icon that has the specified size, colors, and bit patterns. <br/>                                                                                                                                    |
| [**CreateIconFromResource**](createiconfromresource.md)           | Creates an icon or cursor from resource bits describing the icon.<br/>                                                                                                                                          |
| [**CreateIconFromResourceEx**](createiconfromresourceex.md)       | Creates an icon or cursor from resource bits describing the icon. <br/>                                                                                                                                         |
| [**CreateIconIndirect**](createiconindirect.md)                   | Creates an icon or cursor from an [**ICONINFO**](iconinfo.md) structure. <br/>                                                                                                                                 |
| [**DestroyIcon**](destroyicon.md)                                 | Destroys an icon and frees any memory the icon occupied. <br/>                                                                                                                                                  |
| [**DrawIcon**](drawicon.md)                                       | Draws an icon or cursor into the specified device context.<br/>                                                                                                                                                 |
| [**DrawIconEx**](drawiconex.md)                                   | Draws an icon or cursor into the specified device context, performing the specified raster operations, and stretching or compressing the icon or cursor as specified. <br/>                                     |
| [**DuplicateIcon**](duplicateicon.md)                             | Creates a duplicate of a specified icon.<br/>                                                                                                                                                                   |
| [**ExtractAssociatedIcon**](extractassociatedicon.md)             | Retrieves a handle to an indexed icon found in a file or an icon found in an associated executable file. <br/>                                                                                                  |
| [**ExtractIcon**](extracticon.md)                                 | Retrieves a handle to an icon from the specified executable file,DLL, or icon file.<br/>                                                                                                                        |
| [**ExtractIconEx**](extracticonex.md)                             | Creates an array of handles to large or small icons extracted from the specified executable file, DLL, or icon file. <br/>                                                                                      |
| [**GetIconInfo**](geticoninfo.md)                                 | Retrieves information about the specified icon or cursor. <br/>                                                                                                                                                 |
| [**GetIconInfoEx**](geticoninfoex.md)                             | Retrieves information about the specified icon or cursor. [**GetIconInfoEx**](geticoninfoex.md) extends [**GetIconInfo**](geticoninfo.md) by using the newer [**ICONINFOEX**](iconinfoex.md) structure.<br/> |
| [**LoadIcon**](loadicon.md)                                       | Loads the specified icon resource from the executable (.exe) file associated with an application instance.<br/>                                                                                                 |
| [**LookupIconIdFromDirectory**](lookupiconidfromdirectory.md)     | Searches through icon or cursor data for the icon or cursor that best fits the current display device.<br/>                                                                                                     |
| [**LookupIconIdFromDirectoryEx**](lookupiconidfromdirectoryex.md) | Searches through icon or cursor data for the icon or cursor that best fits the current display device. <br/>                                                                                                    |
| [**PrivateExtractIcons**](privateextracticons.md)                 | Creates an array of handles to icons that are extracted from a specified file.<br/>                                                                                                                             |



 

### Icon Structures



| Name                               | Description                                                                                                                                                                                                                                     |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICONINFO**](iconinfo.md)       | Contains information about an icon or a cursor. <br/>                                                                                                                                                                                     |
| [**ICONINFOEX**](iconinfoex.md)   | Contains information about an icon or a cursor. Extends [**ICONINFO**](iconinfo.md). Used by [**GetIconInfoEx**](geticoninfoex.md).<br/>                                                                                                |
| [**ICONMETRICS**](iconmetrics.md) | Contains the scalable metrics associated with icons. This structure is used with the [**SystemParametersInfo**](https://msdn.microsoft.com/library/windows/desktop/ms724947) function when the **SPI\_GETICONMETRICS** or **SPI\_SETICONMETRICS** action is specified.<br/> |



 

 

 






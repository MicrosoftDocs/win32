---
title: Resource File Formats
description: This section describes the format of the binary resource file that the resource compiler creates based on the contents of the resource-definition file.
ms.assetid: a0b17555-f50a-4d58-b2bc-760843dd67eb
ms.topic: article
ms.date: 05/31/2018
---

# Resource File Formats

This section describes the format of the binary resource file that the resource compiler creates based on the contents of the resource-definition file. This file usually has an .res extension. The linker reformats the .res file into a resource object file and then links it to the executable file of an application.

A binary resource file consists of a number of concatenated resource entries. Each entry consists of a resource header and the data for that resource. A resource header is **DWORD**-aligned in the file and consists of the following:

-   A **DWORD** that contains the size of the resource header
-   A **DWORD** that contains the size of the resource data
-   The resource type
-   The resource name
-   Additional resource information

The [**RESOURCEHEADER**](resourceheader.md) structure describes the format of this header. The data for the resource follows the resource header and is specific to each type of resource. Some resources also employ a resource-specific group header structure to provide information about a group of resources.

## Accelerator Table Resources

An accelerator table is one resource entry in a resource file. It does not have a group header. An [**ACCELTABLEENTRY**](acceltableentry.md) structure describes each entry in the accelerator table. Multiple accelerator tables are permitted.

## Cursor and Icon Resources

The system handles each icon and cursor as a single file. However, these are stored in .res files and in executable files as a group of [RT\_GROUP\_ICON](/windows/desktop/menurc/resource-types) icon resources  or a [RT\_GROUP\_CURSOR](/windows/desktop/menurc/resource-types) group of cursor resources. The file formats of icon and cursor resources are similar. In the .res file a resource group header follows all of the individual icon or cursor group components.

The group header for both icon and cursor resources consists of a [**NEWHEADER**](newheader.md) structure plus one or more [**RESDIR**](resdir.md) structures. There is one [**RESDIR**](resdir.md) structure for each icon or cursor. The group header contains the information an application needs to select the correct icon or cursor to display. Both the group header and the data that repeats for each icon or cursor in the group have a fixed length. This allows the application to randomly access the information.

The format of each [RT\_ICON](/windows/desktop/menurc/resource-types) icon or [RT\_CURSOR](/windows/desktop/menurc/resource-types) cursor resource component closely resembles the format of the .ico/.cur file. Each image is stored in a [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfo) structure followed by the color device-independent bitmap (DIB) bits of the icon's **XOR** mask. The monochrome DIB bits of the **AND** mask follow the color DIB bits. Significant difference between cursors and icons is that cursors have a [**LOCALHEADER**](localheader.md) structure with a hotspot inserted before the bitmap data, while icons do not.

Since Windows Vista [RT\_ICON](/windows/desktop/menurc/resource-types) icon or [RT\_CURSOR](/windows/desktop/menurc/resource-types) cursor resource may contain PNG-compressed image data.

## Dialog Box Resources

A dialog box is also one resource entry in the resource file. It consists of one [**DLGTEMPLATE**](/windows/desktop/api/winuser/ns-winuser-dlgtemplate) dialog box header structure plus one [**DLGITEMTEMPLATE**](/windows/desktop/api/winuser/ns-winuser-dlgitemtemplate) structure for each control in the dialog box. The [**DLGTEMPLATEEX**](/windows/desktop/dlgbox/dlgtemplateex) and the [**DLGITEMTEMPLATEEX**](/windows/desktop/dlgbox/dlgitemtemplateex) structures describe the format of extended dialog box resources.

## Font Resources

Fonts are stored in the resource file as a group of resources. Individual fonts make up a font group. A [FONT Statement](./font-statement.md) resource definition statement in the .RC file defines each font. Each individual font in the resource consists of the complete contents of the related .fnt file. A [**FONTGROUPHDR**](fontgrouphdr.md) structure follows all the individual font components in the .res file.

Font resources are not added to the resources of a specific application. Instead, they are normally added to executable files that have a .fon extension. These files are usually resource-only DLLs rather than applications.

## Menu Resources

A *menu resource* consists of a [**MENUHEADER**](menuheader.md) structure followed by one or more [**NORMALMENUITEM**](normalmenuitem.md) or [**POPUPMENUITEM**](popupmenuitem.md) structures, one for each menu item in the menu template. The [**MENUEX\_TEMPLATE\_HEADER**](menuex-template-header.md) and the [**MENUEX\_TEMPLATE\_ITEM**](menuex-template-item.md) structures describe the format of extended menu resources.

## Message Table Resources

A *message table* is a resource that contains formatted text for display as an error message or in a message box. The main structure in a message table resource is the [**MESSAGE\_RESOURCE\_DATA**](/windows/desktop/api/Winnt/ns-winnt-message_resource_data) structure.

## Version Resources

The main structure in a version resource is the [**VS\_FIXEDFILEINFO**](/windows/win32/api/verrsrc/ns-verrsrc-vs_fixedfileinfo) structure. Additional structures include the [**VarFileInfo**](varfileinfo.md) structure to store language information data, and [**StringFileInfo**](stringfileinfo.md) for user-defined string information. All strings in a version resource are in Unicode format. Each block of information is aligned on a **DWORD** boundary.

 

 

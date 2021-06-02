---
description: 'You can use the handle to an enhanced metafile to accomplish the following tasks:'
ms.assetid: 8f887c38-6cfa-4918-aa44-dd5fb837b40b
title: Enhanced Metafile Operations
ms.topic: article
ms.date: 05/31/2018
---

# Enhanced Metafile Operations

You can use the handle to an enhanced metafile to accomplish the following tasks:

-   Display the picture stored in an enhanced metafile.
-   Create copies of an enhanced metafile.
-   Edit an enhanced metafile.
-   Retrieve the optional description stored in an enhanced metafile.
-   Retrieve a copy of an enhanced-metafile header.
-   Retrieve a binary version of an enhanced metafile.
-   Enumerate the colors in the optional palette.

These tasks are discussed in the sections in the remainder of this topic.

## Display the Picture Stored in an Enhanced Metafile

You can display the picture stored in an enhanced metafile using the [**PlayEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-playenhmetafile) function. Pass the function a handle to the enhanced metafile, without being concerned with the format of the enhanced metafile records. However, it is sometimes desirable to enumerate the records in the enhanced metafile to search for a particular GDI function and modify the parameters of the function in some manner. To do this, you can use [**EnumEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-enumenhmetafile) and provide a callback function, [**EnhMetaFileProc**](/windows/win32/api/wingdi/nc-wingdi-enhmfenumproc), to process the enhanced metafile records. To modify the parameters for an enhanced metafile record, you must know the format of the parameters within the record.

## Create Copies of an Enhanced Metafile

Some applications create temporary backup (or duplicate) copies of a file before enabling the user to alter the original. An application can create a backup copy of an enhanced metafile by calling the [**CopyEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-copyenhmetafilea) function, supplying a handle that identifies the enhanced metafile, and supplying a pointer to the name of the new file.

To create a memory-based enhanced-format metafile, call the [**SetEnhMetaFileBits**](/windows/desktop/api/Wingdi/nf-wingdi-setenhmetafilebits) function.

## Edit an Enhanced Metafile

Most drawing, illustration, and computer-aided design (CAD) applications require a means of editing a picture stored in an enhanced metafile. Although editing an enhanced metafile is a complex task, you can use the [**EnumEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-enumenhmetafile) function in combination with other functions to provide this capability in your application. The **EnumEnhMetaFile** function and its associated callback function, [**EnhMetaFileProc**](/windows/win32/api/wingdi/nc-wingdi-enhmfenumproc), enable the application to process individual records in an enhanced metafile.

## Retrieve the Optional Description Stored in an Enhanced Metafile

Some applications display the text description of an enhanced metafile with the corresponding file name in the **Open** dialog box. You can determine whether this string exists in an enhanced metafile by retrieving the metafile header with the [**GetEnhMetaFileHeader**](/windows/desktop/api/Wingdi/nf-wingdi-getenhmetafileheader) function and examining one of its members. If the string exists, the application retrieves it by calling the [**GetEnhMetaFileDescription**](/windows/desktop/api/Wingdi/nf-wingdi-getenhmetafiledescriptiona) function.

## Retrieve a Binary Version of an Enhanced Metafile

You can retrieve the contents of a metafile by calling the [**GetEnhMetaFileBits**](/windows/desktop/api/Wingdi/nf-wingdi-getenhmetafilebits) function; however, before retrieving the contents, you must specify the size of the file. To get the size, you can use the [**GetEnhMetaFileHeader**](/windows/desktop/api/Wingdi/nf-wingdi-getenhmetafileheader) function and examine the appropriate member.

## Enumerate the Colors in the Optional Palette

To achieve consistent colors when a picture is displayed on various output devices, you can call the [**CreatePalette**](/windows/desktop/api/Wingdi/nf-wingdi-createpalette) function and store a logical palette in an enhanced metafile. An application that displays the picture stored in the enhanced metafile retrieves this palette and calls the [**RealizePalette**](/windows/desktop/api/Wingdi/nf-wingdi-realizepalette) function before displaying the picture. To determine whether a palette is stored in an enhanced metafile, retrieve the metafile header and examine the appropriate member. If a palette exists, you can call the [**GetEnhMetaFilePaletteEntries**](/windows/desktop/api/Wingdi/nf-wingdi-getenhmetafilepaletteentries) function to retrieve the logical palette.

 

 

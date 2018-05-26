---
Description: The following functions are used with enhanced-format metafiles.
ms.assetid: 93a17a8c-308b-4442-933e-fedc8b9a84b0
title: Metafile Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Metafile Functions

The following functions are used with enhanced-format metafiles.



| Function                                                             | Description                                                                                                            |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**CloseEnhMetaFile**](/windows/win32/Wingdi/nf-wingdi-closeenhmetafile?branch=master)                         | Closes an enhanced-metafile device context.                                                                            |
| [**CopyEnhMetaFile**](/windows/win32/Wingdi/nf-wingdi-copyenhmetafilea?branch=master)                           | Copies the contents of an enhanced-format metafile to a specified file.                                                |
| [**CreateEnhMetaFile**](/windows/win32/Wingdi/nf-wingdi-createenhmetafilea?branch=master)                       | Creates a device context for an enhanced-format metafile.                                                              |
| [**DeleteEnhMetaFile**](/windows/win32/Wingdi/nf-wingdi-deleteenhmetafile?branch=master)                       | Deletes an enhanced-format metafile or an enhanced-format metafile handle.                                             |
| [**EnhMetaFileProc**](enhmetafileproc.md)                           | An application-defined callback function used with the EnumEnhMetaFile function.                                       |
| [**EnumEnhMetaFile**](/windows/win32/Wingdi/nf-wingdi-enumenhmetafile?branch=master)                           | Enumerates the records within an enhanced-format metafile.                                                             |
| [**GdiComment**](/windows/win32/Wingdi/nf-wingdi-gdicomment?branch=master)                                     | Copies a comment from a buffer into a specified enhanced-format metafile.                                              |
| [**GetEnhMetaFile**](/windows/win32/WinGdi/nf-wingdi-getenhmetafilea?branch=master)                             | Creates a handle that identifies the enhanced-format metafile stored in the specified file.                            |
| [**GetEnhMetaFileBits**](/windows/win32/Wingdi/nf-wingdi-getenhmetafilebits?branch=master)                     | Retrieves the contents of the specified enhanced-format metafile and copies them into a buffer.                        |
| [**GetEnhMetaFileDescription**](/windows/win32/Wingdi/nf-wingdi-getenhmetafiledescriptiona?branch=master)       | Retrieves an optional text description from an enhanced-format metafile and copies the string to the specified buffer. |
| [**GetEnhMetaFileHeader**](/windows/win32/Wingdi/nf-wingdi-getenhmetafileheader?branch=master)                 | Retrieves the record containing the header for the specified enhanced-format metafile.                                 |
| [**GetEnhMetaFilePaletteEntries**](/windows/win32/Wingdi/nf-wingdi-getenhmetafilepaletteentries?branch=master) | Retrieves optional palette entries from the specified enhanced metafile.                                               |
| [**GetMetaFile**](/windows/win32/Wingdi/nf-wingdi-getmetafilea?branch=master)                                   | GetMetaFile is no longer available for use as of Windows 2000. Instead, use [**GetEnhMetaFile**](/windows/win32/WinGdi/nf-wingdi-getenhmetafilea?branch=master).  |
| [**GetWinMetaFileBits**](/windows/win32/Wingdi/nf-wingdi-getwinmetafilebits?branch=master)                     | Converts the enhanced-format records from a metafile into Windows-format records.                                      |
| [**PlayEnhMetaFile**](/windows/win32/Wingdi/nf-wingdi-playenhmetafile?branch=master)                           | Displays the picture stored in the specified enhanced-format metafile.                                                 |
| [**PlayEnhMetaFileRecord**](/windows/win32/Wingdi/nf-wingdi-playenhmetafilerecord?branch=master)               | Plays an enhanced-metafile record by executing the graphics device interface (GDI) functions identified by the record. |
| [**SetEnhMetaFileBits**](/windows/win32/Wingdi/nf-wingdi-setenhmetafilebits?branch=master)                     | Creates a memory-based enhanced-format metafile from the specified data.                                               |
| [**SetWinMetaFileBits**](/windows/win32/Wingdi/nf-wingdi-setwinmetafilebits?branch=master)                     | Converts a metafile from the older Windows format to the new enhanced format.                                          |



 

## Obsolete Functions

The following functions are obsolete. The are provided for compatibility with Windows-format metafiles.

-   [**CloseMetaFile**](/windows/win32/Wingdi/nf-wingdi-closemetafile?branch=master)
-   [**CopyMetaFile**](/windows/win32/Wingdi/nf-wingdi-copymetafilea?branch=master)
-   [**CreateMetaFile**](/windows/win32/Wingdi/nf-wingdi-createmetafilea?branch=master)
-   [**DeleteMetaFile**](/windows/win32/Wingdi/nf-wingdi-deletemetafile?branch=master)
-   [**EnumMetaFile**](/windows/win32/Wingdi/nf-wingdi-enummetafile?branch=master)
-   [**EnumMetaFileProc**](enummetafileproc.md)
-   [**GetMetaFileBitsEx**](/windows/win32/Wingdi/nf-wingdi-getmetafilebitsex?branch=master)
-   [**PlayMetaFile**](/windows/win32/Wingdi/nf-wingdi-playmetafile?branch=master)
-   [**PlayMetaFileRecord**](/windows/win32/Wingdi/nf-wingdi-playmetafilerecord?branch=master)
-   [**SetMetaFileBitsEx**](/windows/win32/Wingdi/nf-wingdi-setmetafilebitsex?branch=master)

 

 




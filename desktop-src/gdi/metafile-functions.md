---
description: The following functions are used with enhanced-format metafiles.
ms.assetid: 93a17a8c-308b-4442-933e-fedc8b9a84b0
title: Metafile Functions
ms.topic: article
ms.date: 05/31/2018
---

# Metafile Functions

The following functions are used with enhanced-format metafiles.



| Function                                                             | Description                                                                                                            |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**CloseEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-closeenhmetafile)                         | Closes an enhanced-metafile device context.                                                                            |
| [**CopyEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-copyenhmetafilea)                           | Copies the contents of an enhanced-format metafile to a specified file.                                                |
| [**CreateEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-createenhmetafilea)                       | Creates a device context for an enhanced-format metafile.                                                              |
| [**DeleteEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-deleteenhmetafile)                       | Deletes an enhanced-format metafile or an enhanced-format metafile handle.                                             |
| [**EnhMetaFileProc**](/windows/win32/api/wingdi/nc-wingdi-enhmfenumproc)                           | An application-defined callback function used with the EnumEnhMetaFile function.                                       |
| [**EnumEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-enumenhmetafile)                           | Enumerates the records within an enhanced-format metafile.                                                             |
| [**GdiComment**](/windows/desktop/api/Wingdi/nf-wingdi-gdicomment)                                     | Copies a comment from a buffer into a specified enhanced-format metafile.                                              |
| [**GetEnhMetaFile**](/windows/desktop/api/WinGdi/nf-wingdi-getenhmetafilea)                             | Creates a handle that identifies the enhanced-format metafile stored in the specified file.                            |
| [**GetEnhMetaFileBits**](/windows/desktop/api/Wingdi/nf-wingdi-getenhmetafilebits)                     | Retrieves the contents of the specified enhanced-format metafile and copies them into a buffer.                        |
| [**GetEnhMetaFileDescription**](/windows/desktop/api/Wingdi/nf-wingdi-getenhmetafiledescriptiona)       | Retrieves an optional text description from an enhanced-format metafile and copies the string to the specified buffer. |
| [**GetEnhMetaFileHeader**](/windows/desktop/api/Wingdi/nf-wingdi-getenhmetafileheader)                 | Retrieves the record containing the header for the specified enhanced-format metafile.                                 |
| [**GetEnhMetaFilePaletteEntries**](/windows/desktop/api/Wingdi/nf-wingdi-getenhmetafilepaletteentries) | Retrieves optional palette entries from the specified enhanced metafile.                                               |
| [**GetMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-getmetafilea)                                   | GetMetaFile is no longer available for use as of Windows 2000. Instead, use [**GetEnhMetaFile**](/windows/desktop/api/WinGdi/nf-wingdi-getenhmetafilea).  |
| [**GetWinMetaFileBits**](/windows/desktop/api/Wingdi/nf-wingdi-getwinmetafilebits)                     | Converts the enhanced-format records from a metafile into Windows-format records.                                      |
| [**PlayEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-playenhmetafile)                           | Displays the picture stored in the specified enhanced-format metafile.                                                 |
| [**PlayEnhMetaFileRecord**](/windows/desktop/api/Wingdi/nf-wingdi-playenhmetafilerecord)               | Plays an enhanced-metafile record by executing the graphics device interface (GDI) functions identified by the record. |
| [**SetEnhMetaFileBits**](/windows/desktop/api/Wingdi/nf-wingdi-setenhmetafilebits)                     | Creates a memory-based enhanced-format metafile from the specified data.                                               |
| [**SetWinMetaFileBits**](/windows/desktop/api/Wingdi/nf-wingdi-setwinmetafilebits)                     | Converts a metafile from the older Windows format to the new enhanced format.                                          |



 

## Obsolete Functions

The following functions are obsolete. The are provided for compatibility with Windows-format metafiles.

-   [**CloseMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-closemetafile)
-   [**CopyMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-copymetafilea)
-   [**CreateMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-createmetafilea)
-   [**DeleteMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-deletemetafile)
-   [**EnumMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-enummetafile)
-   [**EnumMetaFileProc**](/windows/win32/api/wingdi/nc-wingdi-mfenumproc)
-   [**GetMetaFileBitsEx**](/windows/desktop/api/Wingdi/nf-wingdi-getmetafilebitsex)
-   [**PlayMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-playmetafile)
-   [**PlayMetaFileRecord**](/windows/desktop/api/Wingdi/nf-wingdi-playmetafilerecord)
-   [**SetMetaFileBitsEx**](/windows/desktop/api/Wingdi/nf-wingdi-setmetafilebitsex)

 

 

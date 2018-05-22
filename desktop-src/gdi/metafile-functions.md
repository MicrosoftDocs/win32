---
Description: 'The following functions are used with enhanced-format metafiles.'
ms.assetid: '93a17a8c-308b-4442-933e-fedc8b9a84b0'
title: Metafile Functions
---

# Metafile Functions

The following functions are used with enhanced-format metafiles.



| Function                                                             | Description                                                                                                            |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**CloseEnhMetaFile**](closeenhmetafile.md)                         | Closes an enhanced-metafile device context.                                                                            |
| [**CopyEnhMetaFile**](copyenhmetafile.md)                           | Copies the contents of an enhanced-format metafile to a specified file.                                                |
| [**CreateEnhMetaFile**](createenhmetafile.md)                       | Creates a device context for an enhanced-format metafile.                                                              |
| [**DeleteEnhMetaFile**](deleteenhmetafile.md)                       | Deletes an enhanced-format metafile or an enhanced-format metafile handle.                                             |
| [**EnhMetaFileProc**](enhmetafileproc.md)                           | An application-defined callback function used with the EnumEnhMetaFile function.                                       |
| [**EnumEnhMetaFile**](enumenhmetafile.md)                           | Enumerates the records within an enhanced-format metafile.                                                             |
| [**GdiComment**](gdicomment.md)                                     | Copies a comment from a buffer into a specified enhanced-format metafile.                                              |
| [**GetEnhMetaFile**](getenhmetafile.md)                             | Creates a handle that identifies the enhanced-format metafile stored in the specified file.                            |
| [**GetEnhMetaFileBits**](getenhmetafilebits.md)                     | Retrieves the contents of the specified enhanced-format metafile and copies them into a buffer.                        |
| [**GetEnhMetaFileDescription**](getenhmetafiledescription.md)       | Retrieves an optional text description from an enhanced-format metafile and copies the string to the specified buffer. |
| [**GetEnhMetaFileHeader**](getenhmetafileheader.md)                 | Retrieves the record containing the header for the specified enhanced-format metafile.                                 |
| [**GetEnhMetaFilePaletteEntries**](getenhmetafilepaletteentries.md) | Retrieves optional palette entries from the specified enhanced metafile.                                               |
| [**GetMetaFile**](getmetafile.md)                                   | GetMetaFile is no longer available for use as of Windows 2000. Instead, use [**GetEnhMetaFile**](getenhmetafile.md).  |
| [**GetWinMetaFileBits**](getwinmetafilebits.md)                     | Converts the enhanced-format records from a metafile into Windows-format records.                                      |
| [**PlayEnhMetaFile**](playenhmetafile.md)                           | Displays the picture stored in the specified enhanced-format metafile.                                                 |
| [**PlayEnhMetaFileRecord**](playenhmetafilerecord.md)               | Plays an enhanced-metafile record by executing the graphics device interface (GDI) functions identified by the record. |
| [**SetEnhMetaFileBits**](setenhmetafilebits.md)                     | Creates a memory-based enhanced-format metafile from the specified data.                                               |
| [**SetWinMetaFileBits**](setwinmetafilebits.md)                     | Converts a metafile from the older Windows format to the new enhanced format.                                          |



 

## Obsolete Functions

The following functions are obsolete. The are provided for compatibility with Windows-format metafiles.

-   [**CloseMetaFile**](closemetafile.md)
-   [**CopyMetaFile**](copymetafile.md)
-   [**CreateMetaFile**](createmetafile.md)
-   [**DeleteMetaFile**](deletemetafile.md)
-   [**EnumMetaFile**](enummetafile.md)
-   [**EnumMetaFileProc**](enummetafileproc.md)
-   [**GetMetaFileBitsEx**](getmetafilebitsex.md)
-   [**PlayMetaFile**](playmetafile.md)
-   [**PlayMetaFileRecord**](playmetafilerecord.md)
-   [**SetMetaFileBitsEx**](setmetafilebitsex.md)

 

 




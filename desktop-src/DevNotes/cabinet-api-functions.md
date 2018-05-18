---
ms.assetid: '43afef50-8fd2-49ec-9fb4-dafd8ebc009e'
title: Cabinet API Functions
---

# Cabinet API Functions

This section describes the following Cabinet API functions:

## FCI Functions

The FCI (File Compression Interface) library provides the ability to create cabinets (also known as "CAB files"). Additionally, the library provides compression to reduce the size of the file data stored in cabinets.



| Function                                   | Description                                                                                                 |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**FCIAddFile**](fciaddfile.md)           | Adds a file to the cabinet currently being contructed.<br/>                                           |
| [**FCICreate**](fcicreate.md)             | Creates an FCI context.<br/>                                                                          |
| [**FCIDestroy**](fcidestroy.md)           | Deletes an open FCI context, freeing any memory and temporary files associated with the context.<br/> |
| [**FCIFlushCabinet**](fciflushcabinet.md) | Completes the current cabinet.<br/>                                                                   |
| [**FCIFlushFolder**](fciflushfolder.md)   | Forces the current folder under construction to be completed immediately.<br/>                        |



 

## FDI Functions

The FDI (File Decompression Interface) library provides the ability to extract files from cabinets.



| Function                                         | Description                                                                                       |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**FDICopy**](fdicopy.md)                       | Extracts files from cabinets.<br/>                                                          |
| [**FDICreate**](fdicreate.md)                   | Creates an FDI context.<br/>                                                                |
| [**FDIDestroy**](fdidestroy.md)                 | Deletes an open FDI context.<br/>                                                           |
| [**FDIIsCabinet**](fdiiscabinet.md)             | Determines whether a file is a cabinet and, if it is, returns descriptive information.<br/> |
| [**FDITruncateCabinet**](fditruncatecabinet.md) | Truncates a cabinet file starting at the specified folder number.<br/>                      |



 

## Deprecated Functions

-   [**DeleteExtractedFiles**](deleteextractedfiles.md)
-   [**DllGetVersion**](dllgetversion.md)
-   [**Extract**](extract.md)
-   [**GetDllVersion**](getdllversion.md)

## Related topics

<dl> <dt>

[Cabinet API Reference](cabinet-api-reference.md)
</dt> <dt>

[Using the Cabinet API](using-the-cabinet-api.md)
</dt> </dl>

 

 





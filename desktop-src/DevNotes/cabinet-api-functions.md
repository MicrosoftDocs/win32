---
description: "Learn more about: Cabinet API Functions"
ms.assetid: 43afef50-8fd2-49ec-9fb4-dafd8ebc009e
title: Cabinet API Functions
ms.topic: article
ms.date: 05/31/2018
---

# Cabinet API Functions

This section describes the following Cabinet API functions:

## FCI Functions

The FCI (File Compression Interface) library provides the ability to create cabinets (also known as "CAB files"). Additionally, the library provides compression to reduce the size of the file data stored in cabinets.



| Function                                   | Description                                                                                                 |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**FCIAddFile**](/windows/desktop/api/Fci/nf-fci-fciaddfile)           | Adds a file to the cabinet currently being contructed.<br/>                                           |
| [**FCICreate**](/windows/desktop/api/Fci/nf-fci-fcicreate)             | Creates an FCI context.<br/>                                                                          |
| [**FCIDestroy**](/windows/desktop/api/Fci/nf-fci-fcidestroy)           | Deletes an open FCI context, freeing any memory and temporary files associated with the context.<br/> |
| [**FCIFlushCabinet**](/windows/desktop/api/Fci/nf-fci-fciflushcabinet) | Completes the current cabinet.<br/>                                                                   |
| [**FCIFlushFolder**](/windows/desktop/api/Fci/nf-fci-fciflushfolder)   | Forces the current folder under construction to be completed immediately.<br/>                        |



 

## FDI Functions

The FDI (File Decompression Interface) library provides the ability to extract files from cabinets.



| Function                                         | Description                                                                                       |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**FDICopy**](/windows/desktop/api/Fdi/nf-fdi-fdicopy)                       | Extracts files from cabinets.<br/>                                                          |
| [**FDICreate**](/windows/desktop/api/Fdi/nf-fdi-fdicreate)                   | Creates an FDI context.<br/>                                                                |
| [**FDIDestroy**](/windows/desktop/api/Fdi/nf-fdi-fdidestroy)                 | Deletes an open FDI context.<br/>                                                           |
| [**FDIIsCabinet**](/windows/desktop/api/Fdi/nf-fdi-fdiiscabinet)             | Determines whether a file is a cabinet and, if it is, returns descriptive information.<br/> |
| [**FDITruncateCabinet**](/windows/desktop/api/Fdi/nf-fdi-fditruncatecabinet) | Truncates a cabinet file starting at the specified folder number.<br/>                      |



 

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

 

 





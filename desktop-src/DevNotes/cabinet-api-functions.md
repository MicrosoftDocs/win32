---
ms.assetid: 43afef50-8fd2-49ec-9fb4-dafd8ebc009e
title: Cabinet API Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Cabinet API Functions

This section describes the following Cabinet API functions:

## FCI Functions

The FCI (File Compression Interface) library provides the ability to create cabinets (also known as "CAB files"). Additionally, the library provides compression to reduce the size of the file data stored in cabinets.



| Function                                   | Description                                                                                                 |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**FCIAddFile**](/windows/win32/Fci/nf-fci-fciaddfile?branch=master)           | Adds a file to the cabinet currently being contructed.<br/>                                           |
| [**FCICreate**](/windows/win32/Fci/nf-fci-fcicreate?branch=master)             | Creates an FCI context.<br/>                                                                          |
| [**FCIDestroy**](/windows/win32/Fci/nf-fci-fcidestroy?branch=master)           | Deletes an open FCI context, freeing any memory and temporary files associated with the context.<br/> |
| [**FCIFlushCabinet**](/windows/win32/Fci/nf-fci-fciflushcabinet?branch=master) | Completes the current cabinet.<br/>                                                                   |
| [**FCIFlushFolder**](/windows/win32/Fci/nf-fci-fciflushfolder?branch=master)   | Forces the current folder under construction to be completed immediately.<br/>                        |



 

## FDI Functions

The FDI (File Decompression Interface) library provides the ability to extract files from cabinets.



| Function                                         | Description                                                                                       |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**FDICopy**](/windows/win32/Fdi/nf-fdi-fdicopy?branch=master)                       | Extracts files from cabinets.<br/>                                                          |
| [**FDICreate**](/windows/win32/Fdi/nf-fdi-fdicreate?branch=master)                   | Creates an FDI context.<br/>                                                                |
| [**FDIDestroy**](/windows/win32/Fdi/nf-fdi-fdidestroy?branch=master)                 | Deletes an open FDI context.<br/>                                                           |
| [**FDIIsCabinet**](/windows/win32/Fdi/nf-fdi-fdiiscabinet?branch=master)             | Determines whether a file is a cabinet and, if it is, returns descriptive information.<br/> |
| [**FDITruncateCabinet**](/windows/win32/Fdi/nf-fdi-fditruncatecabinet?branch=master) | Truncates a cabinet file starting at the specified folder number.<br/>                      |



 

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

 

 





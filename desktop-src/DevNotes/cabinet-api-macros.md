---
ms.assetid: '85fade43-9fcb-4100-a734-8b36d132b2c0'
title: Cabinet API Macros
---

# Cabinet API Macros

This section details the macros used by the Cabinet API:

## FCI Macros

The following macros are used by FCI:



| Macro                                              | Description                                                                                    |
|----------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**FNFCIALLOC**](fnfcialloc.md)                   | Used to allocate memory in an FCI context.<br/>                                          |
| [**FNFCICLOSE**](fnfciclose.md)                   | Used to close a file.<br/>                                                               |
| [**FNFCIDELETE**](fnfcidelete.md)                 | Used to delete a file.<br/>                                                              |
| [**FNFCIFILEPLACED**](fnfcifileplaced.md)         | Used to notify when a file is placed in the cabinet.<br/>                                |
| [**FNFCIFREE**](fnfcifree.md)                     | Used to free previously allocated memory in an FCI context.<br/>                         |
| [**FNFCIGETNEXTCABINET**](fnfcigetnextcabinet.md) | Used to request information for the next cabinet.<br/>                                   |
| [**FNFCIGETOPENINFO**](fnfcigetopeninfo.md)       | Used to open a file and retrieve file date, time, and attributes.<br/>                   |
| [**FNFCIGETTEMPFILE**](fnfcigettempfile.md)       | Used to obtain a temporary file name.<br/>                                               |
| [**FNFCIOPEN**](fnfciopen.md)                     | Used to open a file in an FCI context.<br/>                                              |
| [**FNFCIREAD**](fnfciread.md)                     | Used to read data from a file.<br/>                                                      |
| [**FNFCISEEK**](fnfciseek.md)                     | Used to move a file pointer to a specified location.<br/>                                |
| [**FNFCISTATUS**](fnfcistatus.md)                 | Used to update the user.<br/>                                                            |
| [**FNFCIWRITE**](fnfciwrite.md)                   | Used to write data to a file.<br/>                                                       |
| [**TCOMPfromLZXWindow**](tcompfromlzxwindow.md)   | Converts windows size into an LXZ TCOMP value for [**FCIAddFile**](fciaddfile.md).<br/> |



 

## FDI Macros

The following macros are used by FDI:



| Macro                              | Description                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| [**FNALLOC**](fnalloc.md)         | Used to allocate memory in an FDI context.<br/>                               |
| [**FNCLOSE**](fnclose.md)         | Used to close a file in an FDI context.<br/>                                  |
| [**FNFDINOTIFY**](fnfdinotify.md) | Used to update the application on the status of the decoder.<br/>             |
| [**FNFREE**](fnfree.md)           | Used to free previously allocated memory in an FDI context.<br/>              |
| [**FNOPEN**](fnopen.md)           | Used to open a file in an FDI context.<br/>                                   |
| [**FNREAD**](fnread.md)           | Used to read data from a file in an FDI context.<br/>                         |
| [**FNSEEK**](fnseek.md)           | Used to move a file pointer to the specified location in an FDI context.<br/> |
| [**FNWRITE**](fnwrite.md)         | Used to write data to a file in an FDI context.<br/>                          |



 

## Related topics

<dl> <dt>

[Cabinet API Reference](cabinet-api-reference.md)
</dt> <dt>

[Using the Cabinet API](using-the-cabinet-api.md)
</dt> </dl>

 

 





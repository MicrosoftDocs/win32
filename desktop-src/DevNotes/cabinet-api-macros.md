---
description: "Learn more about: Cabinet API Macros"
ms.assetid: 85fade43-9fcb-4100-a734-8b36d132b2c0
title: Cabinet API Macros
ms.topic: article
ms.date: 05/31/2018
---

# Cabinet API Macros

This section details the macros used by the Cabinet API:

## FCI Macros

The following macros are used by FCI:



| Macro                                              | Description                                                                                    |
|----------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**FNFCIALLOC**](/windows/desktop/api/fci/nf-fci-fnfcialloc)                   | Used to allocate memory in an FCI context.<br/>                                          |
| [**FNFCICLOSE**](/windows/desktop/api/fci/nf-fci-fnfciclose)                   | Used to close a file.<br/>                                                               |
| [**FNFCIDELETE**](/windows/desktop/api/fci/nf-fci-fnfcidelete)                 | Used to delete a file.<br/>                                                              |
| [**FNFCIFILEPLACED**](/windows/desktop/api/fci/nf-fci-fnfcifileplaced)         | Used to notify when a file is placed in the cabinet.<br/>                                |
| [**FNFCIFREE**](/windows/desktop/api/fci/nf-fci-fnfcifree)                     | Used to free previously allocated memory in an FCI context.<br/>                         |
| [**FNFCIGETNEXTCABINET**](/windows/desktop/api/fci/nf-fci-fnfcigetnextcabinet) | Used to request information for the next cabinet.<br/>                                   |
| [**FNFCIGETOPENINFO**](/windows/desktop/api/fci/nf-fci-fnfcigetopeninfo)       | Used to open a file and retrieve file date, time, and attributes.<br/>                   |
| [**FNFCIGETTEMPFILE**](/windows/desktop/api/fci/nf-fci-fnfcigettempfile)       | Used to obtain a temporary file name.<br/>                                               |
| [**FNFCIOPEN**](/windows/desktop/api/fci/nf-fci-fnfciopen)                     | Used to open a file in an FCI context.<br/>                                              |
| [**FNFCIREAD**](/windows/desktop/api/fci/nf-fci-fnfciread)                     | Used to read data from a file.<br/>                                                      |
| [**FNFCISEEK**](/windows/desktop/api/fci/nf-fci-fnfciseek)                     | Used to move a file pointer to a specified location.<br/>                                |
| [**FNFCISTATUS**](/windows/desktop/api/fci/nf-fci-fnfcistatus)                 | Used to update the user.<br/>                                                            |
| [**FNFCIWRITE**](/windows/desktop/api/fci/nf-fci-fnfciwrite)                   | Used to write data to a file.<br/>                                                       |
| [**TCOMPfromLZXWindow**](/windows/desktop/api/fdi_fci_types/nf-fdi_fci_types-tcompfromlzxwindow)   | Converts windows size into an LXZ TCOMP value for [**FCIAddFile**](/windows/desktop/api/Fci/nf-fci-fciaddfile).<br/> |



 

## FDI Macros

The following macros are used by FDI:



| Macro                              | Description                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| [**FNALLOC**](/windows/desktop/api/fdi/nf-fdi-fnalloc)         | Used to allocate memory in an FDI context.<br/>                               |
| [**FNCLOSE**](/windows/desktop/api/fdi/nf-fdi-fnclose)         | Used to close a file in an FDI context.<br/>                                  |
| [**FNFDINOTIFY**](/windows/desktop/api/fdi/nf-fdi-fnfdinotify) | Used to update the application on the status of the decoder.<br/>             |
| [**FNFREE**](/windows/desktop/api/fdi/nf-fdi-fnfree)           | Used to free previously allocated memory in an FDI context.<br/>              |
| [**FNOPEN**](/windows/desktop/api/fdi/nf-fdi-fnopen)           | Used to open a file in an FDI context.<br/>                                   |
| [**FNREAD**](/windows/desktop/api/fdi/nf-fdi-fnread)           | Used to read data from a file in an FDI context.<br/>                         |
| [**FNSEEK**](/windows/desktop/api/fdi/nf-fdi-fnseek)           | Used to move a file pointer to the specified location in an FDI context.<br/> |
| [**FNWRITE**](/windows/desktop/api/fdi/nf-fdi-fnwrite)         | Used to write data to a file in an FDI context.<br/>                          |



 

## Related topics

<dl> <dt>

[Cabinet API Reference](cabinet-api-reference.md)
</dt> <dt>

[Using the Cabinet API](using-the-cabinet-api.md)
</dt> </dl>

 

 





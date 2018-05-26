---
ms.assetid: 85fade43-9fcb-4100-a734-8b36d132b2c0
title: Cabinet API Macros
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Cabinet API Macros

This section details the macros used by the Cabinet API:

## FCI Macros

The following macros are used by FCI:



| Macro                                              | Description                                                                                    |
|----------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**FNFCIALLOC**](/windows/win32/fci/nf-fci-fnfcialloc?branch=master)                   | Used to allocate memory in an FCI context.<br/>                                          |
| [**FNFCICLOSE**](/windows/win32/fci/nf-fci-fnfciclose?branch=master)                   | Used to close a file.<br/>                                                               |
| [**FNFCIDELETE**](/windows/win32/fci/nf-fci-fnfcidelete?branch=master)                 | Used to delete a file.<br/>                                                              |
| [**FNFCIFILEPLACED**](/windows/win32/fci/nf-fci-fnfcifileplaced?branch=master)         | Used to notify when a file is placed in the cabinet.<br/>                                |
| [**FNFCIFREE**](/windows/win32/fci/nf-fci-fnfcifree?branch=master)                     | Used to free previously allocated memory in an FCI context.<br/>                         |
| [**FNFCIGETNEXTCABINET**](/windows/win32/fci/nf-fci-fnfcigetnextcabinet?branch=master) | Used to request information for the next cabinet.<br/>                                   |
| [**FNFCIGETOPENINFO**](/windows/win32/fci/nf-fci-fnfcigetopeninfo?branch=master)       | Used to open a file and retrieve file date, time, and attributes.<br/>                   |
| [**FNFCIGETTEMPFILE**](/windows/win32/fci/nf-fci-fnfcigettempfile?branch=master)       | Used to obtain a temporary file name.<br/>                                               |
| [**FNFCIOPEN**](/windows/win32/fci/nf-fci-fnfciopen?branch=master)                     | Used to open a file in an FCI context.<br/>                                              |
| [**FNFCIREAD**](/windows/win32/fci/nf-fci-fnfciread?branch=master)                     | Used to read data from a file.<br/>                                                      |
| [**FNFCISEEK**](/windows/win32/fci/nf-fci-fnfciseek?branch=master)                     | Used to move a file pointer to a specified location.<br/>                                |
| [**FNFCISTATUS**](/windows/win32/fci/nf-fci-fnfcistatus?branch=master)                 | Used to update the user.<br/>                                                            |
| [**FNFCIWRITE**](/windows/win32/fci/nf-fci-fnfciwrite?branch=master)                   | Used to write data to a file.<br/>                                                       |
| [**TCOMPfromLZXWindow**](/windows/win32/fdi_fci_types/nf-fdi_fci_types-tcompfromlzxwindow?branch=master)   | Converts windows size into an LXZ TCOMP value for [**FCIAddFile**](/windows/win32/Fci/nf-fci-fciaddfile?branch=master).<br/> |



 

## FDI Macros

The following macros are used by FDI:



| Macro                              | Description                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| [**FNALLOC**](/windows/win32/fdi/nf-fdi-fnalloc?branch=master)         | Used to allocate memory in an FDI context.<br/>                               |
| [**FNCLOSE**](/windows/win32/fdi/nf-fdi-fnclose?branch=master)         | Used to close a file in an FDI context.<br/>                                  |
| [**FNFDINOTIFY**](/windows/win32/fdi/nf-fdi-fnfdinotify?branch=master) | Used to update the application on the status of the decoder.<br/>             |
| [**FNFREE**](/windows/win32/fdi/nf-fdi-fnfree?branch=master)           | Used to free previously allocated memory in an FDI context.<br/>              |
| [**FNOPEN**](/windows/win32/fdi/nf-fdi-fnopen?branch=master)           | Used to open a file in an FDI context.<br/>                                   |
| [**FNREAD**](/windows/win32/fdi/nf-fdi-fnread?branch=master)           | Used to read data from a file in an FDI context.<br/>                         |
| [**FNSEEK**](/windows/win32/fdi/nf-fdi-fnseek?branch=master)           | Used to move a file pointer to the specified location in an FDI context.<br/> |
| [**FNWRITE**](/windows/win32/fdi/nf-fdi-fnwrite?branch=master)         | Used to write data to a file in an FDI context.<br/>                          |



 

## Related topics

<dl> <dt>

[Cabinet API Reference](cabinet-api-reference.md)
</dt> <dt>

[Using the Cabinet API](using-the-cabinet-api.md)
</dt> </dl>

 

 





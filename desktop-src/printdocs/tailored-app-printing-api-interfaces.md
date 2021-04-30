---
description: The following interfaces are used by an app to manage the print document package.
ms.assetid: 576B4527-A753-4A73-899B-896DCB8B8945
title: Print Document Package API Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Print Document Package API Interfaces

The following interfaces are used by an app to manage the print document package.

## In this section



| Topic                                                                                       | Description                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IPrintDocumentPackageStatusEvent**](/windows/desktop/api/Documenttarget/nn-documenttarget-iprintdocumentpackagestatusevent)<br/>     | Represents the progress of the print job.<br/>                                                                                                                                                                        |
| [**IPrintDocumentPackageTarget**](/windows/win32/api/documenttarget/nn-documenttarget-iprintdocumentpackagetarget)<br/>               | Allows users to enumerate the supported package target types and to create one with a given type ID. **IPrintDocumentPackageTarget** also supports the tracking of the package printing progress and cancelling.<br/> |
| [**IPrintDocumentPackageTargetFactory**](/windows/desktop/api/documenttarget/nn-documenttarget-iprintdocumentpackagetargetfactory)<br/> | Used with [IPrintDocumentPackageTarget](/windows/win32/api/documenttarget/nn-documenttarget-iprintdocumentpackagetarget) for starting a print job.<br/>                                                                                                               |



 

 


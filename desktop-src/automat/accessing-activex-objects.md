---
title: Accessing ActiveX Objects
description: To access exposed objects, you can create ActiveX clients using Visual Basic, Microsoft Visual C++, Microsoft Excel, and other applications and programming languages that support the Automation technology.
ms.assetid: 973ca2be-7f0e-43db-8790-0aa07c45675d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Accessing ActiveX Objects

To access exposed objects, you can create ActiveX clients using Visual Basic, Microsoft Visual C++, Microsoft Excel, and other applications and programming languages that support the Automation technology. This section discusses several strategies for accessing exposed objects.

-   Creating scripts with Visual Basic

-   Creating controllers that manipulate objects

-   Creating type information browsers

Regardless of your strategy, an ActiveX client needs to follow these steps:

### To initialize and create the object

1.  Initialize OLE.

2.  Create an instance of the exposed object.

### To manipulate methods and properties

1.  Get information about the object's methods and properties.

2.  Invoke the methods and properties.

### To release OLE when the application or programming tool terminates

1.  Revoke the active object.

2.  Uninitialize OLE.

> [!Note]  
> Throughout this section, the file names of sample applications appear in parentheses before the sample code.

 

## In this section



| Topic                                                                                                                     | Description                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Creating Scripts Using Visual Basic](creating-scripts-using-visual-basic.md)<br/>                                 | Visual Basic provides a complete programming environment for creating Windows applications with which you can manipulate the exposed ActiveX objects of other applications.<br/> |
| [Creating Applications and Tools that Access Objects](creating-applications-and-tools-that-access-objects.md)<br/> | Automation provides interfaces for accessing exposed objects from an application or programming tool written in C or C++.<br/>                                                   |
| [Creating Type Information Browsers](creating-type-information-browsers.md)<br/>                                   | Type information browsers let users scan type libraries to determine what types of objects are available.<br/>                                                                   |



 

## Related topics

<dl> <dt>

[Automation Programming Reference](automation-programming-reference.md)
</dt> </dl>

 

 






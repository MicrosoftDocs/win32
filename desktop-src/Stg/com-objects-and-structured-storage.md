---
title: COM Objects and Structured Storage
description: One of the most common current uses of persistent properties is to use them to store data about a system object, such as a document, with that object.
ms.assetid: 95136e9a-4c80-4704-ae65-9759487cf8f8
keywords:
- COM Objects and Structured Storage
ms.topic: article
ms.date: 05/31/2018
---

# COM Objects and Structured Storage

One of the most common current uses of persistent properties is to use them to store data about a system object, such as a document, with that object. There is, of course, the potential of storing properties with any object, such as a printer, so it would only be necessary to look at its properties to determine its location, its type, and so on. A user object could have a property set that includes data such as First Name, Last Name, Office, and Phone. Applications can be written to query a system-wide set of objects based on their properties, for example, displaying all printers located in a certain building. Current systems, however, most frequently use properties on documents.

The primary property set standard defined by COM is [The Summary Information Property Set](the-summary-information-property-set.md). This property set is both simple and commonly used. Most documents created by applications have a common set of attributes useful to users of those documents. These attributes include the name of the document author, the subject of the document, when it was created, and so on. Two other property sets are defined for Microsoft Office 95, Office 97 and later. These are the COM Document Summary property set and the User-Defined Properties property set. For more information, see [Structured Storage Serialized Property Set Format](structured-storage-serialized-property-set-format.md).

In Windows 3.1, each application had a different way of storing this data within its documents. To examine the summary information for a given document, the user had to run the application that created the document, open it, and invoke the application Summary Information dialog box, so only the application could display its summary information.

COM property sets and the property set interfaces make it possible to see the document properties without running the creating application. For example, all versions of Microsoft Word 6.0 or later, and many other COM-enabled applications now save their documents using COM structured storage and the property set standard described here. Thus, other Office Suite applications are able to display [The Summary Information Property Set](the-summary-information-property-set.md) for such a file, as long as that file is a COM structured storage file, and the creating application saved the information in the COM Property Set format. The Windows 95 or Windows 98 shell, for example, uses this, and allows the end user to view the properties of any Word 6.0 or later document directly from the shell.

To use property sets from other applications, the other applications must recognize how to interpret the properties within a property set, which implies a standard. COM has pioneered this approach by defining one standard property set, the COM Summary Information Property Set. Any application that has the definition of this property set can easily access the summary information contained in any document created by an COM application that uses that property set specification.

 

 





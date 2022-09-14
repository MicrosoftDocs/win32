---
title: Implementing the Summary Information Property Set
description: There are guidelines to follow when implementing a summary information property set for Structured Storage.
ms.assetid: e1204de5-b712-4bd5-bffb-6a12ec8d7052
keywords:
- Implementing the Summary Information Property Set
ms.topic: article
ms.date: 05/31/2018
---

# Implementing the Summary Information Property Set

There are guidelines to follow when implementing a summary information property set for Structured Storage.

The following are the guidelines for implementing [The Summary Information Property Set](the-summary-information-property-set.md):

-   **PID\_TEMPLATE** refers to an external document containing format and style information. The process by which the template is located is implementation-defined.
-   **PID\_LASTAUTHOR** is the name stored in User Information by the application. For example, Mary creates a document on her computer and gives it to John, who then modifies and saves it. Mary is the author, John is the last saved by value.
-   **PID\_REVNUMBER** is the number of times the File/Save command has been called on this document.
-   Each of the date/time values must be stored in Universal Coordinated Time (UTC).
-   **PID\_CREATE\_DTM** is a read-only property; this property should be set when a document is created, but should not be subsequently changed.
-   For **PID\_THUMBNAIL**, applications should store data in **CF\_DIB** or **CF\_METAFILEPICT** format. **CF\_METAFILEPICT** is recommended.
-   **PID\_SECURITY** is the suggested security level for the document. By noting the security level on the document, an application other than the originator of the document can adjust its user interface to the properties. An application should not display any information about a password-protected document or enable modifications to enforced Read-Only or Locked-for-Annotations documents. If the user attempts to modify properties, the application should warn the user about the Read-Only Recommended status.



| Security level         | Value |
|------------------------|-------|
| None                   | 0     |
| Password protected     | 1     |
| Read-only recommended  | 2     |
| Read-only enforced     | 4     |
| Locked for annotations | 8     |



 

 

 





---
Description: Error Messages
ms.assetid: 6baa32d7-58a5-48cc-a7cb-9f7a3fd8813c
title: Error Messages
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Error Messages

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Several errors can occur when submitting queries to the SQL parser. When these errors occur, the OLE DB Provider returns a DB\_E\_ERRORSINCOMMAND error (see [**ICommand::Execute**](https://msdn.microsoft.com/windows/desktop/95b4c895-a55c-4f01-a641-68a7f9a5f106)). It can usually also return a string describing the error. These errors are usually syntax related.

The following error messages are not defined in a public header and the error codes associated with them are not exposed. They are also localized. Parameters shown in italics are specific to each query that is in error.

-   Parser Error
-   Illegal PASSTHROUGH query: *Query\_Expression*
-   Incorrect syntax near *Query\_Token*. SQLSTATE=42000
-   Incorrect syntax near *Query\_Token*. Expected *Token*. SQLSTATE=42000
-   Multiple statement commands are not supported. SQLSTATE=42000
-   ORDER BY ordinal *number* must be between 1 and *Ordinal\_Number*. SQLSTATE=42000
-   View *View\_Name* has not been defined in catalog *Catalog\_Name*. SQLSTATE=42S02
-   Column *Column\_Name* has not been defined. SQLSTATE=42S22
-   View name conflicts with a predefined view definition
-   Out of memory
-   SELECT \* only allowed on views
-   Content\_Search\_Condition OR NOT Content\_Boolean\_Term not allowed
-   Cannot convert *Data\_Type\_1* to type *Data\_Type\_2*
-   *Value* is out of range for type *Data\_Type*
-   Specification of *Relative\_Interval* must be negative
-   *Column\_Name* is not a column in the view definition
-   Property name conflicts with a predefined property definition
-   Weight value must be between 0.0 and 1.0
-   Error in matches string
-   Property name cannot be set because it is already being used in a VIEW. SQLSTATE=42000
-   View *View\_Name* already exists in catalog *Catalog\_Name* and cannot be redefined. SQLSTATE=42S01
-   Invalid catalog name *Catalog\_Name*. SQLSTATE=42000

 

 




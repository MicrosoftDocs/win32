---
Description: Extensions for Queries
ms.assetid: e23da304-fefc-40f2-87bd-725056a5aa2c
title: Extensions for Queries
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Extensions for Queries

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following table summarizes the extensions to the SQL syntax for specifying queries to Indexing Service.



| SQL Extension                                                                                                                                                     | Description                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [SET PROPERTYNAME](set-statement.md)<br/>                                                                                                                  | Defines the column name and a data type for a property. <br/>                                     |
| [SET RANKMETHOD](set-rankmethod.md)<br/>                                                                                                                   | Sets the document ranking method used for the results of queries.<br/>                            |
| [CREATE VIEW \#](create-view-statement.md)<br/>                                                                                                            | Creates a temporary view using column names and scope.<br/>                                       |
| [Indexing Service Predefined Views](indexing-service-predefined-views.md)<br/> [Site Server Predefined Views](site-server-predefined-views.md)<br/> | Defines permanent views using standard Indexing Service properties.<br/>                          |
| [SELECT \*](select-statement.md)<br/>                                                                                                                      | Selects all columns in a predefined or temporary view.<br/>                                       |
| [FROM SCOPE](from-clause.md)<br/>                                                                                                                          | Defines the server, catalog, and path to use to create a virtual table of rows of documents.<br/> |
| [ARRAY predicate](array-predicate.md)<br/>                                                                                                                 | Enables comparison of multivalued Indexing Service properties. <br/>                              |
| [Comparison predicate](comparison-predicate.md)<br/>                                                                                                       | Enables comparison of columns with literal data using relational operators.<br/>                  |
| [MATCHES predicate](matches-predicate.md)<br/>                                                                                                             | Similar to the LIKE predicate, but enables grouping matches against more than one pattern. <br/>  |
| [Batched statements](batched-statements.md)<br/>                                                                                                           | Enables setting and executing several SQL statements as one command. <br/>                        |



 

 

 





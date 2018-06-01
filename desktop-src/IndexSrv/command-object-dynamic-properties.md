---
Description: Command Object Dynamic Properties
ms.assetid: 0ae52e14-1e42-4668-b0ce-1b5afc1c126f
title: Command Object Dynamic Properties
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Command Object Dynamic Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following table includes dynamic properties for use with the ADO **Command** object.



| Property Names                                       | Value | Read/Write | Defined By                                       |
|------------------------------------------------------|-------|------------|--------------------------------------------------|
| Blocking Storage Objects                             | False | RO         | OLE DB                                           |
| Include Bookmark Data                                | False | RW         | OLE DB                                           |
| Skip Deleted Bookmarks                               | False | RO         | OLE DB                                           |
| Bookmark Type                                        | 1     | RO         | OLE DB                                           |
| Fetch Backwards                                      | False | RO         | OLE DB                                           |
| Hold Rows                                            | False | RW         | OLE DB                                           |
| Scroll Backwards                                     | False | RO         | OLE DB                                           |
| Column Privileges                                    | False | RO         | OLE DB                                           |
| Command Time Out                                     | 30    | RW         | OLE DB                                           |
| Literal Bookmarks                                    | False | RO         | OLE DB                                           |
| Literal Row Identity                                 | False | RO         | OLE DB                                           |
| Maximum Open Rows                                    | 0     | RO         | OLE DB                                           |
| Maximum Rows                                         | 0     | RO         | OLE DB                                           |
| Memory Usage                                         | 0     | RW         | OLE DB                                           |
| Bookmarks Ordered                                    | False | RO         | OLE DB                                           |
| Others' Inserts Visible                              | False | RO         | OLE DB                                           |
| Others' Changes Visible                              | False | RO         | OLE DB                                           |
| Quick Restart                                        | False | RO         | OLE DB                                           |
| Reentrant Events                                     | False | RO         | OLE DB                                           |
| Remove Deleted Rows                                  | True  | RO         | OLE DB                                           |
| Row Privileges                                       | True  | RO         | OLE DB                                           |
| Row Threading Model                                  | 1     | RO         | OLE DB                                           |
| Server Cursor                                        | True  | RO         | OLE DB                                           |
| Strong Row Identity                                  | False | RO         | OLE DB                                           |
| Updatability                                         | 0     | RO         | OLE DB                                           |
| IAccessor                                            | True  | RO         | OLE DB                                           |
| IcolumnsInfo                                         | True  | RO         | OLE DB                                           |
| IConnectionPointContainer                            | False | RO         | OLE DB                                           |
| IconvertType                                         | True  | RO         | OLE DB                                           |
| Irowset                                              | True  | RO         | OLE DB                                           |
| IrowsetIdentity                                      | False | RO         | OLE DB                                           |
| IrowsetInfo                                          | True  | RO         | OLE DB                                           |
| Bookmarkable                                         | False | RW         | OLE DB                                           |
| IrowsetScroll                                        | False | RW         | OLE DB                                           |
| ISupportErrorInfo                                    | True  | RO         | OLE DB                                           |
| Always use Content Index                             | False | RW         | Specific to OLE DB Provider for Indexing Service |
| Defer scope and security testing                     | False | RW         | Specific to OLE DB Provider for Indexing Service |
| Return **PROPVARIANT** structures in variant binding | False | RW         | Specific to OLE DB Provider for Indexing Service |
| SQL Content Query Locale String                      | EN    | RW         | Specific to OLE DB Provider for Indexing Service |
| Query Restriction                                    | ""    | RW         | Specific to OLE DB Provider for Indexing Service |



 

 

 




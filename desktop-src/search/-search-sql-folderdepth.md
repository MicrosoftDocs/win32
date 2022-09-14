---
description: Folder depth predicates control the scope of a search by specifying a path and whether to perform a deep or shallow traversal.
ms.assetid: 8eadbd42-3538-412e-9bf8-b2355d23437e
title: SCOPE and DIRECTORY Predicates
ms.topic: article
ms.date: 05/31/2018
---

# SCOPE and DIRECTORY Predicates

Folder depth predicates control the scope of a search by specifying a path and whether to perform a deep or shallow traversal. The following shows the syntax of the folder depth predicates:


```
... WHERE [{SCOPE | DIRECTORY}='<protocol>:[{SID}]<path>']
```



The predicate is followed by an equal sign. The path is exclosed in single quotes and must begin with a protocol and a colon (for example, `file:`, `mapi:`, or `csc:`). The SCOPE predicate performs a deep traversal of the path, including all subfolders, while the DIRECTORY predicate does a shallow traversal of only the folder specified. Like other Structured Query Language (SQL) restrictions, you can specify more than one folder depth restriction in a single query.

To query the local catalog of a remote computer, include the computer name before the catalog and a Universal Naming Convention (UNC) path on the remote computer in the SCOPE or DIRECTORY clause.

## Examples


```
SELECT System.ItemName FROM SystemIndex WHERE SCOPE='file:C:/Files/Reports'

SELECT System.ItemName FROM SystemIndex WHERE DIRECTORY='file:C:/Files/Reports' 

SELECT System.ItemName FROM SystemIndex WHERE SCOPE='file:C:/Files/Published' OR SCOPE='file:C:/Files/Reports' AND NOT SCOPE='file:C:/Files/Reports/Confidential'

SELECT System.ItemName FROM zarasmachine.SystemIndex WHERE SCOPE='file://zarasmachine/C:/Files/Reports'

SELECT System.ItemURL FROM SystemIndex WHERE SCOPE='mapi://{S-1-5-21-2117521111-1604012920-1887927527-2285604}/Mailbox user/' AND CONTAINS('Microsoft')
```



The first SCOPE example searches the C:\\Files\\Reports folder and all its subfolders. The DIRECTORY example searches only the root folder C:\\Files\\Reports.

> [!Note]  
> The file system backslashes (\\) become a URL-style slash marks (sometimes called forward slashes) (/).

 

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[FROM Clause](-search-sql-from.md)
</dt> <dt>

[WHERE Clause](-search-sql-where.md)
</dt> </dl>

 

 




---
title: Enumerated and Indexed Resolution
description: Enumerated and Indexed Resolution
ms.assetid: 09b1cef3-0345-4e1c-9855-92fdc921947a
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerated and Indexed Resolution

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Executing queries that must be enumerated can also slow down performance. Most queries are resolved by using the Content Index, but certain conditions force the query engine to search the disk to locate matching files. These queries include:

-   Regular expressions on properties other than **FileName** which begin with any special regular expression character.
-   Regular expressions on **FileName** which both begin and end with any special regular expression character.
-   Property value queries when the [CiForceUseCi](variables-in-forms-and-in-idq-files.md#-idxs-ciforceuseci-var) parameter is set to FALSE and the index is not up to date.
-   Property value queries involving regular expressions that start and end with any special regular-expression characters (for example, \#filename \*sample\*).
-   Certain property value queries involving OR (such as @write &gt; -1d OR @create &gt; -1d).

Queries can be forced to use the Content Index by setting [CiForceUseCi](variables-in-forms-and-in-idq-files.md#-idxs-ciforceuseci-var) to TRUE in the .idq file. The query engine will always use the Content Index, but query results may be out of date for recently modified files. If the Content Index was used for a query, and some files on disk have been modified more recently than their contents have been filtered, the built-in variable [CiOutOfDate](read-only-variables-available-in-htx-files.md#-idxs-cioutofdate-var) will be set to the value 1. In some cases, a query is simply too complex to be resolved solely through use of the Content Index. In these cases, the built-in variable [CiQueryIncomplete](read-only-variables-available-in-htx-files.md#-idxs-ciqueryincomplete-var) will be set to 1. Content queries can always be out of date and can use the Content Index anytime.

 

 





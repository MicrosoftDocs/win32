---
title: Writing Internet Data Administration Scripts
description: Writing Internet Data Administration Scripts
ms.assetid: 034830bf-3798-4eaa-a927-0773d1fd08ce
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Writing Internet Data Administration Scripts

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Administrative requests are very similar to queries, except that the parameters are stored in an Internet Data Administration (.ida) file instead of an Internet Data Query (.idq) file. You can write your own IDA scripts with the following parameters:



| Parameter                                                                  | Description                                                                                               | Optional |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------|
| [CiCatalog](variables-in-forms-and-in-idq-files.md#-idxs-cicatalog-var)   | Specifies location of catalog. If not found, default specified in registry is used.                       | Yes      |
| [CiTemplate](variables-in-forms-and-in-idq-files.md#-idxs-citemplate-var) | Specifies template to use if administration operation is successful. Standard .idq error semantics apply. | No       |
| [CiLocale](variables-in-forms-and-in-idq-files.md#-idxs-cilocale-var)     | Defines the locale used to issue the query. Indexing Service supports standard HTML locale encoding.      | Yes      |



 

You can also add user-defined variables in the same manner as .idq files.

Some administrative operations can change the state of the index. Administrative operations are restricted based on an access control list (ACL).

> [!Note]  
> Do not put .ida files on a virtual root pointing to a remote Uniform Naming Convention (UNC) share.

 

 

 





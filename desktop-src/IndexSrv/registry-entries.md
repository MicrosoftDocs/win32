---
title: Registry Entries
description: Registry Entries
ms.assetid: '8453a660-c93a-4986-8c1b-0b359925ff47'
---

# Registry Entries

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service uses entries in the registry to control many performance and resource variables for indexing and querying. The registry also includes entries with path names for catalogs and their scopes, with names for files needed to process queries and create formatted results, and for flags that influence what information Indexing Service logs in the Windows event log. The registry also contains language-specific information for the language being indexed.

Indexing Service supplies the [**SetLongProperty**](iadminindexserver-setlongproperty.md), [**SetSZProperty**](iadminindexserver-setszproperty.md), [**GetLongProperty**](iadminindexserver-getlongproperty.md), and [**GetSZProperty**](iadminindexserver-getszproperty.md) methods of the [**AdminIndexServer**](iadminindexserver.md) object for programmatically setting and retrieving Indexing Service registry entries. These methods work in programming environments that support automation, such as Microsoft Visual Basic, Microsoft Visual Basic Scripting Edition (VBScript), and Microsoft JScript.

> \[!Caution\]  
> Incorrectly editing the registry may severely damage your system. Back up the current version of the registry before making any changes. You should also back up any valued data on the computer.

 

Indexing Service registry entries group by functionality into the following categories.

-   [Main Registry Entries](main-registry-entries.md). This group includes the majority of the entries. With the exception of the [**DefaultColumnFile**](defaultcolumnfile.md) entry, they are found under the key:

    **HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**ContentIndex**

    The [**DefaultColumnFile**](defaultcolumnfile.md) entry is found under the key:

    **HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**ContentIndexCommon**

-   [Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md). This group includes entries that define the catalog directories and scopes that determine what gets indexed for each catalog and cached properties. These registry entries are found under the key:

    **HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**ContentIndex**\\**Catalogs**

    and its subkeys, one for each catalog.

-   [Language-Specific Registry Entries](language-specific-registry-entries.md). This group includes entries that control the parts of the indexing and query processes that are language-specific. These registry entries can be found under the key:

    **HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**ContentIndex**\\**Language**

 

 





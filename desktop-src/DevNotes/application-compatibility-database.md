---
description: The compatibility infrastructure uses a database to identify application compatibility issues and their solutions.
ms.assetid: 3b35b758-18ca-40dd-8882-35d9b458264c
title: Application Compatibility Database
ms.topic: article
ms.date: 05/31/2018
---

# Application Compatibility Database

The compatibility infrastructure uses a database to identify application compatibility issues and their solutions. This database is an indexed binary file with an .sdb extension. The compatibility infrastructure provides a programming interface to access the database.

Compatibility issues can be addressed on an application-by-application basis at run time. Each application specified in the database contains one or more components that need a solution. Components are executable files that are generally described using their file attributes (for example, checksum).

The process of database lookup and determining the solutions for each application is called *matching*. The file attributes and the presence of associated files in the folder or subfolder containing the .exe file can be used to create a unique match. The associated files are called *matching files*.

A *TAG* is a unique identifier for the entries and attributes in the database. The *TAG type* indicates the format of the data associated with the [**TAG**](tag.md). For example, **TAG\_NAME** is of type **TAG\_TYPE\_STRINGREF**; the data for **TAG\_NAME** is a name string. A *TAGID* is a pointer to an entry in a particular database. A *TAGREF* is a pointer to an entry that can be used across multiple databases.

*File attributes* are metadata associated with a file on disk. These attributes include the file name, file size, checksum, version, and date. These attributes are used to determine whether a file being loaded by the system matches a database entry. Therefore, these file attributes are also called *matching attributes*.

## Solutions

The most common solutions applied to the components of an application are Apphelp and Appfix.

With Apphelp, a custom localized message notification is displayed, typically when the application is installed or started. It contains brief text that explains the compatibility issue and provides the option to continue running the application. However, some applications will fail dramatically is allowed to run; Apphelp will not give the user the option to continue running these applications.

With Appfix, hooks are installed for APIs called by the components of the application. These hooks point to stub functions that can be called instead of the system functions (also known as *shimming*). The stub functions perform operations needed to enable the application to run on the installed version of Windows. Each stub function may optionally call the system function after completing its work. A *compatibility layer* or *mode* contains one or more shims and flags.

## In this section

-   [**APPHELP\_DATA**](apphelp-data.md)
-   [**ATTRINFO**](attrinfo.md)
-   [**BaseFlushAppcompatCache**](baseflushappcompatcache.md)
-   [**FIND\_INFO**](find-info.md)
-   [**INDEXID**](indexid.md)
-   [**PATH\_TYPE**](path-type.md)
-   [**SdbBeginWriteListTag**](sdbbeginwritelisttag.md)
-   [**SdbCloseDatabase**](sdbclosedatabase.md)
-   [**SdbCloseDatabaseWrite**](sdbclosedatabasewrite.md)
-   [**SdbCommitIndexes**](sdbcommitindexes.md)
-   [**SdbCreateDatabase**](sdbcreatedatabase.md)
-   [**SdbDeclareIndex**](sdbdeclareindex.md)
-   [**SdbEndWriteListTag**](sdbendwritelisttag.md)
-   [**SdbFindFirstDWORDIndexedTag**](sdbfindfirstdwordindexedtag.md)
-   [**SdbFindFirstTag**](sdbfindfirsttag.md)
-   [**SdbFindNextTag**](sdbfindnexttag.md)
-   [**SdbFormatAttribute**](sdbformatattribute.md)
-   [**SdbFreeFileAttributes**](sdbfreefileattributes.md)
-   [**SdbGetAppPatchDir**](sdbgetapppatchdir.md)
-   [**SdbGetBinaryTagData**](sdbgetbinarytagdata.md)
-   [**SdbGetFileAttributes**](sdbgetfileattributes.md)
-   [**SdbGetFirstChild**](sdbgetfirstchild.md)
-   [**SdbGetIndex**](sdbgetindex.md)
-   [**SdbGetMatchingExe**](sdbgetmatchingexe.md)
-   [**SdbGetNextChild**](sdbgetnextchild.md)
-   [**SdbGetStringTagPtr**](sdbgetstringtagptr.md)
-   [**SdbGetTagFromTagID**](sdbgettagfromtagid.md)
-   [**SdbInitDatabase**](sdbinitdatabase.md)
-   [**SdbIsStandardDatabase**](sdbisstandarddatabase.md)
-   [**SdbMakeIndexKeyFromString**](sdbmakeindexkeyfromstring.md)
-   [**SdbOpenApphelpDetailsDatabase**](sdbopenapphelpdetailsdatabase.md)
-   [**SdbOpenApphelpResourceFile**](sdbopenapphelpresourcefile.md)
-   [**SdbOpenDatabase**](sdbopendatabase.md)
-   [**SdbQueryDataExTagID**](sdbquerydataextagid.md)
-   [**SDBQUERYRESULT**](sdbqueryresult.md)
-   [**SdbReadApphelpDetailsData**](sdbreadapphelpdetailsdata.md)
-   [**SdbReadBinaryTag**](sdbreadbinarytag.md)
-   [**SdbReadDWORDTag**](sdbreaddwordtag.md)
-   [**SdbReadQWORDTag**](sdbreadqwordtag.md)
-   [**SdbReadStringTag**](sdbreadstringtag.md)
-   [**SdbRegisterDatabaseEx**](sdbregisterdatabaseex.md)
-   [**SdbReleaseDatabase**](sdbreleasedatabase.md)
-   [**SdbReleaseMatchingExe**](sdbreleasematchingexe.md)
-   [**SdbStartIndexing**](sdbstartindexing.md)
-   [**SdbStopIndexing**](sdbstopindexing.md)
-   [**SdbTagRefToTagID**](sdbtagreftotagid.md)
-   [**SdbTagToString**](sdbtagtostring.md)
-   [**SdbUnregisterDatabase**](sdbunregisterdatabase.md)
-   [**SdbWriteBinaryTag**](sdbwritebinarytag.md)
-   [**SdbWriteBinaryTagFromFile**](sdbwritebinarytagfromfile.md)
-   [**SdbWriteDWORDTag**](sdbwritedwordtag.md)
-   [**SdbWriteNULLTag**](sdbwritenulltag.md)
-   [**SdbWriteQWORDTag**](sdbwriteqwordtag.md)
-   [**SdbWriteStringTag**](sdbwritestringtag.md)
-   [**SdbWriteWORDTag**](sdbwritewordtag.md)
-   [**Shim Database Types**](shim-database-types.md)
-   [**ShimFlushCache**](shimflushcache.md)
-   [**TAG**](tag.md)
-   [**TAG Types**](tag-types.md)
-   [**TAGID**](tagid.md)
-   [**TAGREF**](tagref.md)

 

 




---
description: "Learn more about: Temporary Database Parameters"
title: Temporary Database Parameters
TOCTitle: Temporary Database Parameters
ms:assetid: fa1cd867-6ce4-4de5-b31d-5b886f7c1e77
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294140(v=EXCHG.10)
ms:contentKeyID: 32765754
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# Temporary Database Parameters


_**Applies to:** Windows | Windows Server_

## Temporary Database Parameters

This topic contains parameters that are used for the temporary database.

*JET_paramEnableTempTableVersioning*  
46  

This parameter controls the use of transactions in temporary tables. When this parameter is false, temporary tables will be faster but it will not be possible to rollback any updates made in a transaction.


| 
|
| <p>Default Value:</p> | <p>True</p> | 
| <p>Type:</p> | <p>Boolean</p> | 
| <p>Valid Range:</p> | <p>False, True</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>Yes</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramPageTempDBMin*  
19  

This parameter controls the initial size of the temporary database. The size is in database pages. A size of zero indicates that the default size of an ordinary database should be used.

It is often desirable for small applications to configure the temporary database to be as small as possible. Setting this parameter to 14 will achieve the smallest temporary database possible. Note that one can also entirely eliminate the temporary database by setting **JET_paramMaxTemporaryTables** to zero.


| 
|
| <p>Default Value:</p> | <p>0</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>0 – 2147483647</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>Yes</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramTempPath*  
1  

This parameter indicates the relative or absolute file system path of the folder or file that will contain the temporary database for the instance. If the path is to a folder that will contain the temporary database then it must be terminated with a backslash character. The temporary database is used to hold volatile data that is generated in the process of handling ESE API info calls, creating indexes, or storing the contents of a temporary table.

**Note**  If a relative path is specified then it will be relative to the current working directory of the process that hosts the application that is using the database engine.


| 
|
| <p>Default Value:</p> | <p>"tmp.edb"</p> | 
| <p>Type:</p> | <p>Path (string)</p> | 
| <p>Valid Range:</p> | <p>0 – 247 characters</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>Yes</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>All</p> | 



### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[Extensible Storage Engine Files](./extensible-storage-engine-files.md)  
[JetCreateInstance](./jetcreateinstance-function.md)  
[JetInit](./jetinit-function.md)

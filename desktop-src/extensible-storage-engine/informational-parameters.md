---
description: "Learn more about: Informational Parameters"
title: Informational Parameters
TOCTitle: Informational Parameters
ms:assetid: 48500fc9-6d89-45b8-92ad-afb997b729f3
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269241(v=EXCHG.10)
ms:contentKeyID: 32765543
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

# Informational Parameters


_**Applies to:** Windows | Windows Server_

## Informational Parameters

This topic contains parameters that are used to expose information about the database engine.

*JET_paramKeyMost*  
134  

This read-only parameter indicates the maximum allowable index key length that can be selected for the current database page size (as configured by JET_paramDatabasePageSize).


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>JET_cbKeyMost4KBytePage</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>255 – 65535</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>N/A</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>N/A</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>Starting with Windows Server 2008 and Windows Vista</p> | 



*JET_paramMaxColtyp*  
131  

This read only parameter returns the maximum [JET_COLTYP](./jet-coltyp.md) (JET_coltypMax) for that version of the database engine. This value can be used to test for support of a specific [JET_COLTYP](./jet-coltyp.md). If a given [JET_COLTYP](./jet-coltyp.md) is less than the value of this parameter then it is supported by the database engine.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>JET_coltypUnsignedShort + 1</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>0 – 255</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>N/A</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>N/A</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>Starting with Windows Server 2008 and Windows Vista</p> | 



*JET_paramLVChunkSizeMost*  
163  

Read only parameter that returns the long-value chunk size based on configured page size. If a long-value is to be read or written with multiple Jet{Set,Retrieve}Column calls then using a buffer whose size is a multiple of the chunk size is more efficient.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>2kb page = 1966 bytes<br />4kb page = 4014 bytes<br />8kb page = 8110 bytes<br />16kb page = 4050 bytes<br />32kb page = 8150 bytes</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>0-10000</p> | 
| <p>Scope:</p> | <p></p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p></p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p></p> | 
| <p>Affects Physical Layout:</p> | <p></p> | 
| <p>Affects Reliability:</p> | <p></p> | 
| <p>Affects Performance:</p> | <p></p> | 
| <p>Affects Resources:</p> | <p></p> | 
| <p>Availability:</p> | <p></p> | 



### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JetCreateInstance](./jetcreateinstance-function.md)  
[JetInit](./jetinit-function.md)  
[JET_COLTYP](./jet-coltyp.md)

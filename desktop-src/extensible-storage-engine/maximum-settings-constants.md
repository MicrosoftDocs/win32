---
description: "Learn more about: Maximum Settings Constants"
title: Maximum Settings Constants
TOCTitle: Maximum Settings Constants
ms:assetid: 1111051f-55af-4c33-be38-6a3973c2c815
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269189(v=EXCHG.10)
ms:contentKeyID: 32765492
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

# Maximum Settings Constants


_**Applies to:** Windows | Windows Server_

## Maximum Settings Constants

These constants provide the maximum settings that are allowed on items in an ESE database.


| <p>Constant/value</p> | <p>Description</p> | 
|-----------------------|--------------------|
| <p>JET_BASE_NAME_LENGTH<br />3</p> | <p>Sets the length for the prefix used to name files that are used by the database engine. This length is applicable to the name set for the <a href="gg269235(v=exchg.10).md">JET_paramBaseName</a> system parameter.</p> | 
| <p>JET_MAX_COMPUTERNAME_LENGTH<br />15</p> | <p>Sets the maximum length for <a href="gg269340(v=exchg.10).md">JET_SIGNATURE</a>.</p> | 
| <p>JET_cbBookmarkMost<br />256</p> | <p>The default maximum size of a bookmark. This is valid when the key size is left at its default value.</p> | 
| <p>JET_cbBookmarkMostMost<br />2000</p> | <p>The maximum size of a bookmark when esent is configured to have the largest keys possible.</p><p><strong>Windows 7:</strong> JET_cbBookmarkMostMost is introduced in Windows 7.</p> | 
| <p>JET_cbNameMost<br />64</p> | <p>The maximum length of a object, column, index, or property name.</p><p><strong>Note</strong>  If Unicode, the value is 128.</p> | 
| <p>JET_cbFullNameMost<br />255</p> | <p>The maximum length of a "name.name.name..." construct.</p><p><strong>Note</strong>  If Unicode, the value is 510.</p> | 
| <p>JET_cbColumnLVPageOverhead<br />82</p> | <p>This number can be used to compute the maximum amount of a BLOB that can be stored by the database engine on a single database page. The formula is max size = JET_paramDatabasePageSize–JET_cbColumnLVPageOverhead.</p><p>This value is now obsolete. The long-value chunk size should be retrieved with the JET_paramLVChunkSizeMost parameter.</p> | 
| <p>JET_cbColumnMost<br />255</p> | <p>The maximum size of non-long-value column data.</p> | 
| <p>JET_cbLVDefaultValueMost<br />255</p> | <p>The maximum size of a long-value (LongBinary or LongText) column default value.</p> | 
| <p>JET_cbKeyMost<br />255</p> | <p>The default maximum size of a sort or index key.</p> | 
| <p>JET_cbKeyMostMost<br />2000</p> | <p>The maximum configurable size of a sort or index key for any page size. (See JET_INDEXCREATE2.cbKeyMost)</p><p><strong>Windows 7:</strong> JET_cbKeyMostMost is introduced in the Windows 7 operating system.</p> | 
| <p>JET_cbKeyMost2KBytePage<br />500</p> | <p>The maximum allowable maximum configurable size for an index key in a database using 2048 byte pages. See <a href="gg269186(v=exchg.10).md">JET_INDEXCREATE</a> for more information.</p><p><strong>Windows Vista:</strong> JET_cbKeyMost2KBytePage is introduced in the Windows Vista operating system.</p> | 
| <p>JET_cbKeyMost4KBytePage<br />1000</p> | <p>The maximum allowable maximum configurable size for an index key in a database using 4096 byte pages. See <a href="gg269186(v=exchg.10).md">JET_INDEXCREATE</a> for more information.</p><p><strong>Windows Vista:</strong> JET_cbKeyMost4KBytePage is introduced in Windows Vista.</p> | 
| <p>JET_cbKeyMost8KBytePage<br />2000</p> | <p>The maximum allowable maximum configurable size for an index key in a database using 8192 byte pages. See <a href="gg269186(v=exchg.10).md">JET_INDEXCREATE</a> for more information.</p><p><strong>Windows Vista:  </strong>JET_cbKeyMost8KBytePage is introduced in Windows Vista</p> | 
| <p>JET_cbKeyMostMin<br />255</p> | <p>The minimum allowable maximum size for an index key. See <a href="gg269186(v=exchg.10).md">JET_INDEXCREATE</a> for more information.</p><p><strong>Windows Vista:  </strong>JET_cbKeyMostMin is introduced in Windows Vista.</p> | 
| <p>JET_cbLimitKeyMost<br />256</p> | <p>The maximum key size when the key is formed by using a limit <em>grbit</em>, such as JET_bitStrLimit, which is used in the <a href="gg269329(v=exchg.10).md">JetMakeKey</a> function.</p> | 
| <p>JET_cbPrimaryKeyMost<br />255</p> | <p>The maximum size of the primary index. This is now obsolete.</p> | 
| <p>JET_cbSecondaryKeyMost<br />255</p> | <p>The maximum size of the secondary index. This is now obsolete.</p> | 
| <p>JET_ccolKeyMost<br />12</p> | <p>The maximum number of components in a sort or index key.</p><p><strong>Windows Vista:  </strong>In Windows Vista and later versions of Windows the value is 16.</p> | 
| <p>JET_ccolMost<br />0x0000fee0</p> | <p>The maximum number of columns allowed in a table.</p><p><strong>Windows XP:  </strong>The value 0x0000fee0 is used in Windows XP and later and later versions of Windows</p><p><strong>Windows 2000:  </strong>The value 0x00007ffe is used in Windows 2000.</p> | 
| <p>JET_ccolFixedMost<br />0x0000007f</p> | <p>The maximum number of fixed columns allowed in a table, currently 127.</p> | 
| <p>JET_ccolVarMost<br />0x00000080</p> | <p>The maximum number of variable-length columns that can be contained in a table, currently 128.</p> | 
| <p>JET_ccolTaggedMost<br />( JET_ccolMost - 0x000000ff )</p> | <p>The maximum number of tagged columns that can be contained in a table, currently 64993.</p> | 



### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



---
description: "Learn more about: JET_SNP"
title: JET_SNP
TOCTitle: JET_SNP
ms:assetid: 7f3d1cc5-7b27-454d-8dd1-584ab4b60ab0
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269311(v=EXCHG.10)
ms:contentKeyID: 32765601
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

# JET_SNP


_**Applies to:** Windows | Windows Server_

## JET_SNP

The **JET_SNP** group of constants describe the type of the operation for which progress information is to be obtained. These constants are used as the *snp* parameter of the [JET_PFNSTATUS](./jet-pfnstatus-callback-function.md) callback function.


| <p>Constant/value</p> | <p>Description</p> | 
|-----------------------|--------------------|
| <p>JET_snpRepair<br />2</p> | <p>The callback is for a repair operation.</p> | 
| <p>JET_snpCompact<br />4</p> | <p>The callback is for database defragmentation.</p> | 
| <p>JET_snpRestore<br />8</p> | <p>The callback is for a restore operation.</p> | 
| <p>JET_snpBackup<br />9</p> | <p>The callback is for a backup operation.</p> | 
| <p>JET_snpUpgrade<br />10</p> | <p>Not supported.</p><p><strong>Windows 2000:</strong>  The callback is for the database format upgrade operation.</p> | 
| <p>JET_snpScrub<br />11</p> | <p>The callback is for a database zeroing (that is, scrubbing) operation.</p><p><strong>Windows Server 2003 and Windows 2000 Server:</strong>  Not supported.</p> | 
| <p>JET_snpUpgradeRecordFormat<br />12</p> | <p>The callback is for the process of upgrading the record format of all database pages.</p><p><strong>Windows Server 2003 and Windows 2000 Server:</strong>  Not supported.</p> | 



### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JET_PFNSTATUS](./jet-pfnstatus-callback-function.md)  
[JET_SNPROG](./jet-snprog-structure.md)  
[JET_SNT](./jet-snt.md)

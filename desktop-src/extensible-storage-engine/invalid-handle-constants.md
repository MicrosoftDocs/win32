---
description: "Learn more about: Invalid Handle Constants"
title: Invalid Handle Constants
TOCTitle: Invalid Handle Constants
ms:assetid: 594d7804-725f-4f72-b5f0-56f099c1c17b
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269256(v=EXCHG.10)
ms:contentKeyID: 32765558
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

# Invalid Handle Constants


_**Applies to:** Windows | Windows Server_

## Invalid Handle Constants

The following constants indicate invalid handles for different aspects of ESE.


| <p>Constant/value</p> | <p>Description</p> | 
|-----------------------|--------------------|
| <p>JET_instanceNil<br />(~(JET_INSTANCE)0)</p> | <p>An invalid handle for a database instance.<br /><strong>Windows XP:</strong> Introduced in Windows XP.</p> | 
| <p>JET_sesidNil<br />(~(JET_SESID)0)</p> | <p>An invalid handle for a session ID.</p> | 
| <p>JET_tableidNil<br />(~(JET_TABLEID)0)</p> | <p>An invalid handle for a table ID.</p> | 
| <p>JET_bitNil<br />((JET_GRBIT)0)</p> | <p>An invalid handle for a group of bits.</p> | 
| <p>JET_LSNil<br />(~(JET_LS)0)</p> | <p>An invalid handle for the Local Storage.</p> | 
| <p>JET_dbidNil<br />((JET_DBID) 0xFFFFFFFF)</p> | <p>An invalid handle for the database ID.</p> | 



### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



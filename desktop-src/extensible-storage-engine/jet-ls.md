---
description: "Learn more about: JET_LS"
title: JET_LS
TOCTitle: JET_LS
ms:assetid: 8e4e7902-84b1-404b-8654-bb430a0952aa
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269336(v=EXCHG.10)
ms:contentKeyID: 32765625
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

# JET_LS


_**Applies to:** Windows | Windows Server_

## JET_LS

The **JET_LS** data type contains a context handle to local storage (LS).This handle might be associated with a cursor or a table and might refer to dynamically allocated resources.

**Windows XP:  JET_LS** is introduced in Windows XP.

```cpp
    typedef JET_API_PTR JET_LS;
```

### Data Types

JET_LS

A value of JET_LSNil indicates an invalid context handle.

### Remarks

A context handle is initially associated with the **JET_LS** data type, using [JetSetLS](./jetsetls-function.md). The context handle can be retrieved from the **JET_LS** data type, using [JetGetLS](./jetgetls-function.md).

The context handle can be explicitly disassociated from the **JET_LS** data type using [JetGetLS](./jetgetls-function.md) with JET_bitLSReset. Alternatively, the context handle can be implicitly disassociated from the **JET_LS** data type when the underlying object is released by the database engine as a result of direct or indirect action by the application. In the implicit case, a runtime callback is issued to the application so that it can clean up the context handle. For more information on implicitly disassociating from the **JET_LS** data type, see [JetSetLS](./jetsetls-function.md).

The following flags are associated with the JET_LS data type.


| <p>Term</p> | <p>Description</p> | 
|-------------|--------------------|
| <p>JET_bitLSReset</p> | <p>The context handle is disassociated from the object.</p> | 
| <p>JET_bitLSCursor</p> | <p>Set or retrieve the local storage associated with a table cursor.</p> | 
| <p>JET_bitLSTable</p> | <p>Set or retrieve the local storage associated with a table.</p> | 
| <p>JET_LSNil</p> | <p>The context handle is invalid.</p> | 



### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JetSetLS](./jetsetls-function.md)  
[JetGetLS](./jetgetls-function.md)

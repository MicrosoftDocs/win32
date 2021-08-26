---
description: "Learn more about: JET_PCWSTR"
title: JET_PCWSTR
TOCTitle: JET_PCWSTR
ms:assetid: fef64bb9-c2e0-4cfb-8138-c98ae6f50952
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294145(v=EXCHG.10)
ms:contentKeyID: 32765759
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

# JET_PCWSTR


_**Applies to:** Windows | Windows Server_

## JET_PCWSTR

The **JET_PCWSTR** data type contains a null-terminated, constant **Unicode** string (char \*).

**Windows Vista:  JET_PCWSTR** is introduced in Windows Vista.

```cpp
    typedef __nullterminated const WCHAR * JET_PCWSTR;
```

### Data Types

JET_PCWSTR

Null-terminated, constant Unicode string (char \*).

### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



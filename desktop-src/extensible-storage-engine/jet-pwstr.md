---
description: "Learn more about: JET_PWSTR"
title: JET_PWSTR
TOCTitle: JET_PWSTR
ms:assetid: 6575f0f0-d022-4e70-9f17-c1d884d9e226
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269271(v=EXCHG.10)
ms:contentKeyID: 32765573
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

# JET_PWSTR


_**Applies to:** Windows | Windows Server_

## JET_PWSTR

The **JET_PWSTR** data type contains a null-terminated **Unicode** string (char \*).

**Windows Vista:  JET_PWSTR** is introduced in Windows Vista.

```cpp
    typedef __nullterminated WCHAR * JET_PWSTR;
```

### Data Types

JET_PWSTR

Null-terminated, Unicode string (char \*).

### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



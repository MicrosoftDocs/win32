---
title: MUASORT enumeration
description: Do not use. Specifies how the Contact List should be sorted.
ms.assetid: 5a28f13e-5d58-4d27-8959-553d682f5a1e
keywords:
- MUASORT enumeration Windows Messenger
- LockError enumeration Windows Messenger
topic_type:
- apiref
api_name:
- LockError
api_location:
- Msgrua.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MUASORT enumeration

\[**MUASORT** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Specifies how the Contact List should be sorted.

## Syntax


```C++
typedef enum  { 
  MUASORT_GROUPS,
  MUASORT_ONOFFLINE  = 1
} LockError;
```



## Constants

<dl> <dt>

<span id="MUASORT_GROUPS"></span><span id="muasort_groups"></span>**MUASORT\_GROUPS**
</dt> <dd>

Sorts the local user's contacts by groups.

</dd> <dt>

<span id="MUASORT_ONOFFLINE"></span><span id="muasort_onoffline"></span>**MUASORT\_ONOFFLINE**
</dt> <dd>

Sorts the local user's contacts by online/offline status.

</dd> </dl>

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |



 

 






---
title: NNTPGROUP structure
description: The response from the CommandGROUP function.
ms.assetid: d8c72157-8815-4283-879e-5e1c3d1a0ed9
keywords:
- NNTPGROUP structure Windows Mail (formerly Outlook Express)
- LPNNTPGROUP structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- NNTPGROUP
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# NNTPGROUP structure

\[**NNTPGROUP** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

The response from the [**CommandGROUP**](oe-inntptransport-commandgroup.md) function. The data is the current status of the group that was switched to.

## Syntax


```C++
typedef struct tagNNTPGROUP {
  DWORD dwCount;
  DWORD dwFirst;
  DWORD dwLast;
  LPSTR pszGroup;
} NNTPGROUP, *LPNNTPGROUP;
```



## Members

<dl> <dt>

**dwCount**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Estimated number of articles in the group

</dd> <dt>

**dwFirst**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

First article number in the group

</dd> <dt>

**dwLast**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Last article number in the group

</dd> <dt>

**pszGroup**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Name of the group

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 






---
title: CARD\_FILE\_INFO structure
description: Contains information about a file on a smart card.
ms.assetid: 9acabc20-1de5-44ee-827f-08a8042e6f75
keywords:
- CARD_FILE_INFO structure Security
- PCARD_FILE_INFO structure pointer Security
topic_type:
- apiref
api_name:
- CARD_FILE_INFO
api_location:
- Cardmod.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# CARD\_FILE\_INFO structure

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CARD\_FILE\_INFO** structure contains information about a file on a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
typedef struct _CARD_FILE_INFO {
  DWORD                      dwVersion;
  DWORD                      cbFileSize;
  CARD_FILE_ACCESS_CONDITION AccessCondition;
} CARD_FILE_INFO, *PCARD_FILE_INFO;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

The version number of the structure.

</dd> <dt>

**cbFileSize**
</dt> <dd>

The size, in bytes, of the file.

</dd> <dt>

**AccessCondition**
</dt> <dd>

A [**CARD\_FILE\_ACCESS\_CONDITION**](https://msdn.microsoft.com/library/windows/desktop/aa375998) enumeration value that specifies access control permissions for the file.

</dd> </dl>

## Remarks

The [**CardGetFileInfo**](cardgetfileinfo.md) function initializes this structure.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md)
</dt> <dt>

[**CardCreateFile**](cardcreatefile.md)
</dt> <dt>

[**CardGetFileInfo**](cardgetfileinfo.md)
</dt> </dl>

 

 






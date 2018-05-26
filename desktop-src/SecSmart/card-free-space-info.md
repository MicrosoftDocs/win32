---
title: CARD\_FREE\_SPACE\_INFO structure
description: Contains information about the amount of available memory on a smart card.
ms.assetid: 698ba08f-320a-4d12-baef-536ea95fda5b
keywords:
- CARD_FREE_SPACE_INFO structure Security
- PCARD_FREE_SPACE_INFO structure pointer Security
topic_type:
- apiref
api_name:
- CARD_FREE_SPACE_INFO
api_location:
- Cardmod.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CARD\_FREE\_SPACE\_INFO structure

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CARD\_FREE\_SPACE\_INFO** structure contains information about the amount of available memory on a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
typedef struct _CARD_FREE_SPACE_INFO {
  DWORD dwVersion;
  DWORD dwBytesAvailable;
  DWORD dwKeyContainersAvailable;
  DWORD dwMaxKeyContainers;
} CARD_FREE_SPACE_INFO, *PCARD_FREE_SPACE_INFO;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

The version number of the structure.

</dd> <dt>

**dwBytesAvailable**
</dt> <dd>

The number of bytes of memory available on the smart card.

</dd> <dt>

**dwKeyContainersAvailable**
</dt> <dd>

The number of [*key containers*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-container-gly) available on the smart card.

</dd> <dt>

**dwMaxKeyContainers**
</dt> <dd>

The maximum number of key containers that the smart card supports.

</dd> </dl>

## Remarks

The [**CardQueryFreeSpace**](cardqueryfreespace.md) function initializes this structure. The **CardQueryFreeSpace** function should set any values that are not known to **CARD\_DATA\_VALUE\_UNKNOWN**.

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

[**CardQueryFreeSpace**](cardqueryfreespace.md)
</dt> </dl>

 

 






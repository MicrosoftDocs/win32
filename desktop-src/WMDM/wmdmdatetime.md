---
title: WMDMDATETIME structure
description: The WMDMDATETIME structure contains a date and time of day.
ms.assetid: 47f3994d-66c6-47e4-803d-0c98c70eccc8
keywords:
- WMDMDATETIME structure windows Media Device Manager
- PWMDMDATETIME structure pointer windows Media Device Manager
topic_type:
- apiref
api_name:
- WMDMDATETIME
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDMDATETIME structure

The **WMDMDATETIME** structure contains a date and time of day.

## Syntax


```C++
typedef struct _WMDMDATETIME {
  WORD wYear;
  WORD wMonth;
  WORD wDay;
  WORD wHour;
  WORD wMinute;
  WORD wSecond;
} WMDMDATETIME, *PWMDMDATETIME;
```



## Members

<dl> <dt>

**wYear**
</dt> <dd>

Word containing the four-digit year.

</dd> <dt>

**wMonth**
</dt> <dd>

Word containing the month (1-12).

</dd> <dt>

**wDay**
</dt> <dd>

Word containing the day of the month (1-31).

</dd> <dt>

**wHour**
</dt> <dd>

Word containing the hour (0-23).

</dd> <dt>

**wMinute**
</dt> <dd>

Word containing the minute (0-59).

</dd> <dt>

**wSecond**
</dt> <dd>

Word containing the second (0-59).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMDSPStorage::GetDate**](/windows/desktop/api/mswmdm/nf-mswmdm-imdspstorage-getdate)
</dt> <dt>

[**IWMDMStorage::GetDate**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage-getdate)
</dt> <dt>

[**WMDMRIGHTS**](wmdmrights.md)
</dt> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 






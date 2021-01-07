---
description: The JOB\_INFO\_3 structure is used to link together a set of print jobs.
ms.assetid: a110f555-dc33-450c-ae77-ea26f0f69448
title: JOB_INFO_3 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- JOB_INFO_3
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# JOB\_INFO\_3 structure

The **JOB\_INFO\_3** structure is used to link together a set of print jobs.

## Syntax


```C++
typedef struct _JOB_INFO_3 {
  DWORD JobId;
  DWORD NextJobId;
  DWORD Reserved;
} JOB_INFO_3, *PJOB_INFO_3;
```



## Members

<dl> <dt>

**JobId**
</dt> <dd>

The print job identifier.

</dd> <dt>

**NextJobId**
</dt> <dd>

The print job identifier for the next print job in the linked set of print jobs.

</dd> <dt>

**Reserved**
</dt> <dd>

This value is reserved for future use. You must set it to zero.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**EnumJobs**](enumjobs.md)
</dt> <dt>

[**GetJob**](getjob.md)
</dt> <dt>

[**SetJob**](setjob.md)
</dt> </dl>

 

 





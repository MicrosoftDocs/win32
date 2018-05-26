---
Description: Contains auxiliary information used for Initiator, Target, LUN, and Queue (I\_T\_L\_Q) nexus and multi- data-sequence SCSI pass-through operations.
ms.assetid: 795EED23-D45C-4024-81F4-3514FDA09DEA
title: SCSI\_PASS\_THROUGH\_AUXILIARY structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SCSI\_PASS\_THROUGH\_AUXILIARY structure

\[The following structure is available for use in Windows Server 2012 R2. It may be altered or unavailable in subsequent versions.\]

Contains auxiliary information used for Initiator, Target, LUN, and Queue (I\_T\_L\_Q) nexus and multi- data-sequence SCSI pass-through operations.

## Syntax


```C++
typedef struct _SCSI_PASS_THROUGH_AUXILIARY {
  ULONG          Size;
  UCHAR          Signature[SCSI_PASS_THROUGH_ISCSITGT_SIGNATURE_SIZE];
  SESSION_COOKIE SessionCookie;
  TASK_COOKIE    TaskCookie;
  ULONG          SequenceByteOffset;
  BOOL           IsFinal;
  ULONG          Lun;
} SCSI_PASS_THROUGH_AUXILIARY, *PSCSI_PASS_THROUGH_AUXILIARY;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

Size of the **SCSI\_PASS\_THROUGH\_AUXILIARY** structure.

</dd> <dt>

**Signature**
</dt> <dd>

Signature of the **SCSI\_PASS\_THROUGH\_AUXILIARY** structure.

**SCSI\_PASS\_THROUGH\_ISCSITGT\_SIGNATURE\_SIZE** is defined as 8.

</dd> <dt>

**SessionCookie**
</dt> <dd>

An opaque handle representing a session.

</dd> <dt>

**TaskCookie**
</dt> <dd>

An opaque handle representing the task to which the pass-through operation belongs.

</dd> <dt>

**SequenceByteOffset**
</dt> <dd>

Data sequence offset. An offset of 0 indicates the first data sequence.

</dd> <dt>

**IsFinal**
</dt> <dd>

Whether the data sequence is the final one for the SCSI request.

</dd> <dt>

**Lun**
</dt> <dd>

Initiator-visible Logical Unit Number (LUN).

</dd> </dl>

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                               |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/> |
| End of client support<br/>    | None supported<br/>                               |
| End of server support<br/>    | Windows Server 2012 R2<br/>                       |



## See also

<dl> <dt>

[iSCSI Target Pass-Through](iscsi-target-pass-through.md)
</dt> <dt>

[**SCSI\_PASS\_THROUGH\_DIRECT\_WITH\_AUXILIARY**](scsi-pass-through-direct-with-auxiliary.md)
</dt> </dl>

 

 





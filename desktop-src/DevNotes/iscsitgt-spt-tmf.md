---
Description: Used with the IOCTL\_SCSI\_MINIPORT IOCTL and the CTLCODE\_ISCSITGT\_SPT\_TMF (0x102) control code to invoke a task management function.
ms.assetid: 9683A407-BC36-40E4-A637-17CA7B88F485
title: ISCSITGT\_SPT\_TMF structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ISCSITGT\_SPT\_TMF structure

\[The following structure is available for use in Windows Server 2012 R2. It may be altered or unavailable in subsequent versions.\]

Used with the [**IOCTL\_SCSI\_MINIPORT**](https://msdn.microsoft.com/5a9facc7-c83e-4dd4-9fb4-e3385c1b94ea) IOCTL and the CTLCODE\_ISCSITGT\_SPT\_TMF (0x102) control code to invoke a task management function.

## Syntax


```C++
typedef struct _ISCSITGT_SPT_TMF {
  SRB_IO_CONTROL  Header;
   SESSION_COOKIE ITNexusHandle;
   ULONG          Lun;
   BYTE           TaskManagementFunction;
  TASK_COOKIE     ReferenceTaskCookie;
   BYTE           Response;
} ISCSITGT_SPT_TMF, *PISCSITGT_SPT_TMF;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Mandatory header.

</dd> <dt>

**ITNexusHandle**
</dt> <dd>

An opaque handle representing a session.

</dd> <dt>

**Lun**
</dt> <dd>

Initiator-visible logical unit number (LUN).

</dd> <dt>

**TaskManagementFunction**
</dt> <dd>

iSCSI task management function (TMF) code.

</dd> <dt>

**ReferenceTaskCookie**
</dt> <dd>

Optional. Reference task cookie. Valid when the TMF code is **ABORT TASK**.

</dd> <dt>

**Response**
</dt> <dd>

iSCSI TMF response code.

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

[**SRB\_IO\_CONTROL**](https://msdn.microsoft.com/754d2a4c-6a22-4c25-87e2-e30e87b9c1ba)
</dt> </dl>

 

 





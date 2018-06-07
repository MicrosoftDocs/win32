---
Description: Used with the IOCTL\_SCSI\_MINIPORT IOCTL and the CTLCODE\_ISCSITGT\_SPT\_SESSION\_END (0x101) control code to stop a session.
ms.assetid: 74DAA560-A5BA-475C-AA36-7E6F0EA82EFE
title: ISCSITGT\_SPT\_SESSION\_STOP structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ISCSITGT\_SPT\_SESSION\_STOP structure

\[The following structure is available for use in Windows Server 2012 R2. It may be altered or unavailable in subsequent versions.\]

Used with the [**IOCTL\_SCSI\_MINIPORT**](https://msdn.microsoft.com/5a9facc7-c83e-4dd4-9fb4-e3385c1b94ea) IOCTL and the CTLCODE\_ISCSITGT\_SPT\_SESSION\_END (0x101) control code to stop a session.

## Syntax


```C++
typedef struct _ISCSITGT_SPT_SESSION_STOP {
  SRB_IO_CONTROL Header;
  SESSION_COOKIE ITNexusHandle;
} ISCSITGT_SPT_SESSION_STOP, *PISCSITGT_SPT_SESSION_STOP;
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

 

 





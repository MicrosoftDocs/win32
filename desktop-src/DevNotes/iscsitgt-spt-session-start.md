---
Description: Used with the IOCTL\_SCSI\_MINIPORT IOCTL and the CTLCODE\_ISCSITGT\_SPT\_SESSION\_START (0x100) control code to start a session.
ms.assetid: 2DB99F57-A721-4A63-BA3D-8BDAE40BFE25
title: ISCSITGT\_SPT\_SESSION\_START structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ISCSITGT\_SPT\_SESSION\_START structure

\[The following structure is available for use in Windows Server 2012 R2. It may be altered or unavailable in subsequent versions.\]

Used with the [**IOCTL\_SCSI\_MINIPORT**](https://msdn.microsoft.com/en-us/library/Ff560512(v=VS.85).aspx) IOCTL and the CTLCODE\_ISCSITGT\_SPT\_SESSION\_START (0x100) control code to start a session.

## Syntax


```C++
typedef struct _ISCSITGT_SPT_SESSION_START {
  SRB_IO_CONTROL Header;
  BOOL           IsReinstated;
  SESSION_COOKIE ITNexusHandle;
  WCHAR          PeerAddress[SCSI_PASS_THROUGH_MAX_IPADDR_STRING_LENGTH];
  WCHAR          ITNexus[SCSI_PASS_THROUGH_MAX_ITNEXUS_STRING_LENGTH];
  WCHAR          ChapUserName[SCSI_PASS_THROUGH_MAX_CHAP_USERNAME_LENGTH];
} ISCSITGT_SPT_SESSION_START, *PISCSITGT_SPT_SESSION_START;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Mandatory header.

</dd> <dt>

**IsReinstated**
</dt> <dd>

Whether this is a reinstated session.

</dd> <dt>

**ITNexusHandle**
</dt> <dd>

An opaque handle representing a session.

</dd> <dt>

**PeerAddress**
</dt> <dd>

The peer IP address.

**SCSI\_PASS\_THROUGH\_MAX\_IPADDR\_STRING\_LENGTH** is defined as 64.

</dd> <dt>

**ITNexus**
</dt> <dd>

A NULL-terminated I\_T nexus identifier.

**SCSI\_PASS\_THROUGH\_MAX\_ITNEXUS\_STRING\_LENGTH** is defined as 512.

</dd> <dt>

**ChapUserName**
</dt> <dd>

Optional. Challenge Handshake Authentication Protocol (CHAP) user name if CHAP is used for this session.

**SCSI\_PASS\_THROUGH\_MAX\_CHAP\_USERNAME\_LENGTH** is defined as 256.

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

[**SRB\_IO\_CONTROL**](https://msdn.microsoft.com/en-us/library/Ff566339(v=VS.85).aspx)
</dt> </dl>

 

 





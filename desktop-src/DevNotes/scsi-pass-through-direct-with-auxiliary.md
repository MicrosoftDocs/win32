---
Description: 'Combines a SCSI\_PASS\_THROUGH\_DIRECT structure with sense data and auxiliary information.'
ms.assetid: 'BA7056D1-0FD6-4769-BCFB-59335A96C503'
title: 'SCSI\_PASS\_THROUGH\_DIRECT\_WITH\_AUXILIARY structure'
---

# SCSI\_PASS\_THROUGH\_DIRECT\_WITH\_AUXILIARY structure

\[The following structure is available for use in Windows Server 2012 R2. It may be altered or unavailable in subsequent versions.\]

Combines a **SCSI\_PASS\_THROUGH\_DIRECT** structure with sense data and auxiliary information.

## Syntax


```C++
typedef struct _SCSI_PASS_THROUGH_DIRECT_WITH_AUXILIARY {
  SCSI_PASS_THROUGH_DIRECT    ScsiPassThroughDirect;
  SCSI_PASS_THROUGH_AUXILIARY  ScsiPassThroughAuxiliary;
  SENSE_DATA                  SenseData;
} SCSI_PASS_THROUGH_DIRECT_WITH_AUXILIARY, *PSCSI_PASS_THROUGH_DIRECT_WITH_AUXILIARY;
```



## Members

<dl> <dt>

**ScsiPassThroughDirect**
</dt> <dd>

Information used to send an embedded SCSI command to the target device.

</dd> <dt>

 **ScsiPassThroughAuxiliary**
</dt> <dd>

Auxiliary information used for Initiator, Target, LUN, and Queue (I\_T\_L\_Q) nexus and multi-data-sequence SCSI pass-through operations.

</dd> <dt>

**SenseData**
</dt> <dd>

Device status or error information.

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

[**SCSI\_PASS\_THROUGH\_DIRECT**](scsi-pass-through-direct-with-auxiliary.md)
</dt> <dt>

[**SCSI\_PASS\_THROUGH\_AUXILIARY**](scsi-pass-through-auxiliary.md)
</dt> <dt>

[**SENSE\_DATA**](sense-data.md)
</dt> </dl>

 

 





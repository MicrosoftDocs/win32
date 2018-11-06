---
Description: Data structures for iSCSI Target pass-through devices.
ms.assetid: 5ADD3595-4582-4D49-9F77-F863370A225C
title: iSCSI Target Pass-Through
ms.topic: article
ms.date: 05/31/2018
---

# iSCSI Target Pass-Through

Data structures for iSCSI Target pass-through devices.

## In this section



| Topic                                                                                                      | Description                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ISCSITGT\_SPT\_SESSION\_START**](iscsitgt-spt-session-start.md)<br/>                             | Used with the [**IOCTL\_SCSI\_MINIPORT**](https://msdn.microsoft.com/en-us/library/Ff560512(v=VS.85).aspx) IOCTL and the CTLCODE\_ISCSITGT\_SPT\_SESSION\_START (0x100) control code to start a session.<br/>        |
| [**ISCSITGT\_SPT\_SESSION\_STOP**](iscsitgt-spt-session-stop.md)<br/>                               | Used with the [**IOCTL\_SCSI\_MINIPORT**](https://msdn.microsoft.com/en-us/library/Ff560512(v=VS.85).aspx) IOCTL and the CTLCODE\_ISCSITGT\_SPT\_SESSION\_END (0x101) control code to stop a session.<br/>           |
| [**ISCSITGT\_SPT\_TMF**](iscsitgt-spt-tmf.md)<br/>                                                  | Used with the [**IOCTL\_SCSI\_MINIPORT**](https://msdn.microsoft.com/en-us/library/Ff560512(v=VS.85).aspx) IOCTL and the CTLCODE\_ISCSITGT\_SPT\_TMF (0x102) control code to invoke a task management function.<br/> |
| [**SCSI\_PASS\_THROUGH\_AUXILIARY**](scsi-pass-through-auxiliary.md)<br/>                           | Contains auxiliary information used for Initiator, Target, LUN, and Queue (I\_T\_L\_Q) nexus and multi- data-sequence SCSI pass-through operations.<br/>                         |
| [**SCSI\_PASS\_THROUGH\_DIRECT\_WITH\_AUXILIARY**](scsi-pass-through-direct-with-auxiliary.md)<br/> | Combines a [**SCSI\_PASS\_THROUGH\_DIRECT**](scsi-pass-through-direct-with-auxiliary.md) structure with sense data and auxiliary information.<br/>                              |
| [**SENSE\_DATA**](sense-data.md)<br/>                                                               | Used to report status or error information in response to a SCSI **Request Sense** command.<br/>                                                                                 |



 

 

 





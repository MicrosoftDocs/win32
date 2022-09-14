---
title: Windows Defender Structures
description: Structures used by apps when calling to request scans, signature updates, or information from Windows Defender.
ms.assetid: EF4116D3-DA50-4078-A024-2D624945D8C1
ms.topic: article
ms.date: 05/31/2018
---

# Windows Defender Structures

Structures used by apps when calling to request scans, signature updates, or information from Windows Defender.



| Structure                                                      | Description                                                                             |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**MPCALLBACK\_DATA**](mpcallback-data.md)                    | Data passed to the callback function.<br/>                                        |
| [**MPCLEAN\_DATA**](mpclean-data.md)                          | Notification data passed to clean callback function.<br/>                         |
| [**MPCLEAN\_PRECHECK\_DATA**](mpclean-precheck-data.md)       | Notification data passed to clean precheck callback function.<br/>                |
| [**MPCOMPONENT\_STATUS**](mpcomponent-status.md)              | Component status information.<br/>                                                |
| [**MPCOMPONENT\_VERSION**](mpcomponent-version.md)            | Version and update time for an individual component.<br/>                         |
| [**MPCONFIGURATION\_DATA**](mpconfiguration-data.md)          | Contains data about configuration changes, including the old and new values.<br/> |
| [**MPENDOFLIFE\_DATA**](mpendoflife-data.md)                  | "End of life" notification data.<br/>                                             |
| [**MPEXPIRATION\_DATA**](mpexpiration-data.md)                | Product expiration status notification.<br/>                                      |
| [**MPFASTPATH\_DATA**](mpfastpath-data.md)                    | FastPath update notification.<br/>                                                |
| [**MPHEALTH\_DATA**](mphealth-data.md)                        | Health notification data.<br/>                                                    |
| [**MPMALWARETOAST\_DATA**](mpmalwaretoast-data.md)            | Malware toast notification data.<br/>                                             |
| [**MPNIS\_PRIVATE\_DATA**](mpnis-private-data.md)             | Private NIS notifications.<br/>                                                   |
| [**MPRESERVED\_DATA**](mpreserved-data.md)                    | Reserved notification data.<br/>                                                  |
| [**MPRESOURCE\_INFO**](mpresource-info.md)                    | Resource information structure.<br/>                                              |
| [**MPRESOURCE\_STATS**](mpresource-stats.md)                  | Resource-related statistics.<br/>                                                 |
| [**MPSAMPLE\_DATA**](mpsample-data.md)                        | Notification data passed to the sample submission callback function.<br/>         |
| [**MPSCAN\_DATA**](mpscan-data.md)                            | Scan data passed to the callback.<br/>                                            |
| [**MPSCAN\_RESOURCES**](mpscan-resources.md)                  | Resource information passed during a scan operation.<br/>                         |
| [**MPSCAN\_RESULT**](mpscan-result.md)                        | The results of a scan.<br/>                                                       |
| [**MPSIGUPDATE\_DATA**](mpsigupdate-data.md)                  | Notification data passed to the signature update callback function.<br/>          |
| [**MPSTATUS\_DATA**](mpstatus-data.md)                        | Contains data about the current status of a component of the product.<br/>        |
| [**MPSTATUS\_DATAEX\_UNUSED**](mpstatus-dataex-unused.md)     | Dummy structure for non-SRP.<br/>                                                 |
| [**MPSTATUS\_INFO**](mpstatus-info.md)                        | Status information for the malware protection manager.<br/>                       |
| [**MPTHREAT\_DATA**](mpthreat-data.md)                        | Notification data passed due to threat detection or modification.<br/>            |
| [**MPTHREAT\_INFO**](mpthreat-info.md)                        | Contains information about a threat.<br/>                                         |
| [**MPTHREAT\_INFOEX\_BEHAVIOR**](mpthreat-infoex-behavior.md) | Contains behavior modification-specific information.<br/>                         |
| [**MPTHREAT\_INFOEX\_NIS**](mpthreat-infoex-nis.md)           | Contains NIS-specific information.<br/>                                           |
| [**MPTHREAT\_INFOEX\_UNUSED**](mpthreat-infoex-unused.md)     | Dummy structure for non-behavior modification type threats.<br/>                  |
| [**MPTHREAT\_LOCALIZED\_INFO**](mpthreat-localized-info.md)   | Localized information for a threat.<br/>                                          |
| [**MPTHREAT\_STATS**](mpthreat-stats.md)                      | Threat-related statistics.<br/>                                                   |
| [**MPTHREAT\_STATS\_DATA**](mpthreat-stats-data.md)           | Additional threat statistics data.<br/>                                           |
| [**MPVERSION\_INFO**](mpversion-info.md)                      | Version information for the malware protection manager's components.<br/>         |



 

 

 






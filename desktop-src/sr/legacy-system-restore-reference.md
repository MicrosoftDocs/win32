---
title: Legacy System Restore Reference
description: This documentation describes implementation details of the repository used by a legacy version of System Restore. It does not apply to the implementation of System Restore on Windows Vista.
ms.assetid: d221e83d-beb0-405c-b332-a3ab8aaef688
ms.topic: article
ms.date: 05/31/2018
---

# Legacy System Restore Reference

\[This information applies only to Windows XP with Service Pack 2 (SP2).\]

This documentation describes implementation details of the repository used by a legacy version of System Restore. It does not apply to the implementation of System Restore on Windows Vista.

## System Restore Repository Structure

Windows XP with SP2 contains a repository for System Restore in the following folder: %SYSTEMDRIVE%\\System Volume Information. This repository contains information for restore points, which are essentially a snapshot of the system at a moment in time.

The repository is structured as follows:

**System Volume Information**    **\_restore{*GUID*}**       **RP1**       **RP2**       **RP*n*-1**       **RP*n***    **\_restore{*GUID*}**       **RP1**       **RP2**       **RP*n*-1**       **RP*n***

To determine which \_restore{*GUID*} folder to use, read the **GUID** specified in the following file: SYSTEMROOT%\\System32\\Restore\\MachineGUID.txt.

Within each \_restore{*GUID*} folder, the \_driver.cfg file contains information from a **SR\_PERSISTENT\_CONFIG** structure defined as follows:

``` syntax
typedef struct _SR_PERSISTENT_CONFIG
 {      
  ULONG Signature;            // Set to CPrs
  ULONG FileNameNumber;       // Number for next temp file 
                              // For example, A0000001 would be 1  
  INT64 FileSeqNumber;        // Next sequence number
  ULONG CurrentRestoreNumber; // For example, RP5 would be 5
 } SR_PERSISTENT_CONFIG, * PSR_PERSISTENT_CONFIG;
```

## Files Contained in Each RP*n*Folder

Each RP*n* folder contains a Snapshot folder that contains the following:

-   A snapshot of the registry hives
-   A Repository folder that contains a snapshot of the WMI repository
-   A snapshot of the COM+ database
-   A snapshot of the IIS database

Each RP*n* folder contains an RP.log file that contains general information about the restore point from the [**RESTOREPOINTINFOW**](/windows/win32/api/srrestoreptapi/ns-srrestoreptapi-restorepointinfoa) structure.

Each RP*n* folder may contain files used to track changes for a restore point. The first file is named change.log, the next file is named change.log.1, and so on. Each change log file contains the following structures:

-   [**CHANGE\_LOG\_HEADER**](change-log-header.md)
-   [**CHANGE\_LOG\_ENTRY**](change-log-entry.md)1
-   [**CHANGE\_LOG\_ENTRY**](change-log-entry.md)2
-   ...
-   [**CHANGE\_LOG\_ENTRY**](change-log-entry.md)*n*

## Related topics

<dl> <dt>

[Legacy System Restore Structures](legacy-system-restore-structures.md)
</dt> </dl>

 

 





---
title: BITS and System Restore
description: Not all versions of BITS use the same format to store jobs.
ms.assetid: 97c7fa69-1b35-445b-a0a1-b4d60c3ede42
ms.topic: article
ms.date: 11/29/2018
---

# BITS and System Restore

Not all versions of BITS use the same format to store jobs. If you return the computer to a restore point prior to a BITS upgrade, the old version of BITS may not be able to read the current job information. If this happens, BITS will delete the jobs list and create a new empty jobs list. As a result, the temporary files associated with the previous jobs list are not cleaned up; to reclaim the disk space, you must delete the files manually.

Users familiar with the Windows command line can avoid this problem by using the [BITSAdmin tool](bitsadmin-tool.md) to clear the BITS jobs list before running System Restore. To clear the BITS jobs list, run the following command:

**bitsadmin /reset /allusers**

Note that you must have administrator privileges to run this command.

 

 





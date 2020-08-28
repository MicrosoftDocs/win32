---
title: Tracking modified ranges of a file
description: Tracking modified ranges of a file
ms.assetid: 756881E9-EFD0-42FE-9B1C-4A2EF1998D71
ms.topic: article
ms.date: 05/31/2018
---

# Tracking modified ranges of a file

## Platforms

**Clients -** Windows 8.1 (all SKUs)  
**Servers -** Windows Server 2012 R2  

## Description

The NT File System (NTFS) team has added a new feature to Windows. USN Journal will output an update sequence number (USN) record containing modified ranges for a file upon close. A new record type, USN\_RECORD\_V4 has been introduced to record these changed ranges of a file.

The feature is not enabled by default; users must invoke a file system control (FSCTL) command to enable it. However, because other Windows components may turn on range tracking, users and developers may perceive that the feature is always enabled. Windows will allow developers to query USN journal to find out if range tracking is enabled.

MSDN documentation will be provided at a later date to instruct developers in how to access USN\_RECORD\_V4 records.

## Manifestation

All existing applications that use USN Journal will continue to work well without any compatibility issues.

 

 





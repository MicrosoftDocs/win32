---
title: Monitoring the System
description: Monitoring the System
ms.assetid: e0318aca-4e3e-4272-ba31-c770d6b05272
ms.topic: article
ms.date: 05/31/2018
---

# Monitoring the System

System Restore in Windows Vista and later saves a copy of the volume when generating a restore point. System Restore requires a minimum of 300 MB of free disk space on the system drive at installation.

System Restore in Windows XP monitors a core set of system and application files, archiving the states of these files before system changes are made. System Restore also saves a full snapshot of the registry and some dynamic system files. System Restore requires a minimum of 200 MB of free disk space on the system drive at installation. When the amount of free disk space falls below 50 MB on any drive, System Restore switches to standby mode and stops creating restore points. All restore points are deleted at that time. System Restore reactivates and resumes creating restore points as soon as 200 MB of disk space is free on the system drive. The files that are monitored or excluded from monitoring are specified in the file %windir%\\system32\\restore\\Filelist.xml. For more information, see [Monitored File Name Extensions](monitored-file-extensions.md).

 

 





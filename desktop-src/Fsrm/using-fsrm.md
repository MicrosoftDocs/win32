---
title: Using FSRM
description: The File Server Resource Manager (FSRM) API is used to limit the size of a given directory using directory quotas, restrict the type of data that can be stored under a given directory using file screens, and generate storage reports that administrators can use to analyze storage utilization.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 89fe97bf-24fe-4ff1-9fe0-007b0e23eef3
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager File Server Resource Manager , using
- File Server Resource Manager examples File Server Resource Manager
- examples File Server Resource Manager
- File Server Resource Manager File Server Resource Manager , examples See File Server Resource Manager examples
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using FSRM

The File Server Resource Manager (FSRM) API is used to limit the size of a given directory using directory quotas, restrict the type of data that can be stored under a given directory using file screens, and generate storage reports that administrators can use to analyze storage utilization. You can manage storage on a local or remote server.

## In this section

<dl> <dt>

[Accessing Classification Properties](accessing-classification-properties.md)
</dt> <dd>

Enumerating FSRM classification properties is easily done using the [**FsrmClassificationManager**](/windows/previous-versions/FsrmTlb/?branch=master) object.

</dd> <dt>

[Classifying Files](classifying-files.md)
</dt> <dd>

This sample demonstrates using FSRM to classify multiple files at once. This approach is much faster when dealing with many files, compared to setting the properties using an API call for each file.

</dd> <dt>

[Developing FCI Pipeline Modules](developing-fci-pipeline-modules.md)
</dt> <dd>

You can create extensibility modules that plug into the [File Classification Infrastructure](http://go.microsoft.com/fwlink/p/?linkid=178897) pipeline to extend the methods in which files are classified and how their classification properties can be retrieved and persisted.

</dd> <dt>

[Preventing Files From Being Written to a Directory](preventing-files-from-being-written-to-a-directory.md)
</dt> <dd>

A file screen restricts the types of files that the system or any user can store in a specific directory and its subdirectories.

</dd> <dt>

[Limiting the Amount of Data Written to a Directory](limiting-the-amount-of-data-written-to-a-directory.md)
</dt> <dd>

A quota limits the amount of data that the system or any user can store in a directory.

</dd> <dt>

[Generating Reports](generating-reports.md)
</dt> <dd>

You can generate reports that can help administrators to better understand how storage is utilized in the specified directories.

</dd> </dl>

 

 





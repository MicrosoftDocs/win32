---
title: How to configure a file management task
description: A file management task identifies a set of files given a set of criteria and performs an action on them.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '02860A9D-5B6C-47F0-85A8-AFEAAB3C0EB0'
ms.prod: 'windows-server-dev'
ms.technology: 'dynamic-access-control'
ms.tgt_platform: multiple
keywords: ["Dynamic Access Control developer extensibility DACx , configure a file management task"]
---

# How to configure a file management task

A file management task identifies a set of files given a set of criteria and performs an action on them.

### Using a file management task

The file management task identifies a set of files based on a given criteria—for example, files that have not been accessed in the last 30 days—then it acts on them through a built-in action. This built-in action can be set up for many types of business scenarios, such as the removal of expired data.

For an example of this extensibility point, see [Automatically uploading files from File Server to SharePoint using the File Classification Infrastructure (FCI)](http://blogs.technet.com/b/filecab/archive/2009/12/14/automatically-upload-files-from-file-server-to-sharepoint-using-the-file-classification-infrastructure-fci.aspx).

> [!Note]  
> A file management task sample is not included in the Windows Server 2012 SDK.

 

For more information, see the TechNet article [Create a Custom File Management Task](https://TechNet.Microsoft.Com/library/dd759180.aspx).

### Configuring a custom action

A custom action is a configuration option of a file management task that causes the task to run an operating system command line against an identified set of files that match a given criteria. The custom action could be run as a scheduled item or continuously. Any executable can be defined and stored as a custom action on the file server as part of the [File Server Resource Manager](https://msdn.microsoft.com/library/bb972746) (FSRM) object. Macros can also be used on the command line. FCI allows for a series of macros to be included on the command line to be executed for the custom action. You can get a full list in PowerShell by running the command, **get-FsrmMacroFileManagementJob**.

For example, if a file is initially classified as `businessImpact=LBI` then manually changed to `businessImpact=HBI`, a rule that monitors for this change would run the custom action on the next continuous pass, which could be within a few seconds. The custom action could be any executable you have created for your business needs; for instance, one that encrypts the file then moves it to a more secure directory.

For security, executables used by custom actions must be read-only for any non-administrative users and stored in a location that is read-only for non-administrative users.

 

 





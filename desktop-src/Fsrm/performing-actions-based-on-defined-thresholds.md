---
title: Performing Actions Based on Defined Thresholds
description: You can add up to 16 threshold values to a quota. The threshold is a percentage of the quota limit.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 45111206-cce8-494d-9e78-7eb551dff186
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager examples File Server Resource Manager , performing actions based on defined thresholds
- thresholds File Server Resource Manager
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Performing Actions Based on Defined Thresholds

You can add up to 16 threshold values to a quota. The threshold is a percentage of the quota limit. For example, you can specify a threshold of 85% or 150%.

When the disk space usage charged to the quota reaches the threshold, FSRM performs the actions specified for the threshold. You can specify up to four unique actions for each threshold. For example, you can have FSRM log an event or send email notification to one or more recipients.

For an example that creates a threshold and specifies an action to perform, see [Using Templates to Define Quotas](using-templates-to-define-quotas.md).

 

 





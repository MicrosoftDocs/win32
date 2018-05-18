---
title: Limiting the Amount of Data Written to a Directory
description: A quota limits the amount of data that the system or any user can store in a directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '01934a5a-9a39-4d78-8837-e0c81a06cb4b'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["File Server Resource Manager examples File Server Resource Manager , limiting the amount of data written to a directory", "quotas File Server Resource Manager"]
---

# Limiting the Amount of Data Written to a Directory

A quota limits the amount of data that the system or any user can store in a directory. In addition to the limit, a directory quota may be configured with one or more directory quota thresholds which define a set of actions that are performed when the quota usage reaches the threshold value.

You can create quotas directly but typically you create quota templates from which quotas derive. The template is used to modify properties in bulk by applying the changes to quotas that derive from the quota template.

In addition to creating a quota, you can also create an automatic quota for a directory. The automatic quota is not enforced on the directory with which it is associated, but instead FSRM uses the definition of the automatic quota to automatically create a quota for each new subdirectory that is created under the directory. When you save the automatic quota, FSRM also creates quotas for all existing subdirectories under the directory that do not contain a quota.

For details on quotas, automatic quotas, templates, and actions, see the following topics:

-   [Using Templates to Define Quotas](using-templates-to-define-quotas.md)
-   [Defining a Quota](defining-a-quota.md)
-   [Defining and Using Automatic Quotas](defining-and-using-automatic-quotas.md)
-   [Updating a Quota](updating-a-quota.md)
-   [Performing Actions Based on Defined Thresholds](performing-actions-based-on-defined-thresholds.md)
-   [Getting Current Usage Values](getting-current-usage-values.md)

 

 





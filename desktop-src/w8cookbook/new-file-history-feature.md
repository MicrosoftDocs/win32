---
title: New File History feature
description: New File History feature
ms.assetid: B1EE4638-5591-483B-AA09-600E242ED50B
ms.topic: article
ms.date: 05/31/2018
---

# New File History feature

## Platform

**Clients** – Windows 8 


## Description

The new File History feature replaces the existing Backup and Restore function, and offers protection for user files stored in user libraries. A set of APIs is provided that allows developers to programmatically enable File History and select a specific storage target. Documentation for these APIs is available on MSDN.

It may affect workflows related to data protection and documentation that depend on the Windows Backup and Restore feature.

We do not recommend using both features at the same time. File History checks if a Backup schedule exists and is active and if it finds one, it will not let users to turn it on. In this case, users who want to use File History will have to delete the Windows Backup schedule.

## Manifestation

Workflows may be interrupted and documentation for the previous method for accessing the Windows Backup and Restore feature will need to be updated to reflect these changes.

## Solution

Revise apps that contain workflows that are adversely impacted by the new File History feature to remove any conflicts and incorporate the new set of APIs.

## Tests

The API allows developers to determine if File History is turned on.

 

 





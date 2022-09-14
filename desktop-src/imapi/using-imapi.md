---
title: Using IMAPI
description: The following topics demonstrate the use of the image mastering API.
ms.assetid: c42043db-612f-488f-a6ae-a8caea8ac42b
ms.topic: article
ms.date: 05/31/2018
---

# Using IMAPI

The following topics demonstrate the use of the image mastering API.

## Usage Scenarios

The following documentation provides detailed guidance for common IMAPI scenarios.



| Scenario                                                                                                         | Description                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Checking Drive Support](checking-drive-support.md)                                                             | Demonstrates the detection of support for a media drive.<br/>                                                                                                   |
| [Checking Media Support](checking-media-support.md)                                                             | Demonstrates the detection of support for media.<br/>                                                                                                           |
| [Burning a Disc Image](burning-a-disc.md)                                                                       | Demonstrates mastering (burning a disc) using IMAPI.<br/>                                                                                                       |
| [Adding a Boot Image](adding-a-boot-image.md)                                                                   | Builds on the [Burning a Disc Image](burning-a-disc.md) example by adding code to include a bootable image in the boot section of the disc.<br/>               |
| [Creating a Multisession Disc](creating-a-multisession-disc.md)                                                 | Demonstrates the creation of a multisession disc using IMAPI.<br/>                                                                                              |
| [Monitoring Progress With Events](monitoring-progress-with-events.md)                                           | Demonstrates the use of specific interfaces in order to allow the implementation of an event handler so that progress information may be received. <br/>        |
| [Preventing Logoff or Suspend During a Burn](preventing-logoff-or-suspend-during-a-burn.md)                     | Contains information detailing application development considerations to be made in regards to scenarios involving user 'Logoff' and 'Suspend' in Windows.<br/> |
| [Providing User Permissions for Media Burning Devices](providing-user-permissions-for-media-burning-devices.md) | Details the process required to ensure a user has adequate permissions to utilize media burning devices on Windows XP and Windows Server 2003.<br/>             |



 

## Application Compatibility

The following documentation contains important information to take consideration while developing an application that utilizes IMAPI.



| Guidance                                                   | Description                                                                                                                                                                                                                                                 |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IMAPI Multisession Layout](imapi-multisession-layout.md) | Details the disc layout that IMAPI utilizes to implement multisession. This information is used to ensure interoperability between IMAPI and other burning software, as well as allow the creation of IMAPI-compatible multisession disc images.<br/> |



 

 

 






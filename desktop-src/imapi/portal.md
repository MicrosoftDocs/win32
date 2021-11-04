---
title: Image Mastering API
description: Image Mastering API
ms.assetid: 4902d3fb-3195-4909-ab64-28f8a77ba14c
ms.topic: article
ms.date: 05/31/2018
---

# Image Mastering API

## Purpose

The Microsoft Windows image mastering API enables applications to stage and burn images to CD, DVD, and Blu-ray optical storage media. Other disc-like media that lay images in the same manner can also use this API.

## Developer audience

IMAPI is designed for C/C++ and Visual Basic developers and those writing scripts using VBScript.

Knowledge of CD, DVD, and Blu-ray technologies and file systems is recommended. Developers may benefit from a familiarity with the latest revision of Multimedia Command (MMC) at [ftp://ftp.t10.org/t10/drafts/mmc6](https://www.microsoft.com/?ref=go).

## Run-time requirements

IMAPI 2.0 is supported natively starting with Windows Vista and Windows Server 2008. Enabling IMAPI 2.0 functionality for Windows XP and Windows Server 2003 requires the installation of the [KB932716](https://support.microsoft.com/kb/932716) update package. If this package is not installed, Windows XP still natively supports [IMAPI 1.0](imapiv1.md).

> [!Note]  
> The Windows Feature Pack for Storage is available to the public via the [Microsoft Download Center](https://www.microsoft.com/downloads/details.aspx?FamilyID=63ab51ea-99c9-45c0-980a-c556746fcf05). Additional information regarding specific API changes can be found in the [What's New](what-s-new.md) section.

 

## In this section



| Topic                                             | Description                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------------------|
| [What's New](what-s-new.md)<br/>           | Information detailing each significant release of the Image Mastering API.<br/> |
| [About IMAPI](about-imapi.md)<br/>         | General information about the Image Mastering API.<br/>                         |
| [Using IMAPI](using-imapi.md)<br/>         | Task-related topics that demonstrate how to use the Image Mastering API.<br/>   |
| [IMAPI Reference](imapi-reference.md)<br/> | Detailed descriptions of IMAPI interfaces and other programming elements.<br/>  |



 

## Additional resources

Further information regarding IMAPI and other related subjects can be found at the following locations:



| Topic                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Microsoft Optical Storage Blog](/archive/blogs/opticalstorage/)                | Highlights topics that focus on the implementation of the Image Mastering API in real world development scenarios.                                                                                                                                                                                                                                                 |
| [Optical Platform Discussion Forum](https://social.msdn.microsoft.com/forums/windowsopticalplatform/threads/)              | Discuss CDROM.SYS, IMAPIv2 and Live File System issues. This forum focuses on system-level topics and is intended for application developers rather than endusers.                                                                                                                                                                                                 |
| [T10 Technical Committee](https://www.t10.org/)                       | A Technical Committee of the InterNational Committee on Information Technology Standards (INCITS, pronounced "insights"). INCITS is accredited by, and operates under rules that are approved by, the American National Standards Institute (ANSI). These rules are designed to ensure that voluntary standards are developed by the consensus of industry groups. |
| [Optical Storage Technology Association (OSTA)](http://www.osta.org/) | Works to shape the future of the industry through regular meetings of Commercial Optical Storage Applications (COSA), DVD Compatibility, Marketing, MPV (MusicPhotoVideo), UDF committees, and a new adhoc Blue Laser committee. Interested companies worldwide are invited to join the organization and participate in its committees and programs.               |



 

 


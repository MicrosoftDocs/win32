---
title: Windows Image File Boot (WimBoot)
description: Windows Image File Boot (WimBoot)
ms.assetid: 1C4EFC42-6698-4981-8C55-D1DFC6309F31
ms.topic: article
ms.date: 05/31/2018
---

# Windows Image File Boot (WimBoot)

## Platform

**Clients:** Windows 8.1  

## Description

WimBoot is an alternative way for OEMs to deploy Windows. A WimBoot deployment boots and runs Windows directly out of a compressed Windows Image File (WIM). This WIM file is immutable, and access to it is managed by a new file system filter driver (WoF.sys).

The result is a significant reduction in the disk space required to install Windows.

## Manifestations

Most applications should be completely unaffected by WimBoot. Only applications that access and unlock system files or pre-loaded files for write access may be affected. Since the WIM is immutable, updates to it (that is, system or pre-loaded files) are simply stored on the C:\\ partition.

If an application unlocked write access for all WIM-backed system and pre-loaded files, the savings that WimBoot delivers would be completely lost, as all of these files would be decompressed and placed on the C:\\ volume.

Furthermore, back-up and restore applications need to be aware of WimBoot deployments, as the WIM is present in a separate partition; that is, on back-up, both the C:\\ and WIM partitions must be saved and both must be restored together.

## Solution

New APIs were introduced that allow applications to directly query if a given volume or file is backed by a WIM. This information allows applications to make appropriate decisions, such as opening these files only for read access or to identify volumes/partitions that have to be backed up and restored together.

## Compatibility, performance, reliability, or usability tests

Application developers should test their software and its corresponding scenarios on a WimBoot system, especially if these applications access system or pre-loaded files. Special attention should be paid to a significant reduction in available disk space after a scenario has been completed.

 

 





---
Description: To obtain a handle to a volume for use with update sequence number (USN) change journal operations, call the CreateFile function with the lpFileName parameter set to a string of the following form \\\\.\\X.
ms.assetid: a4f4dac5-76fd-4e9e-a71e-665684840d74
title: Obtaining a Volume Handle for Change Journal Operations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Obtaining a Volume Handle for Change Journal Operations

To obtain a handle to a volume for use with update sequence number (USN) change journal operations, call the [**CreateFile**](/windows/win32/FileAPI/nf-fileapi-createfilea?branch=master) function with the *lpFileName* parameter set to a string of the following form: \\\\.\\*X*:

Note that *X* is the letter that identifies the drive on which the NTFS volume appears.

If the volume does not have a drive letter, use the syntax described in [Naming a Volume](naming-a-volume.md).

 

 




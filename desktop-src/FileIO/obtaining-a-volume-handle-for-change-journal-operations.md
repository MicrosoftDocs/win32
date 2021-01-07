---
description: 'To obtain a handle to a volume for use with update sequence number (USN) change journal operations, call the CreateFile function with the lpFileName parameter set to a string of the following form: \\\\.\\X.'
ms.assetid: a4f4dac5-76fd-4e9e-a71e-665684840d74
title: Obtaining a Volume Handle for Change Journal Operations
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining a Volume Handle for Change Journal Operations

To obtain a handle to a volume for use with update sequence number (USN) change journal operations, call the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function with the *lpFileName* parameter set to a string of the following form: \\\\.\\*X*:

Note that *X* is the letter that identifies the drive on which the NTFS volume appears.

If the volume does not have a drive letter, use the syntax described in [Naming a Volume](naming-a-volume.md).

 

 




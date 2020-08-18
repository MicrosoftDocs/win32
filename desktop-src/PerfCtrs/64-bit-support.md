---
Description: If you provide counters on a 64-bit computer, you must install both the 32-bit and 64-bit version of your provider on the computer if you want to support both 32-bit and 64-bit consumers.
ms.assetid: 2dba2c46-0185-4ce6-a7cc-27cdd9b19b70
title: 64-bit Support
ms.topic: article
ms.date: 05/31/2018
---

# 64-bit Support

If your [V1 provider](providing-counter-data.md) runs on a 64-bit operating system, you must install both the 32-bit and 64-bit version of your provider on the system if you want to support both 32-bit and 64-bit consumers. Place the 32-bit version in the `%windir%\syswow64` folder and the 64-bit version in the `%windir%\system32` folder.

For a 32-bit consumer to consume local counter data, the 32-bit version of the provider must be installed.

For a 64-bit consumer to consume local counter data, the 64-bit version of the provider must be installed.

For a 32-bit consumer to consume remote counter data from a 32-bit operating system, the 32-bit version of the provider must exist on the remote system. A 32-bit consumer can consume remote counter data from a 64-bit operating system only if the remote system contains the 64-bit version of the provider.

For a 64-bit consumer to consume remote counter data from a 32-bit operating system, the 32-bit version of the provider must exist on the remote system. A 64-bit consumer can consume remote counter data from a 64-bit operating system only if the remote system contains the 64-bit version of the provider.

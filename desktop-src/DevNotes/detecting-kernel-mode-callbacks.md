---
description: If a thread is waiting for a kernel-mode callback to complete, the user-mode side of the thread will delay at a call to the ZwCallbackReturn function.
ms.assetid: 6d6d4f94-0e8c-4469-b905-731be6c4083d
title: Detecting Kernel-Mode Callbacks
ms.topic: article
ms.date: 05/31/2018
---

# Detecting Kernel-Mode Callbacks

Most of the code for the Windows operating system runs in kernel mode. The processor mode switches from user mode to kernel mode whenever an application thread calls a function from the Windows API that in turn calls an internal system function that must execute in kernel mode. The processor mode returns to user mode before control returns to the function so that the system data is protected.

If a thread is waiting for a kernel-mode callback to complete, the user-mode side of the thread will delay at a call to the **ZwCallbackReturn** function.

 

 




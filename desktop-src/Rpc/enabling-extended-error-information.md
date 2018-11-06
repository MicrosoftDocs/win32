---
title: Enabling Extended Error Information
description: Enabling extended error information for Remote Procedure Call (RPC).
ms.assetid: 73b72d0a-8533-40ac-8b41-8af4d60f9631
ms.topic: article
ms.date: 05/31/2018
---

# Enabling Extended Error Information

To enable extended error information, take the following steps:

Open the local machine policy using the gpedit.msc interface.

Navigate to the policy located at Computer Configuration/Administrative Templates/System/Remote Procedure Call/Rpc Troubleshooting Support/Propagation of extended error information

Enable the policy, and set the field **Propagation of extended error information** to "On".

This process turns the propagation of extended error information on for all processes on the machine.

To enable extended error information for only certain processes on a computer, or to disable it for only certain processes on the computer, use the **Off with exceptions** or **On with exceptions** options. Both options use the field **Extended Error Information Exceptions** to specify which processes have the default setting, and which processes have the opposite of the default setting. **Extended Error Information Exceptions** contains a list of process names.

If the command line of a process starts with a string that is in the **Extended Error Information Exceptions**, the process will receive the opposite of the default setting. For example, if you want all the process on your computer to propagate extended error information, except for lsass and the process called **Secure Server**, set the **Propagation of extended error information** to **On with exceptions**, and specify in the **Extended Error Information Exceptions** field the following string: lsass "Secure Server".

Strings can be enclosed with double quotes, but doing so is optional if there are no spaces in the string. Also, the beginning of the process command line can be specified. For example, if **Off with exceptions** is specified in the **Propagation of extended error information** field, and in the **Extended Error Information Exceptions** field the following is specified: win.

Each process that begins with "win" propagates extended error information. On many computers, for example, those processes would be winlogon.exe and WINWORD.EXE.

 

 





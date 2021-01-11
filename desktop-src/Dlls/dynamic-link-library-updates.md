---
description: It is sometimes necessary to replace a DLL with a newer version.
ms.assetid: 82349a33-dc2c-4309-b0fc-890f230e3f2c
title: Dynamic-Link Library Updates
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic-Link Library Updates

It is sometimes necessary to replace a DLL with a newer version. Before replacing a DLL, perform a version check to ensure that you are replacing an older version with a newer version. It is possible to replace a DLL that is in use. The method you use to replace DLLs that are in use depends on the operating system you are using. On Windows XP and later, applications should use [Isolated Applications and Side-by-side Assemblies](/windows/desktop/SbsCs/isolated-applications-and-side-by-side-assemblies-portal).

It is not necessary to restart the computer if you perform the following steps:

1.  Use the [**MoveFileEx**](/windows/desktop/api/winbase/nf-winbase-movefileexa) function to rename the DLL being replaced. Do not specify MOVEFILE\_COPY\_ALLOWED, and make sure the renamed file is on the same volume that contains the original file. You could also simply rename the file in the same directory by giving it a different extension.
2.  Copy the new DLL to the directory that contains the renamed DLL. All applications will now use the new DLL.
3.  Use [**MoveFileEx**](/windows/desktop/api/winbase/nf-winbase-movefileexa) with MOVEFILE\_DELAY\_UNTIL\_REBOOT to delete the renamed DLL.

Before you make this replacement, applications will use the original DLL until it is unloaded. After you make the replacement, applications will use the new DLL. When you write a DLL, you must be careful to ensure that it is prepared for this situation, especially if the DLL maintains global state information or communicates with other services. If the DLL is not prepared for a change in global state information or communication protocols, updating the DLL will require you to restart the computer to ensure that all applications are using the same version of the DLL.

 

 

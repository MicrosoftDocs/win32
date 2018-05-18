---
title: Preparing a Development Environment
description: Development environment configuration for Failover Cluster API programming.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1c20dbc0-ee8b-4c91-8d09-eaa4bf983362'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["development environment preparation Failover Cluster"]
---

# Preparing a Development Environment

To setup a development environment to use the failover cluster APIs, verify that the following requirements and steps are complete:

-   [IDE Requirements](#ide-requirements)
-   [Headers and Libraries](#headers-and-libraries)
-   [(Optional) Debugging for Resource DLLs](#debugging-for-resource-dlls)

## Windows Server Requirements

Failover clustering is available on these versions of Windows Server:

-   Windows Server 2016
-   Windows Server 2012 R2
-   Windows Server 2012
-   Windows Server 2008 R2 Enterprise and Windows Server 2008 R2 Datacenter
-   Windows Server 2008 Enterprise and Windows Server 2008 Datacenter

For information about installing, configuring, and administering a failover cluster, see these topics:

-   Windows Server 2008 R2: [Failover Clusters](https://TechNet.Microsoft.Com/library/cc754482.aspx)
-   Windows Server 2012 R2: [Failover Clustering Overview](https://TechNet.Microsoft.Com/library/hh831579.aspx)

## IDE Requirements

To implement the Failover Cluster APIs, this software must be installed:

-   Microsoft Visual C++ version 6.0 or later with the Unicode MFC libraries
-   MIDL compiler version 3.00.44 or later
-   Active Template Library (ATL) version 2.0 or later
-   Microsoft Visual Basic 4.0 or later is required to use VBScript or Visual Basic with the Cluster Automation Server

## Headers and Libraries

Include the necessary headers and libraries in your code:

-   For information on the failover cluster header and library files, see subsets of the [Failover Cluster API](the-server-cluster-api.md).
-   For example C/C++ code that creates a suitable runtime environment, see [ClusDocEx.h](clusdocex-h.md).
-   If you will be using a scripting language with the Cluster Automation Server, make sure your script references the **GUID** of the MSCLUS type library as shown in the following example.

    `<REFERENCE GUID="{F2E606E0-2631-11D1-89F1-00A0C90D061E}" VERSION="1.0"/>`

## Debugging for Resource DLLs

If you are going to debug resource DLLs, you need to configure debugging.

The following procedure describes how to setup debugging for resource DLLs.

**To prepare for debugging resource DLLs**

1.  Install the Debugging Tools for Windows from [http://www.microsoft.com/whdc/devtools/debugging/default.mspx](Http://go.microsoft.com/fwlink/p/?linkid=84137).
2.  Enable kernel debugging, using IEEE1394 (FireWire) if possible. For more details, read "Choosing Kernel Debugging Settings" and "BCDEdit /dbgsettings" in the Debugging Tools for Windows help.
3.  Install Application Verifier from [http://www.microsoft.com/downloads/details.aspx?FamilyID=bd02c19c-1250-433c-8c1b-2619bd93b3a2](Http://go.microsoft.com/fwlink/p/?linkid=120404) and enable it for Resource Hosting Subsystem (RHS).
4.  Enable Application Verifier for RHS by using the following command:

    **AppVerif -enable Heaps Com RPC Handles Locks Memory TLS Exceptions Threadpool InputOutput -for %WinDir%\\Cluster\\rhs.exe**

5.  Set RHS to run under a debugger with the debugger output redirected to the kernel debugger by using the following command:

    **C:\\Progra~1\\Debugg~1\\Gflags.exe -p /enable Rhs.exe /debug "C:\\Progra~1\\Debugg~1\\cdb.exe -gG -y SRV\*C:\\WebSymbols\*http://msdl.microsoft.com/Download/Symbols -ddefer"**

    The following list provides more information about the previous command:

    -   Do not pass the **-gG** argument to **cdb.exe** if you want to set a breakpoint before your dll gets loaded.

    -   This command line assumes that the Debugging Tools for Windows were installed in "C:\\Program Files\\Debugging Tools for Windows" with a short path of "C:\\Progra~1\\Debugg~1" and the local cache of Windows symbols is to be installed in "C:\\WebSymbols". Please adjust the paths as necessary.

    -   To set a breakpoint, use the "bu ResDllName!FunctionName" command in the debugger. For example, to set a breakpoint on the [*Terminate*](terminate.md) callback function for the ClipBook Server sample in the Windows SDK, the command would be "bu ClipBook Server!ClipBookServerTerminate".

    -   To break when the DLL is being loaded, use the "sxe ResDllName.dll" command in the debugger.

    -   The **-ddefer** argument allows the user-mode debugging session to be controlled by a remote debugger. For more information, read "Remote Debugging Through the Debugger" in the Debugging Tools for Windows help.

    -   For more information, read the "Controlling the User-Mode Debugger from the Kernel Debugger" topic in the Debugging Tools for Windows help.

## Related topics

<dl> <dt>

[Using the Failover Cluster APIs](using-the-server-cluster-api.md)
</dt> </dl>

 

 





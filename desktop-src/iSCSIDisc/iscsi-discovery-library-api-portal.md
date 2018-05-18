---
Description: 'The iSCSI Discovery Library API allows initiators to locate any accessible target devices as well as the associated addresses with a minimal amount of required configurations.'
ms.assetid: '84bb8bbc-3b7e-46ee-8b53-a20b5e2aea05'
title: iSCSI Discovery Library API
---

# iSCSI Discovery Library API

## Purpose

The iSCSI Discovery Library API allows initiators to locate any accessible target devices as well as the associated addresses with a minimal amount of required configurations.

The purpose of the iSCSI Discovery Library API is to provide low overhead support for small iSCSI setups, and scalable discovery solutions for large enterprise setups. There is a range of possible implementation scenarios, some of which include:

-   Configure a list of specific targets and associated addresses for each initiator.
-   Allow initiators to discover targets dynamically.

In order for an iSCSI initiator to establish an iSCSI session with an iSCSI target, the initiator requires the IP address, TCP port number and iSCSI device target name information.

This documentation defines only elements specific to the Discovery Library API and does not specify the central management of iSCSI devices. Additionally, this API only facilitates target discovery and the use of the SCSI protocol for LUN discovery is still required.

For specific information regarding the individual elements of the iSCSI Discovery Library API, see [iSCSI Discovery Library Reference](iscsi-discovery-library-reference.md).

## Developer audience

The iSCSI Discovery Library API is designed for C/C++ developer as well as WMI developers who use C/C++, the Microsoft Visual Basic application, or a scripting language that has an engine on Windows and handles Microsoft ActiveX objects. Familiarity with COM programming is helpful but not required. For more information about WMI, see [Windows Management Instrumentation](https://msdn.microsoft.com/library/aa394582).

## Run-time requirements

The iSCSI Discovery Library API is included in Windows Vista, Windows Server 2008, and later.

The iSCSI Initiator WMI API is included in Windows 8, Windows Server 2012, and later.

## In this section

-   [iSCSI Discovery Library Reference](iscsi-discovery-library-reference.md)
-   [iSCSI Initiator WMI API Reference](iscsi-initiator-wmi-api-reference.md)

 

 




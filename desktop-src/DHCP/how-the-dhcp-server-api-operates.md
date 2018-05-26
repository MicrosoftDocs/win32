---
title: How the DHCP Server Callout API Operates
description: Microsoft DHCP Server maintains an internal table of events that, upon their occurrence in DHCP protocol processing, trigger third-party DLL function calls.
ms.assetid: 35ec953e-0345-4c18-8790-33da189c6a43
keywords:
- Server API DHCP , operation
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How the DHCP Server Callout API Operates

Microsoft DHCP Server maintains an internal table of events that, upon their occurrence in DHCP protocol processing, trigger third-party DLL function calls. Developers register to have the occurrence of these events call their functions by creating a specified registry entry that Microsoft DHCP Server reads upon startup.

The location of the registry entry is:

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\DHCPServer\\Parameters**

The following registry key values must be specified for this entry in order to enable the callout server:

| Key Name       | Key Datatype   | Value                                                                                                                        |
|----------------|----------------|------------------------------------------------------------------------------------------------------------------------------|
| CalloutDlls    | REG\_MULTI\_SZ | String that contains the local path to the DHCP callout DLL. For example: "C:\\Program Files\\MyCalloutServer\\my\_dhcp.dll" |
| CalloutEnabled | DWORD          | 32-bit unsigned integer value that specifies 0 if the DHCP callout server is not enabled, and 1 if it is.                    |



 

How Microsoft DHCP Server loads and handles third-party DLLs impacts third-party DLL developers. Microsoft DHCP Server takes the following steps in loading third-party DLLs:

1.  Microsoft DHCP Server checks the previously defined registry location for the presence of third-party DLLs.
2.  If no registry entries are found, the DHCP Server internal hook table remains empty, and no DHCP Server event notifications are sent.
3.  If one or more registry entries is found, Microsoft DHCP Server reads the first registry entry, in alphabetical order, and attempts to load the corresponding third-party DLL. If the DLL loads successfully, Microsoft DHCP Server ceases checking for additional third-party DLLs.
4.  Microsoft DHCP Server calls the [**DhcpServerCalloutEntry**](/windows/previous-versions/Dhcpssdk/nc-dhcpssdk-lpdhcp_entry_point_func?branch=master) function in the loaded third-party DLL, retrieving the associated [**DHCP\_CALLOUT\_TABLE**](/windows/previous-versions/Dhcpssdk/ns-dhcpssdk-_dhcp_callout_table?branch=master) function and thereby determining which events initiate notification to the third-party DLL. Notification comes in the form of corresponding third-party functions: one or more of which can be included in the third-party DLL, and each of which are defined in the following [DHCP Server API](dhcp-server-api.md) reference pages.

Because the DHCP Server API enables developers to hook into the core functionality of Microsoft DHCP Server, use care when writing the third-party DLL functions. Several events that result in third-party DLL function calls occur when locks are held by the DHCP Server, and therefore, poorly written hooks can destroy DHCP Server heaps and critical information in Microsoft DHCP Server structures.

 

 





---
title: DHCP Client API
description: The Dynamic Host Configuration Protocol (DHCP) API, or DHCP Client Options, enables Windows clients to query specific options from DHCP servers.
ms.assetid: 7c0e99db-bd50-4d77-bbe7-bddf2ed5474d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DHCP Client API

The Dynamic Host Configuration Protocol (DHCP) Application Programming Interface (API), also referred to as DHCP Client Options, enables Microsoft Windows clients to query specific options from DHCP servers. This capability enables vendor-specific options exposed through DHCP servers to be queried by Windows clients.

Programmers using the DHCP Client API should note the following:

-   The adapter name being passed in DHCP functions should be the adapter GUID for the routine.
-   The class identifier (ID) parameter in DHCP functions is the binary class identifier (ID) information to pass in the DHCP INFORM packet through use of the USER CLASS option.
-   The *AdapterName* parameter exists on Windows Me/98, but it refers to the adapter index (converted to a string) rather than the adapter name itself. This is necessary because Windows Me/98 does not have the Windows XP/2000 equivalence of adapter names.
-   DHCP functions are exposed through Dhcpcsvc.dll.

 

 





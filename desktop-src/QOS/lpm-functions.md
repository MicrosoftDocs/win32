---
title: LPM Functions
description: The following functions are exposed by the Microsoft-provided LPM, Msidlpm.dll.
ms.assetid: 67550ae2-c7c6-4278-98e8-aecc71abc624
keywords:
- Quality of Service QOS , reference, LPM functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LPM Functions

The following functions are exposed by the Microsoft-provided LPM, Msidlpm.dll.

-   [*cbAdmitResult*](/windows/previous-versions/lpmapi/nc-lpmapi-cbadmitresult?branch=master)
-   [*cbGetRsvpObjects*](/windows/previous-versions/Lpmapi/nc-lpmapi-cbgetrsvpobjects?branch=master)
-   [*PALLOCMEM*](/windows/previous-versions/Lpmapi/nc-lpmapi-pallocmem?branch=master)
-   [*PFREEMEM*](/windows/previous-versions/Lpmapi/nc-lpmapi-pfreemem?branch=master)

The following functions must be exposed by each LPM; they allow the PCM to communicate requests from the Subnet Bandwidth Manager (SBM) (through the PCM). The Microsoft-supplied LPM, implemented as a DLL in Msidlpm.dll, also uses this API. Note that callback functions, identified by their cb prefix, should not be exposed by LPMs; these callback functions, which are exposed by the PCM, facilitate deferred response from LPMs to PCM requests.

-   [*LPM\_AdmitRsvpMsg*](/windows/previous-versions/Lpmapi/nf-lpmapi-lpm_admitrsvpmsg?branch=master)
-   [*LPM\_CommitResv*](/windows/previous-versions/Lpmapi/nf-lpmapi-lpm_commitresv?branch=master)
-   [*LPM\_Deinitialize*](/windows/previous-versions/Lpmapi/nf-lpmapi-lpm_deinitialize?branch=master)
-   [*LPM\_DeleteState*](/windows/previous-versions/Lpmapi/nf-lpmapi-lpm_deletestate?branch=master)
-   [*LPM\_GetRsvpObjects*](/windows/previous-versions/Lpmapi/nf-lpmapi-lpm_getrsvpobjects?branch=master)
-   [*LPM\_Initialize*](/windows/previous-versions/Lpmapi/nf-lpmapi-lpm_initialize?branch=master)
-   [*Lpm\_IpAddressTable*](/windows/previous-versions/Lpmapi/nf-lpmapi-lpm_ipaddresstable?branch=master)

 

 





---
title: LPM Functions
description: The following functions are exposed by the Microsoft-provided LPM, Msidlpm.dll.
ms.assetid: 67550ae2-c7c6-4278-98e8-aecc71abc624
keywords:
- Quality of Service QOS , reference, LPM functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LPM Functions

The following functions are exposed by the Microsoft-provided LPM, Msidlpm.dll.

-   [*cbAdmitResult*](/previous-versions/windows/desktop/api/lpmapi/nc-lpmapi-cbadmitresult)
-   [*cbGetRsvpObjects*](/previous-versions/windows/desktop/api/Lpmapi/nc-lpmapi-cbgetrsvpobjects)
-   [*PALLOCMEM*](/previous-versions/windows/desktop/api/Lpmapi/nc-lpmapi-pallocmem)
-   [*PFREEMEM*](/previous-versions/windows/desktop/api/Lpmapi/nc-lpmapi-pfreemem)

The following functions must be exposed by each LPM; they allow the PCM to communicate requests from the Subnet Bandwidth Manager (SBM) (through the PCM). The Microsoft-supplied LPM, implemented as a DLL in Msidlpm.dll, also uses this API. Note that callback functions, identified by their cb prefix, should not be exposed by LPMs; these callback functions, which are exposed by the PCM, facilitate deferred response from LPMs to PCM requests.

-   [*LPM\_AdmitRsvpMsg*](/previous-versions/windows/desktop/api/Lpmapi/nf-lpmapi-lpm_admitrsvpmsg)
-   [*LPM\_CommitResv*](/previous-versions/windows/desktop/api/Lpmapi/nf-lpmapi-lpm_commitresv)
-   [*LPM\_Deinitialize*](/previous-versions/windows/desktop/api/Lpmapi/nf-lpmapi-lpm_deinitialize)
-   [*LPM\_DeleteState*](/previous-versions/windows/desktop/api/Lpmapi/nf-lpmapi-lpm_deletestate)
-   [*LPM\_GetRsvpObjects*](/previous-versions/windows/desktop/api/Lpmapi/nf-lpmapi-lpm_getrsvpobjects)
-   [*LPM\_Initialize*](/previous-versions/windows/desktop/api/Lpmapi/nf-lpmapi-lpm_initialize)
-   [*Lpm\_IpAddressTable*](/previous-versions/windows/desktop/api/Lpmapi/nf-lpmapi-lpm_ipaddresstable)

 

 





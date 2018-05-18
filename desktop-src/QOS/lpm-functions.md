---
title: LPM Functions
description: The following functions are exposed by the Microsoft-provided LPM, Msidlpm.dll.
ms.assetid: '67550ae2-c7c6-4278-98e8-aecc71abc624'
keywords: ["Quality of Service QOS , reference, LPM functions"]
---

# LPM Functions

The following functions are exposed by the Microsoft-provided LPM, Msidlpm.dll.

-   [*cbAdmitResult*](cbadmitresult.md)
-   [*cbGetRsvpObjects*](cbgetrsvpobjects.md)
-   [*PALLOCMEM*](pallocmem.md)
-   [*PFREEMEM*](pfreemem.md)

The following functions must be exposed by each LPM; they allow the PCM to communicate requests from the Subnet Bandwidth Manager (SBM) (through the PCM). The Microsoft-supplied LPM, implemented as a DLL in Msidlpm.dll, also uses this API. Note that callback functions, identified by their cb prefix, should not be exposed by LPMs; these callback functions, which are exposed by the PCM, facilitate deferred response from LPMs to PCM requests.

-   [*LPM\_AdmitRsvpMsg*](lpm-admitrsvpmsg.md)
-   [*LPM\_CommitResv*](lpm-commitresv.md)
-   [*LPM\_Deinitialize*](lpm-deinitialize.md)
-   [*LPM\_DeleteState*](lpm-deletestate.md)
-   [*LPM\_GetRsvpObjects*](lpm-getrsvpobjects.md)
-   [*LPM\_Initialize*](lpm-initialize.md)
-   [*Lpm\_IpAddressTable*](lpm-ipaddresstable.md)

 

 





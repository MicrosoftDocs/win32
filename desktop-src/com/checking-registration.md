---
title: Checking Registration
description: Checking Registration
ms.assetid: 7df63955-d838-4518-8473-0c1a24e90f69
ms.topic: article
ms.date: 05/31/2018
---

# Checking Registration

Each time an application loads, it should check its registration to determine the following:

-   Whether the CLSIDs are present in the registry. If they are not present, the application should register as the original setup.
-   Whether the application's CLSIDs are present in the register but have no OLE 2-related information in them. If this is the case, the application should register as the original setup.
-   Whether the path containing server entries ([LocalServer](localserver.md) and [LocalServer32](localserver32.md), [InprocServer](inprocserver.md) and [InprocServer32](inprocserver32.md), and [DefaultIcon](defaulticon.md)) points to the location at which the application is currently installed. If the path does not, rewrite the path entries to point to the current location.

## Related topics

<dl> <dt>

[Registering COM Applications](registering-com-applications.md)
</dt> </dl>

 

 





---
title: Obtaining a Machine SDO
description: The first step in using the SDO API is to create an SDO machine object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bdb01437-08d0-4279-94f2-840cb786cc44
ms.prod: windows-server-dev
ms.technology: network-policy-and-access-services
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining a Machine SDO

The first step in using the SDO API is to create an SDO machine object.

Use the [**CLSIDFromProgID**](https://msdn.microsoft.com/windows/desktop/89fb20af-65bf-4ed4-9f71-eb707ee8eb09) function to obtain the class identifier (CLSID) for the SDO machine object. The programmatic identifier (ProgID) to use for the object is "IAS.SdoMachine".

Once you have the CLSID, call [**CoCreateInstance**](https://msdn.microsoft.com/windows/desktop/7295a55b-12c7-4ed0-a7a4-9ecee16afdec) with this CLSID. Specify [**ISdoMachine**](https://msdn.microsoft.com/library/bb960655) as the interface for which to return a pointer.

See [Attaching to an SDO-Enabled Computer](https://msdn.microsoft.com/library/bb960609) for sample code that demonstrates how to obtain a machine SDO.

 

 





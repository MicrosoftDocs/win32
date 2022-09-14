---
title: Obtaining a Machine SDO
description: The first step in using the SDO API is to create an SDO machine object.
ms.assetid: bdb01437-08d0-4279-94f2-840cb786cc44
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining a Machine SDO

The first step in using the SDO API is to create an SDO machine object.

Use the [**CLSIDFromProgID**](/windows/win32/api/combaseapi/nf-combaseapi-clsidfromprogid) function to obtain the class identifier (CLSID) for the SDO machine object. The programmatic identifier (ProgID) to use for the object is "IAS.SdoMachine".

Once you have the CLSID, call [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) with this CLSID. Specify [**ISdoMachine**](/windows/desktop/api/sdoias/nn-sdoias-isdomachine) as the interface for which to return a pointer.

See [Attaching to an SDO-Enabled Computer](/windows/desktop/Nps/sdo-attaching-to-an-sdo-enabled-computer) for sample code that demonstrates how to obtain a machine SDO.

 

 
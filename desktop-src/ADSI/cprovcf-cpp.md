---
title: CPROVCF.CPP
description: In the example provider component, one code example of the ADs provider object class factory code is in cprovcf.cpp.
ms.assetid: 53a4da74-3f36-4e6d-ae93-8d595680bcf3
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# CPROVCF.CPP

In the example provider component, one code example of the ADs provider object class factory code is in cprovcf.cpp. The provider component never directly creates an instance of this object at any time other than when the object is created automatically during the binding operations in [**ADsGetObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsgetobject) or the internal function in the Visual Basic method **GetObject**. The supported method is listed in the following table.



| Method                                  | Description                                                           |
|-----------------------------------------|-----------------------------------------------------------------------|
| **CSampleDSProviderCF::CreateInstance** | Creates an instance of the class factory for the ADS provider object. |



 

 

 





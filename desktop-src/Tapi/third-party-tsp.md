---
description: Specialized communications hardware such as cable modems or telephony cards typically arrive with one or more TSPs and MSPs specific to the device. Documentation for the device should indicate capabilities and give programming guidelines.
ms.assetid: 9033b651-c8f4-47f1-b953-557b519ea3bc
title: Third-Party TSP
ms.topic: article
ms.date: 05/31/2018
---

# Third-Party TSP

Specialized communications hardware such as cable modems or telephony cards typically arrive with one or more TSPs and MSPs specific to the device. Documentation for the device should indicate capabilities and give programming guidelines.

If a legacy TSP does not have an MSP but does use wave devices, TAPI will associate the Wave MSP with that TSP. Legacy TSPs that do not use wave devices will not be assigned an associated MSP, and stream control operations will not be available.

A third-party TSP is installed with the device it is intended to support.

 

 




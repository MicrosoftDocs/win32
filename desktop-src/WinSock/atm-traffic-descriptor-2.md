---
description: This section lists the ATM traffic descriptor.
ms.assetid: 8d15af95-2003-416e-b3b0-a9201972a899
title: ATM Traffic Descriptor
ms.topic: article
ms.date: 05/31/2018
---

# ATM Traffic Descriptor

This section lists the ATM traffic descriptor.

``` syntax
typedef struct {
    ULONG PeakCellRate_CLP0;
    ULONG PeakCellRate_CLP01;
    ULONG SustainableCellRate_CLP0;
    ULONG SustainableCellRate_CLP01;
    ULONG MaxBurstSize_CLP0;
    ULONG MaxBurstSize_CLP01;
    BOOL  Tagging;
} ATM_TD;

typedef struct {
    ATM_TD Forward;
    ATM_TD Backward;
    BOOL   BestEffort;
} ATM_TRAFFIC_DESCRIPTOR_IE;
```

 

 




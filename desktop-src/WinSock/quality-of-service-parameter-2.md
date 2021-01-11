---
description: This section lists the parameters used for quality of service (QoS).
ms.assetid: befbcf01-ecd2-4316-8e5e-889e918272cc
title: Quality of Service Parameter
ms.topic: article
ms.date: 05/31/2018
---

# Quality of Service Parameter

This section lists the parameters used for quality of service (QoS).

``` syntax
#include <windows.h>
/* 
 *  values used for the QOSClassForward and QOSClassBackward
 *  field in struct ATM_QOS_CLASS_IE
 */
#define QOS_CLASS0                  0x00
#define QOS_CLASS1                  0x01
#define QOS_CLASS2                  0x02
#define QOS_CLASS3                  0x03
#define QOS_CLASS4                  0x04

typedef struct {
    UCHAR QOSClassForward;
    UCHAR QOSClassBackward;
} ATM_QOS_CLASS_IE;
```

 

 




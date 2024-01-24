---
description: This section lists the type definition for the calling party number.
ms.assetid: eb930123-28cf-4857-b7ad-f3c1786da7cc
title: Calling Party Number
ms.topic: article
ms.date: 05/31/2018
---

# Calling Party Number

This section lists the type definition for the calling party number.

``` syntax
#include <windows.h>

/* 
 *  values used for the Presentation_Indication field in 
 *  struct ATM_CALLING_PARTY_NUMBER_IE
 */
#define PI_ALLOWED                  0x00
#define PI_RESTRICTED               0x40
#define PI_NUMBER_NOT_AVAILABLE     0x80

/* 
 *  values used for the Screening_Indicator field in 
 *  struct ATM_CALLING_PARTY_NUMBER_IE
 */
#define SI_USER_NOT_SCREENED        0x00
#define SI_USER_PASSED              0x01
#define SI_USER_FAILED              0x02
#define SI_NETWORK                  0x03

typedef struct {
    ATM_ADDRESS ATM_Number;
    UCHAR       Presentation_Indication;
    UCHAR       Screening_Indicator;
} ATM_CALLING_PARTY_NUMBER_IE;
```

 

 




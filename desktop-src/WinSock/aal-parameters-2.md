---
description: AAL parameters.
ms.assetid: 0afc6713-2e91-4914-8039-1ecaed104826
title: AAL Parameters
ms.topic: article
ms.date: 05/31/2018
---

# AAL Parameters

``` syntax
#include <windows.h>

/* 
 *  manifest constants for the AALType field in struct AAL_PARAMETERS_IE
 */
typedef enum {
    AALTYPE_5     = 5,   /* AAL 5 */
    AALTYPE_USER  = 16   /* user-defined AAL */
} AAL_TYPE;

/* 
 *  values used for the Mode field in struct AAL5_PARAMETERS
 */
#define AAL5_MODE_MESSAGE           0x01
#define AAL5_MODE_STREAMING         0x02

/* 
 *  values used for the SSCSType field in struct AAL5_PARAMETERS
 */
#define AAL5_SSCS_NULL              0x00
#define AAL5_SSCS_SSCOP_ASSURED     0x01
#define AAL5_SSCS_SSCOP_NON_ASSURED 0x02
#define AAL5_SSCS_FRAME_RELAY       0x04

typedef struct {
    ULONG ForwardMaxCPCSSDUSize;
    ULONG BackwardMaxCPCSSDUSize;
    UCHAR Mode;                        /* only available in UNI 3.0 */
    UCHAR SSCSType;
} AAL5_PARAMETERS;

typedef struct {
    ULONG UserDefined;
} AALUSER_PARAMETES; 
    
typedef struct {
    AAL_TYPE AALType;
    union {
        AAL5_PARAMETERS     AAL5Parameters;
        AALUSER_PARAMETERS  AALUserParameters;
    } AALSpecificParameters;
} AAL_PARAMETERS_IE;
```

 

 




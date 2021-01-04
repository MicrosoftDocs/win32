---
title: MPCALLBACK_TYPE enumeration (MpClient.h)
description: Possible callback types.
ms.assetid: 8E4F50B7-0F02-434D-B91E-C9966C92CDC0
keywords:
- MPCALLBACK_TYPE enumeration Legacy Windows Environment Features
- PMPCALLBACK_TYPE enumeration pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPCALLBACK_TYPE
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPCALLBACK\_TYPE enumeration

Possible callback types.

## Syntax


```C++
typedef enum tagMPCALLBACK_TYPE { 
  MPCALLBACK_UNKNOWN                     = 0,
  MPCALLBACK_STATUS                      = 1,
  MPCALLBACK_THREAT                      = 2,
  MPCALLBACK_SCAN                        = 3,
  MPCALLBACK_CLEAN                       = 4,
  MPCALLBACK_PRECHECK                    = 5,
  MPCALLBACK_SIGUPDATE                   = 6,
  MPCALLBACK_SAMPLE                      = 7,
  MPCALLBACK_RESERVED                    = 8,
  MPCALLBACK_CONFIGURATION_NOTIFICATION  = 9,
  MPCALLBACK_FASTPATH                    = 10,
  MPCALLBACK_PRODUCT_EXPIRATION          = 11,
  MPCALLBACK_NIS_PRIVATE                 = 12,
  MPCALLBACK_HEALTH                      = 13,
  MPCALLBACK_ENDOFLIFE                   = 14,
  MPCALLBACK_MALWARETOAST                = 15,
  MPCALLBACK_MAXVALUE                    = 15
} MPCALLBACK_TYPE, *PMPCALLBACK_TYPE;
```



## Constants

<dl> <dt>

<span id="MPCALLBACK_UNKNOWN"></span><span id="mpcallback_unknown"></span>**MPCALLBACK\_UNKNOWN**
</dt> <dd></dd> <dt>

<span id="MPCALLBACK_STATUS"></span><span id="mpcallback_status"></span>**MPCALLBACK\_STATUS**
</dt> <dd></dd> <dt>

<span id="MPCALLBACK_THREAT"></span><span id="mpcallback_threat"></span>**MPCALLBACK\_THREAT**
</dt> <dd></dd> <dt>

<span id="MPCALLBACK_SCAN"></span><span id="mpcallback_scan"></span>**MPCALLBACK\_SCAN**
</dt> <dd></dd> <dt>

<span id="MPCALLBACK_CLEAN"></span><span id="mpcallback_clean"></span>**MPCALLBACK\_CLEAN**
</dt> <dd></dd> <dt>

<span id="MPCALLBACK_PRECHECK"></span><span id="mpcallback_precheck"></span>**MPCALLBACK\_PRECHECK**
</dt> <dd></dd> <dt>

<span id="MPCALLBACK_SIGUPDATE"></span><span id="mpcallback_sigupdate"></span>**MPCALLBACK\_SIGUPDATE**
</dt> <dd></dd> <dt>

<span id="MPCALLBACK_SAMPLE"></span><span id="mpcallback_sample"></span>**MPCALLBACK\_SAMPLE**
</dt> <dd></dd> <dt>

<span id="MPCALLBACK_RESERVED"></span><span id="mpcallback_reserved"></span>**MPCALLBACK\_RESERVED**
</dt> <dd></dd> <dt>

<span id="MPCALLBACK_CONFIGURATION_NOTIFICATION"></span><span id="mpcallback_configuration_notification"></span>**MPCALLBACK\_CONFIGURATION\_NOTIFICATION**
</dt> <dd></dd> <dt>

<span id="MPCALLBACK_FASTPATH"></span><span id="mpcallback_fastpath"></span>**MPCALLBACK\_FASTPATH**
</dt> <dd></dd> <dt>

<span id="MPCALLBACK_PRODUCT_EXPIRATION"></span><span id="mpcallback_product_expiration"></span>**MPCALLBACK\_PRODUCT\_EXPIRATION**
</dt> <dd></dd> <dt>

<span id="MPCALLBACK_NIS_PRIVATE"></span><span id="mpcallback_nis_private"></span>**MPCALLBACK\_NIS\_PRIVATE**
</dt> <dd></dd> <dt>

<span id="MPCALLBACK_HEALTH"></span><span id="mpcallback_health"></span>**MPCALLBACK\_HEALTH**
</dt> <dd></dd> <dt>

<span id="MPCALLBACK_ENDOFLIFE"></span><span id="mpcallback_endoflife"></span>**MPCALLBACK\_ENDOFLIFE**
</dt> <dd></dd> <dt>

<span id="MPCALLBACK_MALWARETOAST"></span><span id="mpcallback_malwaretoast"></span>**MPCALLBACK\_MALWARETOAST**
</dt> <dd></dd> <dt>

<span id="MPCALLBACK_MAXVALUE"></span><span id="mpcallback_maxvalue"></span>**MPCALLBACK\_MAXVALUE**
</dt> <dd></dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 






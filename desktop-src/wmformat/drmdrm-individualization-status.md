---
title: DRM_INDIVIDUALIZATION_STATUS enumeration (Wmdrmsdk.h)
description: The DRM\_INDIVIDUALIZATION\_STATUS enumeration type defines the valid states for DRM individualization. | DRM_INDIVIDUALIZATION_STATUS enumeration (Wmdrmsdk.h)
ms.assetid: 4e6712e2-3297-4636-9b0c-07269bd63d52
keywords:
- DRM_INDIVIDUALIZATION_STATUS enumeration windows Media Format
- enumeration windows Media Format
topic_type:
- apiref
api_name:
- DRM_INDIVIDUALIZATION_STATUS
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRM_INDIVIDUALIZATION_STATUS enumeration (Wmdrmsdk.h)

The **DRM\_INDIVIDUALIZATION\_STATUS** enumeration type defines the valid states for DRM individualization.

## Syntax


```C++
typedef enum DRM_INDIVIDUALIZATION_STATUS { 
  INDI_UNDEFINED  = 0x0000,
  INDI_BEGIN      = 0x0001,
  INDI_SUCCEED    = 0x0002,
  INDI_FAIL       = 0x0004,
  INDI_CANCEL     = 0x0008,
  INDI_DOWNLOAD   = 0x0010,
  INDI_INSTALL    = 0x0020
} ;
```



## Constants

<dl> <dt>

<span id="INDI_UNDEFINED"></span><span id="indi_undefined"></span>**INDI\_UNDEFINED**
</dt> <dd>

This value is reserved for future use.

</dd> <dt>

<span id="INDI_BEGIN"></span><span id="indi_begin"></span>**INDI\_BEGIN**
</dt> <dd>

Indicates the start of the individualization process.

</dd> <dt>

<span id="INDI_SUCCEED"></span><span id="indi_succeed"></span>**INDI\_SUCCEED**
</dt> <dd>

Indicates that the individualization process has been completed.

</dd> <dt>

<span id="INDI_FAIL"></span><span id="indi_fail"></span>**INDI\_FAIL**
</dt> <dd>

Indicates that the individualization process failed.

</dd> <dt>

<span id="INDI_CANCEL"></span><span id="indi_cancel"></span>**INDI\_CANCEL**
</dt> <dd>

Indicates that the individualization process was canceled by the application.

</dd> <dt>

<span id="INDI_DOWNLOAD"></span><span id="indi_download"></span>**INDI\_DOWNLOAD**
</dt> <dd>

Indicates that the security upgrade is being downloaded.

</dd> <dt>

<span id="INDI_INSTALL"></span><span id="indi_install"></span>**INDI\_INSTALL**
</dt> <dd>

Indicates that the security upgrade is being installed.

</dd> </dl>

## Remarks

This enumeration is used by the [**WM\_INDIVIDUALIZE\_STATUS**](drmwm-individualize-status.md) structure.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Enumeration Types**](drm-enumeration-types.md)
</dt> </dl>

 

 






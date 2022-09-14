---
title: MSDRM_STATUS enumeration (Wmdrmsdk.h)
description: The MSDRM\_STATUS enumeration type defines status conditions for the DRM subsystem.
ms.assetid: b26600ea-2603-4fca-9408-2d5c88091dcc
keywords:
- MSDRM_STATUS enumeration windows Media Format
- enumeration windows Media Format
topic_type:
- apiref
api_name:
- MSDRM_STATUS
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MSDRM\_STATUS enumeration

The **MSDRM\_STATUS** enumeration type defines status conditions for the DRM subsystem.

## Syntax


```C++
typedef enum MSDRM_STATUS { 
  DRM_ERROR                        = 0,
  DRM_INFORMATION                  = 1,
  DRM_BACKUPRESTORE_BEGIN          = 2,
  DRM_BACKUPRESTORE_END            = 3,
  DRM_BACKUPRESTORE_CONNECTING     = 4,
  DRM_BACKUPRESTORE_DISCONNECTING  = 5,
  DRM_ERROR_WITHURL                = 6,
  DRM_RESTRICTED_LICENSE           = 7,
  DRM_NEEDS_INDIVIDUALIZATION      = 8,
  DRM_PLAY_OPL_NOTIFICATION        = 9,
  DRM_COPY_OPL_NOTIFICATION        = 10,
  DRM_REFRESHCRL_COMPLETE          = 11
} ;
```



## Constants

<dl> <dt>

<span id="DRM_ERROR"></span><span id="drm_error"></span>**DRM\_ERROR**
</dt> <dd>

Specifies that an error has occurred.

</dd> <dt>

<span id="DRM_INFORMATION"></span><span id="drm_information"></span>**DRM\_INFORMATION**
</dt> <dd>

Specifies that there is additional status information.

</dd> <dt>

<span id="DRM_BACKUPRESTORE_BEGIN"></span><span id="drm_backuprestore_begin"></span>**DRM\_BACKUPRESTORE\_BEGIN**
</dt> <dd>

Specifies that a license backup or restore operation has begun.

</dd> <dt>

<span id="DRM_BACKUPRESTORE_END"></span><span id="drm_backuprestore_end"></span>**DRM\_BACKUPRESTORE\_END**
</dt> <dd>

Specifies that a license backup or restore operation has ended.

</dd> <dt>

<span id="DRM_BACKUPRESTORE_CONNECTING"></span><span id="drm_backuprestore_connecting"></span>**DRM\_BACKUPRESTORE\_CONNECTING**
</dt> <dd>

Specifies that a license backup or restore operation is in progress and that the client computer is connecting with the backup server.

</dd> <dt>

<span id="DRM_BACKUPRESTORE_DISCONNECTING"></span><span id="drm_backuprestore_disconnecting"></span>**DRM\_BACKUPRESTORE\_DISCONNECTING**
</dt> <dd>

Specifies that a license backup or restore operation is in progress and that the client computer is disconnecting from the backup server.

</dd> <dt>

<span id="DRM_ERROR_WITHURL"></span><span id="drm_error_withurl"></span>**DRM\_ERROR\_WITHURL**
</dt> <dd>

Specifies that the DRM operation has encountered a bad URL.

</dd> <dt>

<span id="DRM_RESTRICTED_LICENSE"></span><span id="drm_restricted_license"></span>**DRM\_RESTRICTED\_LICENSE**
</dt> <dd>

Specifies that the DRM operation cannot continue because no license granting the required right exists on the client computer.

</dd> <dt>

<span id="DRM_NEEDS_INDIVIDUALIZATION"></span><span id="drm_needs_individualization"></span>**DRM\_NEEDS\_INDIVIDUALIZATION**
</dt> <dd>

Specifies that the DRM operation cannot continue because the DRM subsystem needs to be individualized.

</dd> <dt>

<span id="DRM_PLAY_OPL_NOTIFICATION"></span><span id="drm_play_opl_notification"></span>**DRM\_PLAY\_OPL\_NOTIFICATION**
</dt> <dd>

Specifies that a playback operation cannot be completed because an output protection level requirement has not been met.

</dd> <dt>

<span id="DRM_COPY_OPL_NOTIFICATION"></span><span id="drm_copy_opl_notification"></span>**DRM\_COPY\_OPL\_NOTIFICATION**
</dt> <dd>

Specifies that a copy operation cannot be completed because an output protection level requirement has not been met.

</dd> <dt>

<span id="DRM_REFRESHCRL_COMPLETE"></span><span id="drm_refreshcrl_complete"></span>**DRM\_REFRESHCRL\_COMPLETE**
</dt> <dd>

Specifies that a call to [**IWMDRMSecurity::PerformSecurityUpdate**](iwmdrmsecurity-performsecurityupdate.md) has completed refreshing a revocation list.

</dd> </dl>

## Remarks

None.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Enumeration Types**](drm-enumeration-types.md)
</dt> </dl>

 

 






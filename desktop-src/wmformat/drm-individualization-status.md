---
title: DRM_INDIVIDUALIZATION_STATUS enumeration (Drmexternals.h)
description: The DRM\_INDIVIDUALIZATION\_STATUS enumeration type defines the valid states for DRM individualization. | DRM_INDIVIDUALIZATION_STATUS enumeration (Drmexternals.h)
ms.assetid: '76748fb3-340e-47e2-969d-5e857bb4e4d8'
keywords:
- DRM_INDIVIDUALIZATION_STATUS enumeration windows Media Format
- enumeration windows Media Format
topic_type:
- apiref
api_name:
- DRM_INDIVIDUALIZATION_STATUS
api_location:
- Drmexternals.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRM_INDIVIDUALIZATION_STATUS enumeration (Drmexternals.h)

The **DRM\_INDIVIDUALIZATION\_STATUS** enumeration type defines the valid states for DRM [*individualization*](wmformat-glossary.md). When an application initiates individualization with a call to [**IWMDRMReader::Individualize**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-individualize), the progress of the individualization request is conveyed to the application through calls to the [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) method. Individualization status messages will all use the WMT\_INDIVIDUALIZE member of the [**WMT\_STATUS**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_status) enumeration type as the *Status* parameter. The status of the individualization is passed to **OnStatus** in the *pValue* parameter.

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

Indicates that the individualization process was canceled as the result of a call to [**IWMDRMReader::CancelIndividualization**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-cancelindividualization).

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

This enumeration is used by the [**WM\_INDIVIDUALIZE\_STATUS**](wm-individualize-status.md) structure.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                      |
| Version<br/>                  | Windows Media Format 7 SDK, or later versions of the SDK<br/>                       |
| Header<br/>                   | <dl> <dt>Drmexternals.h</dt> </dl> |



## See also

<dl> <dt>

[**DRM\_HTTP\_STATUS**](drm-http-status.md)
</dt> <dt>

[**Enumeration Types**](enumeration-types.md)
</dt> </dl>

 

 






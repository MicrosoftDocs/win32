---
title: DRM_HTTP_STATUS enumeration (Drmexternals.h)
description: The DRM\_HTTP\_STATUS enumeration type defines a range of states for a DRM request.
ms.assetid: '9e0fb060-3fbf-45d0-872b-4d666ea9a88d'
keywords:
- DRM_HTTP_STATUS enumeration windows Media Format
- enumeration windows Media Format
topic_type:
- apiref
api_name:
- DRM_HTTP_STATUS
api_location:
- Drmexternals.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRM_HTTP_STATUS enumeration (Drmexternals.h)

The **DRM\_HTTP\_STATUS** enumeration type defines a range of states for a [*DRM*](wmformat-glossary.md) request.

## Syntax


```C++
typedef enum DRM_HTTP_STATUS { 
  HTTP_NOTINITIATED  = 0,
  HTTP_CONNECTING    = 1,
  HTTP_REQUESTING    = 2,
  HTTP_RECEIVING     = 3,
  HTTP_COMPLETED     = 4
} ;
```



## Constants

<dl> <dt>

<span id="HTTP_NOTINITIATED"></span><span id="http_notinitiated"></span>**HTTP\_NOTINITIATED**
</dt> <dd>

The HTTP operations have not been initiated.

</dd> <dt>

<span id="HTTP_CONNECTING"></span><span id="http_connecting"></span>**HTTP\_CONNECTING**
</dt> <dd>

The connection is being established.

</dd> <dt>

<span id="HTTP_REQUESTING"></span><span id="http_requesting"></span>**HTTP\_REQUESTING**
</dt> <dd>

Data is being requested.

</dd> <dt>

<span id="HTTP_RECEIVING"></span><span id="http_receiving"></span>**HTTP\_RECEIVING**
</dt> <dd>

Data is being received.

</dd> <dt>

<span id="HTTP_COMPLETED"></span><span id="http_completed"></span>**HTTP\_COMPLETED**
</dt> <dd>

The HTTP operations are complete.

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

[**DRM\_INDIVIDUALIZATION\_STATUS**](drm-individualization-status.md)
</dt> <dt>

[**Enumeration Types**](enumeration-types.md)
</dt> </dl>

 

 






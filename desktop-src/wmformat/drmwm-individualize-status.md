---
title: WM_INDIVIDUALIZE_STATUS structure (Wmdrmsdk.h)
description: The WM\_INDIVIDUALIZE\_STATUS structure holds information about a pending individualization process.
ms.assetid: af7e8758-489b-461f-b241-d7e40c8d61da
keywords:
- WM_INDIVIDUALIZE_STATUS structure windows Media Format
topic_type:
- apiref
api_name:
- WM_INDIVIDUALIZE_STATUS
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM_INDIVIDUALIZE_STATUS structure (Wmdrmsdk.h)

The **WM\_INDIVIDUALIZE\_STATUS** structure holds information about a pending individualization process.

## Syntax


```C++
typedef struct _WMIndividualizeStatus {
  HRESULT                      hr;
  DRM_INDIVIDUALIZATION_STATUS enIndiStatus;
  LPSTR                        pszIndiRespUrl;
  DWORD                        dwHTTPRequest;
  DRM_HTTP_STATUS              enHTTPStatus;
  DWORD                        dwHTTPReadProgress;
  DWORD                        dwHTTPReadTotal;
} WM_INDIVIDUALIZE_STATUS;
```



## Members

<dl> <dt>

**hr**
</dt> <dd>

**HRESULT** return code.

</dd> <dt>

**enIndiStatus**
</dt> <dd>

Value from the [**DRM\_INDIVIDUALIZATION\_STATUS**](drmdrm-individualization-status.md) enumeration type that indicates the current status of the individualization process.

</dd> <dt>

**pszIndiRespUrl**
</dt> <dd>

Pointer to a null-terminated string containing the individualization response URL.

</dd> <dt>

**dwHTTPRequest**
</dt> <dd>

The number of HTTP round trips to the individualization service that have been completed.

</dd> <dt>

**enHTTPStatus**
</dt> <dd>

Value from the [**DRM\_HTTP\_STATUS**](drmdrm-http-status.md) enumeration type.

</dd> <dt>

**dwHTTPReadProgress**
</dt> <dd>

The number of bytes downloaded.

</dd> <dt>

**dwHTTPReadTotal**
</dt> <dd>

The total number of bytes to be downloaded. You can use this value and **dwHTTPReadProgress** to display a user interface indicating how much of the download has completed and how much remains to be done.

</dd> </dl>

## Remarks

This structure is received when you call the [**IWMDRMIndividualizationStatus::GetStatus**](iwmdrmindividualizationstatus-getstatus.md) method. It contains the status of the pending individualization process at the time of the call.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 






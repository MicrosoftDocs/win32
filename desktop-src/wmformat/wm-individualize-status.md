---
title: WM_INDIVIDUALIZE_STATUS structure (Drmexternals.h)
description: The WM\_INDIVIDUALIZE\_STATUS structure records the status of the individualization process.
ms.assetid: '3779ed6f-c133-4a9d-b60c-ef8c41fcc4af'
keywords:
- WM_INDIVIDUALIZE_STATUS structure windows Media Format
topic_type:
- apiref
api_name:
- WM_INDIVIDUALIZE_STATUS
api_location:
- Drmexternals.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM_INDIVIDUALIZE_STATUS structure (Drmexternals.h)

The **WM\_INDIVIDUALIZE\_STATUS** structure records the status of the [*individualization*](wmformat-glossary.md) process.

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

Value from the [**DRM\_INDIVIDUALIZATION\_STATUS**](drm-individualization-status.md) enumeration type.

</dd> <dt>

**pszIndiRespUrl**
</dt> <dd>

Pointer to a null-terminated string containing the individualization response URL.

</dd> <dt>

**dwHTTPRequest**
</dt> <dd>

**DWORD** that indicates the number of HTTP round trips to the individualization service that have been completed..

</dd> <dt>

**enHTTPStatus**
</dt> <dd>

Value from the [**DRM\_HTTP\_STATUS**](drm-http-status.md) enumeration type.

</dd> <dt>

**dwHTTPReadProgress**
</dt> <dd>

**DWORD** containing the number of bytes downloaded until now..

</dd> <dt>

**dwHTTPReadTotal**
</dt> <dd>

**DWORD** containing the total number of bytes to be downloaded. Use this value and **dwHTTPReadProgress** to display a user interface indicating how much of the download has completed and how much remains to be done.

</dd> </dl>

## Remarks

This structure is filled in by the DRM run-time components and is sent to applications in the *pValue* parameter of the applications [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) method when the event equals WMT\_INDIVIDUALIZE. The application receives this event multiple times during the download process.

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

[**Structures**](structures.md)
</dt> </dl>

 

 






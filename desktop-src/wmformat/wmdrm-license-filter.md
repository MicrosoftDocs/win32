---
title: WMDRM_LICENSE_FILTER structure (Wmdrmsdk.h)
description: The WMDRM\_LICENSE\_FILTER structure defines filtering parameters for use when creating a license enumeration.
ms.assetid: 43bbbfdc-1ec4-44a6-8245-96853bbeea86
keywords:
- WMDRM_LICENSE_FILTER structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- WMDRM_LICENSE_FILTER
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDRM\_LICENSE\_FILTER structure

The **WMDRM\_LICENSE\_FILTER** structure defines filtering parameters for use when creating a license enumeration.

## Syntax


```C++
typedef struct WMDRM_LICENSE_FILTER {
  DWORD dwVersion;
  BSTR  bstrKID;
  BSTR  bstrRights;
  BSTR  bstrAllowedSourceIDs;
} ;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

Specifies a minimum version number for the returned licenses.

</dd> <dt>

**bstrKID**
</dt> <dd>

Specifies a key ID to filter licenses for. Only licenses with the specified key ID will be included in the enumeration.

</dd> <dt>

**bstrRights**
</dt> <dd>

Specifies a set of rights to filter licenses for. Only licenses that provide all of the specified rights will be included in the enumeration.

</dd> <dt>

**bstrAllowedSourceIDs**
</dt> <dd>

Specifies the sources of protected content to include in the license search.

</dd> </dl>

## Remarks

This structure is used by the [**IWMDRMLicenseManagement::CreateLicenseEnumeration**](iwmdrmlicensemanagement-createlicenseenumeration.md) method.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 






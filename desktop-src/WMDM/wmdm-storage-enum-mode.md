---
title: WMDM_STORAGE_ENUM_MODE enumeration
description: The WMDM\_STORAGE\_ENUM\_MODE enumeration type defines how the content on the storage is to be enumerated. This enumeration is used by IWMDMStorage3 SetEnumPreference.
ms.assetid: 38293e54-92e4-4f0a-bdea-5dc684a9548b
keywords:
- WMDM_STORAGE_ENUM_MODE enumeration windows Media Device Manager
topic_type:
- apiref
api_name:
- WMDM_STORAGE_ENUM_MODE
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDM\_STORAGE\_ENUM\_MODE enumeration

The **WMDM\_STORAGE\_ENUM\_MODE** enumeration type defines how the content on the storage is to be enumerated. This enumeration is used by [**IWMDMStorage3::SetEnumPreference**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage3-setenumpreference).

## Syntax


```C++
typedef enum tagWMDM_STORAGE_ENUM_MODE { 
  ENUM_MODE_RAW,
  ENUM_MODE_USE_DEVICE_PREF,
  ENUM_MODE_METADATA_VIEWS
} WMDM_STORAGE_ENUM_MODE;
```



## Constants

<dl> <dt>

<span id="ENUM_MODE_RAW"></span><span id="enum_mode_raw"></span>**ENUM\_MODE\_RAW**
</dt> <dd>

Enumerates content on the storage just as it is organized in the file system of the storage.

**ENUM\_MODE\_USE\_DEVICE\_PREF**

Enumerates content on the storage based on the device preference as indicated by the *UseMetadataViews* device parameter.

**ENUM\_MODE\_METADATA\_VIEWS**

Enumerates content on the storage by organizing the content based on a metadata view.

</dd> <dt>

<span id="ENUM_MODE_USE_DEVICE_PREF"></span><span id="enum_mode_use_device_pref"></span>**ENUM\_MODE\_USE\_DEVICE\_PREF**
</dt> <dd>

Enumerates content on the storage based on the device preference as indicated by the *UseMetadataViews* device parameter.

**ENUM\_MODE\_METADATA\_VIEWS**

Enumerates content on the storage by organizing the content based on a metadata view.

</dd> <dt>

<span id="ENUM_MODE_METADATA_VIEWS"></span><span id="enum_mode_metadata_views"></span>**ENUM\_MODE\_METADATA\_VIEWS**
</dt> <dd>

Enumerates content on the storage by organizing the content based on a metadata view.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**Enumeration Types**](enumeration-types.md)
</dt> </dl>

 

 






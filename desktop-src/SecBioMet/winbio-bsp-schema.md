---
title: WINBIO_BSP_SCHEMA structure (Winbio\_types.h)
description: Describes the capabilities of a biometric service provider.
ms.assetid: d690c735-55a1-4e2c-8b39-d52a1972bf93
keywords:
- WINBIO_BSP_SCHEMA structure Windows Biometric Framework API
- PWINBIO_BSP_SCHEMA structure pointer Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_BSP_SCHEMA
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_BSP\_SCHEMA structure

The **WINBIO\_BSP\_SCHEMA** structure describes the capabilities of a biometric service provider. This structure is used by the [**WinBioEnumServiceProviders**](/windows/desktop/api/Winbio/nf-winbio-winbioenumserviceproviders) function.

## Syntax


```C++
typedef struct _WINBIO_BSP_SCHEMA {
  WINBIO_BIOMETRIC_TYPE BiometricFactor;
  WINBIO_UUID           BspId;
  WINBIO_STRING         Description;
  WINBIO_STRING         Vendor;
  WINBIO_VERSION        Version;
} WINBIO_BSP_SCHEMA, *PWINBIO_BSP_SCHEMA;
```



## Members

<dl> <dt>

**BiometricFactor**
</dt> <dd>

The type of biometric measurement used by this device. Currently this must be **WINBIO\_TYPE\_FINGERPRINT**.

</dd> <dt>

**BspId**
</dt> <dd>

A value that uniquely identifies this biometric service provider component.

</dd> <dt>

**Description**
</dt> <dd>

A **NULL**-terminated Unicode string that contains a description of the biometric service provider.

</dd> <dt>

**Vendor**
</dt> <dd>

A **NULL**-terminated Unicode string that contains the name of the vendor supplying the biometric service provider.

</dd> <dt>

**Version**
</dt> <dd>

A [**WINBIO\_VERSION**](winbio-version.md) structure the contains the software version of the biometric service provider component.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Structures](client-application-structures.md)
</dt> <dt>

[**WinBioEnumServiceProviders**](/windows/desktop/api/Winbio/nf-winbio-winbioenumserviceproviders)
</dt> </dl>

 

 






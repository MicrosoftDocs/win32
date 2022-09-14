---
title: WMDM_PROP_CONFIG structure
description: The WMDM\_PROP\_CONFIG structure describes a set of compatible property values across all the properties supported by the device for a particular format. This structure contains a number of property descriptions in an array of WMDM\_PROP\_DESC structures.
ms.assetid: cf116861-e31d-4561-b262-e271888afc24
keywords:
- WMDM_PROP_CONFIG structure windows Media Device Manager
topic_type:
- apiref
api_name:
- WMDM_PROP_CONFIG
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDM\_PROP\_CONFIG structure

The **WMDM\_PROP\_CONFIG** structure describes a set of compatible property values across all the properties supported by the device for a particular format. This structure contains a number of property descriptions in an array of [**WMDM\_PROP\_DESC**](wmdm-prop-desc.md) structures.

## Syntax


```C++
typedef struct _WMDM_PROP_CONFIG {
  UINT           nPreference;
  UINT           nPropDesc;
  WMDM_PROP_DESC *pPropDesc;
} WMDM_PROP_CONFIG;
```



## Members

<dl> <dt>

**nPreference**
</dt> <dd>

Device's level of preference for this configuration. The lowest value indicates the most preferred configuration.

</dd> <dt>

**nPropDesc**
</dt> <dd>

Number of property descriptions contained in this configuration. There is a single property description for each property supported for the specified format.

</dd> <dt>

**pPropDesc**
</dt> <dd>

Pointer to an array of [**WMDM\_PROP\_DESC**](wmdm-prop-desc.md) structures containing property descriptions. The size of the array is equal to the value of **nPropDesc**. The application must free this memory when finished with it.

</dd> </dl>

## Remarks

The [**WMDM\_FORMAT\_CAPABILITY**](wmdm-format-capability.md) structure returned by [**IWMDMDevice3::GetFormatCapability**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice3-getformatcapability) for a particular format consists of a number of property configurations. **WMDM\_PROP\_CONFIG** structures describe those configurations.

A property configuration describes values for all the properties supported for a given format. The values of different properties in a single configuration are compatible with each other. For example, for an audio file, a configuration will include valid values of sample rate and valid values of the bit rate such that all combinations of these sample and bit rates can be played on the device.

The caller is required to free the memory used by **pPropDesc**. For an example of how to do this, see [**WMDM\_FORMAT\_CAPABILITY**](wmdm-format-capability.md).

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**IWMDMDevice3::GetFormatCapability**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice3-getformatcapability)
</dt> <dt>

[**WMDM\_ENUM\_PROP\_VALID\_VALUES\_FORM**](wmdm-enum-prop-valid-values-form.md)
</dt> <dt>

[**WMDM\_FORMAT\_CAPABILITY**](wmdm-format-capability.md)
</dt> <dt>

[**WMDM\_PROP\_DESC**](wmdm-prop-desc.md)
</dt> <dt>

[**WMDM\_PROP\_VALUES\_ENUM**](wmdm-prop-values-enum.md)
</dt> <dt>

[**WMDM\_PROP\_VALUES\_RANGE**](wmdm-prop-values-range.md)
</dt> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 






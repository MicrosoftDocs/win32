---
title: WMDM_PROP_VALUES_ENUM structure
description: The WMDM\_PROP\_VALUES\_ENUM structure contains an enumerated set of valid values for a particular property in a particular property configuration.
ms.assetid: 8094f3c0-a7ed-4e63-8503-aaac3fd9c012
keywords:
- WMDM_PROP_VALUES_ENUM structure windows Media Device Manager
topic_type:
- apiref
api_name:
- WMDM_PROP_VALUES_ENUM
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDM\_PROP\_VALUES\_ENUM structure

The **WMDM\_PROP\_VALUES\_ENUM** structure contains an enumerated set of valid values for a particular property in a particular property configuration.

## Syntax


```C++
typedef struct _WMDM_PROP_VALUES_ENUM {
  UINT        cEnumValues;
  PROPVARIANT *pValues;
} WMDM_PROP_VALUES_ENUM;
```



## Members

<dl> <dt>

**cEnumValues**
</dt> <dd>

Count of enumerated values.

</dd> <dt>

**pValues**
</dt> <dd>

Pointer to an array of values. The size of the array is equal to the value of **cEnumValues**.

</dd> </dl>

## Remarks

This structure is used in the **WMDM\_PROP\_DESC** structure to describe an enumerated set of valid values. An enumerated set of valid values is applicable when WMDM\_ENUM\_PROP\_VALID\_VALUES\_ENUM is selected from the **WMDM\_ENUM\_PROP\_VALID\_VALUES\_FORM** enumeration.

The caller is required to free the memory used by **pValues**. For an example of how to do this, see [**WMDM\_FORMAT\_CAPABILITY**](wmdm-format-capability.md).

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

[**WMDM\_PROP\_CONFIG**](wmdm-prop-config.md)
</dt> <dt>

[**WMDM\_PROP\_DESC**](wmdm-prop-desc.md)
</dt> <dt>

[**WMDM\_PROP\_VALUES\_RANGE**](wmdm-prop-values-range.md)
</dt> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 






---
title: WMDM_PROP_VALUES_RANGE structure
description: The WMDM\_PROP\_VALUES\_RANGE structure describes a range of valid values for a particular property in a particular property configuration.
ms.assetid: fb823a66-cc9c-4632-a4f0-03c7255c3ccb
keywords:
- WMDM_PROP_VALUES_RANGE structure windows Media Device Manager
topic_type:
- apiref
api_name:
- WMDM_PROP_VALUES_RANGE
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDM\_PROP\_VALUES\_RANGE structure

The **WMDM\_PROP\_VALUES\_RANGE** structure describes a range of valid values for a particular property in a particular property configuration.

## Syntax


```C++
typedef struct _WMDM_PROP_VALUES_RANGE {
  PROPVARIANT rangeMin;
  PROPVARIANT rangeMax;
  PROPVARIANT rangeStep;
} WMDM_PROP_VALUES_RANGE;
```



## Members

<dl> <dt>

**rangeMin**
</dt> <dd>

Minimum value in the range.

</dd> <dt>

**rangeMax**
</dt> <dd>

Maximum value in the range.

</dd> <dt>

**rangeStep**
</dt> <dd>

The step size in which valid values increment from the minimum value to the maximum value. This permits specifying discrete permissible values in a range.

</dd> </dl>

## Remarks

This structure is used in the [**WMDM\_PROP\_DESC**](wmdm-prop-desc.md) structure to describe a range of valid values. A range of valid values is applicable when WMDM\_ENUM\_PROP\_VALID\_VALUES\_ENUM is selected from the [**WMDM\_ENUM\_PROP\_VALID\_VALUES\_FORM**](wmdm-enum-prop-valid-values-form.md) enumeration.

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

[**WMDM\_PROP\_VALUES\_ENUM**](wmdm-prop-values-enum.md)
</dt> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 






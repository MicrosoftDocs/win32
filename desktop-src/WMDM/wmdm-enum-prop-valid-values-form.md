---
title: WMDM_ENUM_PROP_VALID_VALUES_FORM enumeration
description: The WMDM\_ENUM\_PROP\_VALID\_VALUES\_FORM enumeration type describes possible forms of valid values for a property.
ms.assetid: 49d174b4-c8a3-4c16-ad21-4b66dcf8088f
keywords:
- WMDM_ENUM_PROP_VALID_VALUES_FORM enumeration windows Media Device Manager
topic_type:
- apiref
api_name:
- WMDM_ENUM_PROP_VALID_VALUES_FORM
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDM\_ENUM\_PROP\_VALID\_VALUES\_FORM enumeration

The **WMDM\_ENUM\_PROP\_VALID\_VALUES\_FORM** enumeration type describes possible forms of valid values for a property.

## Syntax


```C++
typedef enum _WMDM_ENUM_PROP_VALID_VALUES_FORM { 
  WMDM_ENUM_PROP_VALID_VALUES_ANY,
  WMDM_ENUM_PROP_VALID_VALUES_RANGE,
  WMDM_ENUM_PROP_VALID_VALUES_ENUM
} WMDM_ENUM_PROP_VALID_VALUES_FORM;
```



## Constants

<dl> <dt>

<span id="WMDM_ENUM_PROP_VALID_VALUES_ANY"></span><span id="wmdm_enum_prop_valid_values_any"></span>**WMDM\_ENUM\_PROP\_VALID\_VALUES\_ANY**
</dt> <dd>

All values are valid.

</dd> <dt>

<span id="WMDM_ENUM_PROP_VALID_VALUES_RANGE"></span><span id="wmdm_enum_prop_valid_values_range"></span>**WMDM\_ENUM\_PROP\_VALID\_VALUES\_RANGE**
</dt> <dd>

Valid values are expressed as a range. For detailed information, see the [**WMDM\_PROP\_VALUES\_RANGE**](wmdm-prop-values-range.md) structure.

</dd> <dt>

<span id="WMDM_ENUM_PROP_VALID_VALUES_ENUM"></span><span id="wmdm_enum_prop_valid_values_enum"></span>**WMDM\_ENUM\_PROP\_VALID\_VALUES\_ENUM**
</dt> <dd>

Valid values are an enumerated set. For detailed information, see the [**WMDM\_PROP\_VALUES\_ENUM**](wmdm-prop-values-enum.md) structure.

</dd> </dl>

## Remarks

This enumeration is used in the [**WMDM\_PROP\_DESC**](wmdm-prop-desc.md) structure to specify the form of valid values for a property.

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**Enumeration Types**](enumeration-types.md)
</dt> <dt>

[**IWMDMDevice3::GetFormatCapability**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice3-getformatcapability)
</dt> <dt>

[**WMDM\_FORMAT\_CAPABILITY**](wmdm-format-capability.md)
</dt> <dt>

[**WMDM\_PROP\_CONFIG**](wmdm-prop-config.md)
</dt> <dt>

[**WMDM\_PROP\_DESC**](wmdm-prop-desc.md)
</dt> <dt>

[**WMDM\_PROP\_VALUES\_ENUM**](wmdm-prop-values-enum.md)
</dt> <dt>

[**WMDM\_PROP\_VALUES\_RANGE**](wmdm-prop-values-range.md)
</dt> </dl>

 

 






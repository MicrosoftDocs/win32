---
title: WMDM_PROP_DESC structure
description: The WMDM\_PROP\_DESC structure describes valid values of a property in a particular property configuration.
ms.assetid: e4766e1e-6c1b-4a2d-ad2e-c07035ca2be2
keywords:
- WMDM_PROP_DESC structure windows Media Device Manager
topic_type:
- apiref
api_name:
- WMDM_PROP_DESC
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDM\_PROP\_DESC structure

The **WMDM\_PROP\_DESC** structure describes valid values of a property in a particular property configuration.

## Syntax


```C++
typedef struct _WMDM_PROP_DESC {
  LPWSTR                           pwszPropName;
  WMDM_ENUM_PROP_VALID_VALUES_FORM ValidValuesForm;
  union  {
    WMDM_PROP_VALUES_RANGE ValidValuesRange;
    WMDM_PROP_VALUES_ENUM  EnumeratedValidValues;
  } ValidValues;
} WMDM_PROP_DESC;
```



## Members

<dl> <dt>

**pwszPropName**
</dt> <dd>

Name of the property. The application must free this memory when it is done using it.

</dd> <dt>

**ValidValuesForm**
</dt> <dd>

An [**WMDM\_ENUM\_PROP\_VALID\_VALUES\_FORM**](wmdm-enum-prop-valid-values-form.md) enumeration value describing the type of values, such as a range or list. The value of this enumeration determines which member variable is used.

</dd> <dt>

**ValidValues**
</dt> <dd>

Holds the valid values of the property in a particular property configuration. This member holds one of three items: the enumeration value WMDM\_ENUM\_PROP\_VALID\_VALUES\_ANY; the member **ValidValuesRange**; or the member **EnumeratedValidValues**. The value or member is indicated by **ValidValuesForm**.

<dl> <dt>

**ValidValuesRange**
</dt> <dd>

A [**WMDM\_PROP\_VALUES\_RANGE**](wmdm-prop-values-range.md) structure containing a range of valid values. This is present only when **ValidValuesForm** is set to WMDM\_ENUM\_PROP\_VALID\_VALUES\_RANGE. See Remarks.

</dd> <dt>

**EnumeratedValidValues**
</dt> <dd>

A [**WMDM\_PROP\_VALUES\_ENUM**](wmdm-prop-values-enum.md) structure containing an enumerated set of valid values. This is present only when **ValidValuesForm** is set to WMDM\_ENUM\_PROP\_VALID\_VALUES\_ENUM. See Remarks.

</dd> </dl> </dd> </dl>

## Remarks

The **WMDM\_PROP\_DESC** structure contains a property description that consists of a property name and its valid values in a particular configuration.

The caller is required to free the memory used by **ValidValuesRange** or **EnumeratedValues**. For an example of how to do this, see [**WMDM\_FORMAT\_CAPABILITY**](wmdm-format-capability.md).

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

[**WMDM\_PROP\_VALUES\_ENUM**](wmdm-prop-values-enum.md)
</dt> <dt>

[**WMDM\_PROP\_VALUES\_RANGE**](wmdm-prop-values-range.md)
</dt> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 






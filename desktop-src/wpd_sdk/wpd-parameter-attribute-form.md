---
description: Describes how a (method or event) parameter stores its value.
ms.assetid: 066196af-7805-4823-8ab7-cb95c17bba2a
title: WpdParameterAttributeForm enumeration (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WpdParameterAttributeForm
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WpdParameterAttributeForm enumeration

The [**WpdParameterAttributeForm**](/previous-versions/windows/hardware/drivers/ff597895(v=vs.85)) enumeration type describes how a (method or event) parameter stores its value.

## Syntax


```C++
typedef enum tagWpdParameterAttributeForm { 
  WPD_PARAMETER_ATTRIBUTE_FORM_UNSPECIFIED         = 0,
  WPD_PARAMETER_ATTRIBUTE_FORM_RANGE               = 1,
  WPD_PARAMETER_ATTRIBUTE_FORM_ENUMERATION         = 2,
  WPD_PARAMETER_ATTRIBUTE_FORM_REGULAR_EXPRESSION  = 3,
  WPD_PARAMETER_ATTRIBUTE_OBJECT_IDENTIFIER        = 4
} WpdParameterAttributeForm;
```



## Constants

<dl> <dt>

<span id="WPD_PARAMETER_ATTRIBUTE_FORM_UNSPECIFIED"></span><span id="wpd_parameter_attribute_form_unspecified"></span>**WPD\_PARAMETER\_ATTRIBUTE\_FORM\_UNSPECIFIED**
</dt> <dd>

The form of the parameter is not specified.

</dd> <dt>

<span id="WPD_PARAMETER_ATTRIBUTE_FORM_RANGE"></span><span id="wpd_parameter_attribute_form_range"></span>**WPD\_PARAMETER\_ATTRIBUTE\_FORM\_RANGE**
</dt> <dd>

The parameter specifies a range.

</dd> <dt>

<span id="WPD_PARAMETER_ATTRIBUTE_FORM_ENUMERATION"></span><span id="wpd_parameter_attribute_form_enumeration"></span>**WPD\_PARAMETER\_ATTRIBUTE\_FORM\_ENUMERATION**
</dt> <dd>

The parameter is an enumeration.

</dd> <dt>

<span id="WPD_PARAMETER_ATTRIBUTE_FORM_REGULAR_EXPRESSION"></span><span id="wpd_parameter_attribute_form_regular_expression"></span>**WPD\_PARAMETER\_ATTRIBUTE\_FORM\_REGULAR\_EXPRESSION**
</dt> <dd>

The parameter is a regular expression.

</dd> <dt>

<span id="WPD_PARAMETER_ATTRIBUTE_OBJECT_IDENTIFIER"></span><span id="wpd_parameter_attribute_object_identifier"></span>**WPD\_PARAMETER\_ATTRIBUTE\_OBJECT\_IDENTIFIER**
</dt> <dd>

The parameter is an object identifier.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



 


---
description: The WpdAttributeForm enumeration type describes how a property stores its values.
ms.assetid: 3ad8d1f9-1b74-4f34-9af5-1acdd588b650
title: WpdAttributeForm enumeration (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WpdAttributeForm
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WpdAttributeForm enumeration

The **WpdAttributeForm** enumeration type describes how a property stores its values.

## Syntax


```C++
typedef enum WpdAttributeForm { 
  WPD_PROPERTY_ATTRIBUTE_FORM_UNSPECIFIED         = 0,
  WPD_PROPERTY_ATTRIBUTE_FORM_RANGE               = 1,
  WPD_PROPERTY_ATTRIBUTE_FORM_ENUMERATION         = 2,
  WPD_PROPERTY_ATTRIBUTE_FORM_REGULAR_EXPRESSION  = 3,
  WPD_PROPERTY_ATTRIBUTE_FORM_OJBECT_IDENTIFIER   = 4
} ;
```



## Constants

<dl> <dt>

<span id="WPD_PROPERTY_ATTRIBUTE_FORM_UNSPECIFIED"></span><span id="wpd_property_attribute_form_unspecified"></span>**WPD\_PROPERTY\_ATTRIBUTE\_FORM\_UNSPECIFIED**
</dt> <dd>

The form of the property's data is not specified.

</dd> <dt>

<span id="WPD_PROPERTY_ATTRIBUTE_FORM_RANGE"></span><span id="wpd_property_attribute_form_range"></span>**WPD\_PROPERTY\_ATTRIBUTE\_FORM\_RANGE**
</dt> <dd>

The value is expressed as a range of values, with a minimum and a maximum.

</dd> <dt>

<span id="WPD_PROPERTY_ATTRIBUTE_FORM_ENUMERATION"></span><span id="wpd_property_attribute_form_enumeration"></span>**WPD\_PROPERTY\_ATTRIBUTE\_FORM\_ENUMERATION**
</dt> <dd>

The property has a series of individual values.

</dd> <dt>

<span id="WPD_PROPERTY_ATTRIBUTE_FORM_REGULAR_EXPRESSION"></span><span id="wpd_property_attribute_form_regular_expression"></span>**WPD\_PROPERTY\_ATTRIBUTE\_FORM\_REGULAR\_EXPRESSION**
</dt> <dd>

The property value is a regular expression, not a literal expression.

</dd> <dt>

<span id="WPD_PROPERTY_ATTRIBUTE_FORM_OJBECT_IDENTIFIER"></span><span id="wpd_property_attribute_form_ojbect_identifier"></span>**WPD\_PROPERTY\_ATTRIBUTE\_FORM\_OJBECT\_IDENTIFIER**
</dt> <dd>

The property value represents an object identifier.

</dd> </dl>

## Remarks

This enumeration is used by the [WPD\_PROPERTY\_ATTRIBUTE\_FORM](attributes.md) property to describe how a property's data is stored.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures and Enumeration Types**](structures-and-enumeration-types.md)
</dt> </dl>

 

 





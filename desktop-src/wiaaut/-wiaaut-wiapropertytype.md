---
title: WiaPropertyType enumeration
description: Specifies the type of the value of an item property. Item properties can be found in the Properties collection of a Device or Item object.
ms.assetid: '68123772-78cc-4954-8a04-79f49b12e973'
keywords: ["WiaPropertyType enumeration WIA Automation", "WiaDeviceType enumeration WIA Automation"]
topic_type:
- apiref
api_name:
- WiaDeviceType
api_location:
- Wiaaut.h
api_type:
- HeaderDef
---

# WiaPropertyType enumeration

Specifies the type of the value of an item property. Item properties can be found in the Properties collection of a [**Device**](-wiaaut-device.md) or [**Item**](-wiaaut-item.md) object.

## Members



| Member                                        | Description                                                                                                                                    | Value |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| **UnsupportedPropertyType**                   | The value of the property is an unsupported type.<br/>                                                                                   | 0     |
| **BooleanPropertyType**                       | The value of the property is a Boolean.<br/>                                                                                             | 1     |
| **BytePropertyType**                          | The value of the property is a Byte.<br/>                                                                                                | 2     |
| **IntegerPropertyType**                       | The value of the property is an Integer.<br/>                                                                                            | 3     |
| **UnsignedIntegerPropertyType**               | The value of the property is returned as a non-negative Integer.<br/>                                                                    | 4     |
| **LongPropertyType**                          | The value of the property is a Long.<br/>                                                                                                | 5     |
| **UnsignedLongPropertyType**                  | The value of the property is returned as a non-negative Long.<br/>                                                                       | 6     |
| **ErrorCodePropertyType**                     | The value of the property is returned as a Long.<br/>                                                                                    | 7     |
| **LargeIntegerPropertyType**                  | The value of the property is a Large Integer returned as a truncated Long.<br/>                                                          | 8     |
| **UnsignedLargeIntegerPropertyType**          | The value of the property is returned as a truncated non-negative Long.<br/>                                                             | 9     |
| **SinglePropertyType**                        | The value of the property is a Single.<br/>                                                                                              | 10    |
| **DoublePropertyType**                        | The value of the property is a Double.<br/>                                                                                              | 11    |
| **CurrencyPropertyType**                      | The value of the property is a Currency.<br/>                                                                                            | 12    |
| **DatePropertyType**                          | The value of the property is a Date.<br/>                                                                                                | 13    |
| **FileTimePropertyType**                      | The value of the property is returned as a Date.<br/>                                                                                    | 14    |
| **ClassIDPropertyType**                       | The value of the property is returned as a String.<br/>                                                                                  | 15    |
| **StringPropertyType**                        | The value of the property is a String.<br/>                                                                                              | 16    |
| **ObjectPropertyType**                        | The value of the property is an Object.<br/>                                                                                             | 17    |
| **HandlePropertyType**                        | The value of the property is returned as a Variant.<br/>                                                                                 | 18    |
| **VariantPropertyType**                       | The value of the property is a Variant.<br/>                                                                                             | 19    |
| **VectorOfBooleansPropertyType**              | The value of the property is a [**Vector**](-wiaaut-vector.md) object containing Boolean elements.<br/>                                 | 101   |
| **VectorOfBytesPropertyType**                 | The value of the property is a [**Vector**](-wiaaut-vector.md) object containing Byte elements.<br/>                                    | 102   |
| **VectorOfIntegersPropertyType**              | The value of the property is a [**Vector**](-wiaaut-vector.md) object containing Integer elements.<br/>                                 | 103   |
| **VectorOfUnsignedIntegersPropertyType**      | The value of the property is returned as a [**Vector**](-wiaaut-vector.md) object containing non-negative Integer elements.<br/>        | 104   |
| **VectorOfLongsPropertyType**                 | The value of the property is a [**Vector**](-wiaaut-vector.md) object containing Long elements.<br/>                                    | 105   |
| **VectorOfUnsignedLongsPropertyType**         | The value of the property is returned as a [**Vector**](-wiaaut-vector.md) object containing non-negative Long elements.<br/>           | 106   |
| **VectorOfErrorCodesPropertyType**            | The value of the property is returned as a [**Vector**](-wiaaut-vector.md) object containing Long elements.<br/>                        | 107   |
| **VectorOfLargeIntegersPropertyType**         | The value of the property is returned as a [**Vector**](-wiaaut-vector.md) object containing truncated Long elements.<br/>              | 108   |
| **VectorOfUnsignedLargeIntegersPropertyType** | The value of the property is returned as a [**Vector**](-wiaaut-vector.md) object containing truncated non-negative Long elements.<br/> | 109   |
| **VectorOfSinglesPropertyType**               | The value of the property is a [**Vector**](-wiaaut-vector.md) object containing Single elements.<br/>                                  | 110   |
| **VectorOfDoublesPropertyType**               | The value of the property is a [**Vector**](-wiaaut-vector.md) object containing Double elements.<br/>                                  | 111   |
| **VectorOfCurrenciesPropertyType**            | The value of the property is a [**Vector**](-wiaaut-vector.md) object containing Currency elements.<br/>                                | 112   |
| **VectorOfDatesPropertyType**                 | The value of the property is a [**Vector**](-wiaaut-vector.md) object containing Date elements.<br/>                                    | 113   |
| **VectorOfFileTimesPropertyType**             | The value of the property is returned as a [**Vector**](-wiaaut-vector.md) object containing Date elements.<br/>                        | 114   |
| **VectorOfClassIDsPropertyType**              | The value of the property is returned as a [**Vector**](-wiaaut-vector.md) object containing String elements.<br/>                      | 115   |
| **VectorOfStringsPropertyType**               | The value of the property is a [**Vector**](-wiaaut-vector.md) object containing String elements.<br/>                                  | 116   |
| **VectorOfVariantsPropertyType**              | The value of the property is a [**Vector**](-wiaaut-vector.md) object containing Variant elements.<br/>                                 | 119   |



## Remarks

The value of the Type property on a [**Property**](-wiaaut-property.md) object, when it comes from a Properties collection on a [**Device**](-wiaaut-device.md), [**DeviceInfo**](-wiaaut-deviceinfo.md), [**Filter**](-wiaaut-filter.md), or [**Item**](-wiaaut-item.md) object, can return one of the members of the WiaPropertyType enumeration. This gives more information about the type of value contained in the Value property.

For example code, see [Display all the Properties for the Selected Device](-wiaaut-shared-samples.md#display-all-the-properties-for-the-selected-device---1) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



 

 






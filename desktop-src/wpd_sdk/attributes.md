---
description: Windows Portable Devices supports the following property attributes.
ms.assetid: 129ee2b8-075c-457a-85ef-658a56eed541
title: Property Attributes (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Property
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Property Attributes (PortableDevice.h)

Windows Portable Devices supports the following property attributes. These attributes are returned by the following methods:

-   [**IPortableDeviceCapabilities::GetFixedPropertyAttributes**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevicecapabilities-getfixedpropertyattributes)
-   [**IPortableDeviceProperties::GetPropertyAttributes**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledeviceproperties-getpropertyattributes)
-   [**IPortableDeviceServiceCapabilities::GetFormatPropertyAttributes**](/windows/desktop/api/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicecapabilities-getformatpropertyattributes)



| Attribute                                           | VarType         | Description                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------------------------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_ATTRIBUTE\_CAN\_DELETE**           | **VT\_BOOL**    | A Boolean value that specifies whether the client can delete the property. To delete a property, set its value to VT\_EMPTY.                                                                                                                                                                                                                                                                   |
| **WPD\_PROPERTY\_ATTRIBUTE\_CAN\_READ**             | **VT\_BOOL**    | A Boolean value that specifies whether the client can read the property.                                                                                                                                                                                                                                                                                                                       |
| **WPD\_PROPERTY\_ATTRIBUTE\_CAN\_WRITE**            | **VT\_BOOL**    | A Boolean value that specifies whether the client can modify the property.                                                                                                                                                                                                                                                                                                                     |
| **WPD\_PROPERTY\_ATTRIBUTE\_DEFAULT\_VALUE**        | VT\_*XXXX*      | A value that is defined by the device that specifies the default value of a property. This applies to writeable properties only.                                                                                                                                                                                                                                                               |
| **WPD\_PROPERTY\_ATTRIBUTE\_ENUMERATION\_ELEMENTS** | **VT\_UNKNOWN** | An [**IPortableDevicePropVariantCollection**](iportabledevicepropvariantcollection.md) interface that contains a collection of values for a property whose **WPD\_PROPERTY\_ATTRIBUTE\_FORM** attribute is **WPD\_PROPERTY\_ATTRIBUTE\_FORM\_ENUMERATION**. The data type depends on the property being queried.                                                                              |
| **WPD\_PROPERTY\_ATTRIBUTE\_FAST\_PROPERTY**        | **VT\_BOOL**    | If True, then this property belongs to the *fast properties* group. These are properties that can be retrieved from the device quickly.                                                                                                                                                                                                                                                        |
| **WPD\_PROPERTY\_ATTRIBUTE\_FORM**                  | **VT\_UI4**     | A [**WpdAttributeForm**](wpdattributeform.md) enumerated value that specifies the form of the valid values allowed for this property.                                                                                                                                                                                                                                                         |
| **WPD\_PROPERTY\_ATTRIBUTE\_NAME**                  | **VT\_LPWSTR**  | A string that specifies the script-friendly name of the property. Valid characters are alphanumeric \[a-zA-Z0-9\] and '\_'.                                                                                                                                                                                                                                                                    |
| **WPD\_PROPERTY\_ATTRIBUTE\_RANGE\_MAX**            | VT\_*XXXX*      | The maximum value for a property whose **WPD\_PROPERTY\_ATTRIBUTE\_FORM** attribute is **WPD\_PROPERTY\_ATTRIBUTE\_FORM\_RANGE**. The data type can be any of the numeric types.                                                                                                                                                                                                               |
| **WPD\_PROPERTY\_ATTRIBUTE\_RANGE\_MIN**            | VT\_*XXXX*      | The minimum value for a property whose **WPD\_PROPERTY\_ATTRIBUTE\_FORM** attribute is **WPD\_PROPERTY\_ATTRIBUTE\_FORM\_RANGE**. The data type can be any of the numeric types.                                                                                                                                                                                                               |
| **WPD\_PROPERTY\_ATTRIBUTE\_RANGE\_STEP**           | VT\_*XXXX*      | The step value for a property whose **WPD\_PROPERTY\_ATTRIBUTE\_FORM** attribute is **WPD\_PROPERTY\_ATTRIBUTE\_FORM\_RANGE**. The step specifies by how much a range property must change. For example, a property with a minimum value of 10, a maximum value of 20, and a step of 5 could have the following values: **10**, **15**, **20**. The data type can be any of the numeric types. |
| **WPD\_PROPERTY\_ATTRIBUTE\_REGULAR\_EXPRESSION**   | **VT\_LPWSTR**  | A regular expression string that specifies acceptable values for properties whose form is **WPD\_PROPERTY\_ATTRIBUTE\_FORM\_REGULAR\_EXPRESSION**.                                                                                                                                                                                                                                             |
| **WPD\_PROPERTY\_ATTRIBUTE\_VARTYPE**               | **VT\_UI4**     | An integer that specifies the VARTYPE of the property, for example, **VT\_BOOL**.                                                                                                                                                                                                                                                                                                              |
| **WPD\_PROPERTY\_ATTRIBUTE\_MAX\_SIZE**             | **VT\_UI8**     | A value that specifies the maximum size for the value of this property, in bytes.                                                                                                                                                                                                                                                                                                              |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Properties**](properties-and-attributes.md)
</dt> </dl>

 

 





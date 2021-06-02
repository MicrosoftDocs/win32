---
description: For Windows 7, Windows Portable Devices supports the following parameter attributes for methods and events of a device service.
ms.assetid: a7708c60-758a-4fb6-8ef9-074ecdc9cf60
title: Parameter Attributes (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Parameter
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Parameter Attributes

For Windows 7, Windows Portable Devices supports the following parameter attributes for methods and events of a device service. These attributes are returned by the these methods:

-   [**IPortableDeviceServiceCapabilities::GetMethodParameterAttributes**](/windows/desktop/api/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicecapabilities-getmethodparameterattributes)
-   [**IPortableDeviceServiceCapabilities::GetEventParameterAttributes**](/windows/desktop/api/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicecapabilities-geteventparameterattributes)




| Attribute                                            | VarType         | Description                                                                                                                                                                                 |
|------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_PARAMETER\_ATTRIBUTE\_DEFAULT\_VALUE**        | VT\_*XXXX*      | The default value of the parameter.                                                                                                                                                         |
| **WPD\_PARAMETER\_ATTRIBUTE\_ENUMERATION\_ELEMENTS** | **VT\_UNKNOWN** | An [**IPortableDevicePropVariantCollection**](iportabledevicepropvariantcollection.md) interface that contains the enumeration values for the parameter.                                   |
| **WPD\_PARAMETER\_ATTRIBUTE\_FORM**                  | **VT\_UI4**     | The form of valid parameter values allowed.                                                                                                                                                 |
| **WPD\_PARAMETER\_ATTRIBUTE\_MAX\_SIZE**             | **VT\_UI8**     | The maximum size of the parameter, in bytes .                                                                                                                                               |
| **WPD\_PARAMETER\_ATTRIBUTE\_NAME**                  | **VT\_LPWSTR**  | A string that specifies the script-friendly name of an event or method parameter. Valid characters are alphanumeric \[a-zA-Z0-9\] and '\_'.                                                 |
| **WPD\_PARAMETER\_ATTRIBUTE\_ORDER**                 | **VT\_UI4**     | The zero-based parameter-order index, so that an order value of 0 corresponds to the first parameter.                                                                                       |
| **WPD\_PARAMETER\_ATTRIBUTE\_RANGE\_MIN**            | VT\_*XXXX*      | The maximum value for a parameter of the form WPD\_PARAMETER\_ATTRIBUTE\_FORM\_RANGE.                                                                                                       |
| **WPD\_PARAMETER\_ATTRIBUTE\_RANGE\_MAX**            | VT\_*XXXX*      | The minimum value for a parameter of the form WPD\_PARAMETER\_ATTRIBUTE\_FORM\_RANGE.                                                                                                       |
| **WPD\_PARAMETER\_ATTRIBUTE\_RANGE\_STEP**           | VT\_*XXXX*      | The step value for a parameter of the form WPD\_PARAMETER\_ATTRIBUTE\_FORM\_RANGE.                                                                                                          |
| **WPD\_PARAMETER\_ATTRIBUTE\_REGULAR\_EXPRESSION**   | **VT\_LPWSTR**  | A regular expression that specifies acceptable values for parameters of the form WPD\_PARAMETER\_ATTRIBUTE\_FORM\_REGULAR\_EXPRESSION.                                                      |
| **WPD\_PARAMETER\_ATTRIBUTE\_USAGE\_TYPE**           | **VT\_UI4**     | An integer that specifies the usage of a method parameter, for example, in/out. Valid values are of the [**WPD\_PARAMETER\_USAGE\_TYPES**](wpd-parameter-usage-types.md) enumeration type. |
| **WPD\_PARAMETER\_ATTRIBUTE\_VARTYPE**               | **VT\_UI4**     | The parameter VarType.                                                                                                                                                                      |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 





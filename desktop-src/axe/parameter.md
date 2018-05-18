---
title: Parameter class
description: This interface exposes assessment parameter values to the assessment.
ms.assetid: 'ff73ff62-21e8-4040-bf6c-2720ca6278ff'
keywords: ["Parameter class Access Execution Engine", "Parameter class Access Execution Engine , described"]
topic_type:
- apiref
api_name:
- Parameter
api_location:
- AxeCore.dll
api_type:
- COM
---

# Parameter class

This interface exposes assessment parameter values to the assessment.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**Parameter** has these types of members:

-   [Methods](#methods)

### Methods

The **Parameter** class has these methods.



| Method                                     | Description                                                             |
|:-------------------------------------------|:------------------------------------------------------------------------|
| [**~Parameter**](parameter--parameter.md) | Destructor method.<br/>                                           |
| [**ToBoolean**](parameter-toboolean.md)   | Retrieve the value of the parameter as a specific data type.<br/> |
| [**ToByte**](parameter-tobyte.md)         | Retrieve the value of the parameter as a specific data type.<br/> |
| [**ToChar**](parameter-tochar.md)         | Retrieve the value of the parameter as a specific data type.<br/> |
| [**ToDateTime**](parameter-todatetime.md) | Retrieve the value of the parameter as a specific data type.<br/> |
| [**ToDouble**](parameter-todouble.md)     | Retrieve the value of the parameter as a specific data type.<br/> |
| [**ToDuration**](parameter-toduration.md) | Retrieve the value of the parameter as a specific data type.<br/> |
| [**ToInt16**](parameter-toint16.md)       | Retrieve the value of the parameter as a specific data type.<br/> |
| [**ToInt32**](parameter-toint32.md)       | Retrieve the value of the parameter as a specific data type.<br/> |
| [**ToInt64**](parameter-toint64.md)       | Retrieve the value of the parameter as a specific data type.<br/> |
| [**ToSByte**](parameter-tosbyte.md)       | Retrieve the value of the parameter as a specific data type.<br/> |
| [**ToString**](parameter-tostring.md)     | Retrieve the value of the parameter as a specific data type.<br/> |
| [**ToUInt16**](parameter-touint16.md)     | Retrieve the value of the parameter as a specific data type.<br/> |
| [**ToUInt32**](parameter-touint32.md)     | Retrieve the value of the parameter as a specific data type.<br/> |
| [**ToUInt64**](parameter-touint64.md)     | Retrieve the value of the parameter as a specific data type.<br/> |



 

## Remarks

These methods are used to return a type safe value of a parameter. These methods check the underlying data type of the parameter and if the type is not the same as the one requested, or if there is not a mapping then a conversion failed error is returned.

If these return any error, all the bits of the output value are set to zero or to the empty string, and the value of **paramValue** is set to false. A non-zero value has a **Boolean** value of true and a value of zero has a **Boolean** value of false.

The [**ToString**](parameter-tostring.md), [**ToDouble**](parameter-todouble.md) and [**ToDateTime**](parameter-todatetime.md) methods cannot convert a parameter of another type. If these methods are called on a parameter of a different type, the method returns **AXE\_E\_PARAM\_CONVERSION\_FAILED**.

This interface is supported on Windows 7, Windows Server 2008 R2, Windows 8, and Windows Server 2012.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 






---
description: The DELETE\_OBJECT\_OPTIONS enumeration type describes options that are supported by a device when deleting an object.
ms.assetid: d0e46e77-d333-498f-b2f5-26be1461a116
title: DELETE_OBJECT_OPTIONS enumeration (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DELETE_OBJECT_OPTIONS
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# DELETE\_OBJECT\_OPTIONS enumeration

The **DELETE\_OBJECT\_OPTIONS** enumeration type describes options that are supported by a device when deleting an object.

## Syntax


```C++
typedef enum DELETE_OBJECT_OPTIONS { 
  PORTABLE_DEVICE_DELETE_NO_RECURSION    = 0,
  PORTABLE_DEVICE_DELETE_WITH_RECURSION  = 1
} ;
```



## Constants

<dl> <dt>

<span id="PORTABLE_DEVICE_DELETE_NO_RECURSION"></span><span id="portable_device_delete_no_recursion"></span>**PORTABLE\_DEVICE\_DELETE\_NO\_RECURSION**
</dt> <dd>

Delete the object only and fail if it has children.

</dd> <dt>

<span id="PORTABLE_DEVICE_DELETE_WITH_RECURSION"></span><span id="portable_device_delete_with_recursion"></span>**PORTABLE\_DEVICE\_DELETE\_WITH\_RECURSION**
</dt> <dd>

Delete the object and all its children.

</dd> </dl>

## Remarks

The application can retrieve the deletion options that the device supports by calling [**IPortableDeviceCapabilities::GetCommandOptions**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevicecapabilities-getcommandoptions) for the **WPD\_COMMAND\_OBJECT\_MANAGEMENT\_DELETE\_OBJECTS** command. It should examine the **WPD\_OPTION\_OBJECT\_MANAGEMENT\_RECURSIVE\_DELETE\_SUPPORTED** option value that this method returns in an [**IPortableDeviceValuesCollection**](iportabledevicevaluescollection.md) object.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures and Enumeration Types**](structures-and-enumeration-types.md)
</dt> </dl>

 

 





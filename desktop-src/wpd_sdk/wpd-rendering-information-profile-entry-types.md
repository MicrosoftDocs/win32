---
description: The WPD\_RENDERING\_INFORMATION\_PROFILE\_ENTRY\_TYPES enumeration type indicates whether the rendering information profile entry corresponds to an Object or a Resource.
ms.assetid: d019eef6-eed8-416c-bede-5b4eb00ed013
title: WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPES enumeration (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPES
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WPD\_RENDERING\_INFORMATION\_PROFILE\_ENTRY\_TYPES enumeration

The **WPD\_RENDERING\_INFORMATION\_PROFILE\_ENTRY\_TYPES** enumeration type indicates whether the rendering information profile entry corresponds to an Object or a Resource.

## Syntax


```C++
typedef enum SMS_MESSAGE_TYPES { 
  WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_OBJECT    = 0,
  WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_RESOURCE  = 1
} ;
```



## Constants

<dl> <dt>

<span id="WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_OBJECT"></span><span id="wpd_rendering_information_profile_entry_type_object"></span>**WPD\_RENDERING\_INFORMATION\_PROFILE\_ENTRY\_TYPE\_OBJECT**
</dt> <dd>

The entry corresponds to an object.

</dd> <dt>

<span id="WPD_RENDERING_INFORMATION_PROFILE_ENTRY_TYPE_RESOURCE"></span><span id="wpd_rendering_information_profile_entry_type_resource"></span>**WPD\_RENDERING\_INFORMATION\_PROFILE\_ENTRY\_TYPE\_RESOURCE**
</dt> <dd>

The entry corresponds to a resource.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures and Enumeration Types**](structures-and-enumeration-types.md)
</dt> </dl>

 

 





---
description: The WPD\_PARAMETER\_USAGE\_TYPES enumeration type describes how a method parameter is used in a given method.
ms.assetid: 60cbb4fa-c5fd-4402-bfd4-8fd95c009a33
title: WPD_PARAMETER_USAGE_TYPES enumeration (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_PARAMETER_USAGE_TYPES
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WPD\_PARAMETER\_USAGE\_TYPES enumeration

The [**WPD\_PARAMETER\_USAGE\_TYPES**](/windows/desktop/wpd_sdk/wpd-parameter-usage-types) enumeration type describes how a method parameter is used in a given method.

## Syntax


```C++
typedef enum tagWPD_PARAMETER_USAGE_TYPES { 
  WPD_PARAMETER_USAGE_RETURN  = 0,
  WPD_PARAMETER_USAGE_IN      = 1,
  WPD_PARAMETER_USAGE_OUT     = 2,
  WPD_PARAMETER_USAGE_INOUT   = 3
} WPD_PARAMETER_USAGE_TYPES;
```



## Constants

<dl> <dt>

<span id="WPD_PARAMETER_USAGE_RETURN"></span><span id="wpd_parameter_usage_return"></span>**WPD\_PARAMETER\_USAGE\_RETURN**
</dt> <dd>

The parameter receives the return value, if specified by the method.

</dd> <dt>

<span id="WPD_PARAMETER_USAGE_IN"></span><span id="wpd_parameter_usage_in"></span>**WPD\_PARAMETER\_USAGE\_IN**
</dt> <dd>

The parameter contains an input value before the method is called.

</dd> <dt>

<span id="WPD_PARAMETER_USAGE_OUT"></span><span id="wpd_parameter_usage_out"></span>**WPD\_PARAMETER\_USAGE\_OUT**
</dt> <dd>

The parameter contains an output value when the method returns.

</dd> <dt>

<span id="WPD_PARAMETER_USAGE_INOUT"></span><span id="wpd_parameter_usage_inout"></span>**WPD\_PARAMETER\_USAGE\_INOUT**
</dt> <dd>

The parameter contains an input value before the method is called and an output value when it returns.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



 


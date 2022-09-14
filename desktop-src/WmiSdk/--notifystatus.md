---
description: Serves as the parent class for provider-defined error classes.
ms.assetid: fc2747f5-cfbc-4d61-894d-4585a03dda3f
ms.tgt_platform: multiple
title: '__NotifyStatus class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __NotifyStatus
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_NotifyStatus class

The **\_\_NotifyStatus** abstract system class serves as the parent class for provider-defined error classes.

The following syntax is simplified from Managed Object Format (MF) code and includes all inherited properties.

## Syntax

``` syntax
[abstract]
class __NotifyStatus
{
  uint32 StatusCode;
};
```

## Members

The **\_\_NotifyStatus** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_NotifyStatus** class has these properties.

<dl> <dt>

**StatusCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains an error or information code for an operation. This can be any user-defined code, but the value 0 (zero) is usually reserved to indicate success.

</dd> </dl>

## Remarks

Although the **\_\_NotifyStatus** class can be the parent class for provider-defined error classes, it is recommended that providers derive error classes from [**\_\_ExtendedStatus**](--extendedstatus.md) instead. Using **\_\_ExtendedStatus** allows for greater standardization of error classes.

Providers should never create instances of **\_\_NotifyStatus** directly, because these instances convey no more information than a simple return code.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> </dl>

 

 





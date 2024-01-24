---
description: Holds the security rights for the namespace in the form of a security descriptor.
ms.assetid: 84e514f5-b114-4bfc-ab0b-9745f249168b
ms.tgt_platform: multiple
title: '__thisNAMESPACE class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __thisNAMESPACE
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_thisNAMESPACE class

The **\_\_thisNAMESPACE** system class holds the security rights for the namespace in the form of a security descriptor. This class and a single instance is found in all namespaces.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[singleton]
class __thisNAMESPACE : __SystemClass
{
  uint8 SECURITY_DESCRIPTOR[];
};
```

## Members

The **\_\_thisNAMESPACE** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_thisNAMESPACE** class has these properties.

<dl> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Security descriptor describing who can access the namespace and who can read from or write to the namespace. This property is inherited from [**\_\_Event**](--event.md). For more information about the format of security descriptors, see [Security Descriptors](/windows/desktop/SecAuthZ/security-descriptors) in the Security section of the Windows SDK.

</dd> </dl>

## Remarks

The singleton instance of **\_\_thisNAMESPACE** is read-only. To change the settings of the security descriptor property, use the methods of the [**\_\_SystemSecurity**](--systemsecurity.md) class. The **\_\_thisNAMESPACE** class derives from [**\_\_SystemClass**](--systemclass.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_SystemClass**](/windows/desktop/WmiSdk/--systemclass)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> </dl>

 


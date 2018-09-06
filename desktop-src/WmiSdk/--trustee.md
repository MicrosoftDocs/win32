---
Description: The \_\_Trustee abstract system class represents a trustee. Either a name or an SID (byte array) can be used.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 92d17c7c-ebca-4dd0-80d8-6edd999ca394
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: '__Trustee class'
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __Trustee
- All
- All
- All
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_Trustee class

The [**\_\_Trustee**](--securitydescriptor.md) abstract system class represents a [*trustee*](https://msdn.microsoft.com/library/windows/desktop/ms721627#-security-trustee-gly). Either a name or an SID (byte array) can be used.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __Trustee
{
  string Domain;
  string Name;
  uint8  SID[];
  uint32 SidLength;
  string SidString;
  uint64 TIME_CREATED;
};
```

## Members

The **\_\_Trustee** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_Trustee** class has these properties.

<dl> <dt>

**Domain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Domain portion of the account.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Name portion of the account.

</dd> <dt>

**SID**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The SID of the trustee in the binary byte array form.

</dd> <dt>

**SidLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The length of the SID in bytes.

</dd> <dt>

**SidString**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The SID of the trustee in the string format, for example, "S-1-1-0".

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time in the [CIM\_DATETIME](cim-datetime.md) format when the security descriptor was created.

</dd> </dl>

## Remarks

This class provides properties that are inherited by the [**Win32\_Trustee**](https://msdn.microsoft.com/library/aa394501) class, which is a member of the [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) class. For more information, see [WMI Security Descriptor Objects](wmi-security-descriptor-objects.md) and [Changing Access Security on Securable Objects](changing-access-security-on-securable-objects.md). For more information about ACEs, see [Access Control Components](https://msdn.microsoft.com/library/windows/desktop/aa374862).

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[**Win32\_Trustee**](https://msdn.microsoft.com/library/aa394501)
</dt> <dt>

[Maintaining WMI Security](maintaining-wmi-security.md)
</dt> </dl>

 

 





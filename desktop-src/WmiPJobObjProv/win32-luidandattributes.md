---
Description: 'The Win32\_LUIDandAttribute abstract WMI class represents a locally unique identifier (LUID) and its attributes. Each LUID and attributes structure defines the availability of a security privilege.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '2948e600-0960-467f-ad0a-f4cc0a807e39'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_LUIDandAttributes class'
---

# Win32\_LUIDandAttributes class

The **Win32\_LUIDandAttribute** abstract [WMI class](https://msdn.microsoft.com/library/aa393244) represents a locally unique identifier (LUID) and its attributes. Each LUID and attributes structure defines the availability of a security privilege.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{63021F4B-F377-4a88-ABD1-835D14142142}"), AMENDMENT]
class Win32_LUIDandAttributes
{
  uint32     Attributes;
  Win32_LUID LUID;
};
```

## Members

The **Win32\_LUIDandAttributes** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_LUIDandAttributes** class has these properties.

<dl> <dt>

**Attributes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Instance containing the attributes of the LUID. This value holds two 32-bit flags. Its meaning is dependent on the definition and use of the LUID.

</dd> <dt>

**LUID**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LUID**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Representing a LUID value.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipjobj.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipjobj.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





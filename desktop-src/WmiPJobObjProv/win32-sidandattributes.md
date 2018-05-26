---
Description: The Win32\_SIDandAttributes abstract WMI class represents a security identifier (SID) and its attributes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2876468b-7d31-4661-b663-6734a8e211a7
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_SIDandAttributes class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_SIDandAttributes class

The **Win32\_SIDandAttributes** abstract [WMI class](https://msdn.microsoft.com/library/aa393244) represents a security identifier (SID) and its attributes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{DE1B36A6-4157-43ed-937F-D90606C09216}"), AMENDMENT]
class Win32_SIDandAttributes
{
  uint32    Attributes;
  Win32_SID SID;
};
```

## Members

The **Win32\_SIDandAttributes** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SIDandAttributes** class has these properties.

<dl> <dt>

**Attributes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Attributes of the SID. This value contains up to 32 1-bit flags. Its meaning depends on the definition and use of the SID.

</dd> <dt>

**SID**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SID**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to an instance representing a SID.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipjobj.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipjobj.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





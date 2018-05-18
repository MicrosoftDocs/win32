---
Description: 'The Win32\_LUID abstract WMI class represents a locally unique identifier (LUID), an identifier unique on the local computer that is used in security tokens.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '61ddbf75-a0a6-4a34-bda7-1ed453595875'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_LUID class'
---

# Win32\_LUID class

The **Win32\_LUID** abstract [WMI class](https://msdn.microsoft.com/library/aa393244) represents a locally unique identifier (LUID), an identifier unique on the local computer that is used in security tokens.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{0FF18C30-FA51-11d3-9C37-006008B088CE}"), AMENDMENT]
class Win32_LUID
{
  uint32 HighPart;
  uint32 LowPart;
};
```

## Members

The **Win32\_LUID** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_LUID** class has these properties.

<dl> <dt>

**HighPart**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Most significant bits of the LUID.

</dd> <dt>

**LowPart**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Least significant bits of the LUID.

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

 

 





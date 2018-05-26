---
Description: The Win32\_TokenGroups abstract WMI class represents information about the group security identifiers (SIDs) in an access token.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 93288683-3c4c-42c2-a3f4-09fd712d8a49
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_TokenGroups class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_TokenGroups class

The **Win32\_TokenGroups** abstract [WMI class](https://msdn.microsoft.com/library/aa393244) represents information about the group security identifiers (SIDs) in an access token.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{6CDD7B40-369D-4725-AB7F-EFE53EE2C455}"), AMENDMENT]
class Win32_TokenGroups
{
  Win32_SIDandAttributes Groups[];
  uint32                 GroupCount;
};
```

## Members

The **Win32\_TokenGroups** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_TokenGroups** class has these properties.

<dl> <dt>

**GroupCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of groups in the access token.

</dd> <dt>

**Groups**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SIDandAttributes** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Each array element references a an SID and an attribute.

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

 

 





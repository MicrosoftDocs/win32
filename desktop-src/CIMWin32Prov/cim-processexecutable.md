---
Description: The CIM\_ProcessExecutable class represents a link between a process and data file, and indicates that the file participates in the execution of the process.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6db69bf3-b28e-4d0b-8878-558e12052767
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM_ProcessExecutable class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ProcessExecutable
- CIM_ProcessExecutable.Dependent
- CIM_ProcessExecutable.Antecedent
- CIM_ProcessExecutable.BaseAddress
- CIM_ProcessExecutable.GlobalProcessCount
- CIM_ProcessExecutable.ModuleInstance
- CIM_ProcessExecutable.ProcessCount
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_ProcessExecutable class

The **CIM\_ProcessExecutable** class represents a link between a process and data file, and indicates that the file participates in the execution of the process.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Privileges("SeDebugPrivilege"), Dynamic, Provider("CIMWin32"), UUID("{8502C542-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class CIM_ProcessExecutable : CIM_Dependency
{
  CIM_Process  REF Dependent;
  CIM_DataFile REF Antecedent;
  uint64           BaseAddress;
  uint32           GlobalProcessCount;
  uint32           ModuleInstance;
  uint32           ProcessCount;
};
```

## Members

The **CIM\_ProcessExecutable** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ProcessExecutable** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_DataFile**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Antecedent), [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A [**CIM\_DataFile**](cim-datafile.md) that describes the data file participating in the execution of the process.

</dd> <dt>

**BaseAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](https://msdn.microsoft.com/library/aa393650) ("Win32")
</dt> </dl>

Base address of the module in the address space of the associated process.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Process**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Dependent), [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A [**CIM\_Process**](cim-process.md) that describes the process.

</dd> <dt>

**GlobalProcessCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](https://msdn.microsoft.com/library/aa393650) ("Win32")
</dt> </dl>

Current number of processes that have the file loaded in memory.

</dd> <dt>

**ModuleInstance**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651), [**Schema**](https://msdn.microsoft.com/library/aa393650) ("Win32")
</dt> </dl>

Win32 instance handle. This property is obsolete, and there is no replacement value.

</dd> <dt>

**ProcessCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](https://msdn.microsoft.com/library/aa393650) ("Win32")
</dt> </dl>

Reference count of the file in the associated process.

</dd> </dl>

## Remarks

The **CIM\_ProcessExecutable** class is derived from [**CIM\_Dependency**](cim-dependency.md).

WMI implements the **CIM\_ProcessExecutable** class. The **CIM\_ProcessExecutable** class is a dynamic class.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





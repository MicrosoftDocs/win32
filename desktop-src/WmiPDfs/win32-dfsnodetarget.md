---
title: Win32\_DFSNodeTarget class
description: The Win32\_DFSNodeTarget association WMI class relates a Distributed file system (DFS) node to one of its targets.
audience: developer
author: REDMOND\\martinek
manager: REDMOND\\martinek
ms.assetid: 29b30cbc-0be0-4669-a260-82dfa6767d3e
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_DFSNodeTarget class
- Win32_DFSNodeTarget class, described
topic_type:
- apiref
api_name:
- Win32_DFSNodeTarget
- Win32_DFSNodeTarget.Antecedent
- Win32_DFSNodeTarget.Dependent
api_location:
- Wmipdfs.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_DFSNodeTarget class

The **Win32\_DFSNodeTarget** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a Distributed file system (DFS) node to one of its targets.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[dynamic, Provider("DFSProvider"), AMENDMENT]
class Win32_DFSNodeTarget : CIM_Dependency
{
  Win32_DFSTarget REF Antecedent;
  Win32_DFSNode   REF Dependent;
};
```

## Members

The **Win32\_DFSNodeTarget** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_DFSNodeTarget** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_DFSTarget**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Reference to the instance representing a target for a DFS node. Each node has one or more targets. This property overrides the **Antecedent** property inherited from [**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_DFSNode**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to an instance representing a DFS node. This property overrides the **Dependent** property inherited from [**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238).

</dd> </dl>

## Remarks

The **Win32\_DFSNodeTarget** class is derived from [**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238).

## Examples

While Impersonation works with a DFS root server, Delegation is required for all other DC's in a domain-based DFS. The following PowerShell describes how to set delegation.


```PowerShell
Get-WmiObject Win32_DFSTarget -computer <dns-domain-name> -impersonation delegate
```



The following PowerShell code sample shows how to retrieve inaccessable DFS targets


```PowerShell
#To retrieve inaccessible DFS targets:

$failed = gwmi Win32_DfsTarget -comp server | where { !(test-path "\\$($_.ServerName)\$($_.ShareName)") }

#To display info: 

$failed | ft LinkName, ServerName, ShareName

#To remove and display the failures:

$failed | where{ $_.Delete().ReturnValue } | ft LinkName, ServerName, ShareName
```



## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Wmipdfs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipdfs.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 






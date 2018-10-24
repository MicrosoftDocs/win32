---
Description: The CIM\_ProcessThread class represents a link between a process and the threads running in the context of the process.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e71543c5-d9b3-4f98-93a6-08f977a26305
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM_ProcessThread class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ProcessThread
- CIM_ProcessThread.PartComponent
- CIM_ProcessThread.GroupComponent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_ProcessThread class

The **CIM\_ProcessThread** class represents a link between a process and the threads running in the context of the process.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{B7E6042C-DB36-11d2-85FC-0000F8102E5F}"), AMENDMENT]
class CIM_ProcessThread : CIM_Component
{
  CIM_Thread  REF PartComponent;
  CIM_Process REF GroupComponent;
};
```

## Members

The **CIM\_ProcessThread** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ProcessThread** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Process**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent")
</dt> </dl>

A [**CIM\_Process**](cim-process.md) that describes the process.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Thread**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent"), [**Weak**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A [**CIM\_Thread**](cim-thread.md) that describes the thread running in the context of the process.

</dd> </dl>

## Remarks

WMI does not implement this class.

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

[**CIM\_Component**](cim-component.md)
</dt> </dl>

 

 





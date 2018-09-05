---
Description: The CIM\_JobDestinationJobs association describes where a job is submitted for processing (that is, to which job destination).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6f732d34-2284-4909-a966-6b4066780cb0
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM_JobDestinationJobs class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_JobDestinationJobs
- CIM_JobDestinationJobs.Dependent
- CIM_JobDestinationJobs.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_JobDestinationJobs class

The **CIM\_JobDestinationJobs** association describes where a job is submitted for processing (that is, to which job destination).

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{8D079BEE-DB36-11d2-85FC-0000F8102E5F}"), AMENDMENT]
class CIM_JobDestinationJobs : CIM_Dependency
{
  CIM_Job            REF Dependent;
  CIM_JobDestination REF Antecedent;
};
```

## Members

The **CIM\_JobDestinationJobs** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_JobDestinationJobs** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_JobDestination**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A [**CIM\_JobDestination**](cim-jobdestination.md) describing the job destination, possibly a queue.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Job**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**CIM\_Job**](cim-job.md) describing the job that is in the job queue/Destination.

</dd> </dl>

## Remarks

**CIM\_JobDestinationJobs** is derived from [**CIM\_Dependency**](cim-dependency.md).

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

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





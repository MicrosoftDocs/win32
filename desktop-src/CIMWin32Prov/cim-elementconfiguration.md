---
Description: The CIM\_ElementConfiguration association relates a CIM\_Configuration object to one or more managed system elements. The CIM\_Configuration object represents a certain behavior, or a desired functional state for the associated CIM\_ManagedSystemElement.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4d2af009-7466-4394-af42-72c8d96e0786
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_ElementConfiguration class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ElementConfiguration class

The **CIM\_ElementConfiguration** association relates a [**CIM\_Configuration**](cim-configuration.md) object to one or more managed system elements. The **CIM\_Configuration** object represents a certain behavior, or a desired functional state for the associated [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{FC049DCE-DB29-11d2-85FC-0000F8102E5F}"), Association, AMENDMENT]
class CIM_ElementConfiguration
{
  CIM_Configuration        REF Configuration;
  CIM_ManagedSystemElement REF Element;
};
```

## Members

The **CIM\_ElementConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ElementConfiguration** class has these properties.

<dl> <dt>

**Configuration**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Configuration**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the [**CIM\_Configuration**](cim-configuration.md) object that groups the settings and dependencies associated with the managed system element.

</dd> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the managed system element.

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



 

 





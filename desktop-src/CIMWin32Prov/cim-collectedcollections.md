---
Description: 'The CIM\_CollectedCollections class is an aggregation association that represents a collection of Managed System Elements (MSE) contained in a collection of MSEs.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '7baaf429-1211-4545-ace2-c6312d53c0f6'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'CIM\_CollectedCollections class'
---

# CIM\_CollectedCollections class

The **CIM\_CollectedCollections** class is an aggregation association that represents a collection of Managed System Elements (MSE) contained in a collection of MSEs.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class CIM_CollectedCollections
{
  CIM_CollectionOfMSEs REF Collection;
  CIM_CollectionOfMSEs REF CollectionInCollection;
};
```

## Members

The **CIM\_CollectedCollections** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_CollectedCollections** class has these properties.

<dl> <dt>

**Collection**
</dt> <dd> <dl> <dt>

Data type: **CIM\_CollectionOfMSEs**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the "higher level" or parent element in the aggregation.

</dd> <dt>

**CollectionInCollection**
</dt> <dd> <dl> <dt>

Data type: **CIM\_CollectionOfMSEs**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the "collected" **Collection**.

</dd> </dl>

## Remarks

WMI does not implement this class.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



 

 





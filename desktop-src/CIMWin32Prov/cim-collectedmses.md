---
description: The CIM\_CollectedMSEs association class represents the members of the grouping object, a CollectionOfMSEs class.
ms.assetid: 3dca2094-57f1-447e-809c-f924f88a185a
ms.tgt_platform: multiple
title: CIM_CollectedMSEs class (CIMWin32 WMI Providers)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_CollectedMSEs
- CIM_CollectedMSEs.Collection
- CIM_CollectedMSEs.Member
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM_CollectedMSEs class (CIMWin32 WMI Providers)

The **CIM\_CollectedMSEs** association class represents the members of the grouping object, a [**CollectionOfMSEs**](cim-collectionofmses.md) class.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class CIM_CollectedMSEs
{
  CM_CollectionOfMSEs      REF Collection;
  CIM_ManagedSystemElement REF Member;
};
```

## Members

The **CIM\_CollectedMSEs** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_CollectedMSEs** class has these properties.

<dl> <dt>

**Collection**
</dt> <dd> <dl> <dt>

Data type: **CM\_CollectionOfMSEs**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the grouping or "bag" object that represents the collection.

</dd> <dt>

**Member**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to a member of the collection.

</dd> </dl>

## Remarks

WMI does not implement this class. For more information about WMI classes derived from **CIM\_CollectedMSEs**, see [Win32 Classes](win32-provider.md).

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



 

 





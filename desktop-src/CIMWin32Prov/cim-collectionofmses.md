---
description: The CIM\_CollectionOfMSEs object allows the grouping of CIM\_ManagedSystemElement objects for the purpose of associating settings and configurations. It is abstract to require further definition and semantic refinement in subclasses.
ms.assetid: 9448a7a1-defc-4bac-9ce6-29ec2406d573
ms.tgt_platform: multiple
title: CIM_CollectionOfMSEs class (CIMWin32 WMI Providers)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_CollectionOfMSEs
- CIM_CollectionOfMSEs.Caption
- CIM_CollectionOfMSEs.CollectionID
- CIM_CollectionOfMSEs.Description
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM_CollectionOfMSEs class (CIMWin32 WMI Providers)

The **CIM\_CollectionOfMSEs** object allows the grouping of [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md) objects for the purpose of associating settings and configurations. It is abstract to require further definition and semantic refinement in subclasses.

The **CIM\_CollectionOfMSEs** object does not carry any state or status information, but only represents a grouping of elements. For this reason, it is incorrect to subclass groups that have state/status from **CIM\_CollectionOfMSEs**, An example is [**CIM\_RedundancyGroup**](cim-redundancygroup.md) (which is correctly subclassed from [**CIM\_LogicalElement**](cim-logicalelement.md)). Collections typically aggregate 'like' objects, and represent an optimization. Without collections, one is forced to define individual [**CIM\_ElementSetting**](cim-elementsetting.md) and [**CIM\_ElementConfiguration**](cim-elementconfiguration.md) associations, to tie settings and configuration objects to individual [**CIM\_ManagedSystemElements**](cim-managedsystemelement.md). There may be much duplication in assigning the same setting to multiple objects. In addition, using the collection object allows the determination that the setting and configuration associations are indeed the same for the collection's members. This information would otherwise be obtained by defining the collection in a proprietary manner, and then querying the **CIM\_ElementSetting** and **CIM\_ElementConfiguration** associations to determine if the collection set is completely covered.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class CIM_CollectionOfMSEs
{
  string Caption;
  string CollectionID;
  string Description;
};
```

## Members

The **CIM\_CollectionOfMSEs** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_CollectionOfMSEs** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description of the CollectionOfMSEs object.

</dd> <dt>

**CollectionID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identification of the Collection object. When subclassed, the CollectionID property can be overridden to be a Key property.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the CollectionOfMSEs object.

</dd> </dl>

## Remarks

WMI does not implement this class. See [Win32 Classes](win32-provider.md) for WMI classes derived from **CIM\_CollectionOfMSEs**.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



 

 





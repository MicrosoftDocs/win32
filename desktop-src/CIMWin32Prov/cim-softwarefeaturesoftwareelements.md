---
description: The CIM\_SoftwareFeatureSoftwareElements association identifies the software elements that make up a specific software feature.
ms.assetid: 933586c5-b85e-4136-b557-5151a48abc32
ms.tgt_platform: multiple
title: CIM_SoftwareFeatureSoftwareElements class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_SoftwareFeatureSoftwareElements
- CIM_SoftwareFeatureSoftwareElements.PartComponent
- CIM_SoftwareFeatureSoftwareElements.GroupComponent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_SoftwareFeatureSoftwareElements class

The **CIM\_SoftwareFeatureSoftwareElements** association identifies the software elements that make up a specific software feature.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[UUID("{A91081E2-DB37-11d2-85FC-0000F8102E5F}"), Abstract, AMENDMENT]
class CIM_SoftwareFeatureSoftwareElements : CIM_Component
{
  CIM_SoftwareElement REF PartComponent;
  CIM_SoftwareFeature REF GroupComponent;
};
```

## Members

The **CIM\_SoftwareFeatureSoftwareElements** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SoftwareFeatureSoftwareElements** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SoftwareFeature**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

The group component.

This property is inherited from [**CIM\_Component**](cim-component.md).

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SoftwareElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The part component.

This property is inherited from [**CIM\_Component**](cim-component.md).

</dd> </dl>

## Remarks

The **CIM\_SoftwareFeatureSoftwareElements** association is derived from [**CIM\_Component**](cim-component.md).

WMI does not implement this class. For WMI classes derived from **CIM\_SoftwareFeatureSoftwareElements**, see [Win32 Classes](win32-provider.md).

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
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

 


---
description: The CIM\_Setting class represents configuration-related and operational parameters for one or more managed system elements.
ms.assetid: 57c46b00-96c4-4df1-82ad-01f7b4f75ced
ms.tgt_platform: multiple
title: CIM_Setting class (CIMWin32 WMI Providers)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Setting
- CIM_Setting.Caption
- CIM_Setting.Description
- CIM_Setting.SettingID
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM_Setting class (CIMWin32 WMI Providers)

The **CIM\_Setting** class represents configuration-related and operational parameters for one or more managed system elements. A managed system element can have multiple setting objects associated with it. The current operational values for an element's parameters are reflected by properties in the element itself or by properties in its associations. These properties do not have to be the same values present in the setting object. For example, a modem may have a setting baud rate of 56 kilobytes per second, but be operating at 19.2 kilobytes per second.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{8502C572-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class CIM_Setting
{
  string Caption;
  string Description;
  string SettingID;
};
```

## Members

The **CIM\_Setting** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Setting** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Short textual description of the current object.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the current object.

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Identifier by which the current object is known.

</dd> </dl>

## Remarks

WMI does not implement this class. For WMI classes derived from **CIM\_Setting**, see [Win32 Classes](win32-provider.md).

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



 


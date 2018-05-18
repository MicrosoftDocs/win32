---
title: Win32\_ShadowProvider class
description: The Win32\_ShadowProvider class represents a component that is a combination of user-mode and kernel or firmware implementation, that creates and represents volume shadow copies.
ms.assetid: 'c556b472-0f8f-47e0-8d17-c30982be3671'
keywords: ["Win32_ShadowProvider class", "Win32_ShadowProvider class, described"]
topic_type:
- apiref
api_name:
- Win32_ShadowProvider
- Win32_ShadowProvider.ID
- Win32_ShadowProvider.Name
- Win32_ShadowProvider.CLSID
- Win32_ShadowProvider.Type
- Win32_ShadowProvider.Version
- Win32_ShadowProvider.VersionID
api_location:
- Vsswmi.dll
api_type:
- DllExport
---

# Win32\_ShadowProvider class

Typically, the **Win32\_ShadowProvider** class represents a component that is a combination of user-mode and kernel or firmware implementation, that creates and represents volume shadow copies.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_ShadowProvider : CIM_LogicalElement
{
  string ID;
  string Name;
  string CLSID;
  uint32 Type;
  string Version;
  string VersionID;
};
```

## Members

The **Win32\_ShadowProvider** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ShadowProvider** class has these properties.

<dl> <dt>

**CLSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Common Object Model (COM) class ID registered for a shadow provider.

</dd> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Uniquely identifies the shadow provider on a system.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptive name of a provider.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the class to which a shadow provider belongs.

Possible values:



| Value                                                                        | Meaning             |
|------------------------------------------------------------------------------|---------------------|
| <dl> <dt>0</dt> </dl> | Unknown<br/>  |
| <dl> <dt>1</dt> </dl> | System<br/>   |
| <dl> <dt>2</dt> </dl> | Software<br/> |
| <dl> <dt>3</dt> </dl> | Hardware<br/> |



 

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Text representation of a shadow provider version.

</dd> <dt>

**VersionID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Numeric representation of a shadow provider version.

</dd> </dl>

## Examples

The [Get Remote Shadow Volume Information With Powershell](http://gallery.technet.microsoft.com/Get-Remote-Shadow-Volume-e5a72619) PowerShell sample on TechNet gallery uses **Win32\_ShadowProvider** to retrieve shadow volume information.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Vss.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Vsswmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_ShadowCopy**](win32-shadowcopy.md)
</dt> <dt>

[**Win32\_ShadowContext**](win32-shadowcontext.md)
</dt> <dt>

[**Win32\_ShadowStorage**](win32-shadowstorage.md)
</dt> <dt>

[**Win32\_ShadowBy**](win32-shadowby.md)
</dt> <dt>

[**Win32\_ShadowFor**](win32-shadowfor.md)
</dt> <dt>

[**Win32\_ShadowOn**](win32-shadowon.md)
</dt> <dt>

[**Win32\_ShadowVolumeSupport**](win32-shadowvolumesupport.md)
</dt> <dt>

[**Win32\_ShadowDiffVolumeSupport**](win32-shadowdiffvolumesupport.md)
</dt> </dl>

 

 






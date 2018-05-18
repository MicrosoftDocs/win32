---
title: Win32\_ShadowContext class
description: Specifies how a shadow copy is to be created, queried, or deleted, and the degree of writer involvement.
ms.assetid: 'efc9210e-f9e6-4f5d-a343-e6371eeed355'
keywords: ["Win32_ShadowContext class", "Win32_ShadowContext class, described"]
topic_type:
- apiref
api_name:
- Win32_ShadowContext
- Win32_ShadowContext.Name
- Win32_ShadowContext.Persistent
- Win32_ShadowContext.ClientAccessible
- Win32_ShadowContext.NoAutoRelease
- Win32_ShadowContext.NoWriters
- Win32_ShadowContext.Transportable
- Win32_ShadowContext.NotSurfaced
- Win32_ShadowContext.HardwareAssisted
- Win32_ShadowContext.Differential
- Win32_ShadowContext.Plex
- Win32_ShadowContext.Imported
- Win32_ShadowContext.ExposedRemotely
- Win32_ShadowContext.ExposedLocally
api_location:
- Vsswmi.dll
api_type:
- DllExport
---

# Win32\_ShadowContext class

The **Win32\_ShadowContext** class specifies how a shadow copy is to be created, queried, or deleted, and the degree of writer involvement.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_ShadowContext : CIM_Setting
{
  string  Name;
  boolean Persistent;
  boolean ClientAccessible;
  boolean NoAutoRelease;
  boolean NoWriters;
  boolean Transportable;
  boolean NotSurfaced;
  boolean HardwareAssisted;
  boolean Differential;
  boolean Plex;
  boolean Imported;
  boolean ExposedRemotely;
  boolean ExposedLocally;
};
```

## Members

The **Win32\_ShadowContext** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ShadowContext** class has these properties.

<dl> <dt>

**ClientAccessible**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is created by the Windows Previous Versions component.

</dd> <dt>

**Differential**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is created by a differential shadow copy provider. The provider can be implemented in hardware or software.

</dd> <dt>

**ExposedLocally**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is exposed on a remote computer with a network share. If both **ExposedLocally** and **ExposedRemotely** are **false**, the shadow copy is hidden.

</dd> <dt>

**ExposedRemotely**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is exposed on a remote computer with a network share. If both **ExposedRemotely** and **ExposedLocally** are **false**, the shadow copy is hidden.

</dd> <dt>

**HardwareAssisted**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is created by a hardware shadow copy provider.

</dd> <dt>

**Imported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is imported to a computer by using the **Import** method and is not created by using the [**Create**](create-method-in-class-win32-shadowcopy.md) method.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Name of the context.

</dd> <dt>

**NoAutoRelease**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is retained after the requestor process ends. If **false**, the shadow copy is automatically deleted when the shadow copy requestor process ends.

</dd> <dt>

**NotSurfaced**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is not currently in the device namespace of the local computer.

</dd> <dt>

**NoWriters**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is created without involvement of shadow copy writer components.

</dd> <dt>

**Persistent**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy persists across restarts.

</dd> <dt>

**Plex**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy is created by a split-mirror shadow copy provider.

</dd> <dt>

**Transportable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the shadow copy can be surfaced on another computer. If **false**, and the volumes are surfaced locally, it may not be possible to surface them later on a different computer.

</dd> </dl>

## Examples

The [Get Remote Shadow Volume Information With Powershell](http://gallery.technet.microsoft.com/Get-Remote-Shadow-Volume-e5a72619) PowerShell sample on TechNet gallery uses **Win32\_ShadowContext** to retrieve shadow volume information.

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

[**Win32\_ShadowProvider**](win32-shadowprovider.md)
</dt> <dt>

[**Win32\_ShadowCopy**](win32-shadowcopy.md)
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

 

 






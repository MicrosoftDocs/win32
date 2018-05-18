---
title: Win32\_ShadowStorage class
description: The Win32\_ShadowStorage class represents the association between a volume for which a shadow copy is made, and a volume to which differential data is written.
ms.assetid: 'a27a55f3-8b4a-4221-93e9-69d2d3afe4cc'
keywords: ["Win32_ShadowStorage class", "Win32_ShadowStorage class, described"]
topic_type:
- apiref
api_name:
- Win32_ShadowStorage
- Win32_ShadowStorage.AllocatedSpace
- Win32_ShadowStorage.DiffVolume
- Win32_ShadowStorage.MaxSpace
- Win32_ShadowStorage.UsedSpace
- Win32_ShadowStorage.Volume
api_location:
- Vsswmi.dll
api_type:
- DllExport
---

# Win32\_ShadowStorage class

The **Win32\_ShadowStorage** class represents the association between a volume for which a shadow copy is made, and a volume to which differential data is written.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_ShadowStorage
{
  uint64           AllocatedSpace;
  Win32_Volume REF DiffVolume;
  uint64           MaxSpace;
  uint64           UsedSpace;
  Win32_Volume REF Volume;
};
```

## Members

The **Win32\_ShadowStorage** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_ShadowStorage** class has these methods.



| Method                                                       | Description                                                              |
|:-------------------------------------------------------------|:-------------------------------------------------------------------------|
| [**Create**](create-method-in-class-win32-shadowstorage.md) | Creates a differential area storage for the specified Volume.<br/> |



 

### Properties

The **Win32\_ShadowStorage** class has these properties.

<dl> <dt>

**AllocatedSpace**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Allocated space on the differential area volume.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**DiffVolume**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Volume**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Reference to the differential volume.

</dd> <dt>

**MaxSpace**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum space on the differential area volume.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**UsedSpace**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Used space on the differential area volume.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**Volume**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Volume**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Reference to the original volume.

</dd> </dl>

## Examples

The [Get Remote Shadow Volume Information With Powershell](http://gallery.technet.microsoft.com/Get-Remote-Shadow-Volume-e5a72619) PowerShell sample on TechNet gallery uses **Win32\_ShadowStorage** to retrieve shadow volume information.

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

[**Win32\_ShadowContext**](win32-shadowcontext.md)
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

 

 






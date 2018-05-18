---
title: Win32\_VolumeQuota class
description: The Win32\_VolumeQuota association relates a volume to the per volume quota settings.
ms.assetid: 'ba074afc-6d5e-4d75-866f-e8d6959ab890'
keywords: ["Win32_VolumeQuota class", "Win32_VolumeQuota class, described"]
topic_type:
- apiref
api_name:
- Win32_VolumeQuota
- Win32_VolumeQuota.Element
- Win32_VolumeQuota.Setting
api_location:
- Vdswmi.dll
api_type:
- DllExport
---

# Win32\_VolumeQuota class

The **Win32\_VolumeQuota** association relates a volume to the per volume quota settings.

**Windows XP and earlier:** This class is not available

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_VolumeQuota : CIM_ElementSetting
{
  Win32_Volume       REF Element;
  Win32_QuotaSetting REF Setting;
};
```

## Members

The **Win32\_VolumeQuota** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_VolumeQuota** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Volume**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the volume.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_QuotaSetting**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the quota setting.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Vds.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Vdswmi.dll</dt> </dl> |



## See also

<dl> <dt>

[Storage Volume Provider](storage-volume-provider.md)
</dt> <dt>

[**Win32\_Volume**](win32-volume.md)
</dt> <dt>

[**Win32\_VolumeUserQuota**](win32-volumeuserquota.md)
</dt> <dt>

[**Win32\_DefragAnalysis**](win32-defraganalysis.md)
</dt> <dt>

[**Win32\_MountPoint**](win32-mountpoint.md)
</dt> </dl>

 

 






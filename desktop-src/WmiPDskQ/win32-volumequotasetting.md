---
title: Win32\_VolumeQuotaSetting class
description: The Win32\_VolumeQuotaSetting association WMI class relates disk quota settings with a specific disk volume.
ms.assetid: 'ef43c414-0f45-460b-9b3e-e0b9402e36d1'
keywords: ["Win32_VolumeQuotaSetting class", "Win32_VolumeQuotaSetting class, described"]
topic_type:
- apiref
api_name:
- Win32_VolumeQuotaSetting
- Win32_VolumeQuotaSetting.Element
- Win32_VolumeQuotaSetting.Setting
api_location:
- Wmipdskq.dll
api_type:
- DllExport
---

# Win32\_VolumeQuotaSetting class

The **Win32\_VolumeQuotaSetting** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates disk quota settings with a specific disk volume.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_VolumeQuotaSetting : CIM_ElementSetting
{
  Win32_LogicalDisk   REF Element;
  Win32_QuotaSettings REF Setting;
};
```

## Members

The **Win32\_VolumeQuotaSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_VolumeQuotaSetting** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LogicalDisk**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reference to the instance representing the disk volume instance for the associated disk quota settings. This property overrides the **Element** property inherited from [**CIM\_ElementSetting**](https://msdn.microsoft.com/library/aa387263).

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_QuotaSettings**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reference to the instance representing the quota settings instance associated with the referenced logical disk. This property overrides the **Setting** property inherited from [**CIM\_ElementSetting**](https://msdn.microsoft.com/library/aa387263).

</dd> </dl>

## Remarks

The **Win32\_VolumeQuotaSetting** is derived from [**CIM\_ElementSetting**](https://msdn.microsoft.com/library/aa387263).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipdskq.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipdskq.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 






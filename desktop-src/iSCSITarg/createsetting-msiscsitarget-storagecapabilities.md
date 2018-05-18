---
title: CreateSetting method of the MSISCSITARGET\_StorageCapabilities class
description: Creates and populates a MSISCSITARGET\_StorageSetting instance from a MSISCSITARGET\_StorageCapabilities instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c8f8386f-6372-499f-b3e0-bdd8c6d8d786'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateSetting method iSCSI Software Target API", "CreateSetting method iSCSI Software Target API , MSISCSITARGET_StorageCapabilities class", "MSISCSITARGET_StorageCapabilities class iSCSI Software Target API , CreateSetting method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageCapabilities.CreateSetting
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# CreateSetting method of the MSISCSITARGET\_StorageCapabilities class

Creates and populates a [**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md) instance from a **MSISCSITARGET\_StorageCapabilities** instance. If the underlying instrumentation supports the **CIM\_StorageSettingWithHints** subclass, then an instance of that class is created instead.

This method is inherited from the **CIM\_StorageCapabilities** class.

## Syntax


```mof
uint32 CreateSetting(
  [in]  uint16                 SettingType,
  [out] CIM_StorageSetting Ref NewSetting
);
```



## Parameters

<dl> <dt>

*SettingType* \[in\]
</dt> <dd>

Indicates the source to use for the property values of the new [**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md) instance.

<dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>**Default** (2)


</dt> <dd>

Indicates the property values are set to the default values of the parent [**MSISCSITARGET\_StorageCapabilities**](msiscsitarget-storagecapabilities.md) instance.

</dd> <dt>

<span id="Goal"></span><span id="goal"></span><span id="GOAL"></span>

<span id="Goal"></span><span id="goal"></span><span id="GOAL"></span>**Goal** (3)


</dt> <dd>

Indicates the property values are set to the related values of the parent [**MSISCSITARGET\_StorageCapabilities**](msiscsitarget-storagecapabilities.md) instance. For example, the **MSISCSITARGET\_StorageCapabilities**.**DataRedundancyMin**, **DataRedundancyMax**, and **DataRedundancyDefault** property values are propagated to the [**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md).**DataRedundancyMin**, **DataRedundancyMax**, and **DataRedundancyGoal** properties respectively.

</dd> </dl> </dd> <dt>

*NewSetting* \[out\]
</dt> <dd>

On return, contains a reference to the created [**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md) instance.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**DMTF Reserved** (6–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>Smiscsitarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StorageCapabilities**](msiscsitarget-storagecapabilities.md)
</dt> <dt>

[**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md)
</dt> </dl>

 

 






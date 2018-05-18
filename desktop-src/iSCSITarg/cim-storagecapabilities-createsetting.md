---
title: CreateSetting method of the CIM\_StorageCapabilities class
description: Method to create and populate a StorageSetting instance from a StorageCapability instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '60d7877a-4a3e-48e8-89a7-7f4793a07619'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateSetting method iSCSI Software Target API", "CreateSetting method iSCSI Software Target API , CIM_StorageCapabilities class", "CIM_StorageCapabilities class iSCSI Software Target API , CreateSetting method"]
topic_type:
- apiref
api_name:
- CIM_StorageCapabilities.CreateSetting
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# CreateSetting method of the CIM\_StorageCapabilities class

Method to create and populate a StorageSetting instance from a StorageCapability instance. This removes the need to populate default settings and other settings in the context of each StorageCapabilities (which could be numerous). If the underlying instrumentation supports the StorageSettingWithHints subclass, then an instance of that class will be created instead.

## Syntax


```mof
uint32 CreateSetting(
  [in]  uint16                 SettingType,
  [out] CIM_StorageSetting REF NewSetting
);
```



## Parameters

<dl> <dt>

*SettingType* \[in\]
</dt> <dd>

If 'Default' is passed for the CreateDefault parameter, the Max, Goal, and Min setting attributes are set to the Default values of the parent StorageCapabilities when the instance is created.

If set to 'Goal' the new StorageSetting attributes are set to the related attributes of the parent StorageCapabilities, e.g. Min to Min, Goal to Default, and Max to Max.

This method maybe deprecated in lieu of intrinsics once limitations in the CIM Operations are addressed.

<dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>

**Default** (2)


</dt> <dd></dd> <dt>

<span id="Goal"></span><span id="goal"></span><span id="GOAL"></span>

**Goal** (3)


</dt> <dd></dd> </dl> </dd> <dt>

*NewSetting* \[out\]
</dt> <dd>

Reference to the created StorageSetting instance.

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
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StorageCapabilities**](cim-storagecapabilities.md)
</dt> </dl>

 

 






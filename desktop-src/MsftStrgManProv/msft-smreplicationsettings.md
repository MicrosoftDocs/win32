---
title: MSFT\_SMReplicationSettings class
description: Represents the settings configure on a replication group or synchronization pair.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '77cbb833-e1d5-4c92-b332-5783fb24ccfa'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMReplicationSettings class", "MSFT_SMReplicationSettings class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMReplicationSettings
- MSFT_SMReplicationSettings.ObjectId
- MSFT_SMReplicationSettings.Identifier
- MSFT_SMReplicationSettings.TargetElementSupplier
- MSFT_SMReplicationSettings.ThinProvisioningPolicy
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMReplicationSettings class

Represents the settings configure on a replication group or synchronization pair.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("WMIStorage"), AMENDMENT]
class MSFT_SMReplicationSettings : MSFT_SMStorageObject
{
  String ObjectId;
  String Identifier;
  uint16 TargetElementSupplier = 4;
  uint16 ThinProvisioningPolicy = 7;
};
```

## Members

The **MSFT\_SMReplicationSettings** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMReplicationSettings** class has these properties.

<dl> <dt>

**Identifier**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of the logical instance of the object. This ID must be unique within the scope of the storage system.

This property is inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

</dd> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of this class instance. This ID must be unique within the scope of the Windows Storage Management server that hosts the provider object.

This property is inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

</dd> <dt>

**TargetElementSupplier**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates where to retrieve target elements when they are not supplied.

The possible values are:

<dt>

<span id="Use_existing"></span><span id="use_existing"></span><span id="USE_EXISTING"></span>

**Use existing** (1)


</dt> <dd></dd> <dt>

<span id="Create_new"></span><span id="create_new"></span><span id="CREATE_NEW"></span>

**Create new** (2)


</dt> <dd></dd> <dt>

<span id="Use_and_create"></span><span id="use_and_create"></span><span id="USE_AND_CREATE"></span>

**Use and create** (3)


</dt> <dd></dd> <dt>

<span id="Instrumentation_decides"></span><span id="instrumentation_decides"></span><span id="INSTRUMENTATION_DECIDES"></span>

**Instrumentation decides** (4)


</dt> <dd></dd> <dt>

<span id="Client_must_supply"></span><span id="client_must_supply"></span><span id="CLIENT_MUST_SUPPLY"></span>

**Client must supply** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6–32767</dd> <dt>

<span id="Vendor_specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor specific**


</dt> <dd>32768–...</dd> </dl>

</dd> <dt>

**ThinProvisioningPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the provisioning policy of the target element, if the target element is not supplied.

The possible values are:

<dt>

<span id="Copy_thin_source_to_thin_target"></span><span id="copy_thin_source_to_thin_target"></span><span id="COPY_THIN_SOURCE_TO_THIN_TARGET"></span>

**Copy thin source to thin target** (2)


</dt> <dd></dd> <dt>

<span id="Copy_thin_source_to_full_target"></span><span id="copy_thin_source_to_full_target"></span><span id="COPY_THIN_SOURCE_TO_FULL_TARGET"></span>

**Copy thin source to full target** (3)


</dt> <dd></dd> <dt>

<span id="Copy_full_source_to_thin_target"></span><span id="copy_full_source_to_thin_target"></span><span id="COPY_FULL_SOURCE_TO_THIN_TARGET"></span>

**Copy full source to thin target** (4)


</dt> <dd></dd> <dt>

<span id="Provisioning_of_target_same_as_source"></span><span id="provisioning_of_target_same_as_source"></span><span id="PROVISIONING_OF_TARGET_SAME_AS_SOURCE"></span>

**Provisioning of target same as source** (5)


</dt> <dd></dd> <dt>

<span id="Target_pool_decides_provisioning_of_target_element"></span><span id="target_pool_decides_provisioning_of_target_element"></span><span id="TARGET_POOL_DECIDES_PROVISIONING_OF_TARGET_ELEMENT"></span>

**Target pool decides provisioning of target element** (6)


</dt> <dd></dd> <dt>

<span id="Implementation_decides_provisioning_of_target"></span><span id="implementation_decides_provisioning_of_target"></span><span id="IMPLEMENTATION_DECIDES_PROVISIONING_OF_TARGET"></span>

**Implementation decides provisioning of target** (7)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>8–32767</dd> <dt>

<span id="Vendor_specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMStorageObject**](msft-smstorageobject.md)
</dt> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 






---
title: PartialDiscovery method of the MSFT\_SMStorageDiscovery class
description: Starts the Microsoft storage service partial discovery process.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9053deb7-d7e2-4796-81e1-440256a207ec'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PartialDiscovery method", "PartialDiscovery method, MSFT_SMStorageDiscovery class", "MSFT_SMStorageDiscovery class, PartialDiscovery method"]
topic_type:
- apiref
api_name:
- MSFT_SMStorageDiscovery.PartialDiscovery
api_location:
- StorageService.dll
api_type:
- COM
---

# PartialDiscovery method of the MSFT\_SMStorageDiscovery class

Starts the Microsoft storage service partial discovery process.

## Syntax


```mof
Uint32 PartialDiscovery(
  [in]            String                host,
  [in, optional]  String                hostType,
  [in]            String                interopNamespace,
  [in]            String                username,
  [in]            String                password,
  [in, optional]  Uint32                discoveryLevel,
  [in]            Uint32                partialDiscoveryType,
  [in, optional]  String                targetObjectId,
  [in]            Uint32                targetObjectClassType,
  [out]           MSFT_SMJob        REF Job,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*host* \[in\]
</dt> <dd>

The name of the host to discover.

</dd> <dt>

*hostType* \[in, optional\]
</dt> <dd>

The type of the host to discover.

The possible values are.

<dt>

<span id="host-resource"></span><span id="HOST-RESOURCE"></span>

**host-resource** ("host-resource")


</dt> <dd></dd> <dt>

<span id="smis-wmi"></span><span id="SMIS-WMI"></span>

**smis-wmi** ("smis-wmi")


</dt> <dd></dd> <dt>

<span id="smis-cimxml"></span><span id="SMIS-CIMXML"></span>

**smis-cimxml** ("smis-cimxml")


</dt> <dd></dd> </dl> </dd> <dt>

*interopNamespace* \[in\]
</dt> <dd>

The interoperation namespace used for the discovery process.

</dd> <dt>

*username* \[in\]
</dt> <dd>

The username used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*password* \[in\]
</dt> <dd>

The password used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*discoveryLevel* \[in, optional\]
</dt> <dd>

The depth of discovery.

The possible values are.

<dt>

<span id="Top-Level"></span><span id="top-level"></span><span id="TOP-LEVEL"></span>

**Top-Level** (0)


</dt> <dd></dd> <dt>

<span id="Mid-Level"></span><span id="mid-level"></span><span id="MID-LEVEL"></span>

**Mid-Level** (1)


</dt> <dd></dd> <dt>

<span id="AllExceptDiskDrives"></span><span id="allexceptdiskdrives"></span><span id="ALLEXCEPTDISKDRIVES"></span>

**AllExceptDiskDrives** (2)


</dt> <dd></dd> <dt>

<span id="All"></span><span id="all"></span><span id="ALL"></span>

**All** (3)


</dt> <dd></dd> </dl> </dd> <dt>

*partialDiscoveryType* \[in\]
</dt> <dd>

The type of search that will be performed during the operation.

The possible values are.

<dt>

<span id="Full"></span><span id="full"></span><span id="FULL"></span>

**Full** (0)


</dt> <dd></dd> <dt>

<span id="MSFT_SMSystem"></span><span id="msft_smsystem"></span><span id="MSFT_SMSYSTEM"></span>

**MSFT\_SMSystem** (1)


</dt> <dd></dd> <dt>

<span id="MSFT_SMStorageHardwareID"></span><span id="msft_smstoragehardwareid"></span><span id="MSFT_SMSTORAGEHARDWAREID"></span>

**MSFT\_SMStorageHardwareID** (2)


</dt> <dd></dd> <dt>

<span id="MSFT_SMPool"></span><span id="msft_smpool"></span><span id="MSFT_SMPOOL"></span>

**MSFT\_SMPool** (3)


</dt> <dd></dd> <dt>

<span id="MSFT_SMVolume"></span><span id="msft_smvolume"></span><span id="MSFT_SMVOLUME"></span>

**MSFT\_SMVolume** (4)


</dt> <dd></dd> <dt>

<span id="MSFT_SMEndpoint"></span><span id="msft_smendpoint"></span><span id="MSFT_SMENDPOINT"></span>

**MSFT\_SMEndpoint** (5)


</dt> <dd></dd> <dt>

<span id="MSFT_SMiSCSIPortalEndpoint"></span><span id="msft_smiscsiportalendpoint"></span><span id="MSFT_SMISCSIPORTALENDPOINT"></span>

**MSFT\_SMiSCSIPortalEndpoint** (6)


</dt> <dd></dd> <dt>

<span id="MSFT_SMStorageGroup"></span><span id="msft_smstoragegroup"></span><span id="MSFT_SMSTORAGEGROUP"></span>

**MSFT\_SMStorageGroup** (7)


</dt> <dd></dd> <dt>

<span id="MSFT_SMFCPort"></span><span id="msft_smfcport"></span><span id="MSFT_SMFCPORT"></span>

**MSFT\_SMFCPort** (8)


</dt> <dd></dd> <dt>

<span id="MSFT_SMFabric"></span><span id="msft_smfabric"></span><span id="MSFT_SMFABRIC"></span>

**MSFT\_SMFabric** (9)


</dt> <dd></dd> <dt>

<span id="MSFT_SMSwitch"></span><span id="msft_smswitch"></span><span id="MSFT_SMSWITCH"></span>

**MSFT\_SMSwitch** (10)


</dt> <dd></dd> <dt>

<span id="MSFT_SMZoneSet"></span><span id="msft_smzoneset"></span><span id="MSFT_SMZONESET"></span>

**MSFT\_SMZoneSet** (11)


</dt> <dd></dd> <dt>

<span id="MSFT_SMZone"></span><span id="msft_smzone"></span><span id="MSFT_SMZONE"></span>

**MSFT\_SMZone** (12)


</dt> <dd></dd> <dt>

<span id="MSFT_SMZoneMembershipData"></span><span id="msft_smzonemembershipdata"></span><span id="MSFT_SMZONEMEMBERSHIPDATA"></span>

**MSFT\_SMZoneMembershipData** (13)


</dt> <dd></dd> <dt>

<span id="MSFT_SMDiskDrive"></span><span id="msft_smdiskdrive"></span><span id="MSFT_SMDISKDRIVE"></span>

**MSFT\_SMDiskDrive** (14)


</dt> <dd></dd> <dt>

<span id="MSFT_SMProvider"></span><span id="msft_smprovider"></span><span id="MSFT_SMPROVIDER"></span>

**MSFT\_SMProvider** (15)


</dt> <dd></dd> <dt>

<span id="MSFT_SMPoolSetting"></span><span id="msft_smpoolsetting"></span><span id="MSFT_SMPOOLSETTING"></span>

**MSFT\_SMPoolSetting** (16)


</dt> <dd></dd> </dl> </dd> <dt>

*targetObjectId* \[in, optional\]
</dt> <dd>

The ID of the object in which to run the discovery process.

</dd> <dt>

*targetObjectClassType* \[in\]
</dt> <dd>

The class type of the **targetObjectId** object.

The possible values are.

<dt>

<span id="Unspecified"></span><span id="unspecified"></span><span id="UNSPECIFIED"></span>

**Unspecified** (0)


</dt> <dd></dd> <dt>

<span id="MSFT_SMSystem"></span><span id="msft_smsystem"></span><span id="MSFT_SMSYSTEM"></span>

**MSFT\_SMSystem** (1)


</dt> <dd></dd> <dt>

<span id="MSFT_SMStorageHardwareID"></span><span id="msft_smstoragehardwareid"></span><span id="MSFT_SMSTORAGEHARDWAREID"></span>

**MSFT\_SMStorageHardwareID** (2)


</dt> <dd></dd> <dt>

<span id="MSFT_SMPool"></span><span id="msft_smpool"></span><span id="MSFT_SMPOOL"></span>

**MSFT\_SMPool** (3)


</dt> <dd></dd> <dt>

<span id="MSFT_SMVolume"></span><span id="msft_smvolume"></span><span id="MSFT_SMVOLUME"></span>

**MSFT\_SMVolume** (4)


</dt> <dd></dd> <dt>

<span id="MSFT_SMEndpoint"></span><span id="msft_smendpoint"></span><span id="MSFT_SMENDPOINT"></span>

**MSFT\_SMEndpoint** (5)


</dt> <dd></dd> <dt>

<span id="MSFT_SMiSCSIPortalEndpoint"></span><span id="msft_smiscsiportalendpoint"></span><span id="MSFT_SMISCSIPORTALENDPOINT"></span>

**MSFT\_SMiSCSIPortalEndpoint** (6)


</dt> <dd></dd> <dt>

<span id="MSFT_SMStorageGroup"></span><span id="msft_smstoragegroup"></span><span id="MSFT_SMSTORAGEGROUP"></span>

**MSFT\_SMStorageGroup** (7)


</dt> <dd></dd> <dt>

<span id="MSFT_SMFCPort"></span><span id="msft_smfcport"></span><span id="MSFT_SMFCPORT"></span>

**MSFT\_SMFCPort** (8)


</dt> <dd></dd> <dt>

<span id="MSFT_SMFabric"></span><span id="msft_smfabric"></span><span id="MSFT_SMFABRIC"></span>

**MSFT\_SMFabric** (9)


</dt> <dd></dd> <dt>

<span id="MSFT_SMSwitch"></span><span id="msft_smswitch"></span><span id="MSFT_SMSWITCH"></span>

**MSFT\_SMSwitch** (10)


</dt> <dd></dd> <dt>

<span id="MSFT_SMZoneSet"></span><span id="msft_smzoneset"></span><span id="MSFT_SMZONESET"></span>

**MSFT\_SMZoneSet** (11)


</dt> <dd></dd> <dt>

<span id="MSFT_SMZone"></span><span id="msft_smzone"></span><span id="MSFT_SMZONE"></span>

**MSFT\_SMZone** (12)


</dt> <dd></dd> <dt>

<span id="MSFT_SMZoneMembershipData"></span><span id="msft_smzonemembershipdata"></span><span id="MSFT_SMZONEMEMBERSHIPDATA"></span>

**MSFT\_SMZoneMembershipData** (13)


</dt> <dd></dd> <dt>

<span id="MSFT_SMDiskDrive"></span><span id="msft_smdiskdrive"></span><span id="MSFT_SMDISKDRIVE"></span>

**MSFT\_SMDiskDrive** (14)


</dt> <dd></dd> <dt>

<span id="MSFT_SMProvider"></span><span id="msft_smprovider"></span><span id="MSFT_SMPROVIDER"></span>

**MSFT\_SMProvider** (15)


</dt> <dd></dd> <dt>

<span id="MSFT_SMPoolSetting"></span><span id="msft_smpoolsetting"></span><span id="MSFT_SMPOOLSETTING"></span>

**MSFT\_SMPoolSetting** (16)


</dt> <dd></dd> </dl> </dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the [**MSFT\_SMJob**](msft-smjob.md) instance. May be **NULL** if the job is completed.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object that contains the results of this method call.

</dd> </dl>

## Return value

<dl> <dt>

**Success**
</dt> <dd>

0

</dd> <dt>

**Failed**
</dt> <dd>

1

</dd> <dt>

**Discovery already in progress**
</dt> <dd>

2

</dd> <dt>

**Job started**
</dt> <dd>

4096

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMStorageDiscovery**](msft-smstoragediscovery.md)
</dt> </dl>

 

 






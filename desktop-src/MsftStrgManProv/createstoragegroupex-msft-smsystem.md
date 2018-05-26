---
title: CreateStorageGroupEx method of the MSFT\_SMSystem class
description: Creates a Storage Group (SPC).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6ac48930-daba-466f-aad9-728c98866531
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateStorageGroupEx method
- CreateStorageGroupEx method, MSFT_SMSystem class
- MSFT_SMSystem class, CreateStorageGroupEx method
topic_type:
- apiref
api_name:
- MSFT_SMSystem.CreateStorageGroupEx
api_location:
- StorageService.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateStorageGroupEx method of the MSFT\_SMSystem class

Creates a Storage Group (SPC).

## Syntax


```mof
Uint32 CreateStorageGroupEx(
  [in]            String                  Name,
  [in]            String                  LUNames[],
  [in]            String                  DeviceNumbers[],
  [in]            Uint16                  DeviceAccesses[],
  [in]            String                  InitiatorIDs[],
  [in]            String                  TargetPortIDs[],
  [in]            Uint16                  HostType,
  [out]           MSFT_SMStorageGroup REF StorageGroup,
  [out]           MSFT_SMJob          REF Job,
  [out, optional] MSFT_SMExtendedStatus   ExtendedStatus,
  [in, optional]  String                  username,
  [in, optional]  String                  password
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name to be assigned to the [**MSFT\_SMStorageGroup**](msft-smstoragegroup.md) instance.

</dd> <dt>

*LUNames* \[in\]
</dt> <dd>

An array of IDs of existing logical unit instances.

> [!Note]  
> IDs must match the **Name** property of LogicalDevice instances that represent SCSI logical units.

 

</dd> <dt>

*DeviceNumbers* \[in\]
</dt> <dd>

Logical unit numbers to assign to the corresponding item in the *LUNames* parameter. If this parameter is **NULL**, all LU numbers are assigned by the hardware or instrumentation.

</dd> <dt>

*DeviceAccesses* \[in\]
</dt> <dd>

The permissions to assign to the corresponding logical unit in the *LUNames* parameter. Setting this to 'No Access' assigns the DeviceNumber for the associated initiators, but does not grant read or write access. If the *LUNames* parameter is not **NULL** then this parameter is required.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Read_Write"></span><span id="read_write"></span><span id="READ_WRITE"></span>

**Read Write** (2)


</dt> <dd></dd> <dt>

<span id="Read-Only"></span><span id="read-only"></span><span id="READ-ONLY"></span>

**Read-Only** (3)


</dt> <dd></dd> <dt>

<span id="No_Access"></span><span id="no_access"></span><span id="NO_ACCESS"></span>

**No Access** (4)


</dt> <dd></dd> </dl> </dd> <dt>

*InitiatorIDs* \[in\]
</dt> <dd>

IDs of initiator ports.

</dd> <dt>

*TargetPortIDs* \[in\]
</dt> <dd>

IDs of target ports.

</dd> <dt>

*HostType* \[in\]
</dt> <dd>

Defines the operating system, version, driver, and other host environment factors that influence the behavior exposed by storage systems.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Standard"></span><span id="standard"></span><span id="STANDARD"></span>

**Standard** (2)


</dt> <dd></dd> <dt>

<span id="Solaris"></span><span id="solaris"></span><span id="SOLARIS"></span>

**Solaris** (3)


</dt> <dd></dd> <dt>

<span id="HPUX"></span><span id="hpux"></span>

**HPUX** (4)


</dt> <dd></dd> <dt>

<span id="OpenVMS"></span><span id="openvms"></span><span id="OPENVMS"></span>

**OpenVMS** (5)


</dt> <dd></dd> <dt>

<span id="Tru64"></span><span id="tru64"></span><span id="TRU64"></span>

**Tru64** (6)


</dt> <dd></dd> <dt>

<span id="Netware"></span><span id="netware"></span><span id="NETWARE"></span>

**Netware** (7)


</dt> <dd></dd> <dt>

<span id="Sequent"></span><span id="sequent"></span><span id="SEQUENT"></span>

**Sequent** (8)


</dt> <dd></dd> <dt>

<span id="AIX"></span><span id="aix"></span>

**AIX** (9)


</dt> <dd></dd> <dt>

<span id="DGUX"></span><span id="dgux"></span>

**DGUX** (10)


</dt> <dd></dd> <dt>

<span id="Dynix"></span><span id="dynix"></span><span id="DYNIX"></span>

**Dynix** (11)


</dt> <dd></dd> <dt>

<span id="Irix"></span><span id="irix"></span><span id="IRIX"></span>

**Irix** (12)


</dt> <dd></dd> <dt>

<span id="Cisco_iSCSI_Storage_Router"></span><span id="cisco_iscsi_storage_router"></span><span id="CISCO_ISCSI_STORAGE_ROUTER"></span>

**Cisco iSCSI Storage Router** (13)


</dt> <dd></dd> <dt>

<span id="Linux"></span><span id="linux"></span><span id="LINUX"></span>

**Linux** (14)


</dt> <dd></dd> <dt>

<span id="Microsoft_Windows"></span><span id="microsoft_windows"></span><span id="MICROSOFT_WINDOWS"></span>

**Microsoft Windows** (15)


</dt> <dd></dd> <dt>

<span id="OS400"></span><span id="os400"></span>

**OS400** (16)


</dt> <dd></dd> <dt>

<span id="TRESPASS"></span><span id="trespass"></span>

**TRESPASS** (17)


</dt> <dd></dd> <dt>

<span id="HI-UX"></span><span id="hi-ux"></span>

**HI-UX** (18)


</dt> <dd></dd> <dt>

<span id="VMware_ESXi"></span><span id="vmware_esxi"></span><span id="VMWARE_ESXI"></span>

**VMware ESXi** (19)


</dt> <dd></dd> <dt>

<span id="Microsoft_Windows_Server_2008"></span><span id="microsoft_windows_server_2008"></span><span id="MICROSOFT_WINDOWS_SERVER_2008"></span>

**Microsoft Windows Server 2008** (20)


</dt> <dd></dd> <dt>

<span id="Microsoft_Windows_Server_2003"></span><span id="microsoft_windows_server_2003"></span><span id="MICROSOFT_WINDOWS_SERVER_2003"></span>

**Microsoft Windows Server 2003** (21)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>22 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

**Windows Server 2012:** The default for this parameter is 15, **Microsoft Windows**.

</dd> <dt>

*StorageGroup* \[out\]
</dt> <dd>

Reference to the created [**MSFT\_SMStorageGroup**](msft-smstoragegroup.md) (SCSIProtocolController) instance.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the [**MSFT\_SMJob**](msft-smjob.md) instance. May be **NULL** if the job is completed.

**Windows Server 2012:** This parameter is not supported.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object containing the results of calling this method.

</dd> <dt>

*username* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

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

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Invalid logical unit ID** (4097)
</dt> <dt>

**Invalid initiator port ID** (4098)
</dt> <dt>

**Invalid target port ID** (4099)
</dt> <dt>

**Invalid permission** (4100)
</dt> <dt>

**Target/initiator combination already exposed** (4101)
</dt> <dt>

**Requested logical unit number in use** (4102)
</dt> <dt>

**Maximum Map Count Exceeded** (4103)
</dt> <dt>

**StorageService: Error LUNames Required** (40000)
</dt> <dt>

**StorageService: Errpr InitiatorID Required** (40005)
</dt> <dt>

**StorageService: Error TargetPortID Required** (40010)
</dt> <dt>

**StorageService: DeviceAccess Array Size not equal to LUNames Array Size** (40015)
</dt> <dt>

**StorageService: DeviceAccess value is not supported** (40016)
</dt> <dt>

**StorageService: LU Not Found** (40020)
</dt> <dt>

**StorageService: Max Map Count for LU Exceeded** (40025)
</dt> <dt>

**StorageService: Client Should not specify DeviceNumbers for this Array** (40030)
</dt> <dt>

**StorageService: DeviceNumbers Array Size not equal to LUNames Array Size** (40035)
</dt> <dt>

**StorageService: DeviceNumbers Array contains invalid numbers - Acceptable range is 0-254** (40036)
</dt> <dt>

**StorageService: InitiatorID and TargetPortID Combination is associated to another StorageGroup(s);First One is Returned** (40040)
</dt> <dt>

**StorageService: Success, But Multiple StorageGroups (SPCs) Created. First One Returned** (40045)
</dt> <dt>

**StorageService: Success, But Unable To Update StorageGroup (SPC) Name** (40050)
</dt> <dt>

**StorageService: Unable To Wait For Job Completion** (40055)
</dt> <dt>

**StorageService: Unable To Get StroageGroup (SPC) From Job** (40060)
</dt> <dt>

**StorageService: Unable To Get MaskingGroup From Job** (40061)
</dt> <dt>

**StorageService: Success, But Unable to set SPC Name. StorageGroup Name is Already in Use** (40090)
</dt> <dt>

**StorageService: Success, But ElementName Is Not Settable Per Provider's capabilities** (40095)
</dt> <dt>

**StorageService: Provider does not support masking and mapping operations** (40107)
</dt> <dt>

**StorageService: SPC already exists** (40110)
</dt> <dt>

**StorageService: Unable to Find or Create a StorageHardwareID Object on the provider** (40115)
</dt> <dt>

**StorageService: Unable to Find the StorageVolume Object(s) on the provider** (40116)
</dt> <dt>

**StorageService: Unable to Find a TargetMaskingGroup that contains all the provided TargetPorts** (40117)
</dt> <dt>

**StorageService: Failed to Find a TargetMaskingGroup that contains all the provided TargetPorts** (40118)
</dt> <dt>

**StorageService: Warning StorageClientSettingData Not Supported on provider** (40300)
</dt> <dt>

**StorageService: Error processing of StorageClientSettingData** (40700)
</dt> <dt>

**StorageService: Error StorageClientSettingData specified HostType was Not Found** (40701)
</dt> <dt>

**StorageService: Warning StorageClientSettingData HostType Not Found. Other or Standard HostType was used instead** (40702)
</dt> <dt>

**StorageService: Error StorageClientSettingData not found for the specified HardwareId** (40703)
</dt> <dt>

**StorageService: Error StorageClientSettingData provider failure** (40704)
</dt> <dt>

**StorageService: Method invocation failed** (40705)
</dt> <dt>

**StorageService: Error: Provider job completed with errors** (41000)
</dt> <dt>

**StorageService CIM Error: Failed** (43001)
</dt> <dt>

**StorageService CIM Error: Access denied** (43002)
</dt> <dt>

**StorageService CIM Error: Invalid namespace** (43003)
</dt> <dt>

**StorageService CIM Error: Invalid parameter** (43004)
</dt> <dt>

**StorageService CIM Error: Invalid class** (43005)
</dt> <dt>

**StorageService CIM Error: Not found** (43006)
</dt> <dt>

**StorageService CIM Error: Not supported** (43007)
</dt> <dt>

**StorageService CIM Error: Class has children** (43008)
</dt> <dt>

**StorageService CIM Error: Class has instances** (43009)
</dt> <dt>

**StorageService CIM Error: Invalid superclass** (43010)
</dt> <dt>

**StorageService CIM Error: Already exists** (43011)
</dt> <dt>

**StorageService CIM Error: No such property** (43012)
</dt> <dt>

**StorageService CIM Error: Type mismatch** (43013)
</dt> <dt>

**StorageService CIM Error: Query language not supported** (43014)
</dt> <dt>

**StorageService CIM Error: Invalid query** (43015)
</dt> <dt>

**StorageService CIM Error: Method not available** (43016)
</dt> <dt>

**StorageService CIM Error: Method not found** (43017)
</dt> <dt>

**StorageService CIM Error: Unexpected response** (43018)
</dt> <dt>

**StorageService CIM Error: Invalid response destination** (43019)
</dt> <dt>

**StorageService CIM Error: Namespace not empty** (43020)
</dt> <dt>

**StorageService CIM Error: Invalid enumeration context** (43021)
</dt> <dt>

**StorageService CIM Error: Invalid operation timeout** (43022)
</dt> <dt>

**StorageService CIM Error: Pull has been abandoned** (43023)
</dt> <dt>

**StorageService CIM Error: Pull cannot be abandoned** (43024)
</dt> <dt>

**StorageService CIM Error: Filtered enumeration not supported** (43025)
</dt> <dt>

**StorageService CIM Error: Continuation on error not supported** (43026)
</dt> <dt>

**StorageService CIM Error: Server limits exceeded** (43027)
</dt> <dt>

**StorageService CIM Error: Server is shutting down** (43028)
</dt> <dt>

**StorageService CIM Error: Query feature not supported** (43029)
</dt> <dt>

**StorageService: Generic Failure** (51000)
</dt> <dt>

**StorageService: Invalid connection credentials** (51005)
</dt> <dt>

**StorageService: SSL connection failure** (51010)
</dt> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMSystem**](msft-smsystem.md)
</dt> </dl>

 

 






---
title: AddInitiators method of the MSFT\_SMStorageGroup class
description: Adds initiator IDs to a storage group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a8c8099e-2806-46c0-943d-5157334cd2d7
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddInitiators method
- AddInitiators method, MSFT_SMStorageGroup class
- MSFT_SMStorageGroup class, AddInitiators method
topic_type:
- apiref
api_name:
- MSFT_SMStorageGroup.AddInitiators
api_location:
- StorageService.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddInitiators method of the MSFT\_SMStorageGroup class

Adds initiator IDs to a storage group.

## Syntax


```mof
Uint32 AddInitiators(
  [in]            String                InitiatorIDs[],
  [in, optional]  Uint16                HostType,
  [in, optional]  String                username,
  [in, optional]  String                password,
  [out]           MSFT_SMJob        REF Job,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*InitiatorIDs* \[in\]
</dt> <dd>

Identifiers of initiator ports.

</dd> <dt>

*HostType* \[in, optional\]
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


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*username* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the [**MSFT\_SMJob**](msft-smjob.md) instance. May be **NULL** if the job is completed.

**Windows Server 2012:** This parameter is not supported.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object containing the results of calling this method.

</dd> </dl>

## Return value

<dl> <dt>

**Success**
</dt> <dd>

0

</dd> <dt>

**Not Supported**
</dt> <dd>

1

</dd> <dt>

**Unspecified Error**
</dt> <dd>

2

</dd> <dt>

**Timeout**
</dt> <dd>

3

</dd> <dt>

**Failed**
</dt> <dd>

4

</dd> <dt>

**Invalid Parameter**
</dt> <dd>

5

</dd> <dt>

**Method Parameters Checked - Job Started**
</dt> <dd>

4096

**Windows Server 2012:** This value is unavailable prior to Windows Server 2012 R2.

</dd> <dt>

**Invalid initiator port ID**
</dt> <dd>

4098

</dd> <dt>

**Invalid permission**
</dt> <dd>

4100

</dd> <dt>

**Target/initiator combination already exposed**
</dt> <dd>

4101

</dd> <dt>

**StorageService: Error InitiatorID Required**
</dt> <dd>

40005

</dd> <dt>

**StorageService: Not Unique InitiatorID and TargetPortID Combination**
</dt> <dd>

40040

</dd> <dt>

**StorageService: Unable to get MaskingGroup from job**
</dt> <dd>

40061

</dd> <dt>

**StorageService: Error Unable to add InitiatorID - OneHardwareIDPerView is set to true**
</dt> <dd>

40065

</dd> <dt>

**StorageService: Provider does not support masking and mapping operations**
</dt> <dd>

40107

</dd> <dt>

**StorageService: More than one MaskingGroup of the same type are associated with the SPC on the Provider**
</dt> <dd>

40111

</dd> <dt>

**StorageService: Unable to Find or Create a StorageHardwareID Object on the provider**
</dt> <dd>

40115

</dd> <dt>

**StorageService: Warning StorageClientSettingData Not Supported on provider**
</dt> <dd>

40300

</dd> <dt>

**StorageService: Error processing of StorageClientSettingData**
</dt> <dd>

40700

</dd> <dt>

**StorageService: Error StorageClientSettingData specified HostType was Not Found**
</dt> <dd>

40701

</dd> <dt>

**StorageService: Warning StorageClientSettingData HostType Not Found. Other or Standard HostType was used instead**
</dt> <dd>

40702

</dd> <dt>

**StorageService: Error StorageClientSettingData not found for the specified HardwareId**
</dt> <dd>

40703

</dd> <dt>

**StorageService: Error StorageClientSettingData provider failure**
</dt> <dd>

40704

</dd> <dt>

**StorageService: Method invocation failed**
</dt> <dd>

40705

</dd> <dt>

**StorageService: Error: Provider job completed with errors**
</dt> <dd>

41000

</dd> <dt>

**StorageService CIM Error: Failed**
</dt> <dd>

43001

</dd> <dt>

**StorageService CIM Error: Access denied**
</dt> <dd>

43002

</dd> <dt>

**StorageService CIM Error: Invalid namespace**
</dt> <dd>

43003

</dd> <dt>

**StorageService CIM Error: Invalid parameter**
</dt> <dd>

43004

</dd> <dt>

**StorageService CIM Error: Invalid class**
</dt> <dd>

43005

</dd> <dt>

**StorageService CIM Error: Not found**
</dt> <dd>

43006

</dd> <dt>

**StorageService CIM Error: Not supported**
</dt> <dd>

43007

</dd> <dt>

**StorageService CIM Error: Class has children**
</dt> <dd>

43008

</dd> <dt>

**StorageService CIM Error: Class has instances**
</dt> <dd>

43009

</dd> <dt>

**StorageService CIM Error: Invalid superclass**
</dt> <dd>

43010

</dd> <dt>

**StorageService CIM Error: Already exists**
</dt> <dd>

43011

</dd> <dt>

**StorageService CIM Error: No such property**
</dt> <dd>

43012

</dd> <dt>

**StorageService CIM Error: Type mismatch**
</dt> <dd>

43013

</dd> <dt>

**StorageService CIM Error: Query language not supported**
</dt> <dd>

43014

</dd> <dt>

**StorageService CIM Error: Invalid query**
</dt> <dd>

43015

</dd> <dt>

**StorageService CIM Error: Method not available**
</dt> <dd>

43016

</dd> <dt>

**StorageService CIM Error: Method not found**
</dt> <dd>

43017

</dd> <dt>

**StorageService CIM Error: Unexpected response**
</dt> <dd>

43018

</dd> <dt>

**StorageService CIM Error: Invalid response destination**
</dt> <dd>

43019

</dd> <dt>

**StorageService CIM Error: Namespace not empty**
</dt> <dd>

43020

</dd> <dt>

**StorageService CIM Error: Invalid enumeration context**
</dt> <dd>

43021

</dd> <dt>

**StorageService CIM Error: Invalid operation timeout**
</dt> <dd>

43022

</dd> <dt>

**StorageService CIM Error: Pull has been abandoned**
</dt> <dd>

43023

</dd> <dt>

**StorageService CIM Error: Pull cannot be abandoned**
</dt> <dd>

43024

</dd> <dt>

**StorageService CIM Error: Filtered enumeration not supported**
</dt> <dd>

43025

</dd> <dt>

**StorageService CIM Error: Continuation on error not supported**
</dt> <dd>

43026

</dd> <dt>

**StorageService CIM Error: Server limits exceeded**
</dt> <dd>

43027

</dd> <dt>

**StorageService CIM Error: Server is shutting down**
</dt> <dd>

43028

</dd> <dt>

**StorageService CIM Error: Query feature not supported**
</dt> <dd>

43029

</dd> <dt>

**StorageService: Generic Failure**
</dt> <dd>

51000

</dd> <dt>

**StorageService: Invalid connection credentials**
</dt> <dd>

51005

</dd> <dt>

**StorageService: SSL connection failure**
</dt> <dd>

51010

</dd> </dl>

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

[**MSFT\_SMStorageGroup**](msft-smstoragegroup.md)
</dt> </dl>

 

 






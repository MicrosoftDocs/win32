---
title: GetProvisioningProperties method of the Win32_RDMSCollectionProperties class
description: Retrieves the provisioning properties of the virtual desktop collection.
ms.assetid: c314b7a5-8546-4711-833e-b47bb682aa53
ms.tgt_platform: multiple
keywords:
- GetProvisioningProperties method Remote Desktop Services
- GetProvisioningProperties method Remote Desktop Services , Win32_RDMSCollectionProperties class
- Win32_RDMSCollectionProperties class Remote Desktop Services , GetProvisioningProperties method
topic_type:
- apiref
api_name:
- Win32_RDMSCollectionProperties.GetProvisioningProperties
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetProvisioningProperties method of the Win32\_RDMSCollectionProperties class

Retrieves the provisioning properties of the virtual desktop collection.

## Syntax


```mof
uint32 GetProvisioningProperties(
  [out] string  PoolVhdType,
  [out] string  MasterVmLocation,
  [out] string  NamePrefix,
  [out] uint32  NameStartIndex,
  [out] string  LocalVmLocation,
  [out] string  LocalGoldVmLocation,
  [out] boolean RunFromSMB,
  [out] string  SMBLocation,
  [out] boolean SMBStreaming,
  [out] string  VmDomain,
  [out] string  VmOU,
  [out] string  ProductKey
);
```



## Parameters

<dl> <dt>

*PoolVhdType* \[out\]
</dt> <dd>

Specifies the VHD (virtual hard disk) format of the virtual machine pool in the collection.

<dt>

Clone
</dt> <dd>

A cloned VHD.

</dd> <dt>

DiffDisk
</dt> <dd>

A differencing VHD.

</dd> </dl> </dd> <dt>

*MasterVmLocation* \[out\]
</dt> <dd>

Receives the path to the master VM image.

</dd> <dt>

*NamePrefix* \[out\]
</dt> <dd>

Receives the name prefix to append to the beginning of virtual machine names.

</dd> <dt>

*NameStartIndex* \[out\]
</dt> <dd>

Start index.

</dd> <dt>

*LocalVmLocation* \[out\]
</dt> <dd>

Receives the local path to the virtual machines on the Hyper-V servers. If this parameter is set to **NULL** or if it is empty, the default virtual machine directory will be used.

</dd> <dt>

*LocalGoldVmLocation* \[out\]
</dt> <dd>

Receives the local path to the golden VHD image when the *PoolVhdTpe* parameter is set to "DiffDisk". If this parameter is set to **NULL** or if it is empty, the default virtual machine directory will be used.

</dd> <dt>

*RunFromSMB* \[out\]
</dt> <dd>

Receives a value that indicates whether to run the collection from an Server Message Block (SMB) share. **TRUE** to run the virtual machines from an SBM share; otherwise; **FALSE**.

</dd> <dt>

*SMBLocation* \[out\]
</dt> <dd>

Receives the path to the SMB share if SMB sharing is enabled.

</dd> <dt>

*SMBStreaming* \[out\]
</dt> <dd>

Receives a value that indicates whether SMB streaming is enabled. **TRUE** if SMB sharing is enabled; otherwise; **FALSE**.

</dd> <dt>

*VmDomain* \[out\]
</dt> <dd>

Receives the domain name of the virtual machines in the collection.

</dd> <dt>

*VmOU* \[out\]
</dt> <dd>

Receives the Active Directory organization unit (OU) of the virtual machines in the collection.

</dd> <dt>

*ProductKey* \[out\]
</dt> <dd>

Receives the OS product keys for the virtual machines in the collection.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSCollectionProperties**](win32-rdmscollectionproperties.md)
</dt> </dl>

 

 






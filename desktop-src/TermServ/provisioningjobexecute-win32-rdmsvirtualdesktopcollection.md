---
title: ProvisioningJobExecute method of the Win32_RDMSVirtualDesktopCollection class
description: Runs a virtual desktop provisioning job.
ms.assetid: 69f0cc6a-7eef-4cd9-94ac-f0c7e52d02d8
ms.tgt_platform: multiple
keywords:
- ProvisioningJobExecute method Remote Desktop Services
- ProvisioningJobExecute method Remote Desktop Services , Win32_RDMSVirtualDesktopCollection class
- Win32_RDMSVirtualDesktopCollection class Remote Desktop Services , ProvisioningJobExecute method
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktopCollection.ProvisioningJobExecute
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ProvisioningJobExecute method of the Win32\_RDMSVirtualDesktopCollection class

Runs a virtual desktop provisioning job.

## Syntax


```mof
uint32 ProvisioningJobExecute(
  [in]  string JobInputXml,
  [out] string JobGuid
);
```



## Parameters

<dl> <dt>

*JobInputXml* \[in\]
</dt> <dd>

A string that contains the provisioning information in XML format.

</dd> <dt>

*JobGuid* \[out\]
</dt> <dd>

The **GUID** that uniquely identifies the provisioning job to run.

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

[**Win32\_RDMSVirtualDesktopCollection**](win32-rdmsvirtualdesktopcollection.md)
</dt> </dl>

 

 






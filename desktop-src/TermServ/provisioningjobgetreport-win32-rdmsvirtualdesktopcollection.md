---
title: ProvisioningJobGetReport method of the Win32_RDMSVirtualDesktopCollection class
description: Gets a report about the status of a virtual desktop provisioning job.
ms.assetid: 8fc03fed-0838-4530-9b0f-0f561d76769d
ms.tgt_platform: multiple
keywords:
- ProvisioningJobGetReport method Remote Desktop Services
- ProvisioningJobGetReport method Remote Desktop Services , Win32_RDMSVirtualDesktopCollection class
- Win32_RDMSVirtualDesktopCollection class Remote Desktop Services , ProvisioningJobGetReport method
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktopCollection.ProvisioningJobGetReport
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ProvisioningJobGetReport method of the Win32\_RDMSVirtualDesktopCollection class

Gets a report about the status of a virtual desktop provisioning job.

## Syntax


```mof
uint32 ProvisioningJobGetReport(
  [in]  string JobGuid,
  [out] string JobReportXml
);
```



## Parameters

<dl> <dt>

*JobGuid* \[in\]
</dt> <dd>

The **GUID** that uniquely identifies the provisioning job.

</dd> <dt>

*JobReportXml* \[out\]
</dt> <dd>

A string that contains the report in XML format.

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

 

 






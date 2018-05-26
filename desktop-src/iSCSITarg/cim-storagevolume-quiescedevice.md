---
title: QuiesceDevice method of the CIM\_StorageVolume class
description: The QuiesceDevice method has been deprecated in lieu of the more general RequestStateChange method that directly overlaps with the functionality provided by this method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5995b92c-0ca6-44ca-a343-0cd43d717b65
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- QuiesceDevice method iSCSI Software Target API
- QuiesceDevice method iSCSI Software Target API , CIM_StorageVolume class
- CIM_StorageVolume class iSCSI Software Target API , QuiesceDevice method
topic_type:
- apiref
api_name:
- CIM_StorageVolume.QuiesceDevice
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# QuiesceDevice method of the CIM\_StorageVolume class

The QuiesceDevice method has been deprecated in lieu of the more general RequestStateChange method that directly overlaps with the functionality provided by this method. Requests that the LogicalDevice cleanly cease all current activity ("Quiesce" input parameter = TRUE) or resume activity (= FALSE). For this method to quiesce a Device, that Device should have an Availability (or Additional Availability) of "Running/Full Power" (value=3) and an EnabledStatus/StatusInfo of "Enabled". For example, if quiesced, a Device may then be offlined for diagnostics, or disabled for power off and hot swap. For the method to "unquiesce" a Device, that Device should have an Availability (or AdditionalAvailability) of "Quiesced" (value=21) and an EnabledStatus/StatusInfo of "Enabled". In this case, the Device would be returned to an "Enabled" and "Running/Full Power" status. The method's return code should indicate the success or failure of the quiesce. It should return 0 if successful, 1 if the request is not supported at all, 2 if the request is not supported due to the current state of the Device, and some other value if any other error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' may also be specified in the subclass as a Values array qualifier.

## Syntax


```mof
uint32 QuiesceDevice(
  [in] boolean Quiesce
);
```



## Parameters

<dl> <dt>

*Quiesce* \[in\]
</dt> <dd>

If set to TRUE then cleanly cease all activity, if FALSE resume activity.

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StorageVolume**](cim-storagevolume.md)
</dt> </dl>

 

 






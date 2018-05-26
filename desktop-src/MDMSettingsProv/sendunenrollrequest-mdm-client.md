---
title: SendUnenrollRequest method of the MDM\_Client class
description: Unenrolls the device.
ms.assetid: 06023653-d7b7-446a-97bc-db5435de0313
keywords:
- SendUnenrollRequest method MDM Settings
- SendUnenrollRequest method MDM Settings , MDM_Client class
- MDM_Client class MDM Settings , SendUnenrollRequest method
topic_type:
- apiref
api_name:
- MDM_Client.SendUnenrollRequest
api_location:
- MDMSettingsProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SendUnenrollRequest method of the MDM\_Client class

Unenrolls the device.

## Syntax


```mof
uint32 SendUnenrollRequest(
  [in] string DeviceClientID
);
```



## Parameters

<dl> <dt>

*DeviceClientID* \[in\]
</dt> <dd>

The Id of the device.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MDM\_Client**](https://msdn.microsoft.com/library/dn610387)
</dt> </dl>

 

 






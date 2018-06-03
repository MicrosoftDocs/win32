---
title: SetVLActivationInterval method of the SoftwareLicensingService class
description: The activation frequency, in minutes, of how often the current machine should contact the key management service machine before the client is licensed.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f6f34365-b988-42ee-97b3-41ec6688f03e
keywords:
- SetVLActivationInterval method Windows Management Instrumentation
- SetVLActivationInterval method Windows Management Instrumentation , SoftwareLicensingService class
- SoftwareLicensingService class Windows Management Instrumentation , SetVLActivationInterval method
topic_type:
- apiref
api_name:
- SoftwareLicensingService.SetVLActivationInterval
api_location:
- SppWmi.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetVLActivationInterval method of the SoftwareLicensingService class

The activation frequency, in minutes, of how often the current machine should contact the key management service machine before the client is licensed. The frequency must be greater than or equal to 15 and less than or equal to 43200. An error is returned if the method is called and the machine is not a key management service.

## Syntax


```mof
uint32 SetVLActivationInterval(
  [in] uint32 ActivationInterval
);
```



## Parameters

<dl> <dt>

*ActivationInterval* \[in\]
</dt> <dd>

Specifies the activation interval in minutes.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                     |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>SppWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SppWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**SoftwareLicensingService**](softwarelicensingservice.md)
</dt> </dl>

 

 






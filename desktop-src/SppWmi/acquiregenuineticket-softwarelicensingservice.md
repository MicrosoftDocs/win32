---
title: AcquireGenuineTicket method of the SoftwareLicensingService class
description: Acquires a genuine ticket online.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 54aedc49-c49f-46df-b51a-a29824075aff
keywords:
- AcquireGenuineTicket method Windows Management Instrumentation
- AcquireGenuineTicket method Windows Management Instrumentation , SoftwareLicensingService class
- SoftwareLicensingService class Windows Management Instrumentation , AcquireGenuineTicket method
topic_type:
- apiref
api_name:
- SoftwareLicensingService.AcquireGenuineTicket
api_location:
- SppWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AcquireGenuineTicket method of the SoftwareLicensingService class

Acquires a genuine ticket online.

## Syntax


```mof
uint32 AcquireGenuineTicket(
  [in] string TemplateId,
  [in] string ServerUrl
);
```



## Parameters

<dl> <dt>

*TemplateId* \[in\]
</dt> <dd>

Specifies the template ID.

</dd> <dt>

*ServerUrl* \[in\]
</dt> <dd>

Specifies the server URL.

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

 

 






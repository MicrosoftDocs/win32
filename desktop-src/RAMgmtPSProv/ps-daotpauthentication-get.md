---
title: Get method of the PS\_DAOtpAuthentication class
description: Displays the OTP authentication settings for DirectAccess.
audience: developer
ms.assetid: 9f6e856f-b8e7-4646-9265-8350db4ab26a
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DAOtpAuthentication class
- PS_DAOtpAuthentication class, Get method
topic_type:
- apiref
api_name:
- PS_DAOtpAuthentication.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DAOtpAuthentication class

Displays the OTP authentication settings for DirectAccess.

## Syntax


```mof
uint32 Get(
  [in]  string              ComputerName,
  [out] DAOtpAuthentication cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the name or IP address of the server on which the cmdlet should run.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**DAOtpAuthentication**](daotpauthentication.md) that contains the OTP authentication settings.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DAOtpAuthentication**](ps-daotpauthentication.md)
</dt> </dl>

 

 






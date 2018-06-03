---
title: Disable method of the PS\_DAOtpAuthentication class
description: Disables OTP authentication for DirectAccess users.
audience: developer
ms.assetid: 39608899-ba1d-40f6-a70a-48c811b23b88
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Disable method
- Disable method, PS_DAOtpAuthentication class
- PS_DAOtpAuthentication class, Disable method
topic_type:
- apiref
api_name:
- PS_DAOtpAuthentication.Disable
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Disable method of the PS\_DAOtpAuthentication class

Disables OTP authentication for DirectAccess users.

## Syntax


```mof
uint32 Disable(
  [in]  string              ComputerName,
  [in]  boolean             Force,
  [in]  boolean             PassThru,
  [out] DAOtpAuthentication cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the name or IP address of the server on which the cmdlet should run.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Turns off the option that allows a user to confirm or cancel an action initiated by the cmdlet.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the DAOtpAuthentication object that contains OTP authentication configuration settings for DirectAccess.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An [**DAOtpAuthentication**](daotpauthentication.md) that contains the OTP authentication configuration settings.

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

 

 






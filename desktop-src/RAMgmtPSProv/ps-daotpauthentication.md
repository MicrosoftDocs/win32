---
title: PS\_DAOtpAuthentication class
description: Describes the OTP authentication configuration for DirectAccess.
audience: developer
ms.assetid: 888948b5-0348-4809-98b2-afa33bc56150
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DAOtpAuthentication class
- PS_DAOtpAuthentication class, described
topic_type:
- apiref
api_name:
- PS_DAOtpAuthentication
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DAOtpAuthentication class

Describes the OTP authentication configuration for DirectAccess.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_DAOtpAuthentication
{
};
```

## Members

The **PS\_DAOtpAuthentication** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DAOtpAuthentication** class has these methods.



| Method                                            | Description                                                                  |
|:--------------------------------------------------|:-----------------------------------------------------------------------------|
| [**Disable**](ps-daotpauthentication-disable.md) | Disables OTP authentication for DirectAccess users.<br/>               |
| [**Enable**](ps-daotpauthentication-enable.md)   | Enables and configures OTP authentication for DirectAccess users.<br/> |
| [**Get**](ps-daotpauthentication-get.md)         | Displays OTP authentication settings for DirectAccess.<br/>            |
| [**Set**](ps-daotpauthentication-set.md)         | Configures OTP authentication settings for DirectAccess.<br/>          |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 






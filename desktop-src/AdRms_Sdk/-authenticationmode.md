---
Description: Specifies the authentication method to be applied by an Active Directory Rights Management Services (AD RMS) server to a user account.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 54833034-ea1c-4748-b0e1-618ded0d45d0
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AuthenticationMode enumeration
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# AuthenticationMode enumeration

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **AuthenticationMode** enumeration type specifies the authentication method to be applied by an Active Directory Rights Management Services (AD RMS) server to a user account. This enumeration is used by the [**Identification**](-identification.md) object to specify the type of authentication used in the [**PreCertify**](-precertify.md) SOAP web method.


```CSharp
public enum AuthenticationMode
```



## Members



| Member         | Description                                                                | Value |
|----------------|----------------------------------------------------------------------------|-------|
| **Windows**    | Use Windows authentication.<br/>                                     | 0     |
| **Federation** | Use Active Directory Federation Services (ADFS) authentication.<br/> | 1     |



## Requirements



|                    |                                                        |
|--------------------|--------------------------------------------------------|
| Product<br/> | Rights Management Services 1.0 SP2 or later<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Data Types](ad-rms-soap-data-types.md)
</dt> <dt>

[**PreCertify**](-precertify.md)
</dt> <dt>

[**PrecertifyParams**](-precertifyparams.md)
</dt> <dt>

[**PrecertifyResponse**](-precertifyresponse.md)
</dt> </dl>

 

 





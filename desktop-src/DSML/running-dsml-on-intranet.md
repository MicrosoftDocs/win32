---
title: Running DSML Services for Windows on an Intranet
description: In a corporate environment that uses a Windows operating system, you can usually log on to the corporate network one time and then access system resources, including webpages, without giving your credentials again.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f03bba79-0a95-4dc2-8668-17d914874588
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Running DSML Services for Windows on an Intranet DSML
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Running DSML Services for Windows on an Intranet

In a corporate environment that uses a Windows operating system, you can usually log on to the corporate network one time and then access system resources, including webpages, without giving your credentials again. DSML Services for Windows also requires you to log on only one time because it uses the Windows authentication process to verify user access.

![dsml services for windows configured for integrated windows authentication](images/production-computers-3.png)

In an intranet scenario, the IIS server that hosts DSML Services for Windows will usually have its security settings configured for integrated Windows authentication.

DSML clients are not required to pass credentials if the user logs on to the Active Directory forest where DSML Services for Windows resides.

## Accessing DSML Services for Windows

The following Visual Basic code examples show how clients access DSML Services for Windows across an intranet.


```VB
set xmlhttp = CreateObject("Msxml2.XMLHTTP")
xmlhttp.open "POST", "https://fabrikam.com/dsml/adssoap.dsmlx", false, userName, password
```



The following C# code examples show how clients access DSML Services for Windows across an intranet.


```CSharp
Uri site = new Uri("https://fabrikam.com/dsml/adssoap.dsmlx");
WebRequest wReq = WebRequest.Create(site);

wReq.Credentials = CredentialCache.DefaultCredentials;
```



## Restrictions

If NTLM is chosen during the authentication negotiation, IIS and Active Directory must each be installed on the same computer. Kerberos delegation must be enabled if the client, IIS, and Active Directory are all installed on different computers.

If using separate computers for Active Directory and IIS is a requirement, but Kerberos delegation is not an option, you can configure DSML Services for Windows with basic authentication. This configuration will give DSML Services for Windows access to Active Directory, but you will not get the benefits of integrated authentication.

 

 





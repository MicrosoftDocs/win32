---
title: PS\_RemoteAccessLocal class
description: Represents the server provider functions.
audience: developer
ms.assetid: a728539b-85f6-4f37-a8b4-032025b9d951
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_RemoteAccessLocal class
- PS_RemoteAccessLocal class, described
topic_type:
- apiref
api_name:
- PS_RemoteAccessLocal
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_RemoteAccessLocal class

Represents the server provider functions.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class PS_RemoteAccessLocal
{
};
```

## Members

The **PS\_RemoteAccessLocal** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessLocal** class has these methods.



| Method                                                                                          | Description                                                                                                                                                                              |
|:------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CheckInterfaces**](checkinterfaces-ps-remoteaccesslocal.md)                                 | This method validates the interfaces that are passed here are of profile what they say they are.<br/>                                                                              |
| [**CheckServerPreRequisites**](checkserverprerequisites-ps-remoteaccesslocal.md)               | This method checks all the pre-requisites on the DA server itself.<br/>                                                                                                            |
| [**CreateSelfSignedCertificate**](createselfsignedcertificate-ps-remoteaccesslocal.md)         | This method creates a self signed certificate.<br/>                                                                                                                                |
| [**EnableFirewallGroup**](enablefirewallgroup-ps-remoteaccesslocal.md)                         | This method enables the firewall group.<br/>                                                                                                                                       |
| [**EnrollWebServerCertificate**](enrollwebservercertificate-ps-remoteaccesslocal.md)           | This method enrolls a web server certificate.<br/>                                                                                                                                 |
| [**FindNLSCertificate**](findnlscertificate-ps-remoteaccesslocal.md)                           | This method retrieves a Certificate for NLS from the local machine whose subject name does not match the ConnectTo addresses, but resolves to at least one IP from each site.<br/> |
| [**GetConfigurationVersion**](getconfigurationversion-ps-remoteaccesslocal.md)                 | This method gets the server Gpo version information.<br/>                                                                                                                          |
| [**GetCorpPrefix**](getcorpprefix-ps-remoteaccesslocal.md)                                     | This method gets the Corp Prefix configuration.<br/>                                                                                                                               |
| [**GetDACertificateFromRawData**](getdacertificatefromrawdata-ps-remoteaccesslocal.md)         | This method retrieves a Certificate from the local machine which matches the input raw data.<br/>                                                                                  |
| [**GetDACertificateFromSubjectName**](getdacertificatefromsubjectname-ps-remoteaccesslocal.md) | This method retrieves a Certificate from the local machine which matches the specified subject name.<br/>                                                                          |
| [**GetInterfaces**](getinterfaces-ps-remoteaccesslocal.md)                                     | This method gives the Internet and intranet interfaces.<br/>                                                                                                                       |
| [**GetValidDACertificates**](getvaliddacertificates-ps-remoteaccesslocal.md)                   | This method retrieves a list of certificates for DirectAccess based on the purpose specified.<br/>                                                                                 |
| [**SetSSTPCertificate**](ps-remoteaccesslocal-setsstpcertificate.md)                           | This method is used to set the SSTP certificate on the RemoteAccess server.<br/>                                                                                                   |
| [**SetVpnPorts**](setvpnports-ps-remoteaccesslocal.md)                                         | This method sets the ports required by VPN to the default values based on the whether Vpn and/or site-to-site Vpn are enabled.<br/>                                                |
| [**Sync**](sync-ps-remoteaccesslocal.md)                                                       | This method will trigger the process to synchronize the DA server with the Group Policy.<br/>                                                                                      |



 

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 






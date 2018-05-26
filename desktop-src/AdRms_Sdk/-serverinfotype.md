---
Description: Specifies the type of server information retrieved when you call the GetServerInfo method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 9a644e5a-dbcb-4c53-b696-4a9c7a25e9c7
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ServerInfoType enumeration
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
---

# ServerInfoType enumeration

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **ServerInfoType** enumeration specifies the type of server information retrieved when you call the [**GetServerInfo**](-getserverinfo.md) method. This enumeration is used directly by the [**ServerInfoRequest**](-serverinforequest.md) class.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 


```CSharp
public enum ServerInfoType
```



## Members



| Member                        | Description                                                     |
|-------------------------------|-----------------------------------------------------------------|
| **VersionInfo**               | Retrieves information about the server version.<br/>      |
| **ServerFeatureInfo**         | Retrieves the features supported by the server.<br/>      |
| **ServerLicensorCertificate** | Retrieves the server licensor certificate.<br/>           |
| **ServiceLocations**          | Retrieves the known service location for the server.<br/> |



## Web Service Description Page

*ServerURL*/\_wmcs/Certification/Server.asmx?wsdl

## Remarks

The actual structure of the SOAP type varies from language to language. To obtain the structure of the type, query the web service description page.

## Requirements



|                    |                                                        |
|--------------------|--------------------------------------------------------|
| Product<br/> | Rights Management Services 1.0 SP2 or later<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Data Types](ad-rms-soap-data-types.md)
</dt> </dl>

 

 





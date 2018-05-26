---
Description: Defines a property that you can use to specify the type of server information to retrieve when you call the GetServerInfo method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e533c456-b1ce-4a38-84bc-aa077a0fc8df
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ServerInfoRequest class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ServerInfoRequest class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **ServerInfoRequest** class defines a property that you can use to specify the type of server information to retrieve when you call the [**GetServerInfo**](-getserverinfo.md) method.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **ServerInfoRequest** class is derived from **System.Object**.

## Members

### Properties

The **ServerInfoRequest** class has these properties.



| Property                                             | Access type           | Description                                                                                                                       |
|:-----------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| **AdditionalInfo**<br/>                        | Read/write<br/> | This property is reserved for future use.<br/>                                                                              |
| [**ServerInfoType**](-serverinfotype.md)<br/> | Read/write<br/> | A value of the [**ServerInfoType**](-serverinfotype.md) enumeration that specifies the type of information to return.<br/> |



 

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

 

 





---
Description: Specifies the version of AD RMS required by the client and the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e190f57e-67db-4644-9b12-b87a6e7d9b39
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: VersionData class
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# VersionData class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **VersionData** SOAP data type specifies the version of AD RMS required by the client and the server.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **VersionData** class is derived from **SoapHeader**.

## Members

### Properties

The **VersionData** class has these properties.



| Property                      | Access type           | Description                                                                                                                                           |
|:------------------------------|:----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MaximumVersion**<br/> | Read/write<br/> | The maximum version required or understood by the sending party, using the format *a.b.c.d* where a, b, c, and d are nonnegative integers.<br/> |
| **MinimumVersion**<br/> | Read/write<br/> | The minimum version required or understood by the sending party, using the format *a.b.c.d* where a, b, c, and d are nonnegative integers.<br/> |



 

## Web Service Description Page

*ServerURL*/\_wmcs/Licensing/License.asmx?wsdl

## Remarks

When the client sends this value, it specifies the minimum and maximum AD RMS versions that it requires. When the server sends this value, it specifies the AD RMS version compatibility the client must have to continue.

The actual structure of the SOAP type varies from language to language. This structure is defined in the .wsdl page of every SOAP method.

## Requirements



|                    |                                                        |
|--------------------|--------------------------------------------------------|
| Product<br/> | Rights Management Services 1.0 SP2 or later<br/> |



## See also

<dl> <dt>

[SoapHeader](https://msdn.microsoft.com/library/system.web.services.protocols.soapheader.aspx)
</dt> <dt>

[AD RMS SOAP Data Types](ad-rms-soap-data-types.md)
</dt> </dl>

 

 





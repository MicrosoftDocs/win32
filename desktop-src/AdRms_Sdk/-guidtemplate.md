---
Description: Represents a template stored on an AD RMS server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 550cf7bc-17f4-468d-ade2-8974e09e8e03
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: GuidTemplate class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# GuidTemplate class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **GuidTemplate** class represents a template stored on an AD RMS server. An array of these objects is returned by the [**AcquireTemplates**](-acquiretemplates.md) method.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **GuidTemplate** class is derived from **System.Object**.

## Members

## Fields

The **GuidTemplate** class has the following fields.



| Field        | Description                                                                                                                                                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Guid**     | Data type: **String**<br/> A string value that contains a **GUID** for a template.<br/>                                                                                                                                                    |
| **Hash**     | Data type: **String**<br/> A string value that contains a hash of the template. The hash is used by AD RMS to determine whether a template has changed after it was last retrieved. If it has not changed, it will not be downloaded.<br/> |
| **Template** | Data type: **String**<br/> A string that contains the template in XML format.<br/>                                                                                                                                                         |



 

## Web Service Description Page

*ServerURL*/\_wmcs/Licensing/TemplateDistribution.asmx?wsdl

## Remarks

The actual structure of the SOAP type varies from language to language. To obtain the structure of the type, query the web service description page.

You can call the [**AcquireTemplateInformation**](-acquiretemplateinformation.md) method to retrieve a [**TemplateInformation**](-templateinformation.md) object, and you can call the [**AcquireTemplates**](-acquiretemplates.md) method to retrieve an array of active templates from the AD RMS server.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Data Types](ad-rms-soap-data-types.md)
</dt> <dt>

[**AcquireTemplateInformation**](-acquiretemplateinformation.md)
</dt> <dt>

[**AcquireTemplates**](-acquiretemplates.md)
</dt> </dl>

 

 





---
Description: Contains a GUID for an AD RMS template and a hash of the template identified by the GUID.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d25ad762-90b0-4dc1-9f78-b427a62a085b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: GuidHash class
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# GuidHash class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **GuidHash** class contains a GUID for an AD RMS template and a hash of the template identified by the GUID. This object is used by the [**TemplateInformation**](-templateinformation.md) object.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **GuidHash** class is derived from **System.Object**.

## Members

## Fields

The **GuidHash** class has the following fields.



| Field    | Description                                                                                                                                                                                                                                                                             |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Guid** | Data type: **String**<br/> A string value that contains the **GUID**.<br/>                                                                                                                                                                                                  |
| **Hash** | Data type: **String**<br/> A string value that contains a hash of the template identified by the **Guid** field. The hash is used by AD RMS to determine whether a template has changed after it was last retrieved. If it has not changed, it will not be downloaded.<br/> |



 

## Web Service Description Page

*ServerURL*/\_wmcs/Licensing/TemplateDistribution.asmx?wsdl

## Remarks

The actual structure of the SOAP type varies from language to language. To obtain the structure of the type, query the web service description page.

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
</dt> <dt>

[**TemplateInformation**](-templateinformation.md)
</dt> </dl>

 

 





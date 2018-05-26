---
Description: Contains information about the templates stored on an AD RMS server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7be513d3-9756-4fa8-9db3-4391a41b58ec
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TemplateInformation class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# TemplateInformation class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **TemplateInformation** class contains information about the templates stored on an AD RMS server. This object is returned by the [**AcquireTemplateInformation**](-acquiretemplateinformation.md) method.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **TemplateInformation** class is derived from **System.Object**.

## Members

## Fields

The **TemplateInformation** class has the following fields.



| Field               | Description                                                                                                                                                                                                                                                                                |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ServerPublicKey** | Data type: **String**<br/> A string value that contains the public key of the AD RMS server.<br/>                                                                                                                                                                              |
| **GuidHashCount**   | Data type: **Int32**<br/> An integer value that contains the number of active templates stored on the server.<br/>                                                                                                                                                             |
| **GuidHashList**    | Data type: **GuidHash\[\]**<br/> An array of [**GuidHash**](-guidhash.md) objects that contain the template hashes. Hashes are used by AD RMS to determine whether a template has changed after it was last retrieved. If it has not changed, it will not be downloaded.<br/> |



 

## Web Service Description Page

*ServerURL*/\_wmcs/Licensing/TemplateDistribution.asmx?wsdl

## Remarks

The actual structure of the SOAP type varies from language to language. To obtain the structure of the type, query the web service description page.

You can call the [**AcquireTemplateInformation**](-acquiretemplateinformation.md) method to retrieve a **TemplateInformation** object, and you can call the [**AcquireTemplates**](-acquiretemplates.md) method to retrieve an array of active templates from the AD RMS server.

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

 

 





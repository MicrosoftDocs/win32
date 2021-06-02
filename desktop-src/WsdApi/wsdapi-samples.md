---
description: There are two WSDAPI samples included with the Windows SDK for Windows Server 2008.
ms.assetid: 156b79ef-1f05-4ef1-9df9-81fe81c73ca7
title: WSDAPI Samples
ms.topic: article
ms.date: 05/31/2018
---

# WSDAPI Samples

There are two WSDAPI samples included with the Windows SDK for Windows Server 2008. The source code for the samples can be found in <Windows SDK Install Folder>\\Samples\\Web\\WSDAPI. This version of the SDK is available from the [Download Center](https://www.microsoft.com/downloads/details.aspx?FamilyID=f26b1aa4-741a-433a-9be5-fa919850bdbf). The samples are not available in the Windows Vista SDK.

The stock quote sample (located in <Windows SDK Install Folder>\\Samples\\Web\\WSDAPI\\StockQuote) demonstrates a service with basic messaging functionality. The file service sample (located in <Windows SDK Install Folder>\\Samples\\Web\\WSDAPI\\FileService) demonstrates a service with advanced functionality, such as asynchronous messaging, attachments, and eventing.

Both samples include the following types of files.

-   WSDL files that contain the service descriptions.
-   [WsdCodeGen configuration files](wsdcodegen-configuration-file.md) used to generate WSDAPI code.
-   Generated C++ header and source files.
-   Client and service implementation files.
-   Visual Studio project and solution files.

Both samples implement device hosts ([**IWSDDeviceHost**](/windows/desktop/api/WsdHost/nn-wsdhost-iwsddevicehost)), device proxies ([**IWSDDeviceProxy**](/windows/desktop/api/WsdClient/nn-wsdclient-iwsddeviceproxy)), and service proxies ([**IWSDServiceProxy**](/windows/desktop/api/WsdClient/nn-wsdclient-iwsdserviceproxy)). In addition, the file service sample demonstrates the use of asynchronous messaging ([**IWSDAsyncCallback**](/windows/desktop/api/WsdClient/nn-wsdclient-iwsdasynccallback), [**IWSDAsyncResult**](/windows/desktop/api/WsdClient/nn-wsdclient-iwsdasyncresult)), attachments ([**IWSDInboundAttachment**](/windows/desktop/api/WsdAttachment/nn-wsdattachment-iwsdinboundattachment), [**IWSDOutboundAttachment**](/windows/desktop/api/WsdAttachment/nn-wsdattachment-iwsdoutboundattachment)) and eventing.

The FileServiceContract.vcproj and StockQuoteContract.vcproj files included with the samples call [WsdCodeGen](web-services-for-devices-code-generator.md) to generate C++ header and source files from the WSDL file specified in the WsdCodeGen configuration file. This means that if the sample WSDL or WsdCodeGen configuration file is changed and the sample project is rebuilt, WsdCodeGen automatically generates new header and source files that reflect the changes. This is the preferred method for building WSDAPI applications. WsdCodeGen is usually called from the command line. Open the relevant \*.vcproj file to view the example WsdCodeGen command line calls.

## Related topics

<dl> <dt>

[WSD Application Development on Windows](wsd-application-development-on-windows.md)
</dt> </dl>

 

 




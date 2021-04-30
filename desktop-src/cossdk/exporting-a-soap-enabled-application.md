---
description: When you use COM+ to create an XML web service, that service can be used by any authorized client, including those not using COM+ or even Microsoft Windows.
ms.assetid: c40031a6-f3de-4ef4-b9aa-3f49e57da5b4
title: Exporting a SOAP-Enabled Application
ms.topic: article
ms.date: 05/31/2018
---

# Exporting a SOAP-Enabled Application

When you use COM+ to create an XML web service, that service can be used by any authorized client, including those not using COM+ or even Microsoft Windows. However, using a COM+ web service in client-activated object (CAO) mode from a COM+ client application is especially easy. Just export the SOAP-enabled application in proxy mode, and then [import](importing-a-soap-enabled-application.md) it into the client for which you want to access the corresponding XML web service.

## Component Services Administrative Tool

To export a SOAP-enabled application from a server, use the following steps:

1.  In the console tree of the Component Services administrative tool, under **Component Services**, open the **COM+ Applications** folder associated with the computer you want to manage.

2.  Right-click the component you want to expose as an XML web service, and choose **Export**. The **COM+ Application Export Wizard** appears.

3.  In the text box labeled **Enter the full path and filename for the application file to be created**, enter the full path and filename for the MSI file that will contain the exported application, or click **Browse** to select the full path and filename using a dialog box.

4.  Under **Export As**, select the **Application Proxy – Install on other machines to enable access to this machine** radio button.

## Visual Basic

Does not apply.

## C/C++

Does not apply.

## Related topics

<dl> <dt>

[COM+ SOAP Service Overview](com--soap-service-overview.md)
</dt> <dt>

[Creating XML Web Services](creating-xml-web-services.md)
</dt> <dt>

[Importing a SOAP-Enabled Application](importing-a-soap-enabled-application.md)
</dt> </dl>

 

 




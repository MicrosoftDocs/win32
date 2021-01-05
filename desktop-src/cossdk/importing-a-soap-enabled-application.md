---
description: When a SOAP-enabled application has been exported from a server in proxy mode, clients that import it can automatically access the methods of the components it contains, remotely, as web services offered by the server in client-activated object (CAO) mode. This allows you to very easily deploy the functionality of a COM+ application across a network as an XML web service.
ms.assetid: 7f4783f7-4f53-4f0b-bb64-ae7903097d6c
title: Importing a SOAP-Enabled Application
ms.topic: article
ms.date: 05/31/2018
---

# Importing a SOAP-Enabled Application

When a SOAP-enabled application has been [exported](exporting-a-soap-enabled-application.md) from a server in proxy mode, clients that import it can automatically access the methods of the components it contains, remotely, as web services offered by the server in client-activated object (CAO) mode. This allows you to very easily deploy the functionality of a COM+ application across a network as an XML web service.

When the components of an application imported in this way are used on the client, they do not run on the client but instead are accessed remotely by using the XML web service provided by the server from which the application was exported. For details on using the components of an application imported in this way, see [Accessing XML Web Services in CAO Mode](accessing-xml-web-services-in-cao-mode.md).

## Component Services Administrative Tool

To import a SOAP-enabled application into a client, use the following steps:

1.  In the console tree of the Component Services administrative tool, under **Component Services**, open the folder associated with the client computer on which you want to install the application.

2.  Right-click the client's **COM+ Applications** folder, and then choose **New**. The **COM+ Application Install Wizard** appears.

3.  In the **COM+ Application Install Wizard**, click **Install pre-built application(s)**.

4.  Browse the network to locate or specify the network path of the MSI file on the server from which you want to install the application.

## Visual Basic

Does not apply.

## C/C++

Does not apply.

## Remarks

COM components are identified by a GUID, which changes if the components are recompiled. If a configured COM component that is exposed as an XML web service is recompiled, client applications that use it will break. Therefore, when a component that is exposed as an XML web service is recompiled, clients should re-import the applications that use the component.

## Related topics

<dl> <dt>

[COM+ SOAP Service Overview](com--soap-service-overview.md)
</dt> <dt>

[Creating XML Web Services](creating-xml-web-services.md)
</dt> <dt>

[Exporting a SOAP-Enabled Application](exporting-a-soap-enabled-application.md)
</dt> </dl>

 

 




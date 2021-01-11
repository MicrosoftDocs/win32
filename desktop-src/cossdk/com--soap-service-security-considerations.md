---
description: COM+ SOAP Service Security Considerations
ms.assetid: c4f7744c-ff57-4d9d-8632-7e5bbb73449a
title: COM+ SOAP Service Security Considerations
ms.topic: article
ms.date: 05/31/2018
---

# COM+ SOAP Service Security Considerations

The COM+ SOAP service depends on the IIS web server for security. Even in [client-activated object mode](accessing-xml-web-services-in-cao-mode.md), a COM+ RPC does not transmit the client identity and therefore cannot make use of role-based security or any other security feature provided by DCOM. If you want to help protect the privacy of data transmitted to and from your XML web service, or to help protect your XML web service from unauthorized access, you can configure IIS to limit access to an XML web service based on a clients IP address or to require a client to present a digital certificate to verify its identity. If you do not limit access, any client that can communicate with your web server can access your XML web service.

You can configure IIS to encrypt your XML web service communications with clients by using public key encryption SSL or TLS protocols. If you do not encrypt SOAP communications, data exchanged between a client and server could be observed by a third party with access to any network over which the SOAP communication travels; depending on network topology, this might be a small LAN or it might be the Internet.

By default, unencrypted SOAP communications are received at the HTTP port (80) and encrypted SOAP communications are received at the HTTPS port (443). For a client to successfully access an XML web service, any firewalls between the client and the server must be configured to allow TCP SYN packets to reach the appropriate server port. Conversely, to limit access to XML web services, a firewall administrator may choose to close these ports.

The default security settings for a COM component exposed as an XML web service differ depending on which version of the Microsoft .NET Framework is installed. If version 1.0 is installed, XML web services are nonsecure by default; all calls are accepted and no encryption is used. If version 1.1 or later is installed, XML web services are secure by default; callers must be authenticated and encryption is required.

A secured XML web service does not support WKO access via WSDL. Instead, clients that have installed the .NET Framework version 1.1 can call it in CAO mode. If third-party clients need to access your XML web service via WSDL, you must allow anonymous access.

A COM component exposed as an XML web service runs by default with the permissions of the anonymous user (not with the permissions of its caller). You can configure IIS to run the XML web service as a different user; this may sometimes be necessary because your component uses files or other resources to which the anonymous user does not have access. Nevertheless, you should always try to run your component with the fewest privileges possible, to limit the damage a malicious caller might cause.

> [!Note]  
> Because a method you exposed via an XML web service could potentially be exposed to malicious callers, you should always be sure to validate any input parameters on which it depends.

 

For detailed instructions on how to configure specific XML web service security settings, see [Securing XML Web Services](securing-xml-web-services.md).

**To convert a secure SOAP application to an unsecure SOAP application**

1.  Open the Internet Information Services (IIS) administration tool.
2.  Locate the virtual directory for the application and open the **Properties** dialog box.
3.  Check **Enable default content page** on the **Documents** tab.
4.  From the **Directory Security** tab click **Edit** under **Anonymous access and authentication control**.
5.  Check **Anonymous access** to enable anonymous access and click **OK**.
6.  Click **Edit** under **Secure communications**.
7.  Uncheck the **Require secure channel (SSL)** checkbox.

## Related topics

<dl> <dt>

[COM+ SOAP Service Overview](com--soap-service-overview.md)
</dt> </dl>

 

 




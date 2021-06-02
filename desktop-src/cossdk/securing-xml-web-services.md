---
description: Access to COM+ applications exposed as XML web services is controlled by the IIS web server, which processes the incoming requests.
ms.assetid: 440b0636-8afc-4fb3-a179-140958948b94
title: Securing XML Web Services
ms.topic: article
ms.date: 05/31/2018
---

# Securing XML Web Services

Access to COM+ applications exposed as XML web services is controlled by the IIS web server, which processes the incoming requests. You can also configure IIS to require the communications with the caller take place over a secure channel established using the Secure Sockets Layer (SSL) protocol.

> [!Note]  
> A secured XML web service does not support WKO access via WSDL. Instead, clients that have installed the .NET Framework version 1.1 can call it in CAO mode. If third-party clients need to access your XML web service via WSDL, you must allow anonymous access.

 

> [!Note]  
> To use the SSL protocol to establish a secure communication channel, you must obtain and install an SSL certificate.

 

## Component Services Administrative Tool

To select the authentication mechanism for an XML web service, use the following steps:

1.  Right-click the **My Computer** icon on your desktop, and click **Manage**.

2.  Under **Services and Applications** and **Internet Information Service**, locate the icon corresponding to the virtual root directory for your XML web service. Right-click the directory icon, and choose **Properties**.

3.  On the **Directory Security** tab of the properties dialog, locate **Authentication and access control** and click the corresponding **Edit** button.

4.  In the **Authentication Methods** dialog box, under **Authenticated access**, use the check boxes to select the authentication mechanisms you wish to allow. Click **OK**.

    > [!Note]  
    > You can configure IIS to authenticate callers by using any of the following options on the IIS **Authentication Methods** dialog: **Integrated Windows authentication**, **Digest authentication for Windows domain servers**, **Basic authentication (password is sent in clear text)**, or **.NET Passport authentication**. You can also allow anonymous access.

     

5.  In the properties dialog, click **OK**.

To allow nonsecure, anonymous access to an XML web service, use the following steps:

1.  Right-click the **My Computer** icon on your desktop, and click **Manage**.

2.  Under **Services and Applications** and **Internet Information Service**, locate the icon corresponding to the virtual root directory for your XML web service. Right-click the directory icon, and choose **Properties**.

3.  On the **Directory Security** tab of the properties dialog, locate **Authentication and access control**and click the corresponding **Edit** button. Select the **Enable anonymous access** check box. Click **OK**.

4.  On the **Directory Security** tab of the properties dialog, locate **Secure communications** and click the corresponding **Edit** button. Uncheck the **Require secure channel (SSL)** check box. Click **OK**.

5.  In the properties dialog, click **OK**.

## Visual Basic

Does not apply.

## C/C++

Does not apply.

## Additional Security Considerations

By requiring a secure channel, you help protect the confidentiality of the data exchanged by encrypting the communications between the client and your XML web service. If you allow authentication using clear text passwords, you should require a secure channel in order to avoid exposing passwords on the network.

## Related topics

<dl> <dt>

[Accessing XML Web Services in CAO Mode](accessing-xml-web-services-in-cao-mode.md)
</dt> <dt>

[Accessing XML Web Services in WKO Mode](accessing-xml-web-services-in-wko-mode.md)
</dt> <dt>

[COM+ SOAP Service Security Considerations](com--soap-service-security-considerations.md)
</dt> <dt>

[Creating XML Web Services](creating-xml-web-services.md)
</dt> </dl>

 

 




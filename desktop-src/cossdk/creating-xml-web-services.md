---
description: Any COM+ application can be exposed as an XML web service.
ms.assetid: 03c3d5a7-eb98-4916-b6ef-ef6aac86c574
title: Creating XML Web Services
ms.topic: article
ms.date: 05/31/2018
---

# Creating XML Web Services

Any COM+ application can be exposed as an XML web service. The methods in the default interfaces of the applications configured components (components in the servers COM+ catalog) can then be called remotely. You can use the Component Services administrative tool to create an IIS virtual root directory from which the component methods can be called by using SOAP.

> [!Note]  
> The .NET Framework must be installed on your computer in order to expose a COM+ application as an XML web service.

 

**To expose a COM+ application as an XML web service**

1.  In the console tree of the Component Services administrative tool, under **Component Services**, open the **COM+ Applications** folder associated with the computer you want to manage.

2.  Right-click the application you want to expose as an XML web service, and choose **Properties**.

3.  Click the **Activation** tab in the properties dialog.

4.  Select the **Uses SOAP** check box.

5.  In the **SOAP VRoot** text box, enter the name of the IIS virtual root directory from which the components methods can be accessed remotely. Note that a SOAP VRoot cannot be a subdirectory of another SOAP VRoot directory.

6.  Click **OK**.

    If you specify the IIS virtual root directory as *vroot* and if your servers fully qualified domain name is *servername*, the URL where your component is exposed as an XML web service is https://*servername*/*vroot*/.

    The corresponding directory in your file system is \\windows\\system32\\com\\SoapVRoots\\*vroot*\\; COM+ places several configuration files and ASP.NET programs there. For an XML web service under heavy load, you may want to adjust the parameters stored in the file web.config. For information about this file, consult the IIS documentation.

    The default security settings for a COM+ application exposed as an XML web service differ depending on which version of the .NET Framework is installed. If version 1.0 is installed, XML web services are nonsecure by default; all calls are accepted and no encryption is used. If version 1.1 or later is installed, XML web services are secure by default; callers must be authenticated and encryption is required.

## Related topics

<dl> <dt>

[Accessing XML Web Services in CAO Mode](accessing-xml-web-services-in-cao-mode.md)
</dt> <dt>

[Accessing XML Web Services in WKO Mode](accessing-xml-web-services-in-wko-mode.md)
</dt> <dt>

[COM+ SOAP Service Overview](com--soap-service-overview.md)
</dt> <dt>

[Securing XML Web Services](securing-xml-web-services.md)
</dt> </dl>

 

 




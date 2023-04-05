---
title: About the Windows Deployment Services API
description: Windows Deployment Services (WDS) is a suite of components that enable the deployment of Windows operating systems, particularly Windows Vista and later and Windows Server 2008 and later.
ms.assetid: 5742e51a-70e3-4607-bfb7-181362dfb168
keywords:
- Windows Deployment Services Windows Deployment Services , about
ms.topic: article
ms.date: 05/31/2018
---

# About the Windows Deployment Services API

Windows Deployment Services (WDS) is a suite of components that enable the deployment of Windows operating systems, particularly Windows Vista and later and Windows Server 2008 and later. You can use it to set up new computers using network-based installations.

OEMs, system builders, and corporate IT professionals looking for information on how to deploy Windows onto new computers, should see the information about the standard WDS solution in the [Windows Deployment Services Update Step-by-Step Guide](/previous-versions/windows/it-pro/windows-vista/cc766320(v=ws.10)) and the [Windows Automated Installation Kit (WAIK)](https://www.microsoft.com/download/details.aspx?id=10333).

In environments where the standard WDS solution cannot be used, the WDS API enables programmatic access to some WDS components.

-   The [Windows Deployment Services Server Functions](windows-deployment-services-server-functions.md) provide programmatic access to the WDS Pre-Boot Execution Environment (PXE) server. WDS server components include a PXE server and Trivial File Transfer Protocol (TFTP) server for network booting a computer to load and install an operating system.
-   The [Windows Deployment Services Client Functions](windows-deployment-services-client-functions.md) provide programmatic access to the WDS client. The WDS client components include a graphical user interface that runs within the Windows Pre-Installation Environment (Windows PE) and communicates with the server components to select and install an operating system image.
-   There is no API for the WDS management components. These components are a set of tools that you use to manage the server, operating system images, and client computer accounts. For more information about the WDS management components, see [The Windows Deployment Services Update Step-by-Step Guide](/previous-versions/windows/it-pro/windows-vista/cc766320(v=ws.10)).

The WDS PXE Server consists of a PXE server and a PXE provider. The PXE server contains the core networking capability. The PXE server supports plug-in interfaces which are known as PXE providers. This provider model enables development of custom PXE solutions while continuing to use the core PXE server networking code base.

-   Developers can use the [Windows Deployment Services Server Functions](windows-deployment-services-server-functions.md) to write a DLL for a custom provider to replace or run in conjunction with the standard Boot Information Negotiation Layer (BINL), on a WDS server. For example, the custom provider may use a text file as its data store instead of Active Directory.
-   Developers can use the [Windows Deployment Services Server Functions](windows-deployment-services-server-functions.md) to write a filter provider that is sequenced before BINL, or any other PXE provider, in the ordered list of registered providers. The second provider then only services selected PXE requests, while the first provider handles other requests. For example, this can enable the second registered provider in the ordered list to offer new functionality without disrupting the existing WDS solution implemented in the first provider.

The WDS client includes a graphical user interface that runs within the Windows Pre-Installation Environment (Windows PE) and communicates with the server components to select and install an operating system image. The WDS client library supports the development of custom client applications that can use a WDS server.

-   Developers can use the [Windows Deployment Services Client Functions](windows-deployment-services-client-functions.md) to write their own custom client application that replaces the WDS client. For example, the custom application can enumerate the images that are stored on a WDS server and send installation progress messages to the PXE server event log.

## Windows Deployment Services Samples

A sample custom PXE provider, filter provider, and WDS client application is available in the Microsoft Windows Software Development Kit (SDK), see [Microsoft Windows Software Development Kit (SDK)](https://developer.microsoft.com/windows/downloads/windows-sdk/).

You can download the following WDS samples online in the [desktop code gallery](https://github.com/microsoft/Windows-classic-samples).

<dl>

[Windows Deployment Services filter provider sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/WindowsDeploymentServices/FilterProvider)  
[Windows Deployment Services image enumeration sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/WindowsDeploymentServices/ImageEnumeration)  
[Windows Deployment Services multicast consumer sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/WindowsDeploymentServices/Multicast/WdsProvider)  
[Windows Deployment Services multicast provider sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/WindowsDeploymentServices/Multicast/WdsProvider)  
[Windows Deployment Services provider sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/WindowsDeploymentServices/FilterProvider)  
[Windows Deployment Services transport manager sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/WindowsDeploymentServices/Management/WDSTransportManager)  
</dl>

## Related topics

<dl> <dt>

[Using the Windows Deployment Services Server API](using-the-windows-deployment-services-server-api.md)
</dt> <dt>

[Using the Windows Deployment Services Client API](using-the-windows-deployment-services-client-api.md)
</dt> </dl>

 

 
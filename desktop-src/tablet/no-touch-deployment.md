---
description: The Microsoft .NET Framework gives you the ability to deploy applications from a Web or file server.
ms.assetid: 7721cd92-241f-4409-a724-c8e8768a19a9
title: No Touch Deployment
ms.topic: article
ms.date: 05/31/2018
---

# No Touch Deployment

The Microsoft .NET Framework gives you the ability to deploy applications from a Web or file server. This technique, called "no-touch deployment", combines the performance and interactivity of a smart client application with all the deployment advantages of a Web application. To deploy your application over the Web, right-click the folder that contains your executable and select **Properties**. On the **Web Sharing** tab, select **Share this folder**. Enter an alias for the folder. Now, your executable can be run over the Web by using that alias as the directory on your server. For more information on no-touch deployment, see [.NET Smart Clients](/archive/msdn-magazine/2002/july/net-zero-deployment-security-and-versioning-models-in-the-windows-forms-engine-help-you-create-and-deploy-smart-clients) and [No-Touch Deployment in the .NET Framework](/docs/?url=%2flibrary%2fdv_vstechart%2fhtml%2fvbtchno-touchdeploymentinnetframework.asp).

> [!Note]  
> You must have Microsoft Internet Information Services (IIS) installed on your computer to enable the **Web Sharing** tab in the **Properties** dialog box.

 

No-touch deployment is applied to ink-enabled applications in the same way as any other Windows Forms application. The samples provided by the Microsoft Windows XP Tablet PC Edition Software Development Kit (SDK) include a no-touch deployment version of the Auto Claims sample, in the Ink Web Samples section of the samples. This example takes the original [Auto Claims Form Sample](auto-claims-form-sample.md) and provides an installer that puts in on a Web share. When Microsoft Internet Explorer navigates to AutoClaims.exe in the directory that maps to the Web share, the application is launched. See [No-Touch Deployment Web Sample](no-touch-deployment-web-sample.md) for more information about the sample.

> [!Note]  
> When you deploy a .NET application over the Web, the application may be affected by the .NET security model. The [Security and Trust](security-and-trust.md) section describes how security works with ink-enabled Web applications.

 

 

 

---
description: This sample shows how to deploy a managed Tablet PC application over the Web by using no-touch deployment.
ms.assetid: d226bd67-e20d-431b-b0c3-9361b00a9340
title: No-Touch Deployment Web Sample
ms.topic: article
ms.date: 05/31/2018
---

# No-Touch Deployment Web Sample

This sample shows how to deploy a managed Tablet PC application over the Web by using no-touch deployment. You should be familiar with the concepts discussed in [No-Touch Deployment in the .NET Framework](/docs/?url=%2flibrary%2fdv_vstechart%2fhtml%2fvbtchno-touchdeploymentinnetframework.asp). Your computer must have Microsoft Internet Information Services (IIS) installed to run this sample.

## Overview

With no-touch deployment, Tablet PCWindows Forms applications-desktop applications built by using the classes in the System.Windows.Forms namespace of the Microsoft .NET Framework and the Microsoft Windows XP Tablet PC Edition Development Kit 1.7-can be downloaded, installed, and run directly on users' computers without any alteration of the registry or shared system components.

This sample takes the original project for [Auto Claims Form Sample](auto-claims-form-sample.md), AutoClaims, and provides an installer project, AutoClaims\_NoTouchWeb. Once compiled and run, the installer project creates a new virtual root, also called AutoClaims\_NoTouchWeb. The installer copies a file, default.htm, that includes a link to the AutoClaims.exe assembly. To launch the rich client application, navigate to the virtual root with Microsoft Internet Explorer, and then click the link in the default.htm page.

> [!Note]  
> You must navigate to the virtual root by way of IIS (for example, https://localhost/AutoClaims\_NoTouchWeb/default.htm) and not directly through the file system in order for the application to work in the Internet Explorer application domain.

 


```C++
<html>
    <head>
        <title>AutoClaims (No Touch Web)</title>
      </head>
      <body>
          <a href="AutoClaims.exe">Launch AutoClaims Sample</a>
      </body>
</html>
```



## No-Touch Deployment Requirements

All dependent assemblies must be located either in the assembly search path or the root of the virtual directory of the Web site. The AutoClaims\_NoTouchWeb deployment project installs the assembly and the referring page, default.htm, into the same virtual root (AutoClaims\_NoTouchWeb).

> [!Note]  
> The compiled web samples are not installed by the default installation option for the SDK. You must complete a custom installation and select the "Pre-compiled Web Samples" sub-option to install them.

 

For more information about using ink on the Web, see [Ink on the Web](ink-on-the-web.md).

 

 

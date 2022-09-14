---
description: One way to create ink-enabled Web applications is to put Windows Forms controls inside awebpagewithin Microsoft Internet Explorer.
ms.assetid: a4fcd692-cd4a-4d2a-bfad-198010e27c6f
title: Web Controls
ms.topic: article
ms.date: 05/31/2018
---

# Web Controls

One way to create ink-enabled Web applications is to put Windows Forms controls inside awebpagewithin Microsoft Internet Explorer. A good tutorial on this technique can be found at [Using Windows Forms Controls in Internet Explorer](https://windowsclient.net/articles/iesourcing.aspx). The basic steps in the tutorial are:

1.  Create a control that inherits from [**System.Windows.Forms.UserControl**](/dotnet/api/system.windows.forms.usercontrol).
2.  Create an HTML page with an object tag that refers to that UserControl.
3.  Create a virtual directory and set permissions.
4.  Load the URL of the HTML page into the browser.

This technique can be applied to ink-enabled controls, just like any other Windows Forms [**Control**](/dotnet/api/system.windows.forms.control). In fact, the technique can be used with any class in the Microsoft .NET Framework. The samples provided by the Microsoft Windows XP Tablet PC Edition Software Development Kit (SDK) include a Web control version of the Auto Claims sample in the Ink Web Samples section. This example takes the original [Auto Claims Form Sample](auto-claims-form-sample.md) and turns it into a control that is put on a Web page. For more information about Web-enabling this sample, see the [Ink Web Control Sample](ink-web-control-sample.md).

> [!Note]  
> When you deploy an application created by using .NET over the Web, the application may be affected by security model for .NET. For more information about how security works with ink-enabled Web applications, see [Security and Trust](security-and-trust.md).

 

 

 

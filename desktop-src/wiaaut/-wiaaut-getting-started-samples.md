---
title: Getting Started with Samples
description: All the example code contained in the Windows Image Acquisition (WIA) Automation Layer reference works in multiple languages.
ms.assetid: 2c9a5c30-de52-4bbb-a293-d58b66c9ba2d
keywords:
- Windows Image Acquisition (WIA),examples
- WIA (Windows Image Acquisition),examples
- Windows Image Acquisition Automation Layer,examples
- WIA Automation Layer,examples
- Image Acquisition Automation Layer,examples
- Windows Image Acquisition (WIA),sample code
- WIA (Windows Image Acquisition),sample code
- Windows Image Acquisition Automation Layer,sample code
- WIA Automation Layer,sample code
- Image Acquisition Automation Layer,sample code
- Windows Image Acquisition (WIA),Visual Basic
- WIA (Windows Image Acquisition),Visual Basic
- Windows Image Acquisition Automation Layer,Visual Basic
- WIA Automation Layer,Visual Basic
- Image Acquisition Automation Layer,Visual Basic
- Windows Image Acquisition (WIA),Windows Script Host
- WIA (Windows Image Acquisition),Windows Script Host
- Windows Image Acquisition Automation Layer,Windows Script Host
- WIA Automation Layer,Windows Script Host
- Image Acquisition Automation Layer,Windows Script Host
- Windows Image Acquisition (WIA),HTML Application (HTA)
- WIA (Windows Image Acquisition),HTML Application (HTA)
- Windows Image Acquisition Automation Layer,HTML Application (HTA)
- WIA Automation Layer,HTML Application (HTA)
- Image Acquisition Automation Layer,HTML Application (HTA)
- Windows Image Acquisition (WIA),Active Server Pages (ASP)
- WIA (Windows Image Acquisition),Active Server Pages (ASP)
- Windows Image Acquisition Automation Layer,Active Server Pages (ASP)
- WIA Automation Layer,Active Server Pages (ASP)
- Image Acquisition Automation Layer,Active Server Pages (ASP)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Getting Started with Samples

All the example code contained in the Windows Image Acquisition (WIA) Automation Layer reference works in multiple languages. This way you can copy the examples from the reference pages into any of the following:

-   [Visual Basic 6.0](#visual-basic-60)
-   [Windows Script Host](#windows-script-host)
-   [HTML Application](#html-application)
-   [Script in an HTML Application](#script-in-an-html-application)
-   [Active Server Pages](#active-server-pages)

## Visual Basic 6.0

To create a Microsoft Visual Basic project for any of the examples in the reference topics, perform the following steps.

1.  Start the Visual Basic Development Environment.
2.  Select **Standard EXE**.
3.  Click **Components** from the **Project** menu (or press Ctrl-T).
4.  Scroll down and select **Microsoft Windows Image Acquisition Library v2.0** by placing a checkmark in front of it. Of the three new controls that appear on in the Toolbox, double click [**CommonDialog**](-wiaaut-commondialog.md) and [**DeviceManager**](-wiaaut-devicemanager.md) to add them to your form.

> [!Note]  
> The data types are commented out in the examples in the reference pages so you can copy and paste them into Microsoft Visual Basic Scripting Edition (VBScript) where all data types are a **Variant**. Visual Basic programmers should remove the comment mark (') in front of each data type.

 

## Windows Script Host

To create a Windows Script Host project, copy the following into an empty file with a .wsf extension.


```
<job>
<reference object="WIA.DeviceManager" />
<object id="DeviceManager1" progid="WIA.DeviceManager" />
<object id="CommonDialog1" progid="WIA.CommonDialog" />
<script language="VBScript">

'Paste Sample Code Here

</script>
</job>
```



## HTML Application

To create an HTML Application (HTA), copy the following into an empty file with an .hta extension. In addition, if you have not done so already, create the [Visual Basic Script Constants](-wiaaut-vbscript-constants.md) file.


```
<html>
<title>Sample HTA</title>
<hta:application id="oHTA"/>
<object ID="DeviceManager1" Width=0 Height=0 ClassID="CLSID:E1C5D730-7E97-4D8A-9E42-BBAE87C2059F"></object>
<object ID="CommonDialog1" Width=0 Height=0 ClassID="CLSID:850D1D11-70F3-4BE5-9A11-77AA6B2BB201"></object>
<script language="vbscript" src="wiaaut.vbs"></script>
<script language="vbscript">

'Paste Sample Code Here

</script>
</head>
<body scroll="no">
</body>
</html>
```



## Script in an HTML Application

To create an HTML file with script, copy the following into an empty file with an .htm extension. In addition, if you have not done so already, create the [Visual Basic Script Constants](-wiaaut-vbscript-constants.md) file.

> [!Note]  
> Since the Windows Image Acquisition (WIA) Library is not marked safe for scripting, proper functionality is dependent on your security settings.

 


```
<html>
<title>Sample HTML</title>
<object ID="DeviceManager1" Width=0 Height=0 ClassID="CLSID:E1C5D730-7E97-4D8A-9E42-BBAE87C2059F"></object>
<object ID="CommonDialog1" Width=0 Height=0 ClassID="CLSID:850D1D11-70F3-4BE5-9A11-77AA6B2BB201"></object>
<script language="vbscript" src="wiaaut.vbs"></script>
<script language="vbscript">

'Paste Sample Code Here

</script>
</head>
<body>
</body>
</html>
```



## Active Server Pages

To create an Active Server Page, copy the following into an empty file with an .asp extension.

> [!Note]  
> The script on Active Server Pages (ASP) runs on a non-interactive desktop so using the [**CommonDialog**](-wiaaut-commondialog.md) or [**VideoPreview**](-wiaaut-videopreview.md) control in an Active Server Page will not work as expected. In addition, in the interest of increased security, the default Server Security Settings needs to be adjusted before you can successfully create a [**DeviceManager**](-wiaaut-devicemanager.md) object. For instructions on changing your security settings, see [How to Configure Security Settings](-wiaaut-configure-security.md). Also, for security reasons you need to change any calls to the Visual Basic function CreateObject to instead use [Server.CreateObject](http://msdn.microsoft.com/library/7t9k08y5(VS.71).aspx).

 


```
<%@ Language=VBScript %>
<!--METADATA TYPE="TypeLib" UUID="94A0E92D-43C0-494E-AC29-FD45948A5221"-->
<% 

'Paste Sample Code Here

%>
```



 

 





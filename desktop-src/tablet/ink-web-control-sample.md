---
description: This sample shows how to create an ink-enabled control for use in a Web browser. The sample takes the original Auto Claims Form Sample and turns it into a control that is put on a Web page.
ms.assetid: 7a9e304c-57ef-41a3-83be-2b2d31435da8
title: Ink Web Control Sample
ms.topic: article
ms.date: 05/31/2018
---

# Ink Web Control Sample

This sample shows how to create an ink-enabled control for use in a Web browser. The sample takes the original [Auto Claims Form Sample](auto-claims-form-sample.md) and turns it into a control that is put on a Web page.

For more information about using ink on the Web, see [Ink on the Web](ink-on-the-web.md).

## Modifications to the Original Sample Project

This sample consists of a solution that includes two projects and an HTML file. The first project, AutoClaims, is a Microsoft Visual C\# Control Library project (a User Control). The source code for this control is almost identical to that of the AutoClaims sample with two differences:

-   The `AutoClaims` class in this sample inherits from the [UserControl](/dotnet/api/system.windows.forms.usercontrol?view=netcore-3.1&preserve-view=true) class rather than the [Form](/dotnet/api/system.windows.forms.form?view=netcore-3.1&preserve-view=true) class.

    ```C++
    public class AutoClaims : System.Windows.Forms.UserControl 
    ```

    

-   The AutoClaims Class in this sample has an added public method, `DisposeResources` that disposes of the internal child controls used for collecting ink. This method must be called by thewebpageon which the control is used when that page is finished using the control.

## Referencing the Control in HTML

The solution includes an HTML file, default.htm. This file is the page that the browser navigates to in order to load the control. The file contains an &lt;object&gt; tag that references the control. It also includes a script that is called when the page unloads, as indicated by the presence of the onload=" `OnUnload()` " attribute in the &lt;body&gt; tag. This function calls the `DisposeResources` method on the control to make sure that all resources are properly released at shutdown.


```C++
<html>
    <script language="jscript">
        // Release any resources held by the AutoClaims control
        function OnUnload()
        {
            autoClaimsControl.DisposeResources();
        }
    </script>
    <head>
        <title>AutoClaims (Web Control)</title>
    </head>
    <body onunload="OnUnload()">
        <object 
          id="autoClaimsControl" 
          classid="AutoClaims.dll#AutoClaims.AutoClaims">
        </object>
    </body>
</html> 
```



Notice the format of the classid attribute value for the &lt;object&gt; tag. It names the assembly, followed with a \# sign separator, and then the namespace that contains the control and then the class name of the control.

A real-world user control would likely include additional methods used to persist or send the data collected in the application.

## The AutoClaims\_WebControl Project

The AutoClaims\_WebControl project is a Deployment Project that creates a setup that adds a virtual root, AutoClaims\_WebControl, on the Web server when installed. The control and the HTML file are placed in this virtual root.

> [!Note]  
> The compiled web samples are not installed by the default installation option for the SDK. You must complete a custom installation and select the "Pre-compiled Web Samples" sub-option to install them.

 

## Related topics

<dl> <dt>

[Auto Claims Form Sample](auto-claims-form-sample.md)
</dt> <dt>

[Ink on the Web](ink-on-the-web.md)
</dt> </dl>

 

 

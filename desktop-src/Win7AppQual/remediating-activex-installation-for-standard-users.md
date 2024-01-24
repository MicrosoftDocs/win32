---
description: Fixing ActiveX Installation Compatibility Issues for Standard Users
ms.assetid: 4199521A-58E6-4475-9B95-A724AB52969A
title: Fixing ActiveX Installation Compatibility Issues for Standard Users
ms.topic: article
ms.date: 05/31/2018
---

# Fixing ActiveX Installation Compatibility Issues for Standard Users

To develop a secure desktop environment, you must mitigate the threats from malicious ActiveX controls and provide an appropriate level of application compatibility in your environment. An *ActiveX control* is a piece of executable code (typically an OCX file that is packaged within a cabinet file) that is installed and run through Windows Internet Explorer. You can create ActiveX controls to add functionality to web applications that you cannot easily achieve by using standard HTML code or a simple script.

Installing ActiveX controls becomes a compatibility issue when your migration to Windows 7 includes a transition to standard users. This type of transition is a common best practice in which IT professionals move their environment to a [standard user account](https://support.microsoft.com/hub/4338813/windows-help). This transition is not a requirement for deploying Windows Internet Explorer 8.

## ActiveX Control Installation

ActiveX controls have a simple download and execute deployment model. ActiveX controls are installed and run through the HTML **object** element. The **CODEBASE** attribute on this element tells Internet Explorer (by using a URL) where to get the control if it is not already installed on the user’s machine. In that case, Internet Explorer downloads the associated installation package, performs trust verification on the object, and prompts the user for installation permission in Internet Explorer.

During the installation, the rendering page registers and runs the control. After the control is installed, any standard users can run the control. This simple mechanism of distribution and execution provides an easy way to distribute your components to users of your web application. But standard account users cannot directly install per-machine ActiveX controls and they might need administrator privileges to complete the installation.

## ActiveX Installer Service (AXIS)

The ActiveX Installer Service (AXIS) enables you to deploy ActiveX controls by using Group Policy on computers in an organization. You can configure AXIS by Group Policy settings, which you can modify by using the Group Policy Management Console (GPMC) or the Local Group Policy Editor.

There are two policy settings for AXIS:

-   The Approved Installation Sites for ActiveX Controls policy setting consists of a list of approved installation sites, which the AXIS uses to determine whether an ActiveX control can be installed.
-   The ActiveX installation policy for sites in Trusted zones policy setting identifies how Trusted sites zones can be used to install ActiveX controls.

When a website tries to install an ActiveX control, the AXIS checks to see if the URL of the website is listed in the list of approved installation sites or as part of the trusted sites zone. If the site is in either of these lists, the AXIS makes sure that the site meets the requirements that the policy defines. If the site and the ActiveX control meet all of the requirements of the policy settings, the control is installed. For more information, see [Administering the ActiveX Installer Service](/previous-versions/windows/it-pro/windows-7/dd631688(v=ws.10)).

## Related topics

<dl> <dt>

[Fixing Compatibility Issues in Web Applications by Using Compatibility View](remediating-web-applications-and-add-ons.md)
</dt> </dl>

 

 

---
title: Gadgets for Windows Sidebar Security
description: This overview contains information about the security model of the Windows Sidebar.
ms.assetid: e686b4f1-776a-491a-946d-95f5681c5ea4
keywords:
- Windows Sidebar,security
- Sidebar,security
- gadgets,security
- security for Windows Sidebar
- Windows Sidebar,packaging
- Sidebar,packaging
- gadgets,packaging
- Windows Sidebar,Windows Defender
- Sidebar,Windows Defender
- gadgets,Windows Defender
- Windows Defender
- Defender
- Windows Sidebar,HTML Application (HTA)
- Sidebar,HTML Application (HTA)
- gadgets,HTML Application (HTA)
- HTML Application (HTA)
- HTA (HTML Application)
- Windows Sidebar,User Account Control (UAC)
- Sidebar,User Account Control (UAC)
- gadgets,User Account Control (UAC)
- User Account Control (UAC)
- UAC (User Account Control)
- Windows Sidebar,parental controls
- Sidebar,parental controls
- gadgets,parental controls
- parental controls
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Gadgets for Windows Sidebar Security

\[ The Windows Gadget Platform/Sidebar is available for use in the following versions of Windows: Windows 7, Windows Vista, and Windows Server 2008. It may be altered or unavailable in subsequent versions. \]

This overview contains information about the security model of the Windows Sidebar.

-   [Introduction](#introduction)
-   [Packaging](#packaging)
-   [Downloading](#downloading)
-   [HTML runtime](#html-runtime)
-   [User Account Control](#user-account-control)
-   [Parental Controls](#parental-controls)
-   [Full Trust](#full-trust)
-   [Additional Security for Corporations](#additional-security-for-corporations)
-   [For Further Reference](#for-further-reference)

## Introduction

Gadgets for Sidebar, though developed using the functionality of the Microsoft HTML (MSHTML) runtime, are not limited by the standard browser security model. Since gadgets are locally installed mini-applications that provide a rich set of system access APIs, a packaging and deployment method similar to a typical executable distribution is employed. For more information on securing your gadgets, see [Inspect Your Gadget](http://msdn.microsoft.com/library/bb498012.aspx).

## Packaging

A gadget is downloaded as a "package" of resources and configuration files. The package is distributed as a zip file or as a Windows cabinet (.cab) file. Both methods of distribution require that the file name extension, .zip or .cab, be changed to .gadget. If the file is packaged as a .cab file, you can use a code signing certificate to provide information about the origin of the gadget. The user is then presented with this information before the gadget files are extracted. The signtool.exe application included with Visual Studio 2005 can be used to sign a gadget.

> [!Note]  
> There is no requirement that gadgets be digitally signed since the certificates are costly and not commonly used by the developer community who are likely to create gadgets.

 

## Downloading

Windows Defender is a free program that helps protect your computer against pop-ups, slow performance, and security threats caused by spyware and other unwanted software. When integrated with Internet Explorer, Windows Defender performs file scanning on downloads to help ensure that one does not accidentally download malicious software. Gadget packages are included in the Windows Defender scan.

> [!Note]  
> The latest version of Windows Internet Explorer has a new security feature called Protected Mode. Protected Mode is an enhancement designed to protect users while browsing the Internet from malicious software running in the context of an untrusted remote webpage. Protected Mode does not apply to gadgets because they run on the local computer.

 

![the protected mode dialog.](images/security/gadgetinstall-protectedmode.png)

## HTML runtime

The gadget security model can be compared with Internet Explorer and associated domain sandboxing security models. However, gadgets have more in common with HTML Applications (HTAs) than they do with HTML content in Internet Explorer. Because gadgets have a similar download and installation process as other executable code, gadgets have been provided with a similar set of capabilities. The MSHTML runtime is configured with the set of permissions given to HTAs or the Local Machine Zone security configuration.

Gadgets are configured differently from webpages in several ways:

-   Because gadgets are considered executable code, they can instantiate any installed ActiveX object when the option "Initialize and script ActiveX controls not marked as safe for scripting" is enabled in Internet Explorer. ![the internet explorer security settings dialog showing the 'initialize and script activex controls not marked as safe for scripting' radio button selection.](images/security/securitysettngs-activex.png)
-   Since gadgets can aggregate data from various locations, the option "Access data sources across domains" is enabled in Internet Explorer. ![the internet explorer security settings dialog showing the 'access data sources across domains' radio button selection.](images/security/securitysettings-datasources.png)

## User Account Control

User Account Control (UAC) is a new feature of Windows Vista that improves security when running as a standard user. Gadgets run with standard user privileges in the Administrator Approval Mode of UAC even if the user is a member of the administrators group. This helps prevent gadget code from modifying protected resources.

As an additional precaution, Sidebar Gadgets do not display the UAC elevation prompts that are used to run programs with full administrator privileges. If a gadget launches an application installed on the computer, however, that application may display UAC elevation prompts. For example, if a gadget attempts to delete a file in the System32 directory, the delete operation would not succeed and no elevation prompt would be shown to the user. This failure happens because most critical files cannot be modified by standard users.

## Parental Controls

Windows Vista includes a new parental controls feature to help enforce various safe browsing and execution policies on a computer. For example, a parent might only allow a child to run games that are E-rated and only browse to specific websites. The policy for Web browsing applies to gadgets in the Sidebar also; if the parental control policy only allows a child to browse to websites "A" and "B", attempts to communicate with site "C" will fail.

## Full Trust

The choice to run a gadget is presented to the user in the same way that the choice to run any application downloaded from the Internet is presented. Information about the author of the gadget is displayed in a dialog box that indicates there is risk associated with this file. After the user accepts the warning, the gadget will run with all of the permissions associated with the user's login account.

![the security warning dialog presented to a user when a gadget is installed.](images/security/gadgetinstall-install.png)

> [!Note]  
> An individual gadget may only have a single function such as reading files and information from the computer, accessing information from one or more domains, or displaying buttons and information for a utility. However, gadgets mix and match functionality in a variety of ways and, in aggregate, have the same set of functionality as other code.

 

## Additional Security for Corporations

In a computing environment controlled by group policy, the use of gadgets can be further limited. The Sidebar supports three gadget folders, %systemdrive%\\Program Files\\Windows Sidebar\\Shared Gadgets and %systemdrive%\\Program Files\\Windows Sidebar\\Gadgets that can only be modified by the Administrator group and the %systemdrive%\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows Sidebar\\Gadgets folder, where gadgets downloaded by the user are installed.

> [!Note]  
> The Shared Gadgets folder provides access to a gadget for all users of the machine.

 

The Windows Sidebar has the following group policy options available:

-   Turn off Windows Sidebar.

    This policy allows administrators to completely disable the Windows Sidebar.

-   Disable unpacking and installation of gadgets that are not digitally signed.

    This policy allows administrators to require that all gadgets installed by a user are digitally signed. This policy only affects gadgets that are downloaded and installed by double-clicking on the gadget package. All previously installed gadgets, as well as those installed manually, will still function.

-   Turn off user-installed gadgets.

    This policy allows administrators to block gadgets not placed into either the Gadgets or the Shared Gadgets folders (both of which can be modified only by a user in the Administrator group). Gadgets installed into the %systemdrive%\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows Sidebar\\Gadgets folder will not display in the Gadget Gallery dialog box or be allowed to run.

-   Override the "Get more gadgets online" link.

    The Gadget Gallery dialog box provides a link where users can discover more gadgets. By default, this link points to an online Microsoft website; however, administrators can specify that this link point to another website. Administrators can then more easily distribute gadgets that are approved for use within an organization.

## For Further Reference

[Windows Defender](http://go.microsoft.com/fwlink/p/?linkid=142589)

[User Account Control](http://go.microsoft.com/fwlink/p/?linkid=142588)

[Parental Controls](http://go.microsoft.com/fwlink/p/?linkid=142593)

 

 





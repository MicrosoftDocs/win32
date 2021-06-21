---
description: Removal of Windows Mail
ms.assetid: 356f0d79-12dd-49f0-b756-a46f20177efa
title: Removal of Windows Mail
ms.topic: article
ms.date: 05/31/2018
---

# Removal of Windows Mail

## Affected Platforms

**Clients** - Windows 7  
**Servers** - Windows Server 2008 R2  









## Feature Impact

**Severity** - High  
**Frequency** - High  









## Description

Microsoft is deprecating the Windows Mail utility and disabling the API CoStartOutlookExpress. The other mail APIs have been marked as deprecated and are slated for removal in a later Windows version. However, the publicly documented APIs that are not marked as deprecated or obsolete will continue to function in Windows 7. Binaries will remain on the users' systems and will continue to be accessible via the APIs, specifically in the cases mentioned above. In addition, the users' email (.eml) and news (.nws) files will remain on the system.

## Manifestation of Impact

Removal of Windows Mail results in the following:

-   All entry points to Windows Mail and Contacts (for example, Start Menu, user-created Shortcuts, Start -> Run, and so on) are removed or disabled. Some of these are completely removed, others will fail when trying to launch.
-   All DLLs ship in the box
-   Publicly documented APIs continue to work as they did in Windows Vista
-   Any APIs that attempt to launch the main browser UI have been modified to create a silent failure. The function will return success, but will not show the UI to the user. APIs that call other dialog boxes (for example, the Spooler or the Accounts dialog) continue to show that UI
-   Protocol (mailto, ldap, news, snews, nntp) handlers will not be associated with Windows Mail or Contacts. When attempting to launch these, customers will see an error dialog pointing them to the location where they can set these associations to another program
-   File associations (.eml, .nws, .contact, .group, .wab, .p7c, .vfc) are broken or disabled. When attempting to open a file with these extensions, customers will get a dialog box offering them other apps that are installed that they can use and point them to a webpage that offers solutions
-   Any user files (for example, contact files or messages) remain on the system in the upgrade scenario
-   The Contacts folder is hidden by default so customers will not see it
-   APIs are marked as deprecated in MSDN
-   The file preview function is removed
-   Shell hooks in the right-click menu are removed
-   The file search function is removed

## Mitigation

Users should install Windows Live Mail or any other mail product that is able to read .eml and .nws files.

## Solution

Detect if there is a default mail handler installed. If not, advise user to install Windows Live Mail or any other product that is able to read .eml and .nws files.

Do not design code that calls the Windows Mail UI API, since it will not work. You must find other ways to access the .eml and .nws files. In addition, as soon as is feasible, discontinue your reliance on all other Windows Mail APIs.

## Compatibility, Performance, Reliability, and Usability Testing

-   Exercise your application in a Windows 7 environment to ensure that the application does not try to call the UI API.
-   Alternatively, you can run the Application Compatibility Toolkit (ACT) using the Windows Compatibility Evaluator (WCE) to locate any potential issues due to the deprecation of this functionality.

## Links to Other Resources

<dl>

[Application Compatibility Toolkit Download](/windows-hardware/get-started/adk-install)  
</dl>

 

 

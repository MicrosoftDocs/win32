---
description: Evolution of MUI Support across Windows Versions
ms.assetid: a3bda96e-6a54-41b3-88d3-9da88d7c0416
title: Evolution of MUI Support across Windows Versions
ms.topic: article
ms.date: 05/31/2018
---

# Evolution of MUI Support across Windows Versions

-   [Before Windows Vista](#before-windows-vista)
-   [Windows Vista and Beyond](#windows-vista-and-beyond)
    -   [A language neutral/MUI operating system](#a-language-neutralmui-operating-system)
    -   [Deployment scenarios are fully MUI-based](#deployment-scenarios-are-fully-mui-based)
    -   [Single image deployment](#single-image-deployment)
    -   [Improved servicing model](#improved-servicing-model)
    -   [MUI infrastructure](#mui-infrastructure)
    -   [Language management](#language-management)
    -   [Resource handling](#resource-handling)

## Before Windows Vista

Prior to the Windows Vista release, Windows shipped with single-language images, which meant that each localized version of Windows contained a single language for its user interface. MUI was an add-on to the English version of the operating system, and the Multilingual User Interface Packs could only be added to certain English versions of Windows. When installed on the English version of Windows, MUI allowed the user interface language of the operating system to be changed according to the preferences of individual users to one of the supported languages.

The MUI Pack model did not expose MUI support for applications. Although developers could create multi-lingual applications, they had to create their own mechanisms to do so.

## Windows Vista and Beyond

With Windows Vista, Microsoft made a significant investment in MUI. Windows Vista is built from the ground up on a MUI platform. While this represents a major advance in Windows localization strategy as it is a key enabler for Microsoft to provide Windows in more languages than ever before, it is first and foremost a great advance for Windows users and customers.

### A language neutral/MUI operating system

The vast majority of Windows Vista binaries are MUI compliant, and their localizable data are stored separately from the code. This offers flexibility, as different language data can be added at any time.

### Deployment scenarios are fully MUI-based

The Windows Vista packaging and installation design are MUI-based and all localizable data are packaged in language-specific packs, and each language pack can be deployed in different scenarios. For example, although the retail DVDs for Windows Vista contain single-language versions, users of the Ultimate edition can download additional MUI language packs and can switch UI language from the **Regional and Language Options** control panel. Enterprise edition licensees get all languages and can deploy any of them.

### Single image deployment

Enterprise customers and OEMs can now reduce the number of images that they need to maintain in order to deploy Windows and applications onto computers across different locales through single image deployment.

With MUI on Windows Vista, one image containing multiple languages can be deployed to any language users, and users can determine their own preferred languages (within policy) during setup or initial "out of the box experience" with the computer. In particular, OEMs can put many UI languages on their new computers to allow users to select one from the Welcome Center. Thus, from an image with multiple language packs, Setup will display a list of available languages and enable users to pick one of them. All international settings are then set to match the selected language or locale.

### Improved servicing model

The same QFE or security fix package can now be installed on top of any language systems. This is critical as it enables a faster turnaround of security fixes in particular and enables all international users to benefit from the same time availability of all security fixes.

### MUI infrastructure

Starting with Windows Vista, MUI APIs are available to enable developers to take advantage of the MUI mechanisms for their own applications, without having to create custom logic for resource handling and language management.

### Language management

Base MUI APIs that provide UI language management capabilities are available as part of the MUI infrastructure. To help manage the different UI language settings at the system, user, and application level, MUI internally combines them into a single prioritized list. MUI then implements a fallback mechanism based on this prioritized list, allowing for partial localization solutions while providing users with an appropriate—if not preferred—user interface language experience.

For example, a system running the Spanish version of Windows Vista with a Catalan language interface pack (LIP) installed on top of the base operating system can support the following behavior: the system will try and display its resources in Catalan first, and if these resources are not available in Catalan, then provide the user with Spanish resources instead.

### Resource handling

With the improved MUI infrastructure that is available starting with Windows Vista, most common resource technologies are MUI-enabled. The following table provides additional details on the resource handling support available in Windows Vista.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Category</th>
<th>Support</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Supported resource types</td>
<td><ul>
<li>Win32/unmanaged resource: .DLL/.EXE/.OCX</li>
<li>Shell-related registrations</li>
<li>Management-related resources: Event log, Snap-in/MSC files</li>
<li>WMI: MOF/MFL</li>
<li>Group Policy: ADMX/ADML</li>
<li>Managed Resources.dll</li>
</ul></td>
</tr>
<tr class="even">
<td>Development Tools</td>
<td><ul>
<li>For Win32: RC.exe, MUIRCT.exe and Visual Studio 2005 and later</li>
</ul></td>
</tr>
<tr class="odd">
<td>Limited resource type support</td>
<td><ul>
<li>*.chm help files</li>
</ul></td>
</tr>
</tbody>
</table>



 

 

 




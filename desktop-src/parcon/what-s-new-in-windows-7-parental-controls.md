---
description: Gives an overview of the changes to the Windows Parental Controls introduced in Windows 7.
ms.assetid: 5723fddd-52e2-46a1-a48f-647d479b21d9
title: Whats New in Windows 7 Parental Controls
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Windows 7 Parental Controls

## Overview of Parental Controls Changes for Windows 7

The purpose of this document is to give an overview of the changes to the Windows Parental Controls introduced in Windows 7 and to enable third-party parental control solution providers to take advantage of these changes. This document assumes readers' familiarity with Parental Controls for Windows Vista and will only reflect changes made to this functionality in Windows 7 that are relevant for third-party parental control solutions development. A full update of MSDN Windows Parental Control documentation will follow at a later date.

## Key Design Decisions for Windows 7 Parental Control Changes

Changes to Parental Controls introduced in Windows 7 continue the overarching goal of promoting third-party parental control solutions' coexistence with the in-box functionality. The changes are:

-   Removal of web filtering and activity reporting from the in-box parental controls functionality. The in-box parental controls provide core offline Microsoft-implemented restrictions such as time limits, application restrictions, and game restrictions. The web filtering, activity reporting, and other functionality can be provided by Microsoft or third-party parental control solutions. For example, Windows Live Family Safety solution provides web filtering, remote management, and activity monitoring, as well as contact management for all Windows Live applications.
-   Enabling third-party solutions to replace the in-box provider's configuration user interface while still relying on the in-box implementation of time, application, and game restrictions.
-   Enabling third-party solutions to be discovered and enabled on the computer by a parent or guardian (administrator account).

## Parental Controls Top-level User Interface Changes in Windows 7

Windows 7 brings the following changes to the Parental Controls Control Panel top-level user interface:

-   The Additional controls section is introduced where controls that provide additional functionality such as web filtering, activity reporting, and so on, can be selected from a drop down list box. Microsoft or third-party providers need to register their solutions with Windows 7 Parental Controls for them to be selectable from the Additional controls drop down list box. For information about registering a solution, see Provider Registration, later in this topic).
-   The logo image of the currently selected provider is displayed in the upper-right corner of the page.
-   The managed user tiles can display a summary of the parental settings provided by the currently selected provider.

The currently selected provider might choose to use its own user interface for User Control screens for the managed users, or it might select to rely on the in-box WPC implementation of this screen. In-box implementation has the following changes made to its elements:

-   The activity reporting section is removed.
-   The link to view activity reports is removed.

## Parental Controls API Overview: Windows 7 Changes

The integration mechanism for third-party solution providers was expanded to allow:

-   Provider registration. Upon registration, a provider becomes selectable in the Additional controls drop-down list box on the Parental Controls Control Panel screen.
-   Querying for the currently selected provider. A public COM interface is exposed to enable this functionality.
-   Also new is the set of COM interfaces to be implemented by the providers to allow:
    -   Enabling or disabling of the provider by WPC upon user selection of additional controls.
    -   WPC to pass control to the provider to configure managed user's parental control settings.
    -   WPC to query the provider for the summary of managed user's parental control settings.

## Third-party Provider Integration

### Provider Registration

To register a new provider with Parental Controls, a registry value must be written to the Providers key of Windows Parental Controls. The value name is a unique GUID that is used to identify the provider. The value data will be a path to a registry key in **HKEY\_LOCAL\_MACHINE** that contains provider information.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         Windows
            CurrentVersion
               Parental Controls
                  Providers
                     {45D63315-0824-4df4-B8A4-EF137D8810D1} = SOFTWARE\Microsoft\Family Safety\WPC\
```

At the registry key location specified, the following values are expected.



| Term                                                                                                                 | Description                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="LogoImage"></span><span id="logoimage"></span><span id="LOGOIMAGE"></span>**LogoImage**<br/>         | A fully qualified path to a resource binary with a negative resource ID for the provider logo image (stored as an **IMAGE\_BITMAP**).<br/>                                                        |
| <span id="DisplayName"></span><span id="displayname"></span><span id="DISPLAYNAME"></span>**DisplayName**<br/> | A fully qualified path to a resource binary with a negative resource ID for the provider name. **DisplayName** length should not exceed 50 characters.<br/>                                       |
| <span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**<br/> | A fully qualified path to a resource binary with a negative resource ID for the provider description. The description length should not exceed 200 characters.<br/>                               |
| <span id="StateCLSID"></span><span id="stateclsid"></span><span id="STATECLSID"></span>**StateCLSID**<br/>     | The class ID of the provider's class which implements IWPCProviderState.<br/>                                                                                                                     |
| <span id="ConfigCLSID"></span><span id="configclsid"></span><span id="CONFIGCLSID"></span>**ConfigCLSID**<br/> | The class ID of the provider's class, which implements IWPCProviderConfig. **StateCLSID** and **ConfigCLSID** can be the same.<br/>                                                               |
| <span id="GRSVisible"></span><span id="grsvisible"></span><span id="GRSVISIBLE"></span>**GRSVisible**<br/>     | An optional **DWORD** nonzero value that specifies that Windows Parental Controls displays a link to the Game Rating System screen after a provider is selected as the new current provider.<br/> |



 

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         Family Safety
            WPC
               LogoImage = C:\Program Files\Windows Live\Family Safety\fssui.rll,-40001
               DisplayName = C:\Program Files\Windows Live\Family Safety\fssui.rll,-40002
               Description = C:\Program Files\Windows Live\Family Safety\fssui.rll,-40003
               StateCLSID = {B4BAAE4D-3D86-4fa9-86F0-CF82C94D8A6A}
               ConfigCLSID = {B4BAAE4D-3D86-4fa9-86F0-CF82C94D8A6A}
               GRSVisible = 0x00000001 (1)
```

The Parental Controls Control Panel uses the **LogoImage**, **DisplayName**, and **Description** to change the main page of the Parental Controls Control Panel when that provider is selected. The **StateCLSID** value is used when the provider is enabled or disabled. The **ConfigCLSID** value is used when the user interface gets dynamic information about each user (this is only the case if the provider is currently selected).

 

 





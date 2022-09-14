---
description: Gives an overview of the changes to the Windows Parental Controls introduced in Windows 8.
ms.assetid: 7EB33215-8F8B-4EA4-87E6-A98F0D014548
title: Whats New in Windows 8 Family Safety
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Windows 8 Family Safety

## Overview of Parental Controls Changes for Windows 8

The purpose of this document is to give an overview of the changes to the Windows Parental Controls in Windows 8 and to enable third-party parental control solution providers to take advantage of these changes. This document assumes readers' familiarity with Parental Controls for Windows 7 and Windows Vista and will only reflect changes made to this functionality in Windows 8 that are relevant for third-party parental control solutions development.

## Key Design Decisions for Windows 8 Parental Control/Family Safety Changes

Changes to Parental Controls introduced in Windows 8 continue the overarching goal of introducing feature enhancements and at the same time promoting third-party parental control solutions' coexistence with the in-box functionality. The changes are:

-   Use of Microsoft Family Safety to provide remote management and remote activity monitoring.
-   Integration of web filtering as part of in-box Microsoft restrictions and ability to view activity reports on a Windows 8 computer.
-   The Parental Controls feature in the Control Panel was renamed to Family Safety and will be referred to as such throughout this document.
-   The in-box time restrictions were enhanced by providing ability to control total amount of time per day computer can be used (time allowance) in addition to ability to control times when computer can be used (curfew.) Curfew was available in previous versions of Windows.
-   Windows 8 Family Safety functionality can be turned on during standard account creation flow.
-   Windows Vista and Windows 7 Parental Controls extensibility features are continued to be supported by Windows 8 Family Safety including ability by third-party solutions to replace web content filter or to replace in-box configuration UI while still relying on in-box implementation of Time, Application, Game Restrictions and Web Content Filter.
-   Third-party provider activation turns off remote management and reporting of Windows 8 Family Safety controls through Family Safety website.
-   The third-party extensibility for Family Safety is supported for Windows 8 desktop applications only.

## Family Safety and standard account creation in Windows 8

As part of standard account creation in Windows 8, an administrator has ability to turn on monitoring of the account by Family Safety. The following is a list of the functionality and third-party provider ability to control it:

-   On the last screen of Windows 8 standard account creation flow, an administrator is presented with a checkbox to turn on Family Safety for the newly created account.
-   If this checkbox is checked, Family Safety is turned on for the account with the following settings:
    -   Activity Reporting on
    -   All restrictions are off
-   If the administrator used a Microsoft account to logon to Windows, the Windows 8 computer will be configured for remote management of family safety settings and email activity reports. The Family Safety website can be then used to manage such a computer remotely.
-   If the third-party provider wishes for the checkbox to be present in a standard account creation flow the following value should be present among the provider s registration values. For more information on provider registration details, see the [Provider Registration](what-s-new-in-windows-7-parental-controls.md) section on the What's New in Windows 7 Parental Controls topic.

    

    | Term                                                                                                                         | Description                                                                                                                                                                                                                                                                                  |
    |------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | <span id="AddUserVisible"></span><span id="adduservisible"></span><span id="ADDUSERVISIBLE"></span>AddUserVisible<br/> | An optional **DWORD** nonzero value that specifies that the checkbox option to turn on Family Safety monitoring for a newly created account should be visible during standard account creation in Windows 8 after the provider is selected as the current Family Safety provider.<br/> |

    

     

-   Since third-party providers are designed to replace in-box configuration UI for Family Safety controls, by default, installation and activation of a third-party provider will result in the checkbox option to turn on Family Safety during standard account creation not to be shown.

## Family Safety Top-level User Interface Changes in Windows 8

Windows 8 brings the following changes to the Parental Controls Control Panel top-level user interface:

-   When in-box Family Safety controls are turned on for at least one standard account on a Windows 8 computer,  Manage settings on Family Safety website  command link is shown that allows an admin to establish remote management of Windows 8 computer Family Safety settings through Family Safety website.
-   When a Windows 8 computer is configured for remote management through Family Safety website, the More Information control allows an admin to disable remote management of a Windows 8 computer through the Family Safety website.
-   The Controls section is visible only when at least one third-party provider is registered with Family Safety. The UI and functionality of this section is identical to the Additional Controls section in Windows 7 Parental Controls. For more information, see the Parental Controls top-level User interface changes section of the [Windows 7 Parental Controls](what-s-new-in-windows-7-parental-controls.md) topic.
-   When a third-party provider is installed and selected as the current provider, remote management of Windows 8 computer Family Safety settings through the Family Safety website is disabled.

## Family Safety In-Box Restrictions Changes in Windows 8

Windows 8 brings the following changes to the Family Safety in-box restrictions:

Web Restrictions

-   Implementation has changed from a Layered Service Provider (LSP) filter to a Windows Filtering Platform (WFP) driver communicating with the Family Safety monitoring process running in the users  sessions.

Time Limits

-   The in-box time restrictions were enhanced by providing ability to control total amount of time per day computer can be used (time allowance) in addition to ability to control times when computer can be used (curfew) which was available in previous versions of Windows.
-   UI for curfew allows independent control for each day of the week with half-hour granularity.
-   UI for time allowance allows controls for weekdays / weekends or independent control for each day of the week with 15 minute granularity.
-   Fast User Switch (FUS) mechanism is no longer used to forcibly lock out or block login of the controlled user when in blocked time period. A switch to a separate desktop is used for these purposes.
-   Disconnect warning events are no longer available for applications to subscribe to.

## Family Safety API Changes in Windows 8

APIs used for Family Safety expose the policy and in-box restrictions settings, and logging functionality.

Logging

-   Custom events are no longer supported in the Family Safety activity reports viewer.

WMI API Settings Write/Read

-   WpcUserSettings - Previously, timer restrictions supported 1 hour granularity. In Windows 8 the existing property represents the first half-hour for each hour. A new half-hour property has been added to represent the second half of each hour. Additional new property was introduced to represent daily time allowance.

Web Content Filter Allow/Block List Export/Import A Format

-   Web content filter Allow/Block list Export functionality is no longer supported.

Family Settings WMI Provider Schema

-   The following additions were made to the WpcUserSettings class to reflect time restrictions enhancements:
    -   `[write: ToInstance ToSubClass, Description("Logon Half-Hours (30 minute offset) mask for this user"): ToInstance ToSubClass, read: ToInstance ToSubClass] uint32 LogonHalfHours[7];`
    -   `[write: ToInstance ToSubClass, Description("Daily minute allowance"): ToInstance ToSubClass, read: ToInstance ToSubClass] uint32 AllowanceMinutes[7];`

> [!Note]  
> Windows 8 uses a new registry key to indicate that the Family Safety API is enabled for a given user.
>
> **HKLM**\\**Microsoft**\\**Software**\\**Windows**\\**CurrentVersion**\\**Parental Controls**\\**Users**\\**{UserSid}**\\**Web**\\**Filter On**

 

The following registry key is supported for Windows 7 only.

**HKLM**\\**Microsoft**\\**Software**\\**Windows**\\**CurrentVersion**\\**Parental Controls**\\**Users**\\**{UserSid}**\\**Parental Controls On**

For both keys, a value of "0x00" (**DWORD**) indicates the feature is disabled for the current user and a value of "0x01" (**DWORD**) indicates the feature is enabled for the current user. When attempting to read the values of these keys, replace the "{UserSid}" token with the user's system ID.

 

 





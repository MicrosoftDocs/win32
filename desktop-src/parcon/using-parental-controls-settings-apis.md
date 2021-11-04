---
description: Using Parental Controls Settings APIs
ms.assetid: 77a239e9-1cec-4710-b673-7d0cebd502e9
title: Using Parental Controls Settings APIs
ms.topic: article
ms.date: 05/31/2018
---

# Using Parental Controls Settings APIs

Settings are discussed ahead of logging because logging is conditional on the user's settings.

## WMI API Settings Write/Read

The WMI API provides non-abstracted (raw) access to all settings instantiated by the Parental Controls infrastructure as defined in the Wpcsprov.mof schema file. The settings store exists in the \\root\\CIMV2\\Applications\\WindowsParentalControls namespace, with the following class definitions defining a schema. Extensibility elements are noted.

Per-computer:

-   WpcSystemSettings (one instance)
    -   AddUser() and RemoveUser() methods to create and delete parental controls settings for a given SID, respectively.
    -   Properties for current game ratings system in force, and tracking and notification related to admin checking of logs.
    -   Extensibility: Properties for read-only and read/write HTTP application and URL exemption lists for web content filtering, Web Content Filter override ID and name resource DLL path and ID, and custom log event number of fields and header name registration.
-   WpcRatingsSystem (one instance per each ratings system installed)
    -   WpcRating (one instance per rating level).
    -   WpcRatingDescriptor (one instance per rating descriptor).
-   Extensibility: WpcExtension (one instance per each Parental Controls Panel extensibility link added).
    -   Properties for GUID, subsystem, ID, image resource path, disabled state image resource path, executable path, display name resource DLL path and ID, subtitle resource DLL path and ID.

Per-controlled user:

-   WpcUserSettings (one instance per controlled user)
    -   Properties for owning SID, parental controls on/off flag, logging on/off flag, time limits on/off flag, overrides enabled flag, logon hours mask, and General Application Restrictions on/off flag.
    -   In Windows 8 the existing property represents the first half-hour for each hour. A new half-hour property has been added to represent the second half of each hour. An additional new property was introduced to represent daily time allowance.

        **Windows 7 and Windows Vista:** Timer restrictions supported 1 hour granularity.

-   WpcWebSettings (one instance per controlled user)
    -   Properties for owning SID, filter on/off flag, filter level, file downloads blocked flag, unrated sites blocked flag.
-   WpcUrlOverride (one instance per URL explicitly allowed or denied in URL override list used as allow/block list for web content filtering)
    -   Properties for owning SID, URL affected, allowed/blocked state.
-   WpcAppOverride (one instance per path explicitly allowed in General Application Restrictions application override list)
    -   Properties for owning SID. SAFER rule ID, path to application.
-   WpcGamesSettings (one instance per controlled user)
    -   Properties for owning SID, games permitted flag, GUID of ratings system for these settings, allow unrated games flag, ID of maximum allowed rating under current system, collection of denied descriptors.
-   WpcGameOverride (one instance per application ID explicitly allowed or denied)
    -   Properties for owning SID, application ID identifying game, allowed/denied state.

## Data Representation Notes

Several of the settings within the schema are constrained by the .mof file with attribute non\_null. These cannot be set to a null variant. For all non-array types, the Parental Controls code initializes values. For arrays, empty states may be written by using a null variant, empty variant, or zero-sized variant array. The WMI provider will normalize all of these to a null variant state representation on read.

## User Interface Extensibility Link Notes

Using WMI to register a UI extensibility link requires specifying the following information:

-   GUID - multiple links may share the same GUID if they are part of a common package or suite.
-   Subsystem - intended to indicate classifications of link types, such as suites or standalone compliant applications
-   Name resource DLL path and ID - specifies resource for display name to be displayed for the link.
-   Subtitle resource DLL path and ID - specifies resource for additional text below the name.
-   Image path - full path of a 24 × 24 pixel bitmap (BMP), with 8 bits-per-pixel color depth and preferably an alpha channel. This is specified in a manner consistent with shell extensions: <file system path>,<negative resource ID>. As an example: C:\\Windows\\System32\\Wpccpl.dll,-20.
-   Disabled image path - same as image path above, except variant of bitmap showing disabled state. This image is shown when parental controls is off.
-   Exe path - full path to an executable to be invoked by using ShellExecute(). This path must be specified with backslashes, or the link will not invoke the executable. Addition of a %SID% token after the exe path will result in the link execution substituting the SID string for the user for which the hub page is currently being viewed. The executable may then use the SID string to manage functionality for the specified user.

Application uninstallation must remove an extensibility link registration.

## Web Extensibility Link and Web Content Filter Override Notes

By setting the FilterID property to the same GUID as an existing registered UI extensibility link, the link displayed will be promoted from a generic link in Other Settings to the exclusive Web Restrictions link. This is a computer-wide setting, and so will cause the in-box Web Content Filter LSP to bypass all filtering for all controlled users. A descriptive name should also be set in the FilterName property, which is specified by a path to resource DLL and ID.

The Parental Controls system recommends the following from any overriding web filter:

-   Honor the overall Parental Controls on/off state for a user.
-   Honor the Activity Reporting settings for a user.
-   Monitor the FilterID property. If it changes from the vendor's specified GUID, another filter has taken ownership and the vendor's filter should disable itself. A COM interface has been added to reduce the overhead of checking periodically for this change versus a WMI call.
-   Highly recommended to honor both the read-only and read/write HTTP application and URL exemption list entries.
-   Recommended to honor the per-user URL override list (allow/block list).
-   Be robust to fast user switching.

Parental Controls does not place any limitations on how a web or other content filter plugs in to Windows for implementing filtering. Vendors may leverage their current investments or preferred technologies (LSP, TDI, other).

Uninstallation of the vendor's filter must unregister the FilterID and FilterName entries. This is performed by setting FilterID to GUID\_NULL and FilterName to a variant null. The in-box web content filter will then be re-enabled.

Note that re-enabling of the in-box web filter will only filter new sessions, and not sessions active from before the switch.

## Web Content Filter Allow/Block List Export/Import Format

This feature is not supported on Windows 8.

**Windows 7 and Windows Vista:** This feature is supported.

&lt;WebAddresses&gt;

<URL AllowBlock="1">https://alloweddomain.com/&lt;/URL&gt;

<URL AllowBlock="1">https://allowedurl.com/allowed/default.html&lt;/URL&gt;

<URL AllowBlock="2">https://blockeddomain.com/&lt;/URL&gt;

<URL AllowBlock="2">https://blockedurl.com/blocked/default.html&lt;/URL&gt;

&lt;/WebAddresses&gt;

## Application Restrictions Override Notes

Application restrictions overrides are set on a per user basis to allow specific binaries or paths. If a new parentally controlled user is configured and application restrictions overrides are needed for that user, it is recommended that the Windows Run key in the registry be used with a small application marked as requiring elevation deployed to write the overrides. This will result in a one-time credentials prompt to configure the overrides for the user, after which the target binaries for the overrides will not be a nuisance to users due to further administrator override prompts.

## Actions Required for Settings Changes to Become Effective

If an Administrator changes settings for a logged-in standard user, a warning message is generated. It states the settings changes may not take effect until the controlled user logs out and back in again. This is conservative design. Most settings will take effect nearly immediately while the controlled user is logged in. One exception is for games, where settings will take effect the next time the Games Explorer is run or invoking the game is attempted.

## Sample code

C++ samples are provided in the SDK demonstrating use of the settings extensibility features. Please see the Parental Controls Samples section.

## Independent Test Tools

Inspection of classes and instances is facilitated by the Wmimgmt.msc plug-in and the Wbemtest.exe tool.

## 64-Bit Considerations

64-bit Windows operating system versions currently have both a 32-bit WMI provider and a 64-bit provider installed.

## General Code Development and Debugging

If Visual Studio is used for settings management code development, local debugging will require running Visual Studio with administrator rights (invoking with Run as Administrator using command line or right-click option). This is due to process and message isolation implemented by UAC.

## Minimum Compliance API Settings Read

### Interfaces and Methods

The Compliance API controlled by header file Wpcapi.h provides simplified read-only access to the following settings by using COM interfaces.

[**IWindowsParentalControls**](/windows/desktop/api/Wpcapi/nn-wpcapi-iwindowsparentalcontrols) root interface methods provide access to:

-   IWPCSettings methods:
    -   IsLoggingRequired()—is activity reporting configured as on for the user?
    -   GetLastSettingsChangeTime()—application can be aware if any settings policies have changed since a previous check.
    -   GetRestrictions()—read whether web restrictions, time limits, game restrictions, or application restrictions are set to on.
-   IWPCWebSettings methods:
    -   GetSettings()– retrieves flags for filter on or off and downloads blocked.
    -   RequestURLOverride()—input a request into the administrator override (over-the-shoulder approval) mechanism that will present a dialog box that contains the URLs to be approved.
-   IWPCGamesSettings methods:
    -   IsBlocked()—for a given game application ID, is the game blocked by parental controls and for what reason.
-   GetVisibility()—provides information on whether the Parental Controls UI is currently hidden.
-   GetWebFilterInfo()—provides an interface for obtaining the ID of the currently active Web Content Filter.

### Sample code

C++ samples are provided in the SDK demonstrating use of the Compliance API. Please see the Parental Controls Samples section.

 

 




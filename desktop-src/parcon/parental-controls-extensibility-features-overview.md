---
description: Parental controls can be extended by using the settings and logging APIs.
ms.assetid: f0fc1b11-6de4-48f6-afc9-f05c8812d2bd
title: Parental Controls Extensibility Features Overview
ms.topic: article
ms.date: 05/31/2018
---

# Parental Controls Extensibility Features Overview

Parental controls can be extended by using the settings and logging APIs.

-   [Logging—Background](/windows)
-   [Logging Extensibility](#logging-extensibility)
-   [Parental Controls Panel General UI Extensibility Link Addition](#parental-controls-panel-general-ui-extensibility-link-addition)
-   [Web Content Filter Replacement](#web-content-filter-replacement)

## Logging—Background

Microsoft has defined a number of standard events to address common activities:

-   System: parental controls settings changes, account changes, system clock change, failed logon attempts.
-   User:
    -   System/time limits: logon times, logout, application run attempts, and application run duration (see note).
    -   Web restrictions: websites visited and blocked, file download attempts. Web browsers and browser-like applications do not need to log these, as the Web Content Filter LSP does so. Replacement web filters would need to generate these events.
    -   Games: games played and blocked, game end (events together provide duration played).
    -   Allow and block specific programs: run attempt, shutdown, blocked by General Application Restrictions.
    -   Instant Messaging: conversion initiation attempt, conversation join attempt, conversation leave, video/audio/game/short message service/file transfer/URL swap feature, contact list change attempt.
    -   Email: received or receive blocked, send attempt, contact list change attempt.
    -   Media: media played and attempted.

Not all of the previous events are suitable for use by applications. Account changes, the system clock change, and logon and logoff event logging are implemented only by the operating system and so are not exposed publicly.

> [!Note]  
> Instrumentation of application entry and exit events is available within Windows Vista, and is configured by Parental Controls to log this data.

 

## Logging Extensibility

A generic custom event is also defined with 3 tags/values available so ISVs usually will not need to define their own in a manifest. The Log Viewer will recognize and display the tag headers and values if the number of fields used (1 to 3) and headings for each field are registered using the WMI API. The generic Event Viewer may also be used to view custom events.

If the generic custom event is not suitable, an ISV can define its own by using an application manifest and it can register headers for up to three fields by using the same WMI API.

ISVs may choose to define their own events and consume them independently of the Log Viewer through public Windows APIs. This does not have the benefit of full log centralization.

## Parental Controls Panel General UI Extensibility Link Addition

A general-purpose user interface extensibility link is exposed by accessing settings through WMI, creating an extension instance from passed in name resource DLL path and ID, image (bitmap) path, disabled state image (bitmap) path, subtitle resource DLL path and ID, and executable path specifications. After registered, the link will appear in the More Settings area of the Parental Controls Panel, and clicking it will invoke the specified executable.

The executable path string may optionally include a token for the current user's SID to be substituted prior to invocation. This allows the link execution to operate in the context of the user for which the hub page is currently being viewed, if the executable needs to know the SID.

## Web Content Filter Replacement

As noted in the topic, [Parental Controls In-Box Restrictions and User Interfaces](parental-controls-in-box-restrictions-and-user-interfaces.md), the in-box Web Content Filter can be replaced with a vendor-supplied filter. This is performed by accessing settings through WMI to set a GUID and name owning the filtering.

The general UI extensibility mechanism is used to expose a third-party filter. This is the same mechanism as used for any extension that wants to appear in the More Settings section of the top-level Parental Control Panel. Taking the additional step of setting the same GUID and an appropriate name resource DLL path and ID into the system-level filter settings will cause the in-box displayed filter link to be hidden and the third-party entry to be shown at the top of the More Settings section. The name registered for the filter will be shown in the summary section.

Resetting the filter GUID and name path/ID settings will result in the in-box Web Content Filter re-establishing itself as the active filter and appearing again in the Windows Settings section.

Note that third-party filters are not constrained in the technologies used to plug into Windows communications. A filter must merely expose its settings by using an extensibility link and honor appropriate Parental Controls settings.

 

 

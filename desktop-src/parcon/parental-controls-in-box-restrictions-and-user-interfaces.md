---
description: Several restrictions implementations are provided.
ms.assetid: a00d9a3a-d052-492c-b9e7-3ecb1455a392
title: Parental Controls In-Box Restrictions & User Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Parental Controls In-Box Restrictions & User Interfaces

Several restrictions implementations are provided.

-   [Web Restrictions](#web-restrictions)
-   [Time Limits](#time-limits)
-   [Games](#games)
-   [Allow and Block Specific Programs](#allow-and-block-specific-programs)

## Web Restrictions

-   In-box Web Content Filter using a free dynamic rating service. Individually configurable per controlled user.
-   Filters all HTTP traffic when enabled, returns custom formatted page if blocked. Allows acceptable functionality with all major browsers. By monitoring all HTTP Get and Post requests for a page, allows individual webpage parts to be blocked.
-   Highly configurable by using user interface that allows or blocks URL lists, simplified rating category presets, or ActiveX control of 12+ categories, as well as a policy for blocking file downloads.

> [!Note]  
> Actual file download blocking requires applications to implement the restriction, complying with the provided setting.

 

-   Implemented as a Windows Filtering Platform (WFP) driver communicating with the Family Safety monitoring process running in the users' sessions. Implementation has changed from a Layered Service Provider (LSP) filter to a Windows Filtering Platform (WFP) driver communicating with the Family Safety monitoring process running in the users' sessions.

    **Windows 7 and Windows Vista:** Implemented as a Layered Service Provider (LSP) filter communicating with a low-rights service for overall management and monitoring. The filter remains in the LSP chain when disabled, but passes all traffic through. This implementation is supported only for the operating systems listed.

-   Applications may provide user interface to show partial page blocking and honor the policy to block file downloads. They may also invoke an API to allow the user to request permission to view a blocked page. This administrative override invokes a small application that shows the attempted URLs and that requests credentials to allow them.
-   An API is provided for special cases where an application needs to register to bypass filtering, or specific URLs are to be always allowed.
-   Because only one Web Content Filter should ever be running at a time, third parties may register as the active filter and disable the in-box filter. This extensibility, coupled with the ability to show a third-party filter in the UI, allows for simple replacement. Filters must remove their registration when uninstalled.

## Time Limits

-   The in-box time restrictions were enhanced by providing ability to control total amount of time per day computer can be used (time allowance) in addition to ability to control times when computer can be used (curfew) which was available in previous versions of Windows.
-   UI for curfew allows independent control for each day of the week with half-hour granularity
-   UI for time allowance allows controls for weekdays and weekends or independent control for each day of the week with 15 minute granularity
-   Fast User Switch (FUS) mechanism is no longer used to forcibly lock out or block login of the controlled user when in blocked time period. A switch to a separate desktop is used for these purposes. Note that the FUS does preserve the state of the user when locked out.

## Games

-   Works in conjunction with the Games Explorer.
-   Allows administrators to control which games may be played through a rich UI for selecting a games ratings system and level (plus descriptors if present), and/or by specifically allowing or blocking titles.
-   Metadata on games ratings are obtained in one of two ways:
    -   Supported titles deploy their own Game Definition Files (GDFs).
    -   Approximately 2000 legacy titles are covered by an in-box database.
-   Three mechanisms are used for enforcement:
    -   Deny ACLs for controlled user write access to the game folder.
    -   Process termination for legacy titles using application compatibility shim technology.
    -   Self-check API use by supported titles to block run.
-   Awareness of Time Limits events explained in the section above is recommended.
-   Documentation for GDFs and the Games Explorer will be provided primarily through DirectX SDK releases.

## Allow and Block Specific Programs

-   Also referred to as General Application Restrictions (GAR).
-   Off by default. If turned on, it only allows a controlled user to run applications approved by an administrator, with reasonable exceptions.
-   UI provides a list of program names with corresponding paths, each with an allow checkbox. A browse button is also provided.
-   Implemented using Software Restriction Policies (SRP), also known as SAFER:
    -   Prevents execution from all media (USB keys, floppy disks, and so on).
    -   Uses path rules to specify programs allowed to run.
    -   NTFS ACL write permissions are revoked from anything allowed for the controlled user to run.
    -   If blocked and subsequently overridden to allow, the application must be relaunched manually.
-   Exceptions include:
    -   All binaries required for a basic subset of Windows to function.
    -   All executable files that register by using an API are to be allowed for a given user.
    -   Games specified as being allowed under Games Restrictions.
-   Note that the RunAs command is blocked by design for a user when GAR is on.

 

 




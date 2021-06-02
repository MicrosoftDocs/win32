---
description: Parental Controls Top-Level User Interface
ms.assetid: c6dfd3bc-191f-42d1-b9de-cc85a2da0a99
title: Parental Controls Top-Level User Interface
ms.topic: article
ms.date: 05/31/2018
---

# Parental Controls Top-Level User Interface

The strong link between Family Safety and Windows user accounts has driven a combined category appearing as **User Accounts and Family Safety** in Control Panel for consumer-oriented SKUs of Windows Vista.

> [!Note]  
> The category will appear as **User Accounts** when a computer with domain-join capability is joined.

 

If a standard user account has not yet been set up for the controlled user, a link in Control Panel provides a simple workflow for adding a new parentally controlled account.

After an account is created, the Parental Controls Control Panel exposes the top-level user-facing functionality for the controlled user. Elements:

-   Overall Parental Controls restrictions on or off radio buttons.
-   Independent Activity Reporting on or off control radio buttons.
-   A Settings section with the Microsoft-implemented Web Restrictions link conditionally shown, and available core offline Microsoft-implemented restrictions types shown.
-   A More Settings area that appears if User Interface extensions are registered by Microsoft or third parties.
-   A summary status area showing the user name and tile, the View activity reports link, and the state of Parental Controls settings. If on, the display includes the Web Content Filter setting level (if the Microsoft filter is active) or filter name if overridden by a third-party extension, and state of offline settings for the user.

The overall Parental Controls enable radio button is initially set to the off state. When turned on by an administrator, Activity Reporting will also be on by default, but may be turned off independently. As with nearly all settings in Parental Controls, configuration may be performed programmatically through the available APIs.

 

 




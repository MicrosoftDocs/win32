---
title: Update Orchestrator API
description: UpdateOrchestrator schedules your background software updates with user impact in mind. 
ms.date: 12/01/2020
ms.topic: overview
---

# UpdateOrchestrator API

**UpdateOrchestrator** schedules your background software updates with user impact in mind. This API allows you to [specify actions](updateorchestratoractionkind.md), such as downloading or installing, along with their requirements in order to run updates at an optimal time that minimizes user-present impact. These features particularly benefit lower speed dual core CPUs with rotating HDD.

Windows 20H1 includes a first-generation solution for background software update use cases that were adopted by OS updates and Store App updates and exposes an initial ‘Limited Access’ version of this API for a select set of 3rd party background updaters of 'user-mode' apps as described below.

## Features

- Dynamically registers background software updaters
 
- Invokes registered background software updaters during optimal times, such as during user absence, to update 'user mode apps'.
    - Includes the ability to 'keep awake' on AC power to further reduce user-away impact.
 
- Operates on a Trust Model that only invokes trusted 3rd party registered background software updaters
    - There are substantial risks when exposing UpdateOrchestrator to any and all callers such as updating BIOS firmware or drivers when a user is not present.

## Developer Audience

> [!IMPORTANT]
> The UpdateOrchestrator API is currently a [limited access feature](/uwp/api/windows.applicationmodel.limitedaccessfeatures). This API will become publicly available in a future release.

Use UpdateOrchestrator API if you already have background software updaters for Win32 'user mode' applications such as Adobe's updater for Acrobat Reader or Valve's Steam. This interface is not needed for UWP/Store applications as the Microsoft Store already takes advantage of this functionality for background software updates.

To provide the best customer experience, this initial API release is scoped to a select set of registered updaters that meet the following criteria:

- Updates for 'user mode' applications only
- Do not involve BIOS/Firmware/Device or Software Drivers
    - Updating BIOS, firmware, or device/software drivers that have not passed a quality criteria pose a substantial risk, particularly when a user is not present. 
- Participating in the usage of this API entails being able to vouch for all content downloaded and installed by your background software updaters on users systems via audits. 

The initial release of UpdateOrchestrator API as limited access feature is only for updaters that meet above criteria at this time.

Our aim is to improve the functionality of this API and reduce impact from background software updates on Windows. We would appreciate your input through this [**brief survey**](https://aka.ms/UOAPISurvey) to help us understand how UpdateOrchestrator API can better serve your developer needs.


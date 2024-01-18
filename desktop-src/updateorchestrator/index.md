---
title: Update Orchestrator API
description: UpdateOrchestrator schedules your automatic software updates with user impact in mind. 
ms.date: 01/29/2020
ms.topic: overview
---

# UpdateOrchestrator API

**UpdateOrchestrator** schedules your automatic software updates with user impact in mind. This API allows you to [specify actions](updateorchestratoractionkind.md), such as downloading or installing, along with their requirements in order to run updates at an optimal time that minimizes user-present impact. These features particularly benefit lower performance systems with limited or slower computing resources.

Windows 20H1 includes a first-generation solution for automatic software update use cases that were adopted by OS updates and Store App updates and exposes an initial ‘Limited Access’ version of this API for a select set of updaters of 'user-mode' apps as described below.

## Features

- Dynamically registers software updaters
 
- Invokes registered software updaters during optimal times, such as during user absence, to update 'user mode apps'.
    - Includes the ability to 'keep awake' on AC power to further reduce user-away impact.

## Developer Audience

> [!IMPORTANT]
> The UpdateOrchestrator API is currently a [limited access feature](/uwp/api/windows.applicationmodel.limitedaccessfeatures). This API will become publicly available in a future release.

Use UpdateOrchestrator API if you already have background software updaters for Win32 'user mode' applications such as Adobe's updater for Acrobat Reader or Valve's Steam. This interface is not needed for UWP/Store applications as the Microsoft Store already takes advantage of this functionality for software updates.

To provide the best customer experience, this initial API release is scoped to a select set of registered updaters that meet the following criteria:

- Updates for 'user mode' applications only
- Do not involve BIOS/Firmware/Device or Software Drivers
    - Updating BIOS, firmware, or device/software drivers that have not passed a common quality criteria pose a substantial risk, particularly when a user is not present. 
- Participating in the usage of this API entails being able to vouch for all content downloaded and installed by your background software updaters on users systems via audits. 

The initial release of UpdateOrchestrator API as limited access feature is only for updaters that meet above criteria at this time.

Our aim is to improve the functionality of this API and reduce impact from multiple automatic software updaters on Windows. We would appreciate your input through this [**brief survey**](https://aka.ms/UOAPISurvey) to help us understand how UpdateOrchestrator API can better serve your developer needs.

## For OEMs wanting to Expedite Applications 

>[!IMPORTANT]
> Expediting Applications is only available for OEMs and only applicable in select regions. Expediting an application may have negative impacts to the out of box experience for new devices. This functionality is only available on select client builds.

OEMs can register an update to be expedited by writing a new key in the existing staging folder for expedited apps: HKLM\Software\Microsoft\WindowsUpdate\Orchestrator\UScheduler_OOBE 

Each OEM provider registration is in the form of a SubKey (with a unique name that will be used to identify this expedited app), and a set of registry values to indicate specific options for this update. The content of each key is in the following format: 

Key name:  Unique name for this expedited app 

Under Key name OEMs will need to create two additional keys:
- updaterPriority: Number to indicate relative priority of this update 
- expeditedPayload: JSON blob with options for this specific updater

Example: 
{   "PFN": "PFNName", 
    "Endpoint": “SSL_URI”, 
    "AllowedInOobe": false, 
    "MaxRetryCount": 3, 
    “TimeoutDurationInMinutes”: 15, 
    “ExcludedRegions”: [“CN”]   } 

Overview of used terms: 
| State  | Type | Key name | Description | 
| ------ | ---- | -------- | ----------- |
| Required | String | PFN | The Package Family Name of the app (ex MicrosoftTeams_example) |
| Required | String | Endpoint | A string URIs pointing to a location hosting an MSIX package. Must be an SSL URI. | 
| Optional | Boolean | AllowedInOobe | Whether this expedited app should run during user OOBE |
| Optional | Number | MaxRetryCount | The number of times this updater is allowed to retry after failure |
| Optional | Number | TimeoutDurationInMinutes | The duration to wait for this updater to complete work | 
| Optional | Array (String) | ExcludedRegions | CN, US for regions where this flow should not be executed | 

> [!IMPORTANT]
> We recommend against expediting mutilple applicaitons as this can have a significantly negative impact on the user experience when setting up a new device. 





 



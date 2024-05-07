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
> The **UpdateOrchestrator** API is part of a Limited Access Feature (see [LimitedAccessFeatures class](/uwp/api/windows.applicationmodel.limitedaccessfeatures)). For more information or to request an unlock token, please use the [LAF Access Token Request Form](https://go.microsoft.com/fwlink/?linkid=2271232&clcid=0x409).

Use UpdateOrchestrator API if you already have background software updaters for Win32 'user mode' applications such as Adobe's updater for Acrobat Reader or Valve's Steam. This interface is not needed for UWP/Store applications as the Microsoft Store already takes advantage of this functionality for software updates.

To provide the best customer experience, this initial API release is scoped to a select set of registered updaters that meet the following criteria:

- Updates for 'user mode' applications only
- Do not involve BIOS/Firmware/Device or Software Drivers
    - Updating BIOS, firmware, or device/software drivers that have not passed a common quality criteria pose a substantial risk, particularly when a user is not present. 
- Participating in the usage of this API entails being able to vouch for all content downloaded and installed by your background software updaters on users systems via audits. 

The initial release of UpdateOrchestrator API as limited access feature is only for updaters that meet above criteria at this time.

Our aim is to improve the functionality of this API and reduce impact from multiple automatic software updaters on Windows. We would appreciate your input through this [**brief survey**](https://aka.ms/UOAPISurvey) to help us understand how UpdateOrchestrator API can better serve your developer needs.

## Expediting OEM Apps via Universal Orchestrator framework

>[!IMPORTANT]
> Universal Orchestrator provides functionality to OEMs to register an application during the imaging process to perform a one-time expedited install / update.  This installation happens within 30 minutes of a user logging into a new device.  Be aware that expediting an application may have a negative performance impact to the out of box experience for new devices. This functionality is only available on select client builds, and in select regions.

### Requirements
To plug into the expedited app framework, the app must meet the following requirements:
- It must be a Store packaged app in MSIX format
- It must have a valid Product Family Name (PFN)

### Registration

OEMs can register an application to be expedited by writing a new key in the existing staging folder for expedited apps:   

> HKLM\Software\Microsoft\WindowsUpdate\Orchestrator\UScheduler_OOBE 

Each OEM provided registration is in the form of a SubKey (with a unique name that will be used to identify this expedited app), and a set of registry values to indicate specific options for this application. The content of each key is in the following format: 

**Key name:**  Unique name for this expedited app 

Under the Subkey for the expedite app registration, OEMs need to create two values:
- Value name: **updaterPriority**  
  Description: Number to indicate relative priority of this application update  
  Value type: REG_DWORD  
  Data:  A numeric value from 1 - 100. Lower values indicate a higher relative priority to other expedited apps.  
  
- Value name: **expeditedPayload**  
  Description: JSON blob with options for this specific updater  
  Value type: REG_SZ  
  Data: A string representing a valid JSON blob with options for this specific updater  

Overview of contents of the JSON blob: 

| State  | Type | Key name | Description | 
| ------ | ---- | -------- | ----------- |
| Required | String | PFN | The Package Family Name of the app (ex: Microsoft.WindowsStore_8wekyb3d8bbwe) |
| Required | String | Endpoint | A string URI pointing to a location hosting an MSIX package. Must be an SSL URI that begins with 'https'. | 
| Optional | Boolean | AllowedInOobe | Whether this expedited app should run during user OOBE |
| Optional | Number | MaxRetryCount | The number of times this updater is allowed to retry after failure.  Default is 1.  Maximum is 5. |
| Optional | Number | TimeoutDurationInMinutes | The duration in minutes to wait for this updater to complete work.  Default is 15.  Maximum is 30 | 
| Optional | Array (String) | ExcludedRegions | A JSON array of strings for regions where this app should not be expedited. Each entry in the array corresponds to the 2 letter ISO 3166-1 country code of the desired region. For example, `["US"]` would prevent this flow on devices where the region is United States. | 

Sample JSON payload:
````
{  
    "PFN": "PFNName",  
    "Endpoint": "SSL_URI",  
    "AllowedInOobe": false,  
    "MaxRetryCount": 3,  
    "TimeoutDurationInMinutes": 15,  
    "ExcludedRegions": ["CN", "FR"]   
}
````

### Execution
The Universal Orchestrator framework automatically invokes each of the registered apps, in sequence based on relative priority, within the first 30 minutes of a user reaching the Desktop on a new device (or during User OOBE if AllowedInOobe is set to true).  Each registered application added by the OEM registration process will be attempted until either:  
- It is successfully installed  
- It surpasses the maximum amount of failures specified in MaxRetryCount.  After each failure, the app will enter a cooldown period of 30 minutes before it is attempted again.

The Universal Orchestrator framework will not perform expedited attempts if any of the following conditions are true: 
- Device does not have internet access  
- Device is on a metered network  
- Device is on battery, and battery saver is enabled  
- Device is configured with a Windows Update Restricted Network Traffic policy  
- Device is configured with a CTA policy that is not set for AutoApprove  

In each of these cases, the Universal Orchestrator framework will keep the registrations in place until the device configuration allows expedited attempts to proceed.  

> [!IMPORTANT]
> Exercise caution when opting to expedite apps via this framework, as the update operations occur when the device may be in use and can cause a negative performance impact of the user experience on a new device.
 







 



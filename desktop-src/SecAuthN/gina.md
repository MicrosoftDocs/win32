---
description: The purpose of a GINA DLL is to provide customizable user identification and authentication procedures. The default GINA does this by delegating SAS event monitoring to Winlogon, which receives and processes CTL+ALT+DEL secure attention sequences (SASs).
ms.assetid: 035e9c8b-2490-438d-8f02-7e0f039f960f
title: GINA
ms.topic: article
ms.date: 05/31/2018
---

# GINA

The [*GINA*](/windows/desktop/SecGloss/g-gly) operates in the [*context*](/windows/desktop/SecGloss/c-gly) of the [*Winlogon*](/windows/desktop/SecGloss/w-gly) process and, as such, the GINA DLL is loaded very early in the boot process. The GINA DLL must follow rules so that the integrity of the system is maintained, particularly with respect to interaction with the user.

> [!Note]  
> GINA DLLs are ignored in Windows Vista.

 

The most common use of the GINA is to communicate with an external device such as a smart-card [*reader*](/windows/desktop/SecGloss/r-gly). It is essential to set the start parameter for the device driver to system (Winnt.h: SERVICE\_SYSTEM\_START) to ensure that the driver is loaded by the time the GINA is invoked.

The purpose of a GINA DLL is to provide customizable user identification and authentication procedures. The default GINA does this by delegating SAS event monitoring to Winlogon, which receives and processes CTL+ALT+DEL [*secure attention sequences*](/windows/desktop/SecGloss/s-gly) (SASs). A custom GINA is responsible for setting itself up to receive SAS events (other than the default CTRL+ALT+DEL SAS event) and notifying Winlogon when SAS events occur. Winlogon will evaluate its state to determine what is required to process the custom GINA's SAS. This processing usually includes calls to the GINA's SAS processing functions.

For information about specific GINA export functions, see [GINA Export Functions](authentication-functions.md). For information about using GINA structures to pass information, see [GINA Structures](authentication-structures.md).



| Topic                                                                             | Description                                                                     |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [Loading and Running a GINA DLL](loading-and-running-a-gina-dll.md)<br/>   | Which registry key value to alter to load and run a custom GINA DLL.<br/> |
| [Building and Testing a GINA DLL](building-and-testing-a-gina-dll.md)<br/> | How to test a GINA DLL.<br/>                                              |



 

 


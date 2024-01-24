---
description: Fault Tolerant Heap
ms.assetid: f1ac375a-3f08-49cd-8752-6f55db24a60c
title: Fault Tolerant Heap
ms.topic: article
ms.date: 05/31/2018
---

# Fault Tolerant Heap

## Affected Platforms

**Clients -** Windows 7  

## Feature Impact

 **Severity -** Medium  
**Frequency -** Low  


## Description

The Fault Tolerant Heap (FTH) is a subsystem of Windows 7 responsible for monitoring application crashes and autonomously applying mitigations to prevent future crashes on a per application basis. For the vast majority of users, FTH will function with no need for intervention or change on their part. However, in some cases, application developers and software testers may need to override the default behavior of this system.

## Solution

**Viewing Fault Tolerant Heap activity**

Fault Tolerant Heap logs information when the service starts, stops, or starts mitigating problems for a new application. To view this information, follow these steps:

1.  Click the Start menu.
2.  Right-click **Computer** and click **Manage**.
3.  Click **Event Viewer** > **Applications and Services Logs** > **Microsoft** > **Windows > Fault-Tolerant-Heap**
4.  View FTH Events.

The service stop and start events contain no additional data. The FTH Enabled event contains the Process ID (PID), the process image name, and the process instance start time.

**Disabling Fault Tolerant Heap**

**Caution** Serious problems may occur if you modify the registry incorrectly by using Registry Editor or by using another method. These problems may require you to reinstall the operating system. Microsoft cannot guarantee that these problems can be solved. Modify the registry at your own risk.  
 To disable Fault Tolerant Heap entirely on a system, set the REG\_DWORD value **HKLM\\Software\\Microsoft\\FTH\\Enabled** to **0**.

After changing this value, restart the system. FTH will no longer activate for new applications.

**Resetting the list of applications tracked by FTH**

Fault Tolerant heap is self-managing and will autonomously stop applying in the case that mitigations are not effective for a given application. However, if you need to reset the list of applications for which FTH is mitigating problems (for example, if you are testing an application and need to reproduce a crash that FTH is mitigating), you can run the following command from an elevated command prompt:  **Rundll32.exe fthsvc.dll,FthSysprepSpecialize**  
**Caution** Running this command will clear all FTH applications, so applications that are currently functioning properly may begin to crash again after running this command.  

 

 




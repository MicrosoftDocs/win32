---
title: Configuring System Restore
description: System Restore uses Windows Management Instrumentation (WMI) to provide a scriptable way of configuring and using its functionality. It exposes two classes, SystemRestore and SystemRestoreConfig, in the root\\default namespace.
ms.assetid: b510c5b7-71ec-47f9-b567-45fde8c79f57
ms.topic: article
ms.date: 05/31/2018
---

# Configuring System Restore

System Restore uses [Windows Management Instrumentation](/windows/desktop/WmiSdk/wmi-start-page) (WMI) to provide a scriptable way of configuring and using its functionality. It exposes two classes, [**SystemRestore**](systemrestore.md) and [**SystemRestoreConfig**](systemrestoreconfig.md), in the root\\default namespace.

The [**SystemRestore**](systemrestore.md) class provides methods for the following tasks:

-   Disabling and enabling monitoring
-   Listing available restore points
-   Initiating a restore on the local system
-   Retrieving the status of the last system restore

The [**SystemRestoreConfig**](systemrestoreconfig.md) class provides properties for controlling the frequency of scheduled restore point creation and the amount of disk space consumed by System Restore on each drive.

Both classes can be accessed remotely using standard WMI techniques. For a complete description of WMI, see [Windows Management Instrumentation](/windows/desktop/WmiSdk/wmi-start-page).

 

 
---
description: During system boot, the SCM starts all auto-start services and the services on which they depend. For example, if an auto-start service depends on a demand-start service, the demand-start service is also started automatically.
ms.assetid: 8aa60e96-a35e-4670-832c-c045d0903618
title: Automatically Starting Services
ms.topic: article
ms.date: 05/31/2018
---

# Automatically Starting Services

During system boot, the SCM starts all auto-start services and the services on which they depend. For example, if an auto-start service depends on a demand-start service, the demand-start service is also started automatically.

The load order is determined by the following:

1.  The order of groups in the load ordering group list. This information is stored in the **ServiceGroupOrder** value in the following registry key:

    **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**

    To specify the load ordering group for a service, use the *lpLoadOrderGroup* parameter of the [**CreateService**](/windows/desktop/api/Winsvc/nf-winsvc-createservicea) or [**ChangeServiceConfig**](/windows/desktop/api/Winsvc/nf-winsvc-changeserviceconfiga) function.

2.  The order of services within a group specified in the tags order vector. This information is stored in the **GroupOrderList** value in the following registry key:

    **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**

3.  The dependencies listed for each service.

When the boot is complete, the system executes the boot verification program specified by the **BootVerificationProgram** value of the following registry key: **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control**.

By default, this value is not set. The system simply reports that the boot was successful after the first user has logged on. You can supply a boot verification program that checks the system for problems and reports the boot status to the SCM using the [**NotifyBootConfigStatus**](/windows/desktop/api/Winsvc/nf-winsvc-notifybootconfigstatus) function.

After a successful boot, the system saves a clone of the database in the last-known-good (LKG) configuration. The system can restore this copy of the database if changes made to the active database cause the system reboot to fail. The following is the registry key for this database:

**HKEY\_LOCAL\_MACHINE\\SYSTEM\\ControlSet*XXX*\\Services**

where *XXX* is the value saved in the following registry value: **HKEY\_LOCAL\_MACHINE\\System\\Select\\LastKnownGood**.

If an auto-start service with a SERVICE\_ERROR\_CRITICAL error control level fails to start, the SCM reboots the computer using the LKG configuration. If the LKG configuration is already being used, the boot fails.

An auto-start service can be configured as a delayed auto-start service by calling the [**ChangeServiceConfig2**](/windows/desktop/api/Winsvc/nf-winsvc-changeserviceconfig2a) function with SERVICE\_CONFIG\_DELAYED\_AUTO\_START\_INFO. This change takes effect after the next system boot. For more information, see [**SERVICE\_DELAYED\_AUTO\_START\_INFO**](/windows/desktop/api/Winsvc/ns-winsvc-service_delayed_auto_start_info).

 

 




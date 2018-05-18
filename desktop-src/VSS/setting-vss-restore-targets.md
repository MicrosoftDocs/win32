---
Description: 'The IVssComponent interface enables a writer to fine-tune exactly how files are restored on a component-by-component basis.'
ms.assetid: '362c6f44-ca67-4043-8d2c-4e46b5c8edd3'
title: Setting VSS Restore Targets
---

# Setting VSS Restore Targets

The [**IVssComponent**](ivsscomponent.md) interface enables a writer to fine-tune exactly how files are restored on a component-by-component basis.

Because it is possible that the system configuration during restore is something other than that anticipated during backup, the restore target mechanism is provided.

It allows writers to call [**IVssComponent::SetRestoreTarget**](ivsscomponent-setrestoretarget.md) to change how those components that are [*explicitly included*](vssgloss-e.md#base-vssgloss-explicit-component-inclusion) in the Backup Components Document are restored. This also changes the restoration mechanism used on those components that are [*implicitly included*](vssgloss-i.md#base-vssgloss-implicit-component-inclusion).

File restoration that takes place during a system reboot (under the [**VSS\_RESTOREMETHOD\_ENUM**](vss-restoremethod-enum.md) enumeration values VSS\_RME\_RESTORE\_AT\_REBOOT and VSS\_RME\_RESTORE\_AT\_REBOOT\_IF\_CANNOT\_REPLACE) cannot be affected by restore targets because there are no running VSS services when **MoveFileEx** copies files to their final location.

Similarly, VSS\_RME\_CUSTOM restores may or may not be affected, because each custom restore is specific to a given writer and can choose to respect or ignore restore targets.

Requesters and writers can use [**IVssComponent::GetRestoreTarget**](ivsscomponent-getrestoretarget.md) to check the restore target of a component set.

[**IVssComponent**](ivsscomponent.md) supports the following restore targets, which can be set on a component set by component set basis:

-   VSS\_RT\_ORIGINAL. The restore method specified by the [**VSS\_RESTOREMETHOD\_ENUM**](vss-restoremethod-enum.md) enumeration will be respected.
-   VSS\_RT\_ALTERNATE. The files are restored to a location determined from an existing alternate location mapping. If an alternate location mapping matching a path in a component set subcomponent exists, restore to the alternate location if possible; otherwise, return an error.

 

 




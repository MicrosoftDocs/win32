---
title: Using the Hyper-V WMI Provider
description: Using the Hyper-V WMI Provider
ms.assetid: '3698812d-74d0-40e5-80bf-c820d7eb0d2a'
keywords: ["Hyper-V Hyper-V , using", "Hyper-V Hyper-V , examples"]
---

# Using the Hyper-V WMI Provider

The following topic describes considerations in backing up and restoring virtual machines in Hyper-V:

-   [Backing Up and Restoring Virtual Machines](backing-up-and-restoring-virtual-machines.md)

The following topics contain sample code that demonstrates the use of the WMI classes for this provider:

-   [Exporting a Snapshot of a Virtual Machine](exporting-virtual-machines.md)
-   [Exporting the Configuration of a Virtual Machine](exporting-the-configuration-of-a-virtual-machine.md)
-   [Getting the Virtual System DNS Name](getting-the-virtual-system-dns-name.md)
-   [Importing Virtual Machines](importing-virtual-machines.md)
-   [Querying Networking Objects](querying-networking-objects.md)

The following reference topics contain sample code that demonstrate how to call the method:

-   [**Msvm\_ComputerSystem**](msvm-computersystem.md) class
    -   [**RequestStateChange**](requeststatechange-msvm-computersystem.md)
-   [**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md) class
    -   [**CompactVirtualHardDisk**](compactvirtualharddisk-msvm-imagemanagementservice.md)
    -   [**ConvertVirtualHardDisk**](convertvirtualharddisk-msvm-imagemanagementservice.md)
    -   [**CreateDifferencingVirtualHardDisk**](createdifferencingvirtualharddisk-msvm-imagemanagementservice.md)
    -   [**CreateDynamicVirtualHardDisk**](createdynamicvirtualharddisk-msvm-imagemanagementservice.md)
    -   [**CreateFixedVirtualHardDisk**](createfixedvirtualharddisk-msvm-imagemanagementservice.md)
    -   [**CreateVirtualFloppyDisk**](createvirtualfloppydisk-msvm-imagemanagementservice.md)
    -   [**ExpandVirtualHardDisk**](expandvirtualharddisk-msvm-imagemanagementservice.md)
    -   [**GetVirtualHardDiskInfo**](getvirtualharddiskinfo-msvm-imagemanagementservice.md)
    -   [**MergeVirtualHardDisk**](mergevirtualharddisk-msvm-imagemanagementservice.md)
    -   [**Mount**](mount-msvm-imagemanagementservice.md)
    -   [**ReconnectParentVirtualHardDisk**](reconnectparentvirtualharddisk-msvm-imagemanagementservice.md)
    -   [**Unmount**](unmount-msvm-imagemanagementservice.md)
    -   [**ValidateVirtualHardDisk**](validatevirtualharddisk-msvm-imagemanagementservice.md)
-   [**Msvm\_Keyboard**](msvm-keyboard.md) class
    -   [**PressKey**](presskey-msvm-keyboard.md)
    -   [**TypeText**](typetext-msvm-keyboard.md)
-   [**Msvm\_SyntheticMouse**](msvm-syntheticmouse.md) class
    -   [**ClickButton**](clickbutton-msvm-syntheticmouse.md)
-   [**Msvm\_VirtualSwitchManagementService**](msvm-virtualswitchmanagementservice.md) class
    -   [**BindExternalEthernetPort**](bindexternalethernetport-msvm-virtualswitchmanagementservice.md)
    -   [**ConnectSwitchPort**](connectswitchport-msvm-virtualswitchmanagementservice.md)
    -   [**CreateInternalEthernetPort**](createinternalethernetport-msvm-virtualswitchmanagementservice.md)
    -   [**CreateInternalEthernetPortDynamicMac**](createinternalethernetportdynamicmac-msvm-virtualswitchmanagementservice.md)
    -   [**CreateSwitch**](createswitch-msvm-virtualswitchmanagementservice.md)
    -   [**CreateSwitchPort**](createswitchport-msvm-virtualswitchmanagementservice.md)
    -   [**DeleteInternalEthernetPort**](deleteinternalethernetport-msvm-virtualswitchmanagementservice.md)
    -   [**DeleteSwitch**](deleteswitch-msvm-virtualswitchmanagementservice.md)
    -   [**DeleteSwitchPort**](deleteswitchport-msvm-virtualswitchmanagementservice.md)
    -   [**DisconnectSwitchPort**](disconnectswitchport-msvm-virtualswitchmanagementservice.md)
    -   [**SetupSwitch**](setupswitch-msvm-virtualswitchmanagementservice.md)
    -   [**TeardownSwitch**](teardownswitch-msvm-virtualswitchmanagementservice.md)
    -   [**UnbindExternalEthernetPort**](unbindexternalethernetport-msvm-virtualswitchmanagementservice.md)
-   [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class
    -   [**AddKvpItems**](addkvpitems-msvm-virtualsystemmanagementservice.md)
    -   [**AddVirtualSystemResources**](addvirtualsystemresources-msvm-virtualsystemmanagementservice.md)
    -   [**ApplyVirtualSystemSnapshot**](applyvirtualsystemsnapshot-msvm-virtualsystemmanagementservice.md)
    -   [**CreateVirtualSystemSnapshot**](createvirtualsystemsnapshot-msvm-virtualsystemmanagementservice.md)
    -   [**DefineVirtualSystem**](definevirtualsystem-msvm-virtualsystemmanagementservice.md)
    -   [**DestroyVirtualSystem**](destroyvirtualsystem-msvm-virtualsystemmanagementservice.md)
    -   [**ExportVirtualSystem**](exportvirtualsystem-msvm-virtualsystemmanagementservice.md)
    -   [**ExportVirtualSystemEx**](msvm-virtualsystemmanagementservice-exportvirtualsystemex.md)
    -   [**GetSummaryInformation**](getsummaryinformation-msvm-virtualsystemmanagementservice.md)
    -   [**GetVirtualSystemImportSettingData**](msvm-virtualsystemmanagementservice-getvirtualsystemimportsettingdata.md)
    -   [**GetVirtualSystemThumbnailImage**](getvirtualsystemthumbnailimage-msvm-virtualsystemmanagementservice.md)
    -   [**ImportVirtualSystem**](importvirtualsystem-msvm-virtualsystemmanagementservice.md)
    -   [**ImportVirtualSystemEx**](msvm-virtualsystemmanagementservice-importvirtualsystemex.md)
    -   [**ModifyKvpItems**](modifykvpitems-msvm-virtualsystemmanagementservice.md)
    -   [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md)
    -   [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md)
    -   [**RemoveKvpItems**](removekvpitems-msvm-virtualsystemmanagementservice.md)
    -   [**RemoveVirtualSystemResources**](removevirtualsystemresources-msvm-virtualsystemmanagementservice.md)
    -   [**RemoveVirtualSystemSnapshot**](removevirtualsystemsnapshot-msvm-virtualsystemmanagementservice.md)
    -   [**RemoveVirtualSystemSnapshotTree**](removevirtualsystemsnapshottree-msvm-virtualsystemmanagementservice.md)

The C# samples reference some utilities; see [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).

 

 





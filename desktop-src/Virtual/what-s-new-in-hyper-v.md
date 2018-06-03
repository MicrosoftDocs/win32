---
title: What's New in Hyper-V WMI Provider
description: Windows Server 2008 R2 introduced the following changes to the Hyper-V WMI provider.
ms.assetid: cfb88fe1-297e-4ece-b928-523583c19329
keywords:
- What's New in Hyper-V WMI Provider Hyper-V
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Hyper-V WMI Provider

Windows Server 2008 R2 introduced the following changes to the Hyper-V WMI provider:

-   [New Hyper-V Classes](#new-hyper-v-classes)
-   [New Hyper-V Methods](#new-hyper-v-methods)
-   [New Hyper-V Properties](#new-hyper-v-properties)
-   [Modifications to an Existing Hyper-V Method](#modifications-to-an-existing-hyper-v-method)
-   [Modifications to Existing Hyper-V Properties](#modifications-to-existing-hyper-v-properties)

## New Hyper-V Classes

-   [**Msvm\_SystemExportSettingData**](msvm-systemexportsettingdata.md)
-   [**Msvm\_VirtualSystemExportSettingData**](msvm-virtualsystemexportsettingdata.md)
-   [**Msvm\_VirtualSystemImportSettingData**](msvm-virtualsystemimportsettingdata.md)

## New Hyper-V Methods

-   [**Msvm\_Keyboard**](msvm-keyboard.md) class—[**TypeScancodes**](msvm-keyboard-typescancodes.md) method added
-   [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class
    -   [**ApplyVirtualSystemSnapshotEx**](msvm-virtualsystemmanagementservice-applyvirtualsystemsnapshotex.md) method
    -   [**CheckSystemCompatibilityInfo**](msvm-virtualsystemmanagementservice-checksystemcompatibilityinfo.md) method
    -   [**ExportVirtualSystemEx**](msvm-virtualsystemmanagementservice-exportvirtualsystemex.md) method
    -   [**GetSystemCompatibilityInfo**](msvm-virtualsystemmanagementservice-getsystemcompatibilityinfo.md) method
    -   [**GetVirtualSystemImportSettingData**](msvm-virtualsystemmanagementservice-getvirtualsystemimportsettingdata.md) method
    -   [**ImportVirtualSystemEx**](msvm-virtualsystemmanagementservice-importvirtualsystemex.md) method

## New Hyper-V Properties

In addition to the properties added with the new Hyper-V classes listed above, the following properties were added:

-   [**Msvm\_DynamicForwardingEntry**](msvm-dynamicforwardingentry.md) class—**VlanId** property
-   [**Msvm\_KvpExchangeComponentSettingData**](msvm-kvpexchangecomponentsettingdata.md) class—**HostOnlyItems** property
-   [**Msvm\_ProcessorSettingData**](msvm-processorsettingdata.md) class—**LimitProcessorFeatures** property
-   [**Msvm\_ResourceAllocationSettingData**](msvm-resourceallocationsettingdata.md) class—**VirtualSystemIdentifiers** property
-   [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class:
    -   **OperationalStatus** property
    -   **StatusDescriptions** property
-   [**Msvm\_SwitchPort**](msvm-switchport.md) class:
    -   **AllowMacSpoofing** property
    -   **ChimneyOffloadLimit** property
    -   **ChimneyOffloadUsage** property
    -   **ChimneyOffloadWeight** property
    -   **VMQOffloadLimit** property
    -   **VMQOffloadUsage** property
    -   **VMQOffloadWeight** property
-   [**Msvm\_VirtualSwitch**](msvm-virtualswitch.md) class:
    -   **MaxChimneyOffloads** property
    -   **MaxVMQOffloads** property
-   [**Msvm\_VirtualSystemGlobalSettingData**](msvm-virtualsystemglobalsettingdata.md) class is now derived from the [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) class instead of the [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911) class. This adds these properties inherited from the **CIM\_VirtualSystemSettingData** class:

    -   **AutoActivate** property
    -   **CreationTime** property
    -   **OtherVirtualSystemType** property
    -   **SettingType** property
    -   **SystemName** property
    -   **VirtualSystemType** property

    In addition, the **AllowFullSCSICommandSet** and **Version** properties were added.

-   [**Msvm\_VirtualSystemManagementServiceSettingData**](msvm-virtualsystemmanagementservicesettingdata.md) class—**NumaSpanningEnabled** property

## Modifications to an Existing Hyper-V Method

-   [**Msvm\_ProcessorPool**](msvm-processorpool.md) class—[**CalculatePossibleReserve**](calculatepossiblereserve-msvm-processorpool.md) method now computes reserve.

## Modifications to Existing Hyper-V Properties

-   [**Msvm\_ComputerSystem**](msvm-computersystem.md) class:
    -   **EnabledState** property—supported values changed.
    -   **HealthState** property—supported values changed.
    -   **OperationalStatus** property—supported values changed for **OperationalStatus**\[0\] and **OperationalStatus**\[1\] was added.
    -   **RequestedState** property—supported values changed.
-   [**Msvm\_KvpExchangeDataItem**](msvm-kvpexchangedataitem.md) class—new value for **Source** property

 

 





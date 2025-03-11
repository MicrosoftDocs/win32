---
description: Hardware information for a network adapter.
ms.assetid: da286242-935a-4f41-af52-22189171d780
title: MSFT\_NetAdapterHardwareInfoSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterHardwareInfoSettingData
- MSFT_NetAdapterHardwareInfoSettingData.NoInterrupt
- MSFT_NetAdapterHardwareInfoSettingData.LineBasedInterrupts
- MSFT_NetAdapterHardwareInfoSettingData.MsiSupported
- MSFT_NetAdapterHardwareInfoSettingData.MsiEnabled
- MSFT_NetAdapterHardwareInfoSettingData.MsiXSupported
- MSFT_NetAdapterHardwareInfoSettingData.MsiXEnabled
- MSFT_NetAdapterHardwareInfoSettingData.NumMsixTableEntries
- MSFT_NetAdapterHardwareInfoSettingData.NumMsiMessages
- MSFT_NetAdapterHardwareInfoSettingData.NumaNode
- MSFT_NetAdapterHardwareInfoSettingData.LocationInformationString
- MSFT_NetAdapterHardwareInfoSettingData.SegmentNumber
- MSFT_NetAdapterHardwareInfoSettingData.BusNumber
- MSFT_NetAdapterHardwareInfoSettingData.DeviceNumber
- MSFT_NetAdapterHardwareInfoSettingData.FunctionNumber
- MSFT_NetAdapterHardwareInfoSettingData.SlotNumber
- MSFT_NetAdapterHardwareInfoSettingData.PciDeviceType
- MSFT_NetAdapterHardwareInfoSettingData.PciCurrentSpeedAndMode
- MSFT_NetAdapterHardwareInfoSettingData.PciXCurrentSpeedAndMode
- MSFT_NetAdapterHardwareInfoSettingData.PciExpressCurrentPayloadSize
- MSFT_NetAdapterHardwareInfoSettingData.PciExpressMaxPayloadSize
- MSFT_NetAdapterHardwareInfoSettingData.PciExpressMaxReadRequestSize
- MSFT_NetAdapterHardwareInfoSettingData.PciExpressCurrentLinkSpeedEncoded
- MSFT_NetAdapterHardwareInfoSettingData.PciExpressCurrentLinkWidth
- MSFT_NetAdapterHardwareInfoSettingData.PciExpressMaxLinkSpeedEncoded
- MSFT_NetAdapterHardwareInfoSettingData.PciExpressMaxLinkWidth
- MSFT_NetAdapterHardwareInfoSettingData.PciExpressVersion
- MSFT_NetAdapterHardwareInfoSettingData.LineBasedInterruptSupported
- MSFT_NetAdapterHardwareInfoSettingData.MsiInterruptSupported
- MSFT_NetAdapterHardwareInfoSettingData.MsiXInterruptSupported
- MSFT_NetAdapterHardwareInfoSettingData.MaxInterruptMessages
- MSFT_NetAdapterHardwareInfoSettingData.MsixMessageAffinityArray
- MSFT_NetAdapterHardwareInfoSettingData.Dma64BitSupported
- MSFT_NetAdapterHardwareInfoSettingData.SriovSupport
- MSFT_NetAdapterHardwareInfoSettingData.S0WakeupSupported
- MSFT_NetAdapterHardwareInfoSettingData.PciDeviceLabelID
- MSFT_NetAdapterHardwareInfoSettingData.PciDeviceLabelString
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterHardwareInfoSettingData class

Hardware information for a network adapter

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterHardwareInfoSettingData : MSFT_NetAdapterSettingData
{
  boolean NoInterrupt;
  boolean LineBasedInterrupts;
  boolean MsiSupported;
  boolean MsiEnabled;
  boolean MsiXSupported;
  boolean MsiXEnabled;
  uint32  NumMsixTableEntries;
  uint32  NumMsiMessages;
  uint16  NumaNode;
  string  LocationInformationString;
  uint32  SegmentNumber;
  uint32  BusNumber;
  uint32  DeviceNumber;
  uint32  FunctionNumber;
  uint32  SlotNumber;
  uint32  PciDeviceType;
  uint32  PciCurrentSpeedAndMode;
  uint32  PciXCurrentSpeedAndMode;
  uint32  PciExpressCurrentPayloadSize;
  uint32  PciExpressMaxPayloadSize;
  uint32  PciExpressMaxReadRequestSize;
  uint32  PciExpressCurrentLinkSpeedEncoded;
  uint32  PciExpressCurrentLinkWidth;
  uint32  PciExpressMaxLinkSpeedEncoded;
  uint32  PciExpressMaxLinkWidth;
  uint32  PciExpressVersion;
  boolean LineBasedInterruptSupported;
  boolean MsiInterruptSupported;
  boolean MsiXInterruptSupported;
  uint32  MaxInterruptMessages;
  string  MsixMessageAffinityArray[];
  boolean Dma64BitSupported;
  uint32  SriovSupport;
  boolean S0WakeupSupported;
  uint32  PciDeviceLabelID;
  string  PciDeviceLabelString;
};
```

## Members

The **MSFT\_NetAdapterHardwareInfoSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterHardwareInfoSettingData** class has these properties.

<dl> <dt>

**BusNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The bus number of a PCI network adapter.

</dd> <dt>

**DeviceNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The device number of a PCI network adapter.

</dd> <dt>

**Dma64BitSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if a device can do 64 bit DMA.

</dd> <dt>

**FunctionNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The function number of a PCI network adapter.

</dd> <dt>

**LineBasedInterrupts**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Using line based interrupts.

</dd> <dt>

**LineBasedInterruptSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If True, line-based interrupts are supported.

</dd> <dt>

**LocationInformationString**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The location information for a PCI network adapter. This string includes bus, device and function number for the network adapter as displayed in device manager.

</dd> <dt>

**MaxInterruptMessages**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of message interrupts a device supports in hardware. Valid only if the device supports message interrupts.

</dd> <dt>

**MsiEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

MSI is enabled

</dd> <dt>

**MsiInterruptSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If True, MSI interrupts are supported.

</dd> <dt>

**MsiSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

MSI supported.

</dd> <dt>

**MsiXEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

MSI-X Enabled.

</dd> <dt>

**MsiXInterruptSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If True, MSI-X interrupts are supported.

</dd> <dt>

**MsixMessageAffinityArray**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of processor affinity masks of MSI-X messages allocated by the network adapter driver.

</dd> <dt>

**MsiXSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

MSI-X supported.

</dd> <dt>

**NoInterrupt**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Not using interrupts.

</dd> <dt>

**NumaNode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The NUMA node of the network adapter.

</dd> <dt>

**NumMsiMessages**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of MSI messages allocated by the network adapter driver.

</dd> <dt>

**NumMsixTableEntries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of MSI-X table entries supported by the hardware.

</dd> <dt>

**PciCurrentSpeedAndMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current speed and mode, valid only for conventional PCI devices

<dl> <dt>

<span id="Conventional_PCI_33MHz"></span><span id="conventional_pci_33mhz"></span><span id="CONVENTIONAL_PCI_33MHZ"></span>**Conventional PCI 33MHz** (0)
</dt> <dt>

<span id="Conventional_PCI_66MHz_"></span><span id="conventional_pci_66mhz_"></span><span id="CONVENTIONAL_PCI_66MHZ_"></span>**Conventional PCI 66MHz** (1 )
</dt> </dl>

</dd> <dt>

**PciDeviceLabelID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property provides the unique ID associated with a PCI device.

</dd> <dt>

**PciDeviceLabelString**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property provides an identifying string associated with a PCI device.

</dd> <dt>

**PciDeviceType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of PCI device.

<dl> <dt>

<span id="Conventional_PCI"></span><span id="conventional_pci"></span><span id="CONVENTIONAL_PCI"></span>**Conventional PCI** (0)
</dt> <dt>

<span id="PCI-X"></span><span id="pci-x"></span>**PCI-X** (1)
</dt> <dt>

<span id="PCI_Express_endpoint"></span><span id="pci_express_endpoint"></span><span id="PCI_EXPRESS_ENDPOINT"></span>**PCI Express endpoint** (2)
</dt> <dt>

<span id="PCI_Express_legacy_endpoint"></span><span id="pci_express_legacy_endpoint"></span><span id="PCI_EXPRESS_LEGACY_ENDPOINT"></span>**PCI Express legacy endpoint** (3)
</dt> <dt>

<span id="PCI_Express_Root_Complex_integrated_endpoint"></span><span id="pci_express_root_complex_integrated_endpoint"></span><span id="PCI_EXPRESS_ROOT_COMPLEX_INTEGRATED_ENDPOINT"></span>**PCI Express Root Complex integrated endpoint** (4)
</dt> <dt>

<span id="PCI_Express_treated_as_PCI"></span><span id="pci_express_treated_as_pci"></span><span id="PCI_EXPRESS_TREATED_AS_PCI"></span>**PCI Express treated as PCI** (5 )
</dt> </dl>

</dd> <dt>

**PciExpressCurrentLinkSpeedEncoded**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current link speed encoded, valid only for PCI-E devices.

<dl> <dt>

<span id="2.5_Gbps"></span><span id="2.5_gbps"></span><span id="2.5_GBPS"></span>**2.5 Gbps** (1)
</dt> <dt>

<span id="5_Gbps_"></span><span id="5_gbps_"></span><span id="5_GBPS_"></span>**5 Gbps** (2)
</dt> </dl>

</dd> <dt>

**PciExpressCurrentLinkWidth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current link width (1, 2, 4, .., 32), valid only for PCI-E devices.

</dd> <dt>

**PciExpressCurrentPayloadSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current payload size in bytes; valid only for PCI-E devices.

</dd> <dt>

**PciExpressMaxLinkSpeedEncoded**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum link speed encoded, valid only for PCI-E devices.

<dl> <dt>

<span id="2.5_Gbps"></span><span id="2.5_gbps"></span><span id="2.5_GBPS"></span>**2.5 Gbps** (1)
</dt> <dt>

<span id="5_Gbps_"></span><span id="5_gbps_"></span><span id="5_GBPS_"></span>**5 Gbps** (2)
</dt> </dl>

</dd> <dt>

**PciExpressMaxLinkWidth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum link width (1, 2, 4, .., 32), valid only for PCI-E devices.

</dd> <dt>

**PciExpressMaxPayloadSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum payload size in bytes; valid only for PCI-E devices.

</dd> <dt>

**PciExpressMaxReadRequestSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum read request size in bytes; valid only for PCI-E devices

</dd> <dt>

**PciExpressVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

PCI Express specification version, valid for PCI-E devices.

<dl> <dt>

<span id="1.0"></span>**1.0** (1)
</dt> <dt>

<span id="1.1_"></span>**1.1** (2)
</dt> </dl>

</dd> <dt>

**PciXCurrentSpeedAndMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current speed and mode, valid only for PCI-X devices

<dl> <dt>

<span id="PCI-X_Mode_conventional_PCI"></span><span id="pci-x_mode_conventional_pci"></span><span id="PCI-X_MODE_CONVENTIONAL_PCI"></span>**PCI-X Mode conventional PCI** (0)
</dt> <dt>

<span id="PCI-X_Mode1_66MHz"></span><span id="pci-x_mode1_66mhz"></span><span id="PCI-X_MODE1_66MHZ"></span>**PCI-X Mode1 66MHz** (1)
</dt> <dt>

<span id="PCI-X_Mode1_100MHz"></span><span id="pci-x_mode1_100mhz"></span><span id="PCI-X_MODE1_100MHZ"></span>**PCI-X Mode1 100MHz** (2)
</dt> <dt>

<span id="PCI-X_Mode1_133MHz"></span><span id="pci-x_mode1_133mhz"></span><span id="PCI-X_MODE1_133MHZ"></span>**PCI-X Mode1 133MHz** (3)
</dt> <dt>

<span id="PCI-X_Mode1_ECC_66MHz"></span><span id="pci-x_mode1_ecc_66mhz"></span><span id="PCI-X_MODE1_ECC_66MHZ"></span>**PCI-X Mode1 ECC 66MHz** (5)
</dt> <dt>

<span id="PCI-X_Mode1_ECC_100MHz"></span><span id="pci-x_mode1_ecc_100mhz"></span><span id="PCI-X_MODE1_ECC_100MHZ"></span>**PCI-X Mode1 ECC 100MHz** (6)
</dt> <dt>

<span id="PCI-X_Mode1_ECC_133MHz"></span><span id="pci-x_mode1_ecc_133mhz"></span><span id="PCI-X_MODE1_ECC_133MHZ"></span>**PCI-X Mode1 ECC 133MHz** (7)
</dt> <dt>

<span id="PCI-X_Mode2_266_66MHz"></span><span id="pci-x_mode2_266_66mhz"></span><span id="PCI-X_MODE2_266_66MHZ"></span>**PCI-X Mode2 266 66MHz** (9)
</dt> <dt>

<span id="PCI-X_Mode2_266_100MHz"></span><span id="pci-x_mode2_266_100mhz"></span><span id="PCI-X_MODE2_266_100MHZ"></span>**PCI-X Mode2 266 100MHz** (10)
</dt> <dt>

<span id="PCI-X_Mode2_266_133MHz"></span><span id="pci-x_mode2_266_133mhz"></span><span id="PCI-X_MODE2_266_133MHZ"></span>**PCI-X Mode2 266 133MHz** (11)
</dt> <dt>

<span id="PCI-X_Mode2_533_66MHz"></span><span id="pci-x_mode2_533_66mhz"></span><span id="PCI-X_MODE2_533_66MHZ"></span>**PCI-X Mode2 533 66MHz** (13)
</dt> <dt>

<span id="PCI-X_Mode2_533_100MHz"></span><span id="pci-x_mode2_533_100mhz"></span><span id="PCI-X_MODE2_533_100MHZ"></span>**PCI-X Mode2 533 100MHz** (14)
</dt> <dt>

<span id="PCI-X_Mode2_533_133MHz"></span><span id="pci-x_mode2_533_133mhz"></span><span id="PCI-X_MODE2_533_133MHZ"></span>**PCI-X Mode2 533 133MHz** (15)
</dt> </dl>

</dd> <dt>

**S0WakeupSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if a device can wake up via PME while the system is in S0.

</dd> <dt>

**SegmentNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The segment number of a PCI network adapter.

</dd> <dt>

**SlotNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Slot number of a PCI network adapter.

</dd> <dt>

**SriovSupport**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property indicates the status of SR-IOV support for the device.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Supported"></span><span id="supported"></span><span id="SUPPORTED"></span>**Supported** (1)
</dt> <dt>

<span id="Missing_ACS"></span><span id="missing_acs"></span><span id="MISSING_ACS"></span>**Missing ACS** (2)
</dt> <dt>

<span id="Missing_PF_Driver"></span><span id="missing_pf_driver"></span><span id="MISSING_PF_DRIVER"></span>**Missing PF Driver** (3)
</dt> <dt>

<span id="No_bus_resources"></span><span id="no_bus_resources"></span><span id="NO_BUS_RESOURCES"></span>**No bus resources** (4)
</dt> <dt>

<span id="No_IOMMU_support"></span><span id="no_iommu_support"></span><span id="NO_IOMMU_SUPPORT"></span>**No IOMMU support** (5)
</dt> <dt>

<span id="Did_not_Get_Vf_BarSpace"></span><span id="did_not_get_vf_barspace"></span><span id="DID_NOT_GET_VF_BARSPACE"></span>**Did not Get Vf BarSpace** (6)
</dt> <dt>

<span id="No_OCS_Support"></span><span id="no_ocs_support"></span><span id="NO_OCS_SUPPORT"></span>**No OCS Support** (7)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 





---
description: The management characteristics of a USB device.
ms.assetid: c0589346-7683-49c6-bd34-5ee38d71d00e
title: CIM_USBDevice class (Hyper-V management)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_USBDevice
- CIM_USBDevice.USBVersion
- CIM_USBDevice.ClassCode
- CIM_USBDevice.SubclassCode
- CIM_USBDevice.ProtocolCode
- CIM_USBDevice.USBVersionInBCD
- CIM_USBDevice.MaxPacketSize
- CIM_USBDevice.VendorID
- CIM_USBDevice.ProductID
- CIM_USBDevice.DeviceReleaseNumber
- CIM_USBDevice.Manufacturer
- CIM_USBDevice.Product
- CIM_USBDevice.SerialNumber
- CIM_USBDevice.NumberOfConfigs
- CIM_USBDevice.CurrentConfigValue
- CIM_USBDevice.CurrentAlternateSettings
- CIM_USBDevice.CommandTimeout
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM_USBDevice class (Hyper-V management)

The management characteristics of a USB device.

## Syntax

``` syntax
[Abstract, Version("2.22.0"), UMLPackagePath("CIM::Device::USB")]
class CIM_USBDevice : CIM_LogicalDevice
{
  uint16   USBVersion;
  uint8    ClassCode;
  uint8    SubclassCode;
  uint8    ProtocolCode;
  uint16   USBVersionInBCD;
  uint8    MaxPacketSize;
  uint16   VendorID;
  uint16   ProductID;
  uint16   DeviceReleaseNumber;
  string   Manufacturer;
  string   Product;
  string   SerialNumber;
  uint8    NumberOfConfigs;
  uint8    CurrentConfigValue;
  uint8    CurrentAlternateSettings[];
  datetime CommandTimeout;
};
```

## Members

The **CIM\_USBDevice** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CIM\_USBDevice** class has these methods.



| Method                                               | Description                                   |
|:-----------------------------------------------------|:----------------------------------------------|
| [**GetDescriptor**](cim-usbdevice-getdescriptor.md) | Retrieves a USB device descriptor.<br/> |



 

### Properties

The **CIM\_USBDevice** class has these properties.

<dl> <dt>

**ClassCode**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Universal Serial Bus Specification.USB-IF\|Standard Device Descriptor\|bDeviceClass")
</dt> </dl>

The USB class code.

</dd> <dt>

**CommandTimeout**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A timeout interval that is configurable by management applications that support USB redirection. When the redirection service redirects a USB device command to a remote device, and the remote device does not respond before timeout interval, the redirection service will emulate a media eject event. In addition, the service may re-try the command or try to re-establish the connection to the remote device.

</dd> <dt>

**CurrentAlternateSettings**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_USBDevice**.**CurrentConfigValue**")
</dt> </dl>

An array that contains the alternate settings for each interface in the current configuration of the device.

</dd> <dt>

**CurrentConfigValue**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_USBDevice**.**CurrentAlternateSettings**")
</dt> </dl>

The configuration currently selected for the device. If this value is zero, the Device is not configured.

</dd> <dt>

**DeviceReleaseNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Universal Serial Bus Specification.USB-IF\|Standard Device Descriptor\|bcdDevice")
</dt> </dl>

The device release number in BCD format.

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Universal Serial Bus Specification.USB-IF\|Standard Device Descriptor\|iManufacturer")
</dt> </dl>

The manufacturer string of the device.

</dd> <dt>

**MaxPacketSize**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Universal Serial Bus Specification.USB-IF\|Standard Device Descriptor\|bMaxPacketSize")
</dt> </dl>

The maximum packet size for the USB zero endpoint.

</dd> <dt>

**NumberOfConfigs**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Universal Serial Bus Specification.USB-IF\|Standard Device Descriptor\|bNumConfigurations")
</dt> </dl>

The number of device configurations that are defined for the Device.

</dd> <dt>

**Product**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Universal Serial Bus Specification.USB-IF\|Standard Device Descriptor\|iProduct")
</dt> </dl>

The product string of the device.

</dd> <dt>

**ProductID**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Universal Serial Bus Specification.USB-IF\|Standard Device Descriptor\|idProduct")
</dt> </dl>

The product ID assigned to the device by manufacturer.

</dd> <dt>

**ProtocolCode**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Universal Serial Bus Specification.USB-IF\|Standard Device Descriptor\|bDeviceProtocol")
</dt> </dl>

The USB protocol code.

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Universal Serial Bus Specification.USB-IF\|Standard Device Descriptor\|iSerialNumber")
</dt> </dl>

The serial number of the device.

</dd> <dt>

**SubclassCode**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Universal Serial Bus Specification.USB-IF\|Standard Device Descriptor\|bDeviceSubClass")
</dt> </dl>

The USB subclass code.

</dd> <dt>

**USBVersion**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The latest USB Version supported by the USB Device. The property is expressed as a binary-coded decimal (BCD) that contains a decimal point between the 2nd and 3rd digits. For example, a value of 0x201 indicates that version 2.01 is supported.

</dd> <dt>

**USBVersionInBCD**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Universal Serial Bus Specification.USB-IF\|Standard Device Descriptor\|bcdUSB")
</dt> </dl>

The USB specification number that the device complies with. This property is formatted with BCD format.

</dd> <dt>

**VendorID**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Universal Serial Bus Specification.USB-IF\|Standard Device Descriptor\|idVendor")
</dt> </dl>

The vendor ID assigned to the device by USB.org.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_LogicalDevice**](cim-logicaldevice.md)
</dt> </dl>

 


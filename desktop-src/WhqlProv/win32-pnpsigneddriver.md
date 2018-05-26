---
title: Win32\_PnPSignedDriver class
description: The Win32\_PnPSignedDriver WMI class provides digital signature information about drivers.
ms.assetid: 8ada3b4d-c9de-4847-ba78-470bae70820e
keywords:
- Win32_PnPSignedDriver class
- Win32_PnPSignedDriver class, described
topic_type:
- apiref
api_name:
- Win32_PnPSignedDriver
- Win32_PnPSignedDriver.ClassGuid
- Win32_PnPSignedDriver.CompatID
- Win32_PnPSignedDriver.Description
- Win32_PnPSignedDriver.DeviceClass
- Win32_PnPSignedDriver.DeviceID
- Win32_PnPSignedDriver.DeviceName
- Win32_PnPSignedDriver.DevLoader
- Win32_PnPSignedDriver.DriverDate
- Win32_PnPSignedDriver.DriverName
- Win32_PnPSignedDriver.DriverVersion
- Win32_PnPSignedDriver.FriendlyName
- Win32_PnPSignedDriver.HardWareID
- Win32_PnPSignedDriver.InfName
- Win32_PnPSignedDriver.InstallDate
- Win32_PnPSignedDriver.IsSigned
- Win32_PnPSignedDriver.Location
- Win32_PnPSignedDriver.Manufacturer
- Win32_PnPSignedDriver.Name
- Win32_PnPSignedDriver.PDO
- Win32_PnPSignedDriver.DriverProviderName
- Win32_PnPSignedDriver.Signer
- Win32_PnPSignedDriver.Started
- Win32_PnPSignedDriver.StartMode
- Win32_PnPSignedDriver.Status
- Win32_PnPSignedDriver.SystemCreationClassName
- Win32_PnPSignedDriver.SystemName
api_location:
- SignDrv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_PnPSignedDriver class

The **Win32\_PnPSignedDriver** [WMI class](https://msdn.microsoft.com/library/aa393244) provides digital signature information about drivers.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_PnPSignedDriver : CIM_Service
{
  string   ClassGuid;
  string   CompatID;
  string   Description;
  string   DeviceClass;
  string   DeviceID;
  string   DeviceName;
  string   DevLoader;
  string   DriverDate;
  string   DriverName;
  string   DriverVersion;
  string   FriendlyName;
  string   HardWareID;
  string   InfName;
  datetime InstallDate;
  boolean  IsSigned;
  string   Location;
  string   Manufacturer;
  string   Name;
  string   PDO;
  string   DriverProviderName;
  string   Signer;
  boolean  Started;
  string   StartMode;
  string   Status;
  string   SystemCreationClassName;
  string   SystemName;
};
```

## Members

The **Win32\_PnPSignedDriver** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_PnPSignedDriver** class has these methods.



| Method                                                                     | Description                    |
|:---------------------------------------------------------------------------|:-------------------------------|
| [**StartService**](startservice-method-in-class-win32-pnpsigneddriver.md) | Starts the service.<br/> |
| [**StopService**](stopservice-method-in-class-win32-pnpsigneddriver.md)   | Stops the service.<br/>  |



 

### Properties

The **Win32\_PnPSignedDriver** class has these properties.

<dl> <dt>

**ClassGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

GUID of the device class. Example: "{71A27CDD-11D0-BEC7-08002BE2092F}"

</dd> <dt>

**CompatID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Compatibility identifier for the driver. Example: "DETECTEDInternal\\ftdisk"

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the driver.

</dd> <dt>

**DeviceClass**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Device class of the driver. Example: "SYSTEM"

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Device identifier of the device. Example: "ROOT\\FTDISK\\0000"

</dd> <dt>

**DeviceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the device.

</dd> <dt>

**DevLoader**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Device loader for the device.

</dd> <dt>

**DriverDate**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Build date of the driver (from the manufacturer). Example: "1-25-2001"

</dd> <dt>

**DriverName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the driver.

</dd> <dt>

**DriverProviderName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provider of the driver. Example: "Microsoft"

</dd> <dt>

**DriverVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Version of the driver. Example: "5.1.2427.1"

</dd> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Friendly name of the driver. Example: "Communications Port (COM2)"

</dd> <dt>

**HardWareID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Hardware identifier for the driver. Example: "ROOT\\FTDISK"

</dd> <dt>

**InfName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the .inf file that installed the device. Example: "machine.inf"

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date the driver was installed. Lack of value does not indicate that the driver is not installed. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**IsSigned**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the driver is signed.

</dd> <dt>

**Location**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Location of the driver.

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Manufacturer of the driver. Example: "Microsoft"

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Name of the driver. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**PDO**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Physical device object (PDO). PDOs represent individual devices on a bus. Other drivers for the device attach on top of the PDO. It is always at the bottom of the device stack. Example: "\\Device\\00000002"

</dd> <dt>

**Signer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Signer of driver, if it is signed. Example: "ntbuild"

</dd> <dt>

**Started**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the driver is started. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442).

</dd> <dt>

**StartMode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Start mode of the driver. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", can apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is online, yet the managed element is neither "OK" nor in one of the other states. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

The values are:

<dl><span id="OK"></span><span id="ok"></span><dt>

**"OK"**
</dt><span id="Error"></span><span id="error"></span><span id="ERROR"></span><dt>

**"Error"**
</dt><span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dt>

**"Degraded"**
</dt><span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dt>

**"Unknown"**
</dt><span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span><dt>

**"Pred Fail"**
</dt><span id="Starting"></span><span id="starting"></span><span id="STARTING"></span><dt>

**"Starting"**
</dt><span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span><dt>

**"Stopping"**
</dt><span id="Service"></span><span id="service"></span><span id="SERVICE"></span><dt>

**"Service"**
</dt><span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span><dt>

**"Stressed"**
</dt><span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span><dt>

**"NonRecover"**
</dt><span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span><dt>

**"No Contact"**
</dt><span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span><dt>

**"Lost Comm"**
</dt> </dl>

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Value of the scoping computer's **CreationClassName** property. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

System name. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442).

</dd> </dl>

## Remarks

For more information on using this class, see [How Can I Get a List of Installed Device Drivers?](http://blogs.technet.com/b/heyscriptingguy/archive/2006/03/20/how-can-i-get-a-list-of-installed-device-drivers.aspx) and [Hey, Scripting Guy! How Can I Tell If a Computer Has a SmartCard Reader Attached?](http://blogs.technet.com/b/heyscriptingguy/archive/2007/11/19/hey-scripting-guy-how-can-i-tell-if-a-computer-has-a-smartcard-reader-attached.aspx).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>WhqlProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SignDrv.dll</dt> </dl>  |



## See also

<dl> <dt>

[Computer System Hardware Classes](https://msdn.microsoft.com/library/aa389273)
</dt> </dl>

 

 






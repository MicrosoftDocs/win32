---
title: MSFT\_StorageEnclosure class
description: Represents a storage enclosure.
ms.assetid: '617DA7A7-E594-42C0-AD69-F95E55BC0D4B'
keywords: ["MSFT_StorageEnclosure class Windows Storage Management API", "MSFT_StorageEnclosure class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageEnclosure
- MSFT_StorageEnclosure.DeviceId
- MSFT_StorageEnclosure.FriendlyName
- MSFT_StorageEnclosure.FirmwareVersion
- MSFT_StorageEnclosure.NumberOfSlots
- MSFT_StorageEnclosure.PowerSupplyOperationalStatus
- MSFT_StorageEnclosure.FanOperationalStatus
- MSFT_StorageEnclosure.TemperatureSensorOperationalStatus
- MSFT_StorageEnclosure.VoltageSensorOperationalStatus
- MSFT_StorageEnclosure.CurrentSensorOperationalStatus
- MSFT_StorageEnclosure.IOControllerOperationalStatus
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageEnclosure class

Represents a storage enclosure.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_StorageEnclosure : MSFT_StorageFaultDomain
{
  String DeviceId;
  String FriendlyName;
  String FirmwareVersion;
  UInt32 NumberOfSlots;
  UInt16 PowerSupplyOperationalStatus[];
  UInt16 FanOperationalStatus[];
  UInt16 TemperatureSensorOperationalStatus[];
  UInt16 VoltageSensorOperationalStatus[];
  UInt16 CurrentSensorOperationalStatus[];
  UInt16 IOControllerOperationalStatus[];
};
```

## Members

The **MSFT\_StorageEnclosure** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StorageEnclosure** class has these methods.



| Method                                                           | Description                                                                                  |
|:-----------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**GetVendorData**](msft-storageenclosure-getvendordata.md)     | Returns the vendor-specific data from an enclosure.<br/>                               |
| [**IdentifyElement**](msft-storageenclosure-identifyelement.md) | Permits a user to perform identification tasks on the enclosure and its elements.<br/> |



 

### Properties

The **MSFT\_StorageEnclosure** class has these properties.

<dl> <dt>

**CurrentSensorOperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array containing the operational status of each current sensor of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                         | The operational status of the element is unknown.<br/>                 |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                  | The element is present and working, with no issues detected.<br/>      |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                     | The element detects a non-critical issue.<br/>                         |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                 | The element detects a critical issue.<br/>                             |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl> | The element detects a non-recoverable issue.<br/>                      |
| <span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span><dl> <dt>**Not Installed**</dt> <dt>0xD009</dt> </dl>                            | The element is not present.<br/>                                       |
| <span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span><dl> <dt>**Not Available**</dt> <dt>0xD00A</dt> </dl>                            | The element is present but has problems that make it unavailable.<br/> |
| <span id="No_Access_Allowed"></span><span id="no_access_allowed"></span><span id="NO_ACCESS_ALLOWED"></span><dl> <dt>**No Access Allowed**</dt> <dt>0xD00B</dt> </dl>            | No access is allowed to the element.<br/>                              |
| <span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span><dl> <dt>**Not Supported**</dt> <dt>0xD00C</dt> </dl>                            | The element is not supported.<br/>                                     |



 

</dd> <dt>

**DeviceId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An address or other identifier that uniquely names the enclosure.

</dd> <dt>

**FanOperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array containing the operational status of each fan of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                         | The operational status of the element is unknown.<br/>                 |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                  | The element is present and working, with no issues detected.<br/>      |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                     | The element detects a non-critical issue.<br/>                         |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                 | The element detects a critical issue.<br/>                             |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl> | The element detects a non-recoverable issue.<br/>                      |
| <span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span><dl> <dt>**Not Installed**</dt> <dt>0xD009</dt> </dl>                            | The element is not present.<br/>                                       |
| <span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span><dl> <dt>**Not Available**</dt> <dt>0xD00A</dt> </dl>                            | The element is present but has problems that make it unavailable.<br/> |
| <span id="No_Access_Allowed"></span><span id="no_access_allowed"></span><span id="NO_ACCESS_ALLOWED"></span><dl> <dt>**No Access Allowed**</dt> <dt>0xD00B</dt> </dl>            | No access is allowed to the element.<br/>                              |
| <span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span><dl> <dt>**Not Supported**</dt> <dt>0xD00C</dt> </dl>                            | The element is not supported.<br/>                                     |



 

</dd> <dt>

**FirmwareVersion**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A string representation of the enclosure's firmware version.

</dd> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A user-friendly string representing the name of the enclosure.

</dd> <dt>

**IOControllerOperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array containing the operational status of each IO controller module of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                         | The operational status of the element is unknown.<br/>                 |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                  | The element is present and working, with no issues detected.<br/>      |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                     | The element detects a non-critical issue.<br/>                         |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                 | The element detects a critical issue.<br/>                             |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl> | The element detects a non-recoverable issue.<br/>                      |
| <span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span><dl> <dt>**Not Installed**</dt> <dt>0xD009</dt> </dl>                            | The element is not present.<br/>                                       |
| <span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span><dl> <dt>**Not Available**</dt> <dt>0xD00A</dt> </dl>                            | The element is present but has problems that make it unavailable.<br/> |
| <span id="No_Access_Allowed"></span><span id="no_access_allowed"></span><span id="NO_ACCESS_ALLOWED"></span><dl> <dt>**No Access Allowed**</dt> <dt>0xD00B</dt> </dl>            | No access is allowed to the element.<br/>                              |
| <span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span><dl> <dt>**Not Supported**</dt> <dt>0xD00C</dt> </dl>                            | The element is not supported.<br/>                                     |



 

</dd> <dt>

**NumberOfSlots**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Number of slots hosted within the enclosure.

</dd> <dt>

**PowerSupplyOperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array containing the operational status of each power supply module of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                         | The operational status of the element is unknown.<br/>                 |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                  | The element is present and working, with no issues detected.<br/>      |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                     | The element detects a non-critical issue.<br/>                         |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                 | The element detects a critical issue.<br/>                             |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl> | The element detects a non-recoverable issue.<br/>                      |
| <span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span><dl> <dt>**Not Installed**</dt> <dt>0xD009</dt> </dl>                            | The element is not present.<br/>                                       |
| <span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span><dl> <dt>**Not Available**</dt> <dt>0xD00A</dt> </dl>                            | The element is present but has problems that make it unavailable.<br/> |
| <span id="No_Access_Allowed"></span><span id="no_access_allowed"></span><span id="NO_ACCESS_ALLOWED"></span><dl> <dt>**No Access Allowed**</dt> <dt>0xD00B</dt> </dl>            | No access is allowed to the element.<br/>                              |
| <span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span><dl> <dt>**Not Supported**</dt> <dt>0xD00C</dt> </dl>                            | The element is not supported.<br/>                                     |



 

</dd> <dt>

**TemperatureSensorOperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array containing the operational status of each temperature sensor of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                         | The operational status of the element is unknown.<br/>                 |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                  | The element is present and working, with no issues detected.<br/>      |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                     | The element detects a non-critical issue.<br/>                         |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                 | The element detects a critical issue.<br/>                             |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl> | The element detects a non-recoverable issue.<br/>                      |
| <span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span><dl> <dt>**Not Installed**</dt> <dt>0xD009</dt> </dl>                            | The element is not present.<br/>                                       |
| <span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span><dl> <dt>**Not Available**</dt> <dt>0xD00A</dt> </dl>                            | The element is present but has problems that make it unavailable.<br/> |
| <span id="No_Access_Allowed"></span><span id="no_access_allowed"></span><span id="NO_ACCESS_ALLOWED"></span><dl> <dt>**No Access Allowed**</dt> <dt>0xD00B</dt> </dl>            | No access is allowed to the element.<br/>                              |
| <span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span><dl> <dt>**Not Supported**</dt> <dt>0xD00C</dt> </dl>                            | The element is not supported.<br/>                                     |



 

</dd> <dt>

**VoltageSensorOperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array containing the operational status of each voltage sensor of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                         | The operational status of the element is unknown.<br/>                 |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                  | The element is present and working, with no issues detected.<br/>      |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                     | The element detects a non-critical issue.<br/>                         |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                 | The element detects a critical issue.<br/>                             |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl> | The element detects a non-recoverable issue.<br/>                      |
| <span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span><dl> <dt>**Not Installed**</dt> <dt>0xD009</dt> </dl>                            | The element is not present.<br/>                                       |
| <span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span><dl> <dt>**Not Available**</dt> <dt>0xD00A</dt> </dl>                            | The element is present but has problems that make it unavailable.<br/> |
| <span id="No_Access_Allowed"></span><span id="no_access_allowed"></span><span id="NO_ACCESS_ALLOWED"></span><dl> <dt>**No Access Allowed**</dt> <dt>0xD00B</dt> </dl>            | No access is allowed to the element.<br/>                              |
| <span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span><dl> <dt>**Not Supported**</dt> <dt>0xD00C</dt> </dl>                            | The element is not supported.<br/>                                     |



 

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageFaultDomain**](msft-storagefaultdomain.md)
</dt> </dl>

 

 






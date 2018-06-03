---
title: MSFT\_StorageNodeToStorageEnclosure class
description: Association between StorageNode and StorageEnclosure.
ms.assetid: 1EC3975C-618B-4DE0-B1CC-B6B63D1936BE
keywords:
- MSFT_StorageNodeToStorageEnclosure class Windows Storage Management API
- MSFT_StorageNodeToStorageEnclosure class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageNodeToStorageEnclosure
- MSFT_StorageNodeToStorageEnclosure.StorageNode
- MSFT_StorageNodeToStorageEnclosure.StorageEnclosure
- MSFT_StorageNodeToStorageEnclosure.HealthStatus
- MSFT_StorageNodeToStorageEnclosure.PowerSupplyOperationalStatus
- MSFT_StorageNodeToStorageEnclosure.FanOperationalStatus
- MSFT_StorageNodeToStorageEnclosure.TemperatureSensorOperationalStatus
- MSFT_StorageNodeToStorageEnclosure.VoltageSensorOperationalStatus
- MSFT_StorageNodeToStorageEnclosure.CurrentSensorOperationalStatus
- MSFT_StorageNodeToStorageEnclosure.IOControllerOperationalStatus
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageNodeToStorageEnclosure class

Association between [**StorageNode**](msft-storagenode.md) and [**StorageEnclosure**](msft-storageenclosure.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association]
class MSFT_StorageNodeToStorageEnclosure
{
  MSFT_StorageNode      REF StorageNode;
  MSFT_StorageEnclosure REF StorageEnclosure;
  UInt16                    HealthStatus;
  UInt16                    PowerSupplyOperationalStatus[];
  UInt16                    FanOperationalStatus[];
  UInt16                    TemperatureSensorOperationalStatus[];
  UInt16                    VoltageSensorOperationalStatus[];
  UInt16                    CurrentSensorOperationalStatus[];
  UInt16                    IOControllerOperationalStatus[];
};
```

## Members

The **MSFT\_StorageNodeToStorageEnclosure** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageNodeToStorageEnclosure** class has these properties.

<dl> <dt>

**CurrentSensorOperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Starting in Windows 10:** An array containing the operational status of each current sensor of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                         |                                                                        |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                  | The element is present and working with no issues detected.<br/> |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                     | The element detected one or more non-critical issues.<br/>       |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                 | The element detected one or more critical issues.<br/>           |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl> | The element detected one or more non-recoverable issues.<br/>    |
| <span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span><dl> <dt>**Not Installed**</dt> <dt>0xD009</dt> </dl>                            | The element is not present.<br/>                                 |
| <span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span><dl> <dt>**Not Available**</dt> <dt>0xD00A</dt> </dl>                            | The element is present but has problems.<br/>                    |
| <span id="No_Access_Allowed"></span><span id="no_access_allowed"></span><span id="NO_ACCESS_ALLOWED"></span><dl> <dt>**No Access Allowed**</dt> <dt>0xD00B</dt> </dl>            | No access is allowed to the element.<br/>                        |
| <span id="Not_Reported"></span><span id="not_reported"></span><span id="NOT_REPORTED"></span><dl> <dt>**Not Reported**</dt> <dt>0xD00C</dt> </dl>                                |                                                                        |



 

</dd> <dt>

**FanOperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Starting in Windows 10:** An array containing the operational status of each fan of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                         |                                                                        |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                  | The element is present and working with no issues detected.<br/> |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                     | The element detected one or more non-critical issues.<br/>       |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                 | The element detected one or more critical issues.<br/>           |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl> | The element detected one or more non-recoverable issues.<br/>    |
| <span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span><dl> <dt>**Not Installed**</dt> <dt>0xD009</dt> </dl>                            | The element is not present.<br/>                                 |
| <span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span><dl> <dt>**Not Available**</dt> <dt>0xD00A</dt> </dl>                            | The element is present but has problems.<br/>                    |
| <span id="No_Access_Allowed"></span><span id="no_access_allowed"></span><span id="NO_ACCESS_ALLOWED"></span><dl> <dt>**No Access Allowed**</dt> <dt>0xD00B</dt> </dl>            | No access is allowed to the element.<br/>                        |
| <span id="Not_Reported"></span><span id="not_reported"></span><span id="NOT_REPORTED"></span><dl> <dt>**Not Reported**</dt> <dt>0xD00C</dt> </dl>                                |                                                                        |



 

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Starting in Windows 10:** Denotes the current health status of the enclosure.

<dl> <dt>

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>**Healthy** (0)
</dt> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>**Warning** (1)
</dt> <dt>

<span id="Unhealthy"></span><span id="unhealthy"></span><span id="UNHEALTHY"></span>**Unhealthy** (2)
</dt> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (5)
</dt> </dl>

</dd> <dt>

**IOControllerOperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Starting in Windows 10:** An array containing the operational status of each controller of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                         |                                                                        |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                  | The element is present and working with no issues detected.<br/> |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                     | The element detected one or more non-critical issues.<br/>       |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                 | The element detected one or more critical issues.<br/>           |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl> | The element detected one or more non-recoverable issues.<br/>    |
| <span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span><dl> <dt>**Not Installed**</dt> <dt>0xD009</dt> </dl>                            | The element is not present.<br/>                                 |
| <span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span><dl> <dt>**Not Available**</dt> <dt>0xD00A</dt> </dl>                            | The element is present but has problems.<br/>                    |
| <span id="No_Access_Allowed"></span><span id="no_access_allowed"></span><span id="NO_ACCESS_ALLOWED"></span><dl> <dt>**No Access Allowed**</dt> <dt>0xD00B</dt> </dl>            | No access is allowed to the element.<br/>                        |
| <span id="Not_Reported"></span><span id="not_reported"></span><span id="NOT_REPORTED"></span><dl> <dt>**Not Reported**</dt> <dt>0xD00C</dt> </dl>                                |                                                                        |



 

</dd> <dt>

**PowerSupplyOperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Starting in Windows 10:** An array containing the operational status of each power supply of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                         |                                                                        |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                  | The element is present and working with no issues detected.<br/> |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                     | The element detected one or more non-critical issues.<br/>       |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                 | The element detected one or more critical issues.<br/>           |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl> | The element detected one or more non-recoverable issues.<br/>    |
| <span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span><dl> <dt>**Not Installed**</dt> <dt>0xD009</dt> </dl>                            | The element is not present.<br/>                                 |
| <span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span><dl> <dt>**Not Available**</dt> <dt>0xD00A</dt> </dl>                            | The element is present but has problems.<br/>                    |
| <span id="No_Access_Allowed"></span><span id="no_access_allowed"></span><span id="NO_ACCESS_ALLOWED"></span><dl> <dt>**No Access Allowed**</dt> <dt>0xD00B</dt> </dl>            | No access is allowed to the element.<br/>                        |
| <span id="Not_Reported"></span><span id="not_reported"></span><span id="NOT_REPORTED"></span><dl> <dt>**Not Reported**</dt> <dt>0xD00C</dt> </dl>                                |                                                                        |



 

</dd> <dt>

**StorageEnclosure**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageEnclosure**](msft-storageenclosure.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

</dd> <dt>

**StorageNode**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageNode**](msft-storagenode.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

</dd> <dt>

**TemperatureSensorOperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Starting in Windows 10:** An array containing the operational status of each temperature sensor of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                         |                                                                        |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                  | The element is present and working with no issues detected.<br/> |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                     | The element detected one or more non-critical issues.<br/>       |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                 | The element detected one or more critical issues.<br/>           |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl> | The element detected one or more non-recoverable issues.<br/>    |
| <span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span><dl> <dt>**Not Installed**</dt> <dt>0xD009</dt> </dl>                            | The element is not present.<br/>                                 |
| <span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span><dl> <dt>**Not Available**</dt> <dt>0xD00A</dt> </dl>                            | The element is present but has problems.<br/>                    |
| <span id="No_Access_Allowed"></span><span id="no_access_allowed"></span><span id="NO_ACCESS_ALLOWED"></span><dl> <dt>**No Access Allowed**</dt> <dt>0xD00B</dt> </dl>            | No access is allowed to the element.<br/>                        |
| <span id="Not_Reported"></span><span id="not_reported"></span><span id="NOT_REPORTED"></span><dl> <dt>**Not Reported**</dt> <dt>0xD00C</dt> </dl>                                |                                                                        |



 

</dd> <dt>

**VoltageSensorOperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Starting in Windows 10:** An array containing the operational status of each voltage sensor of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                         |                                                                        |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                  | The element is present and working with no issues detected.<br/> |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                     | The element detected one or more non-critical issues.<br/>       |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                 | The element detected one or more critical issues.<br/>           |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl> | The element detected one or more non-recoverable issues.<br/>    |
| <span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span><dl> <dt>**Not Installed**</dt> <dt>0xD009</dt> </dl>                            | The element is not present.<br/>                                 |
| <span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span><dl> <dt>**Not Available**</dt> <dt>0xD00A</dt> </dl>                            | The element is present but has problems.<br/>                    |
| <span id="No_Access_Allowed"></span><span id="no_access_allowed"></span><span id="NO_ACCESS_ALLOWED"></span><dl> <dt>**No Access Allowed**</dt> <dt>0xD00B</dt> </dl>            | No access is allowed to the element.<br/>                        |
| <span id="Not_Reported"></span><span id="not_reported"></span><span id="NOT_REPORTED"></span><dl> <dt>**Not Reported**</dt> <dt>0xD00C</dt> </dl>                                |                                                                        |



 

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageNode**](msft-storagenode.md)
</dt> <dt>

[**MSFT\_StorageEnclosure**](msft-storageenclosure.md)
</dt> </dl>

 

 






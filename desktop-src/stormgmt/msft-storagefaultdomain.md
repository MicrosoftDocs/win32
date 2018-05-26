---
title: MSFT\_StorageFaultDomain class
description: Common base class for all storage fault domain objects.
ms.assetid: 662C4D52-AE58-4922-BB01-0470B5B3F3C3
keywords:
- MSFT_StorageFaultDomain class Windows Storage Management API
- MSFT_StorageFaultDomain class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageFaultDomain
- MSFT_StorageFaultDomain.Manufacturer
- MSFT_StorageFaultDomain.Model
- MSFT_StorageFaultDomain.SerialNumber
- MSFT_StorageFaultDomain.PhysicalLocation
- MSFT_StorageFaultDomain.HealthStatus
- MSFT_StorageFaultDomain.OperationalStatus
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_StorageFaultDomain class

Common base class for all storage fault domain objects.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_StorageFaultDomain : MSFT_StorageObject
{
  String Manufacturer;
  String Model;
  String SerialNumber;
  String PhysicalLocation;
  UInt16 HealthStatus;
  UInt16 OperationalStatus[];
};
```

## Members

The **MSFT\_StorageFaultDomain** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageFaultDomain** class has these properties.

<dl> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The health status of the object.



| Value                                                                                                                                                                                                                               | Meaning                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| <span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span><dl> <dt>**Healthy**</dt> <dt>0</dt> </dl>         | The object is in a good state. There has been no reported read or write packet loss.<br/>          |
| <span id="Warning"></span><span id="warning"></span><span id="WARNING"></span><dl> <dt>**Warning**</dt> <dt>1</dt> </dl>         | The object may be failing some read requests, but there have been no reported write failures.<br/> |
| <span id="Unhealthy"></span><span id="unhealthy"></span><span id="UNHEALTHY"></span><dl> <dt>**Unhealthy**</dt> <dt>2</dt> </dl> | The object is failing read and write requests, or is no longer responding to any commands.<br/>    |
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>5</dt> </dl>         | The health status is unknown.<br/>                                                                 |



 

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the company responsible for the hardware backing the fault domain object. For [**MSFT\_PhysicalDisk**](msft-physicaldisk.md) it must match the disk's SCSI inquiry data.

</dd> <dt>

**Model**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Represents the model number of the hardware. For [**MSFT\_PhysicalDisk**](msft-physicaldisk.md) it must match the disk's SCSI inquiry data.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of values that specify the operational status of the object.



| Value                                                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                                              | The operational status of the object is unknown.<br/>                                                                                                                               |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                                                                      | A vendor-specific operational status has been specified.<br/>                                                                                                                       |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                                       | The object is responding to commands and is in a normal operating state.<br/>                                                                                                       |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                                          | The object is responding to commands but is not running in an optimal operating state.<br/>                                                                                         |
| <span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span><dl> <dt>**Stressed**</dt> <dt>4</dt> </dl>                                                                          | The object is functioning but needs attention. For example, it might be overloaded or overheated.<br/>                                                                              |
| <span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span><dl> <dt>**Predictive Failure**</dt> <dt>5</dt> </dl>                                  | The object is functioning nominally, but a failure in the near future is predicted.<br/>                                                                                            |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                                      | An error has occurred.<br/>                                                                                                                                                         |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl>                      | A nonrecoverable error has occurred.<br/>                                                                                                                                           |
| <span id="Starting"></span><span id="starting"></span><span id="STARTING"></span><dl> <dt>**Starting**</dt> <dt>8</dt> </dl>                                                                          | The object is in the process of starting.<br/>                                                                                                                                      |
| <span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span><dl> <dt>**Stopping**</dt> <dt>9</dt> </dl>                                                                          | The object is in the process of stopping.<br/>                                                                                                                                      |
| <span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span><dl> <dt>**Stopped**</dt> <dt>10</dt> </dl>                                                                             | The object was stopped or shut down in a clean and orderly fashion.<br/>                                                                                                            |
| <span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span><dl> <dt>**In Service**</dt> <dt>11</dt> </dl>                                                                 | The object is being configured, maintained, cleaned, or otherwise administered.<br/>                                                                                                |
| <span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span><dl> <dt>**No Contact**</dt> <dt>12</dt> </dl>                                                                 | The storage provider has knowledge of the object but has never been able to establish communication with it.<br/>                                                                   |
| <span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span><dl> <dt>**Lost Communication**</dt> <dt>13</dt> </dl>                                 | The object is known to exist and has been contacted successfully in the past but is currently unreachable.<br/>                                                                     |
| <span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span><dl> <dt>**Aborted**</dt> <dt>14</dt> </dl>                                                                             | Similar to **Stopped**, except that the object stopped abruptly and may require configuration or maintenance.<br/>                                                                  |
| <span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span><dl> <dt>**Dormant**</dt> <dt>15</dt> </dl>                                                                             | The object is reachable, but it is inactive.<br/>                                                                                                                                   |
| <span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span><dl> <dt>**Supporting Entity in Error**</dt> <dt>16</dt> </dl> | This status value does not necessarily indicate trouble with the object, but it does indicate that another device or connection that the object depends on may need attention.<br/> |
| <span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span><dl> <dt>**Completed**</dt> <dt>17</dt> </dl>                                                                     | The object has completed an operation. This status value should be combined with **OK**, **Error**, or **Degraded**, depending on the outcome of the operation<br/>                 |
| <span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span><dl> <dt>**Power Mode**</dt> <dt>18</dt> </dl>                                                                 | This value is reserved for system use.<br/>                                                                                                                                         |
| <span id="Relocating"></span><span id="relocating"></span><span id="RELOCATING"></span><dl> <dt>**Relocating**</dt> <dt>19</dt> </dl>                                                                 | The object is in the process of relocating.<br/>                                                                                                                                    |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>..</dt> </dl>                                 | This value is reserved for system use.<br/>                                                                                                                                         |
| <span id="Failed_Media"></span><span id="failed_media"></span><span id="FAILED_MEDIA"></span><dl> <dt>**Failed Media**</dt> <dt>0xD004</dt> </dl>                                                     |                                                                                                                                                                                           |
| <span id="Split"></span><span id="split"></span><span id="SPLIT"></span><dl> <dt>**Split**</dt> <dt>0xD005</dt> </dl>                                                                                 |                                                                                                                                                                                           |
| <span id="Stale_Metadata"></span><span id="stale_metadata"></span><span id="STALE_METADATA"></span><dl> <dt>**Stale Metadata**</dt> <dt>0xD006</dt> </dl>                                             |                                                                                                                                                                                           |
| <span id="IO_Error"></span><span id="io_error"></span><span id="IO_ERROR"></span><dl> <dt>**IO Error**</dt> <dt>0xD007</dt> </dl>                                                                     |                                                                                                                                                                                           |
| <span id="Unrecognized_Metadata"></span><span id="unrecognized_metadata"></span><span id="UNRECOGNIZED_METADATA"></span><dl> <dt>**Unrecognized Metadata**</dt> <dt>0xD008</dt> </dl>                 |                                                                                                                                                                                           |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>0xD009..</dt> </dl>                           | This value is reserved for system use.<br/>                                                                                                                                         |



 

</dd> <dt>

**PhysicalLocation**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A free-form string indicating where the hardware is located.

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Represents the serial number of the hardware. For [**MSFT\_PhysicalDisk**](msft-physicaldisk.md) it must match the disk's SCSI inquiry data.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> </dl>

 

 






---
title: MSFT\_StorageReliabilityCounter class
description: The MSFT\_StorageReliabilityCounter class provides reliability statistics or counters reported by a storage device.
ms.assetid: A64126B3-0399-47A3-95E3-0755EE34C2C4
keywords:
- MSFT_StorageReliabilityCounter class Windows Storage Management API
- MSFT_StorageReliabilityCounter class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageReliabilityCounter
- MSFT_StorageReliabilityCounter.DeviceId
- MSFT_StorageReliabilityCounter.Temperature
- MSFT_StorageReliabilityCounter.TemperatureMax
- MSFT_StorageReliabilityCounter.ReadErrorsTotal
- MSFT_StorageReliabilityCounter.ReadErrorsCorrected
- MSFT_StorageReliabilityCounter.ReadErrorsUncorrected
- MSFT_StorageReliabilityCounter.WriteErrorsTotal
- MSFT_StorageReliabilityCounter.WriteErrorsCorrected
- MSFT_StorageReliabilityCounter.WriteErrorsUncorrected
- MSFT_StorageReliabilityCounter.ManufactureDate
- MSFT_StorageReliabilityCounter.StartStopCycleCount
- MSFT_StorageReliabilityCounter.StartStopCycleCountMax
- MSFT_StorageReliabilityCounter.LoadUnloadCycleCount
- MSFT_StorageReliabilityCounter.LoadUnloadCycleCountMax
- MSFT_StorageReliabilityCounter.Wear
- MSFT_StorageReliabilityCounter.PowerOnHours
- MSFT_StorageReliabilityCounter.ReadLatencyMax
- MSFT_StorageReliabilityCounter.WriteLatencyMax
- MSFT_StorageReliabilityCounter.FlushLatencyMax
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

# MSFT\_StorageReliabilityCounter class

The **MSFT\_StorageReliabilityCounter** class provides reliability statistics or counters reported by a storage device.

This information is dynamic and should be obtained from the storage device whenever needed.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_StorageReliabilityCounter : MSFT_StorageObject
{
  String DeviceId;
  UInt8  Temperature;
  UInt8  TemperatureMax;
  UInt64 ReadErrorsTotal;
  UInt64 ReadErrorsCorrected;
  UInt64 ReadErrorsUncorrected;
  UInt64 WriteErrorsTotal;
  UInt64 WriteErrorsCorrected;
  UInt64 WriteErrorsUncorrected;
  String ManufactureDate;
  UInt32 StartStopCycleCount;
  UInt32 StartStopCycleCountMax;
  UInt32 LoadUnloadCycleCount;
  UInt32 LoadUnloadCycleCountMax;
  UInt8  Wear;
  UInt16 PowerOnHours;
  UInt64 ReadLatencyMax;
  UInt64 WriteLatencyMax;
  UInt64 FlushLatencyMax;
};
```

## Members

The **MSFT\_StorageReliabilityCounter** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StorageReliabilityCounter** class has these methods.



| Method                                                | Description                           |
|:------------------------------------------------------|:--------------------------------------|
| [**Reset**](msft-storagereliabilitycounter-reset.md) | Resets reliability values.<br/> |



 

### Properties

The **MSFT\_StorageReliabilityCounter** class has these properties.

<dl> <dt>

**DeviceId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An identifier that uniquely names the associated storage device. When associated with an [**MSFT\_PhysicalDisk**](msft-physicaldisk.md), it will be the same as its **DeviceId** member. When associated with an [**MSFT\_Disk**](msft-disk.md), it will be the same as its **Number** field.

</dd> <dt>

**FlushLatencyMax**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum latency experienced by a flush request, in milliseconds. A value greater than 10 seconds may indicate a problem with the disk or the HBA.

</dd> <dt>

**LoadUnloadCycleCount**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of load-unload cycles that were performed by the storage device.

</dd> <dt>

**LoadUnloadCycleCountMax**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of load-unload cycles that can be performed by the storage device in normal operation.

</dd> <dt>

**ManufactureDate**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The year and week when the storage device was manufactured.

</dd> <dt>

**PowerOnHours**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of hours that the storage device has been powered on since it was manufactured.

</dd> <dt>

**ReadErrorsCorrected**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of read errors that were corrected by the storage device.

</dd> <dt>

**ReadErrorsTotal**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of read errors that were encountered by the storage device.

</dd> <dt>

**ReadErrorsUncorrected**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of read errors that were not corrected by the storage device.

</dd> <dt>

**ReadLatencyMax**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum latency experienced by a read request, in milliseconds. A value greater than 10 seconds may indicate a problem with the disk or the HBA.

</dd> <dt>

**StartStopCycleCount**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of start-stop cycles that were performed by the storage device.

</dd> <dt>

**StartStopCycleCountMax**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of start-stop cycles that can be performed by the storage device in normal operation.

</dd> <dt>

**Temperature**
</dt> <dd> <dl> <dt>

Data type: **UInt8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current temperature of the storage device in degrees Celsius.

</dd> <dt>

**TemperatureMax**
</dt> <dd> <dl> <dt>

Data type: **UInt8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum temperature in degrees Celsius at which the storage device is capable of normal operation.

</dd> <dt>

**Wear**
</dt> <dd> <dl> <dt>

Data type: **UInt8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The storage device wear indicator, in percentage. At 100 percent, the estimated wear limit will have been reached.

</dd> <dt>

**WriteErrorsCorrected**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of write errors that were corrected by the storage device.

</dd> <dt>

**WriteErrorsTotal**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of write errors that were encountered by the storage device.

</dd> <dt>

**WriteErrorsUncorrected**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of write errors that were not corrected by the storage device.

</dd> <dt>

**WriteLatencyMax**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum latency experienced by a write request, in milliseconds. A value greater than 10 seconds may indicate a problem with the disk or the HBA.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> <dt>

[**MSFT\_DiskToStorageReliabilityCounter**](msft-disktostoragereliabilitycounter.md)
</dt> <dt>

[**MSFT\_PhysicalDiskToStorageReliabilityCounter**](msft-physicaldisktostoragereliabilitycounter.md)
</dt> </dl>

 

 






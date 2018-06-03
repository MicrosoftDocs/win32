---
title: STORAGE\_PROPERTY\_ID enumeration
description: This enumeration is used in the STORAGE\_PROPERTY\_QUERY structure in conjunction with IOCTL\_STORAGE\_QUERY\_PROPERTY to retrieve information about a storage device or adapter.
ms.assetid: b6952d79-ae93-4109-83cc-7621aa61107c
keywords:
- STORAGE_PROPERTY_ID enumeration Storage Devices
- PSTORAGE_PROPERTY_ID enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_PROPERTY_ID
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# STORAGE\_PROPERTY\_ID enumeration

This enumeration is used in the [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md) structure in conjunction with [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) to retrieve information about a storage device or adapter.

## Syntax


```C++
typedef enum _STORAGE_PROPERTY_ID { 
  StorageDeviceProperty                   = 0,
  StorageAdapterProperty,
  StorageDeviceIdProperty,
  StorageDeviceUniqueIdProperty,
  StorageDeviceWriteCacheProperty,
  StorageMiniportProperty,
  StorageAccessAlignmentProperty,
  StorageDeviceSeekPenaltyProperty,
  StorageDeviceTrimProperty,
  StorageDeviceWriteAggregationProperty,
  StorageDeviceDeviceTelemetryProperty,
  StorageDeviceLBProvisioningProperty,
  StorageDevicePowerProperty,
  StorageDeviceCopyOffloadProperty,
  StorageDeviceResiliencyProperty,
  StorageDeviceMediumProductType,
  StorageAdapterCryptoProperty,
  StorageDeviceIoCapabilityProperty       = 48,
  StorageAdapterProtocolSpecificProperty,
  StorageDeviceProtocolSpecificProperty,
  StorageAdapterTemperatureProperty,
  StorageDeviceTemperatureProperty,
  StorageAdapterPhysicalTopologyProperty,
  StorageDevicePhysicalTopologyProperty,
  StorageDeviceAttributesProperty
} STORAGE_PROPERTY_ID, *PSTORAGE_PROPERTY_ID;
```



## Constants

<dl> <dt>

<span id="StorageDeviceProperty"></span><span id="storagedeviceproperty"></span><span id="STORAGEDEVICEPROPERTY"></span>**StorageDeviceProperty**
</dt> <dd>

Indicates that the caller is querying for the device descriptor, [**STORAGE\_DEVICE\_DESCRIPTOR**](storage-device-descriptor.md).

</dd> <dt>

<span id="StorageAdapterProperty"></span><span id="storageadapterproperty"></span><span id="STORAGEADAPTERPROPERTY"></span>**StorageAdapterProperty**
</dt> <dd>

Indicates that the caller is querying for the adapter descriptor, [**STORAGE\_ADAPTER\_DESCRIPTOR**](storage-adapter-descriptor.md).

</dd> <dt>

<span id="StorageDeviceIdProperty"></span><span id="storagedeviceidproperty"></span><span id="STORAGEDEVICEIDPROPERTY"></span>**StorageDeviceIdProperty**
</dt> <dd>

Indicates that the caller is querying for the device identifiers provided with the SCSI vital product data pages. Data is returned using the [**STORAGE\_DEVICE\_ID\_DESCRIPTOR**](storage-device-id-descriptor.md) structure.

</dd> <dt>

<span id="StorageDeviceUniqueIdProperty"></span><span id="storagedeviceuniqueidproperty"></span><span id="STORAGEDEVICEUNIQUEIDPROPERTY"></span>**StorageDeviceUniqueIdProperty**
</dt> <dd>

Indicates that the caller is querying for the unique device identifiers. Data is returned using the [**STORAGE\_DEVICE\_UNIQUE\_IDENTIFIER**](storage-device-unique-identifier.md) structure.

</dd> <dt>

<span id="StorageDeviceWriteCacheProperty"></span><span id="storagedevicewritecacheproperty"></span><span id="STORAGEDEVICEWRITECACHEPROPERTY"></span>**StorageDeviceWriteCacheProperty**
</dt> <dd>

Indicates that the caller is querying for the write cache property. Data is returned using the [**STORAGE\_WRITE\_CACHE\_PROPERTY**](storage-write-cache-property.md) structure.

</dd> <dt>

<span id="StorageMiniportProperty"></span><span id="storageminiportproperty"></span><span id="STORAGEMINIPORTPROPERTY"></span>**StorageMiniportProperty**
</dt> <dd>

Reserved for system use.

</dd> <dt>

<span id="StorageAccessAlignmentProperty"></span><span id="storageaccessalignmentproperty"></span><span id="STORAGEACCESSALIGNMENTPROPERTY"></span>**StorageAccessAlignmentProperty**
</dt> <dd>

Indicates that the caller is querying for the access alignment descriptor, [**STORAGE\_ACCESS\_ALIGNMENT\_DESCRIPTOR**](storage-access-alignment-descriptor.md).

</dd> <dt>

<span id="StorageDeviceSeekPenaltyProperty"></span><span id="storagedeviceseekpenaltyproperty"></span><span id="STORAGEDEVICESEEKPENALTYPROPERTY"></span>**StorageDeviceSeekPenaltyProperty**
</dt> <dd>

Indicates that the caller is querying for the seek penalty descriptor, [**DEVICE\_SEEK\_PENALTY\_DESCRIPTOR**](device-seek-penalty-descriptor.md).

</dd> <dt>

<span id="StorageDeviceTrimProperty"></span><span id="storagedevicetrimproperty"></span><span id="STORAGEDEVICETRIMPROPERTY"></span>**StorageDeviceTrimProperty**
</dt> <dd>

Indicates that the caller is querying for the trim descriptor, [**DEVICE\_TRIM\_DESCRIPTOR**](device-trim-descriptor.md).

</dd> <dt>

<span id="StorageDeviceWriteAggregationProperty"></span><span id="storagedevicewriteaggregationproperty"></span><span id="STORAGEDEVICEWRITEAGGREGATIONPROPERTY"></span>**StorageDeviceWriteAggregationProperty**
</dt> <dd>

Reserved for system use.

</dd> <dt>

<span id="StorageDeviceDeviceTelemetryProperty"></span><span id="storagedevicedevicetelemetryproperty"></span><span id="STORAGEDEVICEDEVICETELEMETRYPROPERTY"></span>**StorageDeviceDeviceTelemetryProperty**
</dt> <dd>

Reserved for system use.

</dd> <dt>

<span id="StorageDeviceLBProvisioningProperty"></span><span id="storagedevicelbprovisioningproperty"></span><span id="STORAGEDEVICELBPROVISIONINGPROPERTY"></span>**StorageDeviceLBProvisioningProperty**
</dt> <dd>

Indicates that the caller is querying for the logical block provisioning property. Data is returned using the [**DEVICE\_LB\_PROVISIONING\_DESCRIPTOR**](device-lb-provisioning-descriptor.md) structure.

</dd> <dt>

<span id="StorageDevicePowerProperty"></span><span id="storagedevicepowerproperty"></span><span id="STORAGEDEVICEPOWERPROPERTY"></span>**StorageDevicePowerProperty**
</dt> <dd>

Indicates that the caller is querying for the device power descriptor. Data is returned using the [**DEVICE\_POWER\_DESCRIPTOR**](device-power-descriptor.md) structure.

</dd> <dt>

<span id="StorageDeviceCopyOffloadProperty"></span><span id="storagedevicecopyoffloadproperty"></span><span id="STORAGEDEVICECOPYOFFLOADPROPERTY"></span>**StorageDeviceCopyOffloadProperty**
</dt> <dd>

Indicates that the caller is querying for the copy offload parameters property. Data is returned using the [**DEVICE\_COPY\_OFFLOAD\_DESCRIPTOR**](device-copy-offload-descriptor.md) structure.

</dd> <dt>

<span id="StorageDeviceResiliencyProperty"></span><span id="storagedeviceresiliencyproperty"></span><span id="STORAGEDEVICERESILIENCYPROPERTY"></span>**StorageDeviceResiliencyProperty**
</dt> <dd>

Reserved for system use.

</dd> <dt>

<span id="StorageDeviceMediumProductType"></span><span id="storagedevicemediumproducttype"></span><span id="STORAGEDEVICEMEDIUMPRODUCTTYPE"></span>**StorageDeviceMediumProductType**
</dt> <dd>

Indicates that the caller is querying for the medium product type. Data is returned using the [**STORAGE\_MEDIUM\_PRODUCT\_TYPE\_DESCRIPTOR**](storage-medium-product-type-descriptor.md) structure.

</dd> <dt>

<span id="StorageAdapterCryptoProperty"></span><span id="storageadaptercryptoproperty"></span><span id="STORAGEADAPTERCRYPTOPROPERTY"></span>**StorageAdapterCryptoProperty**
</dt> <dd>

Reserved for system use.

</dd> <dt>

<span id="StorageDeviceIoCapabilityProperty"></span><span id="storagedeviceiocapabilityproperty"></span><span id="STORAGEDEVICEIOCAPABILITYPROPERTY"></span>**StorageDeviceIoCapabilityProperty**
</dt> <dd>

Indicates that the caller is querying for the device I/O capability property. Data is returned using the [**DEVICE\_IO\_CAPABILITY\_DESCRIPTOR**](storage-device-io-capability-descriptor.md) structure.

</dd> <dt>

<span id="StorageAdapterProtocolSpecificProperty"></span><span id="storageadapterprotocolspecificproperty"></span><span id="STORAGEADAPTERPROTOCOLSPECIFICPROPERTY"></span>**StorageAdapterProtocolSpecificProperty**
</dt> <dd>

Indicates that the caller is querying for protocol-specific data from the adapter. Data is returned using the [**STORAGE\_PROTOCOL\_DATA\_DESCRIPTOR**](storage-protocol-data-descriptor.md) structure. See the remarks for more info.

</dd> <dt>

<span id="StorageDeviceProtocolSpecificProperty"></span><span id="storagedeviceprotocolspecificproperty"></span><span id="STORAGEDEVICEPROTOCOLSPECIFICPROPERTY"></span>**StorageDeviceProtocolSpecificProperty**
</dt> <dd>

Indicates that the caller is querying for protocol-specific data from the device. Data is returned using the [**STORAGE\_PROTOCOL\_DATA\_DESCRIPTOR**](storage-protocol-data-descriptor.md) structure. See the remarks for more info.

</dd> <dt>

<span id="StorageAdapterTemperatureProperty"></span><span id="storageadaptertemperatureproperty"></span><span id="STORAGEADAPTERTEMPERATUREPROPERTY"></span>**StorageAdapterTemperatureProperty**
</dt> <dd>

Indicates that the caller is querying temperature data from the adapter. Data is returned using the [**STORAGE\_TEMPERATURE\_DATA\_DESCRIPTOR**](storage-temperature-data-descriptor.md) structure.

</dd> <dt>

<span id="StorageDeviceTemperatureProperty"></span><span id="storagedevicetemperatureproperty"></span><span id="STORAGEDEVICETEMPERATUREPROPERTY"></span>**StorageDeviceTemperatureProperty**
</dt> <dd>

Indicates that the caller is querying for temperature data from the device. Data is returned using the [**STORAGE\_TEMPERATURE\_DATA\_DESCRIPTOR**](storage-temperature-data-descriptor.md) structure.

</dd> <dt>

<span id="StorageAdapterPhysicalTopologyProperty"></span><span id="storageadapterphysicaltopologyproperty"></span><span id="STORAGEADAPTERPHYSICALTOPOLOGYPROPERTY"></span>**StorageAdapterPhysicalTopologyProperty**
</dt> <dd>

Indicates that the caller is querying for topology information from the adapter. Data is returned using the [**STORAGE\_PHYSICAL\_TOPOLOGY\_DESCRIPTOR**](storage-physical-topology-descriptor.md) structure.

</dd> <dt>

<span id="StorageDevicePhysicalTopologyProperty"></span><span id="storagedevicephysicaltopologyproperty"></span><span id="STORAGEDEVICEPHYSICALTOPOLOGYPROPERTY"></span>**StorageDevicePhysicalTopologyProperty**
</dt> <dd>

Indicates that the caller is querying for topology information from the device. Data is returned using the [**STORAGE\_PHYSICAL\_TOPOLOGY\_DESCRIPTOR**](storage-physical-topology-descriptor.md) structure.

</dd> <dt>

<span id="StorageDeviceAttributesProperty"></span><span id="storagedeviceattributesproperty"></span><span id="STORAGEDEVICEATTRIBUTESPROPERTY"></span>**StorageDeviceAttributesProperty**
</dt> <dd>

Indicates that the caller is querying for attributes information from the device. Data is returned using the [**STORAGE\_DEVICE\_ATTRIBUTES\_DESCRIPTOR**](storage-device-attributes-descriptor.md) structure.

</dd> </dl>

## Remarks

Enumeration values have been added over time. See the header file in the respective Windows Software Development Kit (SDK) to determine availability.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> <dt>

[**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md)
</dt> <dt>

[**STORAGE\_QUERY\_TYPE**](storage-query-type.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_PROPERTY_ID%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







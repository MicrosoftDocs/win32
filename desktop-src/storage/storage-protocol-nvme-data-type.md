---
title: STORAGE\_PROTOCOL\_NVME\_DATA\_TYPE enumeration
description: Describes the type of NVMe protocol-specific data that's to be queried during an IOCTL\_STORAGE\_QUERY\_PROPERTY request.
ms.assetid: '02DB004B-F5B9-4CA2-9CA8-9C7BFB9BA5CD'
keywords: ["STORAGE_PROTOCOL_NVME_DATA_TYPE enumeration Storage Devices", "PSTORAGE_PROTOCOL_NVME_DATA_TYPE enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_PROTOCOL_NVME_DATA_TYPE
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_PROTOCOL\_NVME\_DATA\_TYPE enumeration

Describes the type of NVMe protocol-specific data that's to be queried during an [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request.

## Syntax


```C++
typedef enum _STORAGE_PROTOCOL_NVME_DATA_TYPE { 
  NVMeDataTypeUnknown   = 0,
  NVMeDataTypeIdentify,
  NVMeDataTypeLogPage,
  NVMeDataTypeFeature
} STORAGE_PROTOCOL_NVME_DATA_TYPE, *PSTORAGE_PROTOCOL_NVME_DATA_TYPE;
```



## Constants

<dl> <dt>

<span id="NVMeDataTypeUnknown"></span><span id="nvmedatatypeunknown"></span><span id="NVMEDATATYPEUNKNOWN"></span>**NVMeDataTypeUnknown**
</dt> <dd>

Unknown data type.

</dd> <dt>

<span id="NVMeDataTypeIdentify"></span><span id="nvmedatatypeidentify"></span><span id="NVMEDATATYPEIDENTIFY"></span>**NVMeDataTypeIdentify**
</dt> <dd>

Identify data type. This can be either Identify Controller data or Identify Namespace data. When this type of data is being queried, the ProtocolDataRequestValue field of [**STORAGE\_PROTOCOL\_SPECIFIC\_DATA**](storage-protocol-specific-data.md) will have a value of **NVME\_IDENTIFY\_CNS\_CONTROLLER** for adapter or **NVME\_IDENTIFY\_CNS\_SPECIFIC\_NAMESPACE** for namespace. If the ProtocolDataRequestValue is **NVME\_IDENTIFY\_CNS\_SPECIFIC\_NAMESPACE**, the ProtocolDataRequestSubValue field from the **STORAGE\_PROTOCOL\_SPECIFIC\_DATA** structure will have a value of the namespace ID.

</dd> <dt>

<span id="NVMeDataTypeLogPage"></span><span id="nvmedatatypelogpage"></span><span id="NVMEDATATYPELOGPAGE"></span>**NVMeDataTypeLogPage**
</dt> <dd>

Log page data type.

</dd> <dt>

<span id="NVMeDataTypeFeature"></span><span id="nvmedatatypefeature"></span><span id="NVMEDATATYPEFEATURE"></span>**NVMeDataTypeFeature**
</dt> <dd>

Feature data type.

</dd> </dl>

## Remarks

When using [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) to retrieve protocol-specific information in the [**STORAGE\_PROTOCOL\_DATA\_DESCRIPTOR**](storage-protocol-data-descriptor.md), configure the [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md) structure as follows:

-   Allocate a buffer that can contains both a [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md) and a [**STORAGE\_PROTOCOL\_SPECIFIC\_DATA**](storage-protocol-specific-data.md) structure.

-   Set the **PropertyID** field to **StorageAdapterProtocolSpecificProperty** or **StorageDeviceProtocolSpecificProperty** for a controller or device/namespace request, respectively.

-   Set the **QueryType** field to **PropertyStandardQuery**.

-   Fill the [**STORAGE\_PROTOCOL\_SPECIFIC\_DATA**](storage-protocol-specific-data.md) structure with the desired values. The start of the **STORAGE\_PROTOCOL\_SPECIFIC\_DATA** is the **AdditionalParameters** field of [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md).

To specify a type of NVMe protocol-specific information, configure the [**STORAGE\_PROTOCOL\_SPECIFIC\_DATA**](storage-protocol-specific-data.md) structure as follows:

-   Set the **ProtocolType** field to **ProtocolTypeNVMe**.

-   Set the **DataType** field to an enumeration value defined by **STORAGE\_PROTOCOL\_NVME\_DATA\_TYPE**:

    -   Use **NVMeDataTypeIdentify** to get Identify Controller data or Identify Namespace data.
    -   Use **NVMeDataTypeLogPage** to get log pages (including SMART/health data).
    -   Use **NVMeDataTypeFeature** to get features of the NVMe drive.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                                      |
| Server<br/> | Windows Server 2016<br/>                                                                             |
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> <dt>

[**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md)
</dt> <dt>

[**STORAGE\_PROPERTY\_ID**](storage-property-id.md)
</dt> <dt>

[**STORAGE\_PROTOCOL\_SPECIFIC\_DATA**](storage-protocol-specific-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_PROTOCOL_NVME_DATA_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







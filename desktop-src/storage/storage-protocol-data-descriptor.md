---
title: STORAGE\_PROTOCOL\_DATA\_DESCRIPTOR structure
description: This structure is used in conjunction with IOCTL\_STORAGE\_QUERY\_PROPERTY to return protocol-specific data from a storage device or adapter.
ms.assetid: '292EE243-2952-4020-8EB0-C5127DF92318'
keywords: ["STORAGE_PROTOCOL_DATA_DESCRIPTOR structure Storage Devices", "PSTORAGE_PROTOCOL_DATA_DESCRIPTOR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_PROTOCOL_DATA_DESCRIPTOR
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_PROTOCOL\_DATA\_DESCRIPTOR structure

This structure is used in conjunction with [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) to return protocol-specific data from a storage device or adapter. .

## Syntax


```C++
typedef struct _STORAGE_PROTOCOL_DATA_DESCRIPTOR {
  ULONG                          Version;
  ULONG                          Size;
  STORAGE_PROTOCOL_SPECIFIC_DATA ProtocolSpecificData;
} STORAGE_PROTOCOL_DATA_DESCRIPTOR, *PSTORAGE_PROTOCOL_DATA_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure.

</dd> <dt>

**Size**
</dt> <dd>

The total size of the descriptor, including the space for all protocol data.

</dd> <dt>

**ProtocolSpecificData**
</dt> <dd>

The protocol-specific data, of type [**STORAGE\_PROTOCOL\_SPECIFIC\_DATA**](storage-protocol-specific-data.md).

</dd> </dl>

## Remarks

When using [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) to retrieve protocol-specific information in the **STORAGE\_PROTOCOL\_DATA\_DESCRIPTOR**, configure the [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md) structure as follows:

-   Allocate a buffer that can contains both a [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md) and a [**STORAGE\_PROTOCOL\_SPECIFIC\_DATA**](storage-protocol-specific-data.md) structure.

-   Set the **PropertyID** field to **StorageAdapterProtocolSpecificProperty** or **StorageDeviceProtocolSpecificProperty** for a controller or device/namespace request, respectively.

-   Set the **QueryType** field to **PropertyStandardQuery**.

-   Fill the [**STORAGE\_PROTOCOL\_SPECIFIC\_DATA**](storage-protocol-specific-data.md) structure with the desired values. The start of the **STORAGE\_PROTOCOL\_SPECIFIC\_DATA** is the **AdditionalParameters** field of [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md).

To specify a type of NVMe protocol-specific information, configure the [**STORAGE\_PROTOCOL\_SPECIFIC\_DATA**](storage-protocol-specific-data.md) structure as follows:

-   Set the **ProtocolType** field to **ProtocolTypeNVMe**.

-   Set the **DataType** field to an enumeration value defined by [**STORAGE\_PROTOCOL\_NVME\_DATA\_TYPE**](storage-protocol-nvme-data-type.md):

    -   Use **NVMeDataTypeIdentify** to get Identify Controller data or Identify Namespace data.
    -   Use **NVMeDataTypeLogPage** to get log pages (including SMART/health data).
    -   Use **NVMeDataTypeFeature** to get features of the NVMe drive.

To specify a type of ATA protocol-specific information, configure the [**STORAGE\_PROTOCOL\_SPECIFIC\_DATA**](storage-protocol-specific-data.md) structure as follows:

-   Set the **ProtocolType** field to **ProtocolTypeAta**.

-   Set the **DataType** field to an enumeration value defined by [**STORAGE\_PROTOCOL\_ATA\_DATA\_TYPE**](storage-protocol-ata-data-type.md):

    -   Use **AtaDataTypeIdentify** to identify the ATA drive.
    -   Use **AtaDataTypeLogPage** to get log pages from the ATA drive.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_PROTOCOL_DATA_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







---
title: STORAGE\_PROTOCOL\_ATA\_DATA\_TYPE enumeration
description: The ATA protocol data type.
ms.assetid: '4B42E143-17F5-4841-A9EA-C225B167E242'
keywords: ["STORAGE_PROTOCOL_ATA_DATA_TYPE enumeration Storage Devices", "PSTORAGE_PROTOCOL_ATA_DATA_TYPE enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_PROTOCOL_ATA_DATA_TYPE
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_PROTOCOL\_ATA\_DATA\_TYPE enumeration

The ATA protocol data type.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef enum _STORAGE_PROTOCOL_ATA_DATA_TYPE { 
  AtaDataTypeUnknown   = 0,
  AtaDataTypeIdentify,
  AtaDataTypeLogPage
} STORAGE_PROTOCOL_ATA_DATA_TYPE, *PSTORAGE_PROTOCOL_ATA_DATA_TYPE;
```



## Constants

<dl> <dt>

<span id="AtaDataTypeUnknown"></span><span id="atadatatypeunknown"></span><span id="ATADATATYPEUNKNOWN"></span>**AtaDataTypeUnknown**
</dt> <dd>

Unknown data type.

</dd> <dt>

<span id="AtaDataTypeIdentify"></span><span id="atadatatypeidentify"></span><span id="ATADATATYPEIDENTIFY"></span>**AtaDataTypeIdentify**
</dt> <dd>

Identify device data type.

</dd> <dt>

<span id="AtaDataTypeLogPage"></span><span id="atadatatypelogpage"></span><span id="ATADATATYPELOGPAGE"></span>**AtaDataTypeLogPage**
</dt> <dd>

Log page data type.

</dd> </dl>

## Remarks

When using [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) to retrieve protocol-specific information in the [**STORAGE\_PROTOCOL\_DATA\_DESCRIPTOR**](storage-protocol-data-descriptor.md), configure the [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md) structure as follows:

-   Allocate a buffer that can contains both a [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md) and a [**STORAGE\_PROTOCOL\_SPECIFIC\_DATA**](storage-protocol-specific-data.md) structure.

-   Set the **PropertyID** field to **StorageAdapterProtocolSpecificProperty** or **StorageDeviceProtocolSpecificProperty** for a controller or device/namespace request, respectively.

-   Set the **QueryType** field to **PropertyStandardQuery**.

-   Fill the [**STORAGE\_PROTOCOL\_SPECIFIC\_DATA**](storage-protocol-specific-data.md) structure with the desired values. The start of the **STORAGE\_PROTOCOL\_SPECIFIC\_DATA** is the **AdditionalParameters** field of [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md).

To specify a type of ATA protocol-specific information, configure the [**STORAGE\_PROTOCOL\_SPECIFIC\_DATA**](storage-protocol-specific-data.md) structure as follows:

-   Set the **ProtocolType** field to **ProtocolTypeAta**.

-   Set the **DataType** field to an enumeration value defined by **STORAGE\_PROTOCOL\_ATA\_DATA\_TYPE**:

    -   Use **AtaDataTypeIdentify** to identify the ATA drive.
    -   Use **AtaDataTypeLogPage** to get log pages from the ATA drive.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                 |
| Server<br/> | Windows Server 2016<br/>                                                        |
| Header<br/> | <dl> <dt>Ntddstor.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_PROTOCOL_ATA_DATA_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






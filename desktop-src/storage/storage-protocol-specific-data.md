---
title: STORAGE\_PROTOCOL\_SPECIFIC\_DATA structure
description: Describes protocol-specific device data, provided in the input and output buffer of an IOCTL\_STORAGE\_QUERY\_PROPERTY request.
ms.assetid: 74569A0A-5828-4533-8974-4DE0B4EAAAEB
keywords:
- STORAGE_PROTOCOL_SPECIFIC_DATA structure Storage Devices
- PSTORAGE_PROTOCOL_SPECIFIC_DATA structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_PROTOCOL_SPECIFIC_DATA
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_PROTOCOL\_SPECIFIC\_DATA structure

Describes protocol-specific device data, provided in the input and output buffer of an [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request.

## Syntax


```C++
typedef struct _STORAGE_PROTOCOL_SPECIFIC_DATA {
  STORAGE_PROTOCOL_TYPE ProtocolType;
  ULONG                 DataType;
  ULONG                 ProtocolDataRequestValue;
  ULONG                 ProtocolDataRequestSubValue;
  ULONG                 ProtocolDataOffset;
  ULONG                 ProtocolDataLength;
  ULONG                 FixedProtocolReturnData;
  ULONG                 Reserved[3];
} STORAGE_PROTOCOL_SPECIFIC_DATA, *PSTORAGE_PROTOCOL_SPECIFIC_DATA;
```



## Members

<dl> <dt>

**ProtocolType**
</dt> <dd>

The protocol type. Values for this member are defined in the [**STORAGE\_PROTOCOL\_TYPE**](storage-protocol-type.md) enumeration.

</dd> <dt>

**DataType**
</dt> <dd>

The protocol data type. Data types are defined in the [**STORAGE\_PROTOCOL\_NVME\_DATA\_TYPE**](storage-protocol-nvme-data-type.md) and [**STORAGE\_PROTOCOL\_ATA\_DATA\_TYPE**](storage-protocol-ata-data-type.md) enumerations.

</dd> <dt>

**ProtocolDataRequestValue**
</dt> <dd>

The protocol data request value.

</dd> <dt>

**ProtocolDataRequestSubValue**
</dt> <dd>

The sub value of the protocol data request.

</dd> <dt>

**ProtocolDataOffset**
</dt> <dd>

The offset of the data buffer that is from the beginning of this structure. The typical value can be sizeof(**STORAGE\_PROTOCOL\_SPECIFIC\_DATA**).

</dd> <dt>

**ProtocolDataLength**
</dt> <dd>

The length of the protocol data.

</dd> <dt>

**FixedProtocolReturnData**
</dt> <dd>

The returned data.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use.

</dd> </dl>

## Remarks

When using [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) to retrieve protocol-specific information in the [**STORAGE\_PROTOCOL\_DATA\_DESCRIPTOR**](storage-protocol-data-descriptor.md), configure the [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md) structure as follows:

-   Allocate a buffer that can contains both a [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md) and a **STORAGE\_PROTOCOL\_SPECIFIC\_DATA** structure.

-   Set the **PropertyID** field to **StorageAdapterProtocolSpecificProperty** or **StorageDeviceProtocolSpecificProperty** for a controller or device/namespace request, respectively.

-   Set the **QueryType** field to **PropertyStandardQuery**.

-   Fill the **STORAGE\_PROTOCOL\_SPECIFIC\_DATA** structure with the desired values. The start of the **STORAGE\_PROTOCOL\_SPECIFIC\_DATA** is the **AdditionalParameters** field of [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md).

To specify a type of NVMe protocol-specific information, configure the **STORAGE\_PROTOCOL\_SPECIFIC\_DATA** structure as follows:

-   Set the **ProtocolType** field to **ProtocolTypeNVMe**.

-   Set the **DataType** field to an enumeration value defined by [**STORAGE\_PROTOCOL\_NVME\_DATA\_TYPE**](storage-protocol-nvme-data-type.md):

    -   Use **NVMeDataTypeIdentify** to get Identify Controller data or Identify Namespace data.
    -   Use **NVMeDataTypeLogPage** to get log pages (including SMART/health data).
    -   Use **NVMeDataTypeFeature** to get features of the NVMe drive.

To specify a type of ATA protocol-specific information, configure the **STORAGE\_PROTOCOL\_SPECIFIC\_DATA** structure as follows:

-   Set the **ProtocolType** field to **ProtocolTypeAta**.

-   Set the **DataType** field to an enumeration value defined by [**STORAGE\_PROTOCOL\_ATA\_DATA\_TYPE**](storage-protocol-ata-data-type.md):

    -   Use **AtaDataTypeIdentify** to identify the ATA drive.
    -   Use **AtaDataTypeLogPage** to get log pages from the ATA drive.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                                      |
| Server<br/> | Windows Server 2016<br/>                                                                             |
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_PROTOCOL_SPECIFIC_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







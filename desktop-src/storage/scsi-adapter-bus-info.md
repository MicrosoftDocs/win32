---
title: SCSI\_ADAPTER\_BUS\_INFO structure
description: The SCSI\_ADAPTER\_BUS\_INFO structure is used in conjunction with the IOCTL\_SCSI\_GET\_INQUIRY\_DATA request to retrieve the SCSI inquiry data for all devices on a given SCSI bus.
ms.assetid: '786d6813-a9f3-437e-9b41-d69e0fce9a4c'
keywords: ["SCSI_ADAPTER_BUS_INFO structure Storage Devices", "PSCSI_ADAPTER_BUS_INFO structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SCSI_ADAPTER_BUS_INFO
api_location:
- ntddscsi.h
api_type:
- HeaderDef
---

# SCSI\_ADAPTER\_BUS\_INFO structure

The SCSI\_ADAPTER\_BUS\_INFO structure is used in conjunction with the [**IOCTL\_SCSI\_GET\_INQUIRY\_DATA**](ioctl-scsi-get-inquiry-data.md) request to retrieve the SCSI inquiry data for all devices on a given SCSI bus.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SCSI_ADAPTER_BUS_INFO {
  UCHAR         NumberOfBuses;
  SCSI_BUS_DATA BusData[1];
} SCSI_ADAPTER_BUS_INFO, *PSCSI_ADAPTER_BUS_INFO;
```



## Members

<dl> <dt>

**NumberOfBuses**
</dt> <dd>

Contains the number of buses on the adapter for which inquiry data is being reported.

</dd> <dt>

**BusData**
</dt> <dd>

Contains a variable length array of [**SCSI\_BUS\_DATA**](scsi-bus-data.md) structures that hold the inquiry data.

</dd> </dl>

## Remarks

SCSI\_ADAPTER\_BUS\_INFO is a header structure that describes the layout of the output buffer of the [**IOCTL\_SCSI\_GET\_INQUIRY\_DATA**](ioctl-scsi-get-inquiry-data.md) request. This request returns SCSI inquiry data for all of the logical units on all of the buses associated with a particular SCSI host bus adapter (HBA). The **BusData** member of SCSI\_ADAPTER\_BUS\_INFO contains a variable length array of [**SCSI\_BUS\_DATA**](scsi-bus-data.md) structures. This array has one element for each SCSI bus on the adapter, so its size is equal to the number of buses indicated in the **NumberOfBuses** member of SCSI\_ADAPTER\_BUS\_INFO.

In most cases, **NumberOfBuses** will have a value of 1. Early SCSI buses were limited to 36 targets (rather than the current limit of 128), so some vendors manufactured HBAs with several buses, in order to increase the maximum number of targets. To support these older HBAs, Windows provides a mechanism for retrieving inquiry data from HBAs with multiple buses. For adapters with a single bus, **NumberOfBuses** will be one, and the **BusData** member of SCSI\_ADAPTER\_BUS\_INFO will have only one element, but HBAs with multiple buses will generate data for multiple SCSI\_BUS\_DATA structures, and **NumberOfBuses** will be greater than 1.

Immediately following the array in **BusData** is the inquiry data for all of the devices on all the buses that belong to the HBA. The **InquiryDataOffset** member of each SCSI\_BUS\_DATA structure provides an offset to the inquiry data for the corresponding SCSI bus.

The inquiry data for each SCSI bus includes information about all of the logical units on that bus. Each logical unit's inquiry data is formatted in a structure of type [**SCSI\_INQUIRY\_DATA**](scsi-inquiry-data.md), and all of the SCSI\_INQUIRY\_DATA structures for a particular bus are linked together by the **NextInquiryDataOffset** member. There will be a separate list for each SCSI bus, and the **NextInquiryDataOffset** member of the last structure in each list contains a value of zero.

The following pseudocode example illustrates how to step through the SCSI buses on an HBA, and the logical units for each bus, reading and printing the inquiry data for each logical unit:


```
VOID
PrintInquiryData(PCHAR  DataBuffer)
{
    PSCSI_ADAPTER_BUS_INFO  adapterInfo;
    PSCSI_INQUIRY_DATA inquiryData;
    ULONG i, j;

    adapterInfo = (PSCSI_ADAPTER_BUS_INFO) DataBuffer;
    for (i = 0; i < adapterInfo->NumberOfBuses; i++) {
       inquiryData = (PSCSI_INQUIRY_DATA) (DataBuffer +
          adapterInfo->BusData[i].InquiryDataOffset);
       while (adapterInfo->BusData[i].InquiryDataOffset) {
          printf(" %d   %d  %3d    %s    %.28s ",
             i,
             inquiryData->TargetId,
             inquiryData->Lun,
             (inquiryData->DeviceClaimed) ? "Y" : "N",
             &amp;inquiryData->InquiryData[8]);
          for (j = 0; j < 8; j++) {
             printf("%02X ", inquiryData->InquiryData[j]);
          }
          printf("\n");
          if (inquiryData->NextInquiryDataOffset == 0) {
             break;
          }
          inquiryData = (PSCSI_INQUIRY_DATA) (DataBuffer +
             inquiryData->NextInquiryDataOffset);
       }
    }
    printf("\n\n");
}
```



You must use **NextInquiryDataOffset** member to locate the inquiry data for next logical unit. Do not try to do this by pointer arithmetic. The positioning of each SCSI\_INQUIRY\_DATA structure is potentially different for each HBA miniport driver, because it depends on data alignment requirements.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_SCSI\_GET\_INQUIRY\_DATA**](ioctl-scsi-get-inquiry-data.md)
</dt> <dt>

[**SCSI\_BUS\_DATA**](scsi-bus-data.md)
</dt> <dt>

[**SCSI\_INQUIRY\_DATA**](scsi-inquiry-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SCSI_ADAPTER_BUS_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







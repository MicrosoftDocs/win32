---
Description: Starting in Windows 10, drivers can implement the Energy Metering Interface (EMI) to expose energy consumption data to clients.
ms.assetid: D11C97E8-8E7F-41D7-A8A9-0B5426B20818
title: Energy Metering Interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Energy Metering Interface

Starting in Windows 10, drivers can implement the Energy Metering Interface (EMI) to expose energy consumption data to clients. This interface consists of a set of standardized IOCTLs for clients to get energy data as well as data about the metering hardware and the hardware being metered.

On-board energy meters periodically measure voltage and current on a rail, calculate a power product, and integrate the total energy consumed over time. These meters are distinct from the existing [power meter (PMI)](https://www.bing.com/search?q=power meter (PMI)) concept because power meters have a global averaging interval. Energy meters allow multiple consumers to determine average power over different intervals according to their needs by returning total energy consumption up to the present.

The EMI interface provides the conduit for energy data to be consumed by interested client applications and services. Clients calculate energy consumed since their last query by subtracting the previous values from the latest values, and optionally convert to average power by simple division.

## Discovering devices that implement EMI

Clients discover devices that support the EMI through calls to [**SetupDiEnumDeviceInterfaces**](https://www.bing.com/search?q=**SetupDiEnumDeviceInterfaces**) and [**SetupDiGetDeviceInterfaceDetail**](https://www.bing.com/search?q=**SetupDiGetDeviceInterfaceDetail**). One instance of an EMI device interface is created for each energy metering device that is EMI-compliant and is present in the system.

The GUID for the EMI device interface is {45BD8344-7ED6-49cf-A440-C276C933B053}, as defined in emi.h. Code can alternatively use GUID\_DEVICE\_ENERGY\_METER to specify this GUID.

## Using the EMI interface

Client code typically interacts with the EMI using the following process:

1.  Call [**IOCTL\_EMI\_GET\_VERSION**](/windows/desktop/api/emi/ni-emi-ioctl_emi_get_version) and verify the EMI interface version supported by the device in the returned [**EMI\_VERSION**](/windows/desktop/api/emi/ns-emi-emi_version) value. In Windows 10, devices can support **EMI\_VERSION\_V1**. Future operating system releases may introduce later versions.
2.  Call [**IOCTL\_EMI\_GET\_METADATA\_SIZE**](/windows/desktop/api/emi/ni-emi-ioctl_emi_get_metadata_size) to get size of the EMI metadata.
3.  Allocate a buffer of the required EMI metadata size and call [**IOCTL\_EMI\_GET\_METADATA**](/windows/desktop/api/emi/ni-emi-ioctl_emi_get_metadata). Verify that the returned [**EMI\_MEASUREMENT\_UNIT**](/windows/desktop/api/emi/ne-emi-emi_measurement_unit) is **EmiMeasurementUnitPicowattHours**. Releases after Windows 10 may define additional unit types.
4.  To measure total energy consumption, call [**IOCTL\_EMI\_GET\_MEASUREMENT**](/windows/desktop/api/emi/ni-emi-ioctl_emi_get_measurement). The **AbsoluteEnergy** value in the returned [**EMI\_MEASUREMENT\_DATA**](/windows/desktop/api/emi/ns-emi-emi_measurement_data) is the total accumulated energy in picowatt-hours with some arbitrary zero-point. In general, you need to compare samples at two different times and subtract the energy values for energy consumption over that interval.
5.  To measure average power consumption, call [**IOCTL\_EMI\_GET\_MEASUREMENT**](/windows/desktop/api/emi/ni-emi-ioctl_emi_get_measurement) at the beginning and end of the desired interval. Subtract the **AbsoluteEnergy** and **AbsoluteTime** values of the [**EMI\_MEASUREMENT\_DATA**](/windows/desktop/api/emi/ns-emi-emi_measurement_data) returned by the latter sample from those of the earlier sample.

## In this section



| Topic                                                                             | Description                                                                                                                     |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [EMI IOCTLs](emi-ioctls.md)<br/>                                           | This section describes the I/O control codes (IOCTLs) that are supported by the Energy Measurement Interface (EMI).<br/>  |
| [EMI Enumerations and Structures](emi-enumerations-and-structures.md)<br/> | This section describes the enumerations and structures that are supported by the Energy Measurement Interface (EMI).<br/> |



 

## Related topics

<dl> <dt>

[Using Device Interfaces](https://www.bing.com/search?q=Using Device Interfaces)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bpowermeter\powermeter%5D:%20Energy%20Metering%20Interface%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")






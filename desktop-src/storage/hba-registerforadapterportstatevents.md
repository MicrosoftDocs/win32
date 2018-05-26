---
title: HBA\_RegisterForAdapterPortStatEvents routine
description: The HBA\_RegisterForAdapterPortStatEvents routine registers the indicated user callback routine to call when a port statistics event occurs.
ms.assetid: 82598ba4-6e01-44eb-9359-4b85e8f7980c
keywords:
- HBA_RegisterForAdapterPortStatEvents routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_RegisterForAdapterPortStatEvents
api_location:
- Hbaapi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HBA\_RegisterForAdapterPortStatEvents routine

The **HBA\_RegisterForAdapterPortStatEvents** routine registers the indicated user callback routine to call when a port statistics event occurs.

## Syntax


```C++
HBA_STATUS HBA_API HBA_RegisterForAdapterPortStatEvents(
   HBA_PORTSTAT_CALLBACK callback,
   void                  *userData,
   HBA_HANDLE            handle,
   HBA_WWN               PortWWN,
   PHBA_PORTSTATISTICS   stats,
   HBA_UINT32            statType,
   HBA_CALLBACKHANDLE    *callbackHandle
);
```



## Parameters

<dl> <dt>

*callback* 
</dt> <dd>

Pointer to a callback routine of type [**HBA\_PORTSTAT\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff557117) that is called when an adapter is added to the system.

</dd> <dt>

*userData* 
</dt> <dd>

Pointer to a buffer that is passed to the callback routine with each event. This data correlates the event with the source of the event registration.

</dd> <dt>

*handle* 
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA for which the adapter events are generated.

</dd> <dt>

*PortWWN* 
</dt> <dd>

Contains a 64-bit worldwide name (WWN) that uniquely identifies the HBA port from which port events are reported. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

*stats* 
</dt> <dd>

Pointer to a structure of type [**HBA\_PortStatistics**](hba-portstatistics.md) that, on input, holds the statistical levels that determine when port statistics events are generated. On output, this member holds statistical data gathered for the port referenced by *PortWWN.*

</dd> <dt>

*statType* 
</dt> <dd>

Holds a value that indicates the mechanism used to trigger port statistics events. If the value is HBA\_EVENT\_PORT\_STAT\_THRESHOLD, then each non-NULL member of the HBA\_PortStatistics structure pointed to by *stats* will indicate the threshold at which an event is generated for that particular statistical parameter. For example, if the **TxWords** member of the HBA\_PortStatistics structure holds a value of 1,000,000, then an event will be generated once 1,000,000 words have been transmitted.

If the value of *statType* is HBA\_EVENT\_PORT\_STAT\_GROWTH, then the values in the HBA\_PortStatistics structure will be interpreted as growth-rate numbers. The T11 committee's *Fibre Channel HBA API* specification recommends that port statistics be checked once a minute, and if the value or a given statistics parameter has grown by more than the number indicated for that parameter in HBA\_PortStatistics, an event is generated, but the actual frequency with which growth is monitored is hardware-specific.

</dd> <dt>

*callbackHandle* 
</dt> <dd>

Pointer to an opaque identifier that the user must pass to [**HBA\_RemoveCallback**](hba-removecallback.md) to de-register the callback routine.

</dd> </dl>

## Return value

The **HBA\_RegisterForAdapterPortStatEvents** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, this member should have one of the following values.



| Return code                                                                                                       | Description                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_OK**</dt> </dl>                    | Returned if the callback routine was successfully registered. <br/>                                                   |
| <dl> <dt>**HBA\_STATUS\_ERROR\_ILLEGAL\_WWN**</dt> </dl>   | Returned if the HBA referenced by *handle* does not have a port with a name that matches the value in *PortWWN*.<br/> |
| <dl> <dt>**HBA\_STATUS\_ERROR\_NOT\_SUPPORTED**</dt> </dl> | Returned if the hardware does not support statistic events. <br/>                                                     |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl>                 | Returned if an unspecified error occurred that prevented the registration of the callback routine. <br/>              |



 

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Hbaapi.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>Hbaapi.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**HBA\_OpenAdapter**](hba-openadapter.md)
</dt> <dt>

[**HBA\_PORTSTAT\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff557117)
</dt> <dt>

[**HBA\_PortStatistics**](hba-portstatistics.md)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_RegisterForAdapterPortStatEvents%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







---
title: HBA\_GetPortStatistics routine
description: The HBA\_GetPortStatistics routine retrieves statistics for the indicated port on the HBA.
ms.assetid: 282eccaf-7cb9-4675-9cc3-9261ed1322ca
keywords:
- HBA_GetPortStatistics routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_GetPortStatistics
api_location:
- Hbaapi.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HBA\_GetPortStatistics routine

The **HBA\_GetPortStatistics** routine retrieves statistics for the indicated port on the HBA.

## Syntax


```C++
HBA_STATUS HBA_API HBA_GetPortStatistics(
  _In_  HBA_HANDLE         HbaHandle,
  _In_  HBA_UINT32         PortIndex,
  _Out_ HBA_PORTSTATISTICS *HbaPortStatistics
);
```



## Parameters

<dl> <dt>

*HbaHandle* \[in\]
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA on which the port is located.

</dd> <dt>

*PortIndex* \[in\]
</dt> <dd>

Contains an index that identifies which port on the HBA to query for statistics.

</dd> <dt>

*HbaPortStatistics* \[out\]
</dt> <dd>

Contains a structure of type [**HBA\_PortStatistics**](hba-portstatistics.md) that holds the statistics that were retrieved for the port.

</dd> </dl>

## Return value

The **HBA\_GetPortStatistics** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, **HBA\_GetPortStatistics** returns one of the following qualifiers.



| Return code                                                                                       | Description                                                                                           |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_OK**</dt> </dl>    | Returned if the statistics for the port were successfully retrieved. <br/>                      |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl> | Returned if an unspecified error occurred that prevented the retrieval of the statistics. <br/> |



 

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

[**HBA\_PortStatistics**](hba-portstatistics.md)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_GetPortStatistics%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







---
title: HBA\_GetFC4Statistics routine
description: The HBA\_GetFC4Statistics routine retrieves traffic statistics that a specific FC-4 protocol has collected for the indicated port and local adapter.
ms.assetid: 9c86c753-dddf-488d-b332-4b79602c454a
keywords:
- HBA_GetFC4Statistics routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_GetFC4Statistics
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

# HBA\_GetFC4Statistics routine

The **HBA\_GetFC4Statistics** routine retrieves traffic statistics that a specific FC-4 protocol has collected for the indicated port and local adapter.

## Syntax


```C++
HBA_STATUS HBA_API HBA_GetFC4Statistics(
  _In_  HBA_HANDLE        handle,
  _In_  HBA_WWN           portWWN,
  _In_  HBA_UINT8         FC4type,
  _Out_ HBA_FC4STATISTICS *statistics
);
```



## Parameters

<dl> <dt>

*handle* \[in\]
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA on which the port is located.

</dd> <dt>

*portWWN* \[in\]
</dt> <dd>

Contains a 64-bit world-wide name (WWN) that uniquely identifies the local HBA port for which this routine retrieves traffic statistics for a specific FC-4 protocol. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

*FC4type* \[in\]
</dt> <dd>

Contains a value that indicates the type FC-4 protocol. For an explanation of FC4 types and the values that can be assigned to this parameter, see the T11 committee's *Fibre Channel Generic Services - 4* specification.

</dd> <dt>

*statistics* \[out\]
</dt> <dd>

Pointer to a structure of type [**HBA\_FC4Statistics**](hba-fc4statistics.md) that contains statistics for the specified port and FC-4 protocol.

</dd> </dl>

## Return value

The **HBA\_GetFC4Statistics** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, **HBA\_GetFC4Statistics** returns one of the following qualifiers.



| Return code                                                                                                       | Description                                                                                               |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_ERROR\_ILLEGAL\_WWN**</dt> </dl>   | Returned if the adapter does not contain a port with the name *HbaPortWWN*. <br/>                   |
| <dl> <dt>**HBA\_STATUS\_ERROR\_NOT\_SUPPORTED**</dt> </dl> | Returned if the adapter does not support the specified FC-4 protocol. <br/>                         |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl>                 | Returned if an unspecified error occurred that prevented the retrieval of the port attributes.<br/> |



 

## Remarks

Statistics counters in [**HBA\_FC4Statistics**](hba-fc4statistics.md) are 64-bit signed integers that wrap to zero on exceeding 2\*\*63-1. If an HBA does not support a specific statistic, it returns a value with every bit set to 1 for that statistic. For an explanation of how the counter values are determined, see the T11 committee's *Fibre Channel Generic Services - 4* specification.

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Hbaapi.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>Hbaapi.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**HBA\_FC4Statistics**](hba-fc4statistics.md)
</dt> <dt>

[**HBA\_OpenAdapter**](hba-openadapter.md)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_GetFC4Statistics%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







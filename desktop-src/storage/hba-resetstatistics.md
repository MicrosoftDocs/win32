---
title: HBA\_ResetStatistics routine
description: The HBA\_ResetStatistics routine resets the statistics counters for the indicated port and HBA.
ms.assetid: '4e889905-9c5e-446c-8d0e-09e445f7c1a4'
keywords: ["HBA_ResetStatistics routine Storage Devices"]
topic_type:
- apiref
api_name:
- HBA_ResetStatistics
api_location:
- Hbaapi.dll
api_type:
- DllExport
---

# HBA\_ResetStatistics routine

The **HBA\_ResetStatistics** routine resets the statistics counters for the indicated port and HBA.

## Syntax


```C++
void HBA_API HBA_ResetStatistics(
  _In_ HBA_HANDLE HbaHandle,
  _In_ HBA_UINT32 PortIndex
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

Indicates for which port on the HBA the statistics counters should be reset.

</dd> </dl>

## Return value

None

## Remarks

The **HBA\_ResetStatistics** routine serves similar purpose to the **ResetStatistics** method of the [MSFC\_FibrePortHBAMethods WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562501).

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

[MSFC\_FibrePortHBAMethods WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562501)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_ResetStatistics%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







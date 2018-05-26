---
title: HBA\_GetBindingSupport routine
description: The HBA\_GetBindingSupport routine retrieves the binding capabilities currently enabled for the specified port.
ms.assetid: 60542ed9-fbb0-48a3-bc97-ce3db7b4ae10
keywords:
- HBA_GetBindingSupport routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_GetBindingSupport
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

# HBA\_GetBindingSupport routine

The **HBA\_GetBindingSupport** routine retrieves the binding capabilities currently enabled for the specified port.

## Syntax


```C++
HBA_STATUS HBA_API HBA_GetBindingSupport(
  _In_  HBA_HANDLE          Handle,
  _In_  HBA_WWN             HbaPortWWN,
  _Out_ HBA_BIND_CAPABILITY *Flags
);
```



## Parameters

<dl> <dt>

*Handle* \[in\]
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA on which the port is located.

</dd> <dt>

*HbaPortWWN* \[in\]
</dt> <dd>

Contains a 64-bit world-wide name (WWN) that uniquely identifies the local HBA port for which this routine retrieves persistent binding capabilities that are currently enabled. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

*Flags* \[out\]
</dt> <dd>

Contains a bitwise OR of flags associated with the [HBA\_BIND\_TYPE](https://msdn.microsoft.com/library/windows/hardware/ff556046) WMI property qualifier that represent the persistent binding capabilities of the port that are currently enabled.

</dd> </dl>

## Return value

The **HBA\_GetBindingSupport** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, **HBA\_GetBindingCapability** returns one of the following qualifiers.



| Return code                                                                                                       | Description                                                                                               |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_ERROR\_ILLEGAL\_WWN**</dt> </dl>   | Returned if the adapter does not contain a port with the name *HbaPortWWN*. <br/>                   |
| <dl> <dt>**HBA\_STATUS\_ERROR\_NOT\_SUPPORTED**</dt> </dl> | Returned if the adapter does not support persistent bindings. <br/>                                 |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl>                 | Returned if an unspecified error occurred that prevented the retrieval of the port attributes.<br/> |



 

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Hbaapi.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>Hbaapi.dll</dt> </dl>                  |



## See also

<dl> <dt>

[HBA\_BIND\_TYPE](https://msdn.microsoft.com/library/windows/hardware/ff556046)
</dt> <dt>

[**HBA\_OpenAdapter**](hba-openadapter.md)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_GetBindingSupport%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







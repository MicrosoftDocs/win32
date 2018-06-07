---
title: HBA\_GetDiscoveredPortAttributes routine
description: The HBA\_GetDiscoveredPortAttributes routine retrieves the attributes for a specified remote fibre channel port.
ms.assetid: 64c6ed50-a4b9-4a8c-b38c-b2fcdf5ccee9
keywords:
- HBA_GetDiscoveredPortAttributes routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_GetDiscoveredPortAttributes
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

# HBA\_GetDiscoveredPortAttributes routine

The **HBA\_GetDiscoveredPortAttributes** routine retrieves the attributes for a specified remote fibre channel port.

## Syntax


```C++
HBA_STATUS HBA_API HBA_GetDiscoveredPortAttributes(
  _In_  HBA_HANDLE         HbaHandle,
  _In_  HBA_UINT32         PortIndex,
  _In_  HBA_UINT32         DiscoveredPortIndex,
  _Out_ HBA_PORTATTRIBUTES *HbaPortAttributes
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

Indicates the index of the local port of type Nx\_Port through which to query the discovered remote port. For a definition of Nx\_Port, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

*DiscoveredPortIndex* \[in\]
</dt> <dd>

Indicates the index of the remote port to query.

</dd> <dt>

*HbaPortAttributes* \[out\]
</dt> <dd>

Contains a structure of type [**HBA\_PortAttributes**](hba-portattributes.md) that reports the port attributes.

</dd> </dl>

## Return value

The **HBA\_GetDiscoveredPortAttributes** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA.

## Remarks

The **HBA\_GetDiscoveredPortAttributes** library routine corresponds to the [**GetDiscoveredPortAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff553925) WMI method.

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Hbaapi.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>Hbaapi.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**GetDiscoveredPortAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff553925)
</dt> <dt>

[**HBA\_OpenAdapter**](hba-openadapter.md)
</dt> <dt>

[**HBA\_PortAttributes**](hba-portattributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_GetDiscoveredPortAttributes%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







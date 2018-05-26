---
title: HBA\_GetAdapterAttributes routine
description: The HBA\_GetAdapterAttributes routine retrieves the attributes for an HBA.
ms.assetid: a172f53c-9993-4d52-ae3f-35a8ab5745f6
keywords:
- HBA_GetAdapterAttributes routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_GetAdapterAttributes
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

# HBA\_GetAdapterAttributes routine

The **HBA\_GetAdapterAttributes** routine retrieves the attributes for an HBA.

## Syntax


```C++
HBA_STATUS HBA_API HBA_GetAdapterAttributes(
  _In_  HBA_HANDLE            HbaHandle,
  _Out_ HBA_ADAPTERATTRIBUTES *HbaAdapterAttributes
);
```



## Parameters

<dl> <dt>

*HbaHandle* \[in\]
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA on which the port is located.

</dd> <dt>

*HbaAdapterAttributes* \[out\]
</dt> <dd>

Contains, on return, a structure of type [**HBA\_AdapterAttributes**](hba-adapterattributes.md) that holds the HBA attributes.

</dd> </dl>

## Return value

The **HBA\_GetAdapterAttributes** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA.

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Hbaapi.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>Hbaapi.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**HBA\_AdapterAttributes**](hba-adapterattributes.md)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_GetAdapterAttributes%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







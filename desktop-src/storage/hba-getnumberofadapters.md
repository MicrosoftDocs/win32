---
title: HBA\_GetNumberOfAdapters routine
description: The HBA\_GetNumberOfAdapters routine returns the number of HBAs supported by the library.
ms.assetid: '5864a535-4ff8-4c9a-abf9-f835c7fde305'
keywords: ["HBA_GetNumberOfAdapters routine Storage Devices"]
topic_type:
- apiref
api_name:
- HBA_GetNumberOfAdapters
api_location:
- Hbaapi.dll
api_type:
- DllExport
---

# HBA\_GetNumberOfAdapters routine

The **HBA\_GetNumberOfAdapters** routine returns the number of HBAs supported by the library.

## Syntax


```C++
HBA_UINT32 HBA_API HBA_GetNumberOfAdapters(void);
```



## Parameters

This routine has no parameters.

## Return value

The **HBA\_GetNumberOfAdapters** routine returns the number of adapters supported by this library. If no adapters are supported, **HBA\_GetNumberOfAdapters** returns 0.

## Remarks

The **HBA\_GetNumberOfAdapters** routine allows the caller to dynamically determine the size of the HBA inventory without having to restart the system, the HBA drivers, or the library.

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Hbaapi.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>Hbaapi.dll</dt> </dl>                  |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_GetNumberOfAdapters%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






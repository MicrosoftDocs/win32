---
title: HBA\_GetWrapperLibraryAttributes routine
description: The HBA\_GetWrapperLibraryAttributes routine retrieves the attributes of the fibre channel HBA API library that are operating system-specific.
ms.assetid: c40b8f20-65e9-4e43-a402-14bd30f15975
keywords:
- HBA_GetWrapperLibraryAttributes routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_GetWrapperLibraryAttributes
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

# HBA\_GetWrapperLibraryAttributes routine

The **HBA\_GetWrapperLibraryAttributes** routine retrieves the attributes of the fibre channel HBA API library that are operating system-specific.

## Syntax


```C++
HBA_UINT32 HBA_API HBA_GetWrapperLibraryAttributes(
  _Out_ HBA_LIBRARYATTRIBUTES *Attributes
);
```



## Parameters

<dl> <dt>

*Attributes* \[out\]
</dt> <dd>

Pointer, on return, to a structure of type [**HBA\_LibraryAttributes**](hba-libraryattributes.md) that holds the attributes of the wrapper library.

</dd> </dl>

## Return value

The **HBA\_GetWrapperLibraryAttributes** routine returns a value that indicates the version of the specification with which the library is compliant. A value of 1 indicates version 1 of the specification. A value of 2 indicates version 2 of the specification. All other values are reserved until the future versions of the specification are published.

## Remarks

The **HBA\_GetWrapperLibraryAttributes** routine, as defined by the T11 committee's *Fibre Channel HBA API* specification, retrieves information about a system-supplied HBA API library, and the related routine [**HBA\_GetVendorLibraryAttributes**](hba-getvendorlibraryattributes.md) reports the characteristics of a system-supplied wrapper library that works with the vendor library to provide the fibre channel HBA API.

In particular, the **HBA\_GetWrapperLibraryAttributes** routine allows the caller to determine whether a compatible library is installed.

Microsoft supplies both libraries, so currently they return the same information.

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Hbaapi.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>Hbaapi.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**HBA\_GetVendorLibraryAttributes**](hba-getvendorlibraryattributes.md)
</dt> <dt>

[**HBA\_LibraryAttributes**](hba-libraryattributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_GetWrapperLibraryAttributes%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







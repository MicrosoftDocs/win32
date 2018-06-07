---
title: HBA\_GetVendorLibraryAttributes routine
description: The HBA\_GetVendorLibraryAttributes routine retrieves the vendor-specific attributes of the fibre channel HBA API library.
ms.assetid: 43c55364-1f73-4413-99fb-27c85600d7a6
keywords:
- HBA_GetVendorLibraryAttributes routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_GetVendorLibraryAttributes
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

# HBA\_GetVendorLibraryAttributes routine

The **HBA\_GetVendorLibraryAttributes** routine retrieves the vendor-specific attributes of the fibre channel HBA API library.

## Syntax


```C++
HBA_UINT32 HBA_API HBA_GetVendorLibraryAttributes(
  _In_  HBA_UINT32            AdapterIndex,
  _Out_ HBA_LIBRARYATTRIBUTES *Attributes
);
```



## Parameters

<dl> <dt>

*AdapterIndex* \[in\]
</dt> <dd>

Contains an adapter index that identifies which library to query. Each library is associated with one or more HBAs. This routine uses an index to identify the HBA so that the caller does not have to open the adapter to obtain a name or handle. The HBA API library can be associated with more than one HBA, so the same library attributes might be retrieved for different HBAs. The adapter index must be within the range of values returned by [**HBA\_GetNumberOfAdapters**](hba-getnumberofadapters.md).

</dd> <dt>

*Attributes* \[out\]
</dt> <dd>

Pointer, on return, to a structure of type [**HBA\_LibraryAttributes**](hba-libraryattributes.md) that holds the attributes of the library associated with the adapter referenced by *AdapterIndex*.

</dd> </dl>

## Return value

The **HBA\_GetVendorLibraryAttributes** routine returns a value that indicates the version of the specification with which the library is compliant. A value of 1 indicates version 1 of the specification. A value of 2 indicates version 2 of the specification. All other values are reserved until the future versions of the specification are published.

## Remarks

The **HBA\_GetVendorLibraryAttributes** routine, as defined by the T11 committee's *Fibre Channel HBA API* specification, retrieves information about a vendor-supplied HBA API library, and the related routine [**HBA\_GetWrapperLibraryAttributes**](hba-getwrapperlibraryattributes.md) reports the characteristics of a system-supplied wrapper library that works with the vendor library to provide the fibre channel HBA API.

In particular, the **HBA\_GetVendorLibraryAttributes** routine allows the caller to determine whether a compatible library is installed.

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

[**HBA\_GetNumberOfAdapters**](hba-getnumberofadapters.md)
</dt> <dt>

[**HBA\_GetWrapperLibraryAttributes**](hba-getwrapperlibraryattributes.md)
</dt> <dt>

[**HBA\_LibraryAttributes**](hba-libraryattributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_GetVendorLibraryAttributes%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







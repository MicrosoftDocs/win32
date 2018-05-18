---
title: HBA\_GetAdapterPortAttributes routine
description: The HBA\_GetAdapterPortAttributes routine retrieves the attributes for a specified remote fibre channel port.
ms.assetid: 'f1f5dc4e-8069-4e3e-94a0-a9a7c359bdb4'
keywords: ["HBA_GetAdapterPortAttributes routine Storage Devices"]
topic_type:
- apiref
api_name:
- HBA_GetAdapterPortAttributes
api_location:
- Hbaapi.dll
api_type:
- DllExport
---

# HBA\_GetAdapterPortAttributes routine

The **HBA\_GetAdapterPortAttributes** routine retrieves the attributes for a specified remote fibre channel port.

## Syntax


```C++
HBA_STATUS HBA_API HBA_GetAdapterPortAttributes(
  _In_  HBA_HANDLE         HbaHandle,
  _In_  HBA_UINT32         PortIndex,
  _Out_ HBA_PORTATTRIBUTES *PortAttributes
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

Indicates which remote port to query on the HBA specified by *HbaHandle*.

</dd> <dt>

*PortAttributes* \[out\]
</dt> <dd>

Pointer to a structure of type [**HBA\_PortAttributes**](hba-portattributes.md) that, on return, contains the attributes of the remote port with an index of *PortIndex* on the HBA specified by *HbaHandle.*

</dd> </dl>

## Return value

The **HBA\_GetAdapterPortAttributes** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. A value of HBA\_STATUS\_OK indicates that the operation succeeded. A value of HBA\_STATUS\_ERROR indicates that an unspecified error occurred that prevented the retrieval of the port attributes.

## Remarks

The **HBA\_GetAdapterPortAttributes** routine retrieves attributes for remote ports of type Nx\_Port. For a definition of Nx\_Port, see the T11 committee's specification for *Fibre Channel HBA API*.

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

[**HBA\_PortAttributes**](hba-portattributes.md)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_GetAdapterPortAttributes%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







---
title: HBA\_GetPersistentBindingV2 routine
description: The HBA\_GetPersistentBindingV2 routine retrieves persistent bindings, including extended bindings, for logical units that the HBA enumerates on the indicated port.
ms.assetid: 549edba4-8622-4117-b013-bcaf1787e8b4
keywords:
- HBA_GetPersistentBindingV2 routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_GetPersistentBindingV2
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

# HBA\_GetPersistentBindingV2 routine

The **HBA\_GetPersistentBindingV2** routine retrieves persistent bindings, including extended bindings, for logical units that the HBA enumerates on the indicated port.

## Syntax


```C++
HBA_STATUS HBA_API HBA_GetPersistentBindingV2(
  _In_    HBA_HANDLE       HbaHandle,
  _In_    HBA_WWN          HbaPortWWN,
  _Inout_ PHBA_FCPBINDING2 Binding
);
```



## Parameters

<dl> <dt>

*HbaHandle* \[in\]
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA to query for the persistent bindings. The HBA returns bindings for the logical units that it can enumerate on the port specified by *HbaPortWWN*.

</dd> <dt>

*HbaPortWWN* \[in\]
</dt> <dd>

Contains a 64-bit worldwide name (WWN) that uniquely identifies the fibre channel port on which the logical units are enumerated. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

*Binding* \[in, out\]
</dt> <dd>

Contains a structure of type [**HBA\_FCPBinding2**](hba-fcpbinding2.md) that holds an array of elements of type [**HBA\_FCPBindingEntry2**](hba-fcpbindingentry2.md), each of which holds a persistent binding between operating system and fibre channel protocol (FCP) identifiers for a logical unit. On input, the **NumberOfEntries** member of HBA\_FCPBinding2 should contain the number of bindings that fit in the output buffer. On output, **NumberOfEntries** holds the number of bindings actually returned, which is equal to the number specified on input, or the full set of available bindings, whichever is smaller. The value in **NumberOfEntries** contains the number of persistent bindings returned even when an error occurred because of insufficient buffer space.

On output, the **Status** member of each HBA\_FCPBindingEntry2 structure is 0.

</dd> </dl>

## Return value

The **HBA\_GetPersistentBindingV2** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, **HBA\_GetPersistentBindingV2** returns one of the following qualifiers.



| Return code                                                                                                       | Description                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_OK**</dt> </dl>                    | Returned if the persistent bindings were successfully retrieved. <br/>                                               |
| <dl> <dt>**HBA\_STATUS\_ERROR\_ILLEGAL\_WWN**</dt> </dl>   | Returned if the HBA referenced by *HbaHandle* does not contain a port with the name specified in *HbaPortWWN*. <br/> |
| <dl> <dt>**HBA\_STATUS\_ERROR\_NOT\_SUPPORTED**</dt> </dl> | Returned if the adapter referenced by *HbaHandle* does not support persistent binding. <br/>                         |
| <dl> <dt>**HBA\_STATUS\_ERROR\_MORE\_DATA**</dt> </dl>     | Returned if a larger buffer is required to contain binding information.<br/>                                         |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl>                 | Returned if an unspecified error occurred that prevented the retrieval of the persistent bindings. <br/>             |



 

## Remarks

The **HBA\_GetPersistentBindingV2** routine retrieves a set of bindings between operating system and FCP identifiers for the logical units that the HBA referenced by *HbaHandle* can enumerate on the port specified by *HbaPortWWN*. The bindings that **HBA\_GetPersistentBindingV2** retrieves persist across reboots of the operating system.

This routine is similar to the [**HBA\_GetFcpPersistentBinding**](hba-getfcppersistentbinding.md) routine. The key difference is that the bindings that **HBA\_GetPersistentBindingV2** returns include a logical unit ID descriptor (LUID) derived from vital product data retrieved with a SCSI inquiry command. If the vital product data for a logical unit provides more than one LUID, then the LUID that **HBA\_GetPersistentBindingV2** returns depends on the types of LUIDs provided. For a complete explanation of how the LUID is chosen when more than one LUID is available, see the T11 committee's *Fibre Channel HBA API* specification.

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Hbaapi.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>Hbaapi.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**HBA\_FCPBinding**](hba-fcpbinding.md)
</dt> <dt>

[**HBA\_FCPBindingEntry2**](hba-fcpbindingentry2.md)
</dt> <dt>

[**HBA\_GetFcpPersistentBinding**](hba-getfcppersistentbinding.md)
</dt> <dt>

[**HBA\_OpenAdapter**](hba-openadapter.md)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_GetPersistentBindingV2%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







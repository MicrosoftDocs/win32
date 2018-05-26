---
title: HBA\_GetFcpPersistentBinding routine
description: The HBA\_GetFcpPersistentBinding routine retrieves the persistent bindings that are associated with the logical units that the HBA can enumerate.
ms.assetid: a17a6dfa-c067-4a85-8787-ffb4fb6cb7ad
keywords:
- HBA_GetFcpPersistentBinding routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_GetFcpPersistentBinding
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

# HBA\_GetFcpPersistentBinding routine

The **HBA\_GetFcpPersistentBinding** routine retrieves the persistent bindings that are associated with the logical units that the HBA can enumerate.

## Syntax


```C++
HBA_STATUS HBA_API HBA_GetFcpPersistentBinding(
  _In_    HBA_HANDLE      Handle,
  _Inout_ PHBA_FCPBINDING Binding
);
```



## Parameters

<dl> <dt>

*Handle* \[in\]
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA to query for the bindings. The HBA returns bindings for the targets that it can enumerate.

</dd> <dt>

*Binding* \[in, out\]
</dt> <dd>

Contains a structure of type [**HBA\_FCPBinding**](hba-fcpbinding.md) that holds an array of elements of type [HBA\_FCPBindingEntry](hba-fcpbindingentry.md), each of which holds a persistent binding between operating system and fibre channel protocol (FCP) identifiers for a logical unit. On input, the **NumberOfEntries** member of HBA\_FCPBinding should contain the number of bindings that fit in the output buffer. On output, **NumberOfEntries** holds the number of entries actually returned, which is equal to the number specified on input, or the full set of available bindings, whichever is smaller. The value in **NumberOfEntries** will contain the number of persistent bindings returned even when an error occurred because of insufficient buffer space.

</dd> </dl>

## Return value

The **HBA\_GetFcpPersistentBinding** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, **HBA\_GetFcpPersistentBinding** returns one of the following qualifiers.



| Return code                                                                                                       | Description                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_OK**</dt> </dl>                    | Returned if the persistent bindings were successfully retrieved. <br/>                                   |
| <dl> <dt>**HBA\_STATUS\_ERROR\_NOT\_SUPPORTED**</dt> </dl> | Returned if the adapter referenced by *HbaHandle* does not support persistent binding. <br/>             |
| <dl> <dt>**HBA\_STATUS\_ERROR\_MORE\_DATA**</dt> </dl>     | Returned if a larger buffer is required to contain binding information.<br/>                             |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl>                 | Returned if an unspecified error occurred that prevented the retrieval of the persistent bindings. <br/> |



 

## Remarks

The **HBA\_GetFcpPersistentBinding** routine retrieves a set of bindings between operating system and fibre channel protocol (FCP) identifiers for the logical units that it can enumerate. These bindings persist across reboots of the operating system.

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

[**HBA\_OpenAdapter**](hba-openadapter.md)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_GetFcpPersistentBinding%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







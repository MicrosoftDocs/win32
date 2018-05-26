---
title: HBA\_GetEventBuffer routine
description: The HBA\_GetEventBuffer routine retrieves the indicated number of events, if available, from the HBAs event queue.
ms.assetid: 0f06b154-7d85-4a60-b354-bd61fbc597dc
keywords:
- HBA_GetEventBuffer routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_GetEventBuffer
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

# HBA\_GetEventBuffer routine

The **HBA\_GetEventBuffer** routine retrieves the indicated number of events, if available, from the HBA's event queue.

## Syntax


```C++
HBA_STATUS HBA_API HBA_GetEventBuffer(
  _In_    HBA_HANDLE     handle,
  _Out_   PHBA_EVENTINFO EventBuffer,
  _Inout_ HBA_UINT32     *EventCount
);
```



## Parameters

<dl> <dt>

*handle* \[in\]
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA on which the port is located.

</dd> <dt>

*EventBuffer* \[out\]
</dt> <dd>

Pointer to a buffer that on return holds a structure of type [**HBA\_EventInfo**](hba-eventinfo.md) that contains information about an event.

</dd> <dt>

*EventCount* \[in, out\]
</dt> <dd>

Indicates, on input, the number of event records that fit in the buffer pointed to by *EventBuffer.* If the full number of events requested cannot be retrieved, on return, this member contains the number of event records actually retrieved.

</dd> </dl>

## Return value

The **HBA\_GetEventBuffer** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, **HBA\_GetEventBuffer** returns one of the following qualifiers.



| Return code                                                                                       | Description                                                                                                           |
|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_OK**</dt> </dl>    | Returned if the operation was successful and *EventCount* indicates the number of event records returned. <br/> |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl> | Returned if an unspecified error occurred that prevented the retrieval of the event records. <br/>              |



 

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

[**HBA\_EventInfo**](hba-eventinfo.md)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_GetEventBuffer%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







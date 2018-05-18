---
title: MSFC\_EventBuffer structure
description: The MSFC\_EventBuffer structure is used in conjunction with the GetEventBuffer method to retrieve the next events in the HBA's event queue.
ms.assetid: '7d41c092-251e-4f93-b5be-ff989b37196b'
keywords: ["MSFC_EventBuffer structure Storage Devices", "PMSFC_EventBuffer structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MSFC_EventBuffer
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# MSFC\_EventBuffer structure

The MSFC\_EventBuffer structure is used in conjunction with the [**GetEventBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff553935) method to retrieve the next events in the HBA's event queue.

## Syntax


```C++
typedef struct _MSFC_EventBuffer {
  ULONG EventType;
  ULONG EventInfo[4];
} MSFC_EventBuffer, *PMSFC_EventBuffer;
```



## Members

<dl> <dt>

**EventType**
</dt> <dd>

Indicates the type of the event. The values that can be assigned to this member are defined by the [EVENT\_TYPE\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff553764) WMI class qualifier.

</dd> <dt>

**EventInfo**
</dt> <dd>

Contains a structure of type [**HBA\_EventInfo**](hba-eventinfo.md) that holds information about the events that were retrieved.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration for this structure in *hbapiwm.h* after compiling the [MSFC\_EventBuffer WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562483).

The [**HBA\_EventInfo**](hba-eventinfo.md) structure is declared in *hbaapi.h*. You must include *hbaapi.h* to reference this structure.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[EVENT\_TYPE\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff553764)
</dt> <dt>

[**GetEventBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff553935)
</dt> <dt>

[**HBA\_EventInfo**](hba-eventinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSFC_EventBuffer%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







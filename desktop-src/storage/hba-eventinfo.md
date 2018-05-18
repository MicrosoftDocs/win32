---
title: HBA\_EventInfo structure
description: The HBA\_EventInfo structure contains information about an event of the indicated type.
ms.assetid: 'fc6b73ac-f86c-4978-9d71-9bd8398c116b'
keywords: ["HBA_EventInfo structure Storage Devices", "HBA_EVENTINFO structure Storage Devices", "PHBA_EVENTINFO structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- HBA_EVENTINFO
api_location:
- hbaapi.h
api_type:
- HeaderDef
---

# HBA\_EventInfo structure

The HBA\_EventInfo structure contains information about an event of the indicated type.

## Syntax


```C++
typedef struct HBA_EventInfo {
  HBA_UINT32 EventCode;
  union {
    HBA_LINK_EVENTINFO Link_EventInfo;
    HBA_RSCN_EVENTINFO RSCN_EventInfo;
    HBA_PTY_EVENTINFO  Pty_EventInfo;
  } Event;
} HBA_EVENTINFO, *PHBA_EVENTINFO;
```



## Members

<dl> <dt>

**EventCode**
</dt> <dd>

Contains a code indicating the type of event. The following table lists the values that this member can have:



| Value                                       | Meaning                                                           |
|---------------------------------------------|-------------------------------------------------------------------|
| HBA\_EVENT\_LIP\_OCCURRED<br/>        | A loop initialization primitive event occurred.<br/>        |
| HBA\_EVENT\_LINK\_UP<br/>             | A link up event occurred. <br/>                             |
| HBA\_EVENT\_LINK\_DOWN<br/>           | A link down event occurred. <br/>                           |
| HBA\_EVENT\_LIP\_RESET\_OCCURRED<br/> | A loop initialization primitive resest event occurred.<br/> |
| HBA\_EVENT\_RSCN<br/>                 | An RSCN event occurred.<br/>                                |
| HBA\_EVENT\_PROPRIETARY<br/>          | A proprietary event occurred. <br/>                         |



 

</dd> <dt>

**Event**
</dt> <dd> <dl> <dt>

**Link\_EventInfo**
</dt> <dd>

Contains a structure of type [**HBA\_Link\_EventInfo**](hba-link-eventinfo.md) that holds information associated with a link event.

</dd> <dt>

**RSCN\_EventInfo**
</dt> <dd>

Contains a structure of type [**HBA\_RSCN\_EventInfo**](hba-rscn-eventinfo.md) that holds information associated with a link event.

</dd> <dt>

**Pty\_EventInfo**
</dt> <dd>

Contains a structure of type [**HBA\_Pty\_EventInfo**](hba-pty-eventinfo.md) that holds information associated with a link event.

</dd> </dl> </dd> </dl>

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HBA\_Link\_EventInfo**](hba-link-eventinfo.md)
</dt> <dt>

[**HBA\_Pty\_EventInfo**](hba-pty-eventinfo.md)
</dt> <dt>

[**HBA\_RSCN\_EventInfo**](hba-rscn-eventinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_EventInfo%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







---
description: Describes the display sink object data included in a notification or notification result.
ms.assetid: 40D931F6-C068-48EB-A968-9CBAA3F9FAD8
title: WFD_DISPLAY_SINK_OBJECT_HEADER structure (Wfdsink.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WFD_DISPLAY_SINK_OBJECT_HEADER
api_type: 
- HeaderDef
api_location: 
- wfdsink.h
---

# WFD\_DISPLAY\_SINK\_OBJECT\_HEADER structure

The **WFD\_DISPLAY\_SINK\_OBJECT\_HEADER** structure describes the display sink object data included in a notification or notification result.

## Syntax


```C++
typedef struct _WFD_DISPLAY_SINK_OBJECT_HEADER {
  UCHAR  Type;
  UCHAR  Revision;
  USHORT Length;
} WFD_DISPLAY_SINK_OBJECT_HEADER, *PWFD_DISPLAY_SINK_OBJECT_HEADER;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

The type of the display sink object. You can use the identifier **WFD\_DISPLAY\_SINK\_OBJECT\_TYPE\_DEFAULT** which is defined as the value 1.

</dd> <dt>

**Revision**
</dt> <dd>

The revision version of the display sink object. You can use the identifier **WFD\_DISPLAY\_SINK\_OBJECT\_REVISION\_VERSION\_1** which is defined as the value 1.

</dd> <dt>

**Length**
</dt> <dd>

The length of the data in the notification or notification result.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Wfdsink.h</dt> </dl> |



 

 





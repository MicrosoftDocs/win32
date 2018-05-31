---
title: MUX\_PID\_TYPE enumeration
description: Specifies an MPEG-2 stream type.
ms.assetid: 2db22de7-9b82-4894-a6f3-5a73ab5efb7d
keywords:
- MUX_PID_TYPE enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- MUX_PID_TYPE
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
api_location:
- bdatypes.h
api_type:
- HeaderDef
---

# MUX\_PID\_TYPE enumeration

Specifies an MPEG-2 stream type.

## Syntax


```C++
typedef enum MUX_PID_TYPE { 
  PID_OTHER                 = -1,
  PID_ELEMENTARY_STREAM,
  PID_MPEG2_SECTION_PSI_SI
} MUX_PID_TYPE;
```



## Constants

<dl> <dt>

<span id="PID_OTHER"></span><span id="pid_other"></span>**PID\_OTHER**
</dt> <dd>

Other.

</dd> <dt>

<span id="PID_ELEMENTARY_STREAM"></span><span id="pid_elementary_stream"></span>**PID\_ELEMENTARY\_STREAM**
</dt> <dd>

Packetized elementary stream (PES) payloads.

</dd> <dt>

<span id="PID_MPEG2_SECTION_PSI_SI"></span><span id="pid_mpeg2_section_psi_si"></span>**PID\_MPEG2\_SECTION\_PSI\_SI**
</dt> <dd>

Program Specific Information (PSI) sections.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdatypes.h</dt> </dl> |



## See also

<dl> <dt>

[**BDA\_MUX\_PIDLISTITEM**](bda-mux-pidlistitem.md)
</dt> </dl>

 

 






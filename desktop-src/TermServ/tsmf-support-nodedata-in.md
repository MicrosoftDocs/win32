---
title: TSMF_SUPPORT_NODEDATA_IN structure
description: Used inside the TSMF\_SUPPORT\_DATA\_IN structure to contain information about supported media formats.
ms.assetid: 9aee9d6d-2182-44ec-ba8b-d2747d3edf71
ms.tgt_platform: multiple
keywords:
- TSMF_SUPPORT_NODEDATA_IN structure Remote Desktop Services
- PTSMF_SUPPORT_NODEDATA_IN structure pointer Remote Desktop Services
topic_type:
- apiref
api_name:
- TSMF_SUPPORT_NODEDATA_IN
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TSMF\_SUPPORT\_NODEDATA\_IN structure

Used inside the [**TSMF\_SUPPORT\_DATA\_IN**](tsmf-support-data-in.md) structure to contain information about supported media formats.

## Syntax


```C++
typedef struct tagTSMF_SUPPORT_NODEDATA_IN {
  UINT32           byteCount;
  INT64            nodeId;
  UINT32           numMediaTypes;
  TS_AM_MEDIA_TYPE ...;
} TSMF_SUPPORT_NODEDATA_IN, *PTSMF_SUPPORT_NODEDATA_IN;
```



## Members

<dl> <dt>

**byteCount**
</dt> <dd>

The size of the structure in bytes.

</dd> <dt>

**nodeId**
</dt> <dd>

The node.

</dd> <dt>

**numMediaTypes**
</dt> <dd>

The number of media format structures.

</dd> <dt>

**...**
</dt> <dd>

A variable number of structures defining audio or video media formats. The **FormatType** is either **FORMAT\_WaveFormatEx** for audio or **FORMAT\_MFVideoFormat** for video.

For details of this structure, see [TS\_AM\_MEDIA\_TYPE Structure](/openspecs/windows_protocols/ms-rdpev/22a57950-042e-48bd-8135-3580f3a3f934).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | None supported<br/>         |
| Minimum supported server<br/> | Windows Server 2008 R2<br/> |



## See also

<dl> <dt>

[**QueryProperty**](/windows/desktop/api/Wtsprotocol/nf-wtsprotocol-iwrdsprotocolconnection-queryproperty)
</dt> <dt>

[**TSMF\_SUPPORT\_DATA\_IN**](tsmf-support-data-in.md)
</dt> </dl>

 


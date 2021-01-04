---
title: TSMF_SUPPORT_NODEDATA_OUT structure
description: Used inside the TSMF\_SUPPORT\_DATA\_OUT structure to contain information about supported media formats.
ms.assetid: cac0af9e-6750-4735-b075-46c77aea7d41
ms.tgt_platform: multiple
keywords:
- TSMF_SUPPORT_NODEDATA_OUT structure Remote Desktop Services
- PTSMF_SUPPORT_NODEDATA_OUT structure pointer Remote Desktop Services
topic_type:
- apiref
api_name:
- TSMF_SUPPORT_NODEDATA_OUT
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TSMF\_SUPPORT\_NODEDATA\_OUT structure

Used inside the [**TSMF\_SUPPORT\_DATA\_OUT**](tsmf-support-data-out.md) structure to contain information about supported media formats.

## Syntax


```C++
typedef struct tagTSMF_SUPPORT_NODEDATA_OUT {
  INT64   nodeId;
  HRESULT hrSupportStatus;
  CLSID   clsidNewSink;
  UINT32  supportedMediaTypeIndex;
} TSMF_SUPPORT_NODEDATA_OUT, *PTSMF_SUPPORT_NODEDATA_OUT;
```



## Members

<dl> <dt>

**nodeId**
</dt> <dd>

The node.

</dd> <dt>

**hrSupportStatus**
</dt> <dd>

Whether the sink identified by the *clsidNewSink* parameter is supported.

The possible values are.

<dt>

0
</dt> <dd>

Not supported

</dd> <dt>

1
</dt> <dd>

Supported

</dd> </dl>

Other values are undefined.

</dd> <dt>

**clsidNewSink**
</dt> <dd>

The sink associated with the media type.

</dd> <dt>

**supportedMediaTypeIndex**
</dt> <dd>

The zero-based index of the media type supported by the sink.

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

[**TSMF\_SUPPORT\_DATA\_OUT**](tsmf-support-data-out.md)
</dt> </dl>

 

 






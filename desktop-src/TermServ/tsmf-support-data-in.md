---
title: TSMF_SUPPORT_DATA_IN structure
description: Contains information about media formats. | TSMF_SUPPORT_DATA_IN structure
ms.assetid: cd1a8295-22b7-4d75-8325-94da4d7380d0
ms.tgt_platform: multiple
keywords:
- TSMF_SUPPORT_DATA_IN structure Remote Desktop Services
- PTSMF_SUPPORT_DATA_IN structure pointer Remote Desktop Services
topic_type:
- apiref
api_name:
- TSMF_SUPPORT_DATA_IN
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TSMF\_SUPPORT\_DATA\_IN structure

Contains information about media formats. This structure is used by the [**QueryProperty**](/windows/desktop/api/Wtsprotocol/nf-wtsprotocol-iwrdsprotocolconnection-queryproperty) method during **WRDS\_QUERY\_MF\_FORMAT\_SUPPORT** queries.

## Syntax


```C++
typedef struct tagTSMF_SUPPORT_DATA_IN {
  GUID                     guidMfSession;
  UINT32                   numEntries;
  TSMF_SUPPORT_NODEDATA_IN ...;
} TSMF_SUPPORT_DATA_IN, *PTSMF_SUPPORT_DATA_IN;
```



## Members

<dl> <dt>

**guidMfSession**
</dt> <dd>

The session.

</dd> <dt>

**numEntries**
</dt> <dd>

The number of structures in the variable length data.

</dd> <dt>

**...**
</dt> <dd>

A variable number of structures containing media format data.

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

[**TSMF\_SUPPORT\_NODEDATA\_IN**](tsmf-support-nodedata-in.md)
</dt> </dl>

 

 






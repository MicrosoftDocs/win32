---
title: TSMF_SUPPORT_DATA_OUT structure
description: Contains information about media formats. | TSMF_SUPPORT_DATA_OUT structure
ms.assetid: 987ede31-ad15-489f-90e5-fb707c6b38a9
ms.tgt_platform: multiple
keywords:
- TSMF_SUPPORT_DATA_OUT structure Remote Desktop Services
- PTSMF_SUPPORT_DATA_OUT structure pointer Remote Desktop Services
topic_type:
- apiref
api_name:
- TSMF_SUPPORT_DATA_OUT
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TSMF\_SUPPORT\_DATA\_OUT structure

Contains information about media formats. This structure is used by the [**QueryProperty**](/windows/desktop/api/Wtsprotocol/nf-wtsprotocol-iwrdsprotocolconnection-queryproperty) method during **WRDS\_QUERY\_MF\_FORMAT\_SUPPORT** queries.

## Syntax


```C++
typedef struct tagTSMF_SUPPORT_DATA_OUT {
  GUID                      guidMfSession;
  UINT32                    numEntries;
  TSMF_SUPPORT_NODEDATA_OUT ...;
} TSMF_SUPPORT_DATA_OUT, *PTSMF_SUPPORT_DATA_OUT;
```



## Members

<dl> <dt>

**guidMfSession**
</dt> <dd>

This must match the **guidMfSession** property in the corresponding [**TSMF\_SUPPORT\_DATA\_IN**](tsmf-support-data-in.md) structure.

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

[**TSMF\_SUPPORT\_NODEDATA\_OUT**](tsmf-support-nodedata-out.md)
</dt> </dl>

 

 






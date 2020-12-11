---
title: MPCONFIGURATION_DATA structure (MpClient.h)
description: Contains data about configuration changes, including the old and new values.
ms.assetid: AB70B1C0-C148-44BC-8C0E-CC5D2A66BCA5
keywords:
- MPCONFIGURATION_DATA structure Legacy Windows Environment Features
- PMPCONFIGURATION_DATA structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPCONFIGURATION_DATA
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPCONFIGURATION\_DATA structure

Contains data about configuration changes, including the old and new values.

## Syntax


```C++
typedef struct tagMPCONFIGURATION_DATA {
  MP_MIDL_STRING LPWSTR ConfigurationName;
  DWORD                 DataType;
  DWORD                 PreviousDataSize;
  BYTE                  *pPreviousData;
  DWORD                 CurrentDataSize;
  BYTE                  *pCurrentData;
} MPCONFIGURATION_DATA, *PMPCONFIGURATION_DATA;
```



## Members

<dl> <dt>

**ConfigurationName**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

Name of the configuration that changed.

</dd> <dt>

**DataType**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The type of data used.

</dd> <dt>

**PreviousDataSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Size of previous data, in bytes.

</dd> <dt>

**pPreviousData**
</dt> <dd>

Type: **BYTE\***

</dd> <dd>

Pointer to previous data.

</dd> <dt>

**CurrentDataSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Size of new data, in bytes.

</dd> <dt>

**pCurrentData**
</dt> <dd>

Type: **BYTE\***

</dd> <dd>

Pointer to new data.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 






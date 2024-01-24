---
title: MPSIGUPDATE_DATA structure (MpClient.h)
description: Notification data passed to the signature update callback function.
ms.assetid: E999ABC2-CC72-43CC-86D9-4F29E9128E1A
keywords:
- MPSIGUPDATE_DATA structure Legacy Windows Environment Features
- PMPSIGUPDATE_DATA structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPSIGUPDATE_DATA
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPSIGUPDATE\_DATA structure

Notification data passed to the signature update callback function.

## Syntax


```C++
typedef struct tagMPSIGUPDATE_DATA {
  DWORD                 dwPercentComplete;
  DWORD                 dwTotalUpdates;
  DWORD                 dwCurrentUpdateIndex;
  MPSIGUPDATE_TYPE      eType;
  MP_UPDATE_STAGE       Stage;
  MP_MIDL_STRING LPWSTR Path;
} MPSIGUPDATE_DATA, *PMPSIGUPDATE_DATA;
```



## Members

<dl> <dt>

**dwPercentComplete**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

An estimate of the percentage across all the updates that have been downloaded and/or installed.

</dd> <dt>

**dwTotalUpdates**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Total number of updates to download and/or install.

</dd> <dt>

**dwCurrentUpdateIndex**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Zero-based index value that specifies which update among those required is currently being downloaded and/or installed.

</dd> <dt>

**eType**
</dt> <dd>

Type: **MPSIGUPDATE\_TYPE**

</dd> <dd>

Update type. One of the following possible values:



| Value                                                                                                                                                                                                                             | Meaning                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <span id="MPSIGUPDATE_TYPE_NONE"></span><span id="mpsigupdate_type_none"></span><dl> <dt>**MPSIGUPDATE\_TYPE\_NONE**</dt> </dl>                                            |                                                                             |
| <span id="MPSIGUPDATE_TYPE_MANAGED"></span><span id="mpsigupdate_type_managed"></span><dl> <dt>**MPSIGUPDATE\_TYPE\_MANAGED**</dt> </dl>                                   | WSUS update. Cancel requires administrator rights.<br/>               |
| <span id="MPSIGUPDATE_TYPE_HTTP"></span><span id="mpsigupdate_type_http"></span><dl> <dt>**MPSIGUPDATE\_TYPE\_HTTP**</dt> </dl>                                            | HTTP update. Administrator rights not needed to cancel.<br/>          |
| <span id="MPSIGUPDATE_TYPE_HTTP_SRV"></span><span id="mpsigupdate_type_http_srv"></span><dl> <dt>**MPSIGUPDATE\_TYPE\_HTTP\_SRV**</dt> </dl>                               | HTTP from service. Cancel requires administrator rights.<br/>         |
| <span id="MPSIGUPDATE_TYPE_UNC"></span><span id="mpsigupdate_type_unc"></span><dl> <dt>**MPSIGUPDATE\_TYPE\_UNC**</dt> </dl>                                               | UNC share. Administrator rights not needed to cancel.<br/>            |
| <span id="MPSIGUPDATE_TYPE_UNMANAGED"></span><span id="mpsigupdate_type_unmanaged"></span><dl> <dt>**MPSIGUPDATE\_TYPE\_UNMANAGED**</dt> </dl>                             | MU/WU update. Cancel requires administrator rights.<br/>              |
| <span id="MPSIGUPDATE_TYPE_MANAGED_PLATFORM"></span><span id="mpsigupdate_type_managed_platform"></span><dl> <dt>**MPSIGUPDATE\_TYPE\_MANAGED\_PLATFORM**</dt> </dl>       | WSUS update for PLATFORM. Cancel requires administrator rights.<br/>  |
| <span id="MPSIGUPDATE_TYPE_UNMANAGED_PLATFORM"></span><span id="mpsigupdate_type_unmanaged_platform"></span><dl> <dt>**MPSIGUPDATE\_TYPE\_UNMANAGED\_PLATFORM**</dt> </dl> | MU/WU update for PLATFORM. Cancel requires administrator rights.<br/> |



 

</dd> <dt>

**Stage**
</dt> <dd>

Type: **MP\_UPDATE\_STAGE**

</dd> <dd>

Update stage. One of the following possible values:



| Value                                                                                                                                                                         | Meaning                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| <span id="MP_STAGE_UNKNOWN"></span><span id="mp_stage_unknown"></span><dl> <dt>**MP\_STAGE\_UNKNOWN**</dt> </dl>       | Update stage unknown.<br/>  |
| <span id="MP_SEARCH_UPDATE"></span><span id="mp_search_update"></span><dl> <dt>**MP\_SEARCH\_UPDATE**</dt> </dl>       | Update search stage.<br/>   |
| <span id="MP_DOWNLOAD_UPDATE"></span><span id="mp_download_update"></span><dl> <dt>**MP\_DOWNLOAD\_UPDATE**</dt> </dl> | Update download stage.<br/> |
| <span id="MP_INSTALL_UPDATE"></span><span id="mp_install_update"></span><dl> <dt>**MP\_INSTALL\_UPDATE**</dt> </dl>    | Update install stage.<br/>  |



 

</dd> <dt>

**Path**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

Update path.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 






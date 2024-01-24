---
title: ADSI Print Job Status Constants (Adssts.h)
description: The following constants are used with the IADsPrintJobOperations.Status property to indicate the status of a print job.
ms.assetid: 44a981cc-1098-4b6d-8332-e678953c9112
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- ADS_JOB_PAUSED
- ADS_JOB_ERROR
- ADS_JOB_DELETING
- ADS_JOB_SPOOLING
- ADS_JOB_PRINTING
- ADS_JOB_OFFLINE
- ADS_JOB_PAPEROUT
- ADS_JOB_PRINTED
- ADS_JOB_DELETED
api_location:
- Adssts.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ADSI Print Job Status Constants

The following constants are used with the [**IADsPrintJobOperations.Status**](iadsprintjoboperations-property-methods.md) property to indicate the status of a print job.

<dl> <dt>

<span id="ADS_JOB_PAUSED"></span><span id="ads_job_paused"></span>**ADS\_JOB\_PAUSED**
</dt> <dd> <dl> <dt>

1 (0x1)
</dt> <dt>



The print job is paused.


</dt> </dl> </dd> <dt>

<span id="ADS_JOB_ERROR"></span><span id="ads_job_error"></span>**ADS\_JOB\_ERROR**
</dt> <dd> <dl> <dt>

2 (0x2)
</dt> <dt>



An error occurred.


</dt> </dl> </dd> <dt>

<span id="ADS_JOB_DELETING"></span><span id="ads_job_deleting"></span>**ADS\_JOB\_DELETING**
</dt> <dd> <dl> <dt>

4 (0x4)
</dt> <dt>



The print job is being deleted.


</dt> </dl> </dd> <dt>

<span id="ADS_JOB_SPOOLING"></span><span id="ads_job_spooling"></span>**ADS\_JOB\_SPOOLING**
</dt> <dd> <dl> <dt>

8 (0x8)
</dt> <dt>



The print job is being spooled.


</dt> </dl> </dd> <dt>

<span id="ADS_JOB_PRINTING"></span><span id="ads_job_printing"></span>**ADS\_JOB\_PRINTING**
</dt> <dd> <dl> <dt>

16 (0x10)
</dt> <dt>



The print job is being printed.


</dt> </dl> </dd> <dt>

<span id="ADS_JOB_OFFLINE"></span><span id="ads_job_offline"></span>**ADS\_JOB\_OFFLINE**
</dt> <dd> <dl> <dt>

32 (0x20)
</dt> <dt>



The printer is offline.


</dt> </dl> </dd> <dt>

<span id="ADS_JOB_PAPEROUT"></span><span id="ads_job_paperout"></span>**ADS\_JOB\_PAPEROUT**
</dt> <dd> <dl> <dt>

64 (0x40)
</dt> <dt>



The printer is out of paper.


</dt> </dl> </dd> <dt>

<span id="ADS_JOB_PRINTED"></span><span id="ads_job_printed"></span>**ADS\_JOB\_PRINTED**
</dt> <dd> <dl> <dt>

128 (0x80)
</dt> <dt>



The print job has been printed.


</dt> </dl> </dd> <dt>

<span id="ADS_JOB_DELETED"></span><span id="ads_job_deleted"></span>**ADS\_JOB\_DELETED**
</dt> <dd> <dl> <dt>

256 (0x100)
</dt> <dt>



The print job has been deleted.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>Adssts.h</dt> </dl> |



 

 






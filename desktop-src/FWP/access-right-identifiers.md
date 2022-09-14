---
title: Access Right Identifiers (Fwpmu.h)
description: Windows Filtering Platform (WFP) uses the standard Win32 access rights plus a set of WFP-specific access rights built into the filtering platform.
ms.assetid: 77f0a1ac-3e99-4cba-a7c6-b8747f35cd0c
topic_type:
- apiref
api_name:
- FWPM_ACTRL_ADD
- FWPM_ACTRL_ADD_LINK
- FWPM_ACTRL_BEGIN_READ_TXN
- FWPM_ACTRL_BEGIN_WRITE_TXN
- FWPM_ACTRL_CLASSIFY
- FWPM_ACTRL_ENUM
- FWPM_ACTRL_OPEN
- FWPM_ACTRL_READ
- FWPM_ACTRL_READ_STATS
- FWPM_ACTRL_SUBSCRIBE
- FWPM_ACTRL_WRITE
- FWPM_GENERIC_READ
- FWPM_GENERIC_EXECUTE
- FWPM_GENERIC_WRITE
- FWPM_GENERIC_ALL
api_location:
- fwpmu.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Access Right Identifiers

Windows Filtering Platform (WFP) uses the [standard Win32 access rights](/windows/desktop/SecAuthZ/standard-access-rights) plus a set of WFP-specific access rights built into the filtering platform. These access rights are used to secure objects in user mode only. Kernel-mode callers bypass all access checks.

WFP specific access right identifiers are as follows.

<dl> <dt>

<span id="FWPM_ACTRL_ADD"></span><span id="fwpm_actrl_add"></span>**FWPM\_ACTRL\_ADD**
</dt> <dd> <dl> <dt>



Add an object to the Base Filtering Engine (BFE). This access right is needed in order to call [**Fwpm\*Add0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmipsectunneladd0) functions.


</dt> </dl> </dd> <dt>

<span id="FWPM_ACTRL_ADD_LINK"></span><span id="fwpm_actrl_add_link"></span>**FWPM\_ACTRL\_ADD\_LINK**
</dt> <dd> <dl> <dt>



Add an object referenced through a link. For example, this access right is needed for callouts referenced through GUIDs.


</dt> </dl> </dd> <dt>

<span id="FWPM_ACTRL_BEGIN_READ_TXN"></span><span id="fwpm_actrl_begin_read_txn"></span>**FWPM\_ACTRL\_BEGIN\_READ\_TXN**
</dt> <dd> <dl> <dt>



Begin a read-only transaction. This access right is needed in order to call [**FwpmTransactionBegin0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmtransactionbegin0).


</dt> </dl> </dd> <dt>

<span id="FWPM_ACTRL_BEGIN_WRITE_TXN"></span><span id="fwpm_actrl_begin_write_txn"></span>**FWPM\_ACTRL\_BEGIN\_WRITE\_TXN**
</dt> <dd> <dl> <dt>



Begin a read/write transaction. This access right is needed in order to call [**FwpmTransactionBegin0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmtransactionbegin0) for a read/write transaction.


</dt> </dl> </dd> <dt>

<span id="FWPM_ACTRL_CLASSIFY"></span><span id="fwpm_actrl_classify"></span>**FWPM\_ACTRL\_CLASSIFY**
</dt> <dd> <dl> <dt>



Classify Remote Procedure Call (RPC). This access right is needed by the RPC run-time in order to enforce RPC filters.


</dt> </dl> </dd> <dt>

<span id="FWPM_ACTRL_ENUM"></span><span id="fwpm_actrl_enum"></span>**FWPM\_ACTRL\_ENUM**
</dt> <dd> <dl> <dt>



Enumerate. This access right is needed in order to call [**Fwpm\*CreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutcreateenumhandle0) functions. To enumerate an object, the caller also needs FWPM\_ACTRL\_READ access to the object.


</dt> </dl> </dd> <dt>

<span id="FWPM_ACTRL_OPEN"></span><span id="fwpm_actrl_open"></span>**FWPM\_ACTRL\_OPEN**
</dt> <dd> <dl> <dt>



Open a session to the filter engine. This access right is needed in order to call [**FwpmEngineOpen0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmengineopen0).


</dt> </dl> </dd> <dt>

<span id="FWPM_ACTRL_READ"></span><span id="fwpm_actrl_read"></span>**FWPM\_ACTRL\_READ**
</dt> <dd> <dl> <dt>



Read. This access right is needed in order to call [**Fwpm\*GetById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutgetbyid0) and [**Fwpm\*GetByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutgetbykey0) functions.


</dt> </dl> </dd> <dt>

<span id="FWPM_ACTRL_READ_STATS"></span><span id="fwpm_actrl_read_stats"></span>**FWPM\_ACTRL\_READ\_STATS**
</dt> <dd> <dl> <dt>



Read statistics. This access right is needed in order to call [**IPsecGetStatistics0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecgetstatistics0) and [**IkeextGetStatistics0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ikeextgetstatistics0).


</dt> </dl> </dd> <dt>

<span id="FWPM_ACTRL_SUBSCRIBE"></span><span id="fwpm_actrl_subscribe"></span>**FWPM\_ACTRL\_SUBSCRIBE**
</dt> <dd> <dl> <dt>



Subscribe. This access right is needed in order to call [**Fwpm\*SubscribeChanges0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidersubscribechanges0) functions. To receive a notification for an object, a subscriber also needs FWPM\_ACTRL\_READ access to the object.


</dt> </dl> </dd> <dt>

<span id="FWPM_ACTRL_WRITE"></span><span id="fwpm_actrl_write"></span>**FWPM\_ACTRL\_WRITE**
</dt> <dd> <dl> <dt>



Write engine options. This access right is needed in order to call [**FwpmEngineSetOption0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmenginesetoption0).


</dt> </dl> </dd> <dt>

<span id="FWPM_GENERIC_READ"></span><span id="fwpm_generic_read"></span>**FWPM\_GENERIC\_READ**
</dt> <dd> <dl> <dt>



STANDARD\_RIGHTS\_READ \| FWPM\_ACTRL\_BEGIN\_READ\_TXN \| FWPM\_ACTRL\_CLASSIFY \| FWPM\_ACTRL\_OPEN \| FWPM\_ACTRL\_READ \| FWPM\_ACTRL\_READ\_STATS


</dt> </dl> </dd> <dt>

<span id="FWPM_GENERIC_EXECUTE"></span><span id="fwpm_generic_execute"></span>**FWPM\_GENERIC\_EXECUTE**
</dt> <dd> <dl> <dt>



STANDARD\_RIGHTS\_EXECUTE \| FWPM\_ACTRL\_ENUM \| FWPM\_ACTRL\_SUBSCRIBE


</dt> </dl> </dd> <dt>

<span id="FWPM_GENERIC_WRITE"></span><span id="fwpm_generic_write"></span>**FWPM\_GENERIC\_WRITE**
</dt> <dd> <dl> <dt>



STANDARD\_RIGHTS\_WRITE \| DELETE \| FWPM\_ACTRL\_ADD \| FWPM\_ACTRL\_ADD\_LINK \| FWPM\_ACTRL\_BEGIN\_WRITE\_TXN \| FWPM\_ACTRL\_WRITE


</dt> </dl> </dd> <dt>

<span id="FWPM_GENERIC_ALL"></span><span id="fwpm_generic_all"></span>**FWPM\_GENERIC\_ALL**
</dt> <dd> <dl> <dt>



STANDARD\_RIGHTS\_REQUIRED \| FWPM\_ACTRL\_ADD \| FWPM\_ACTRL\_ADD\_LINK \| FWPM\_ACTRL\_BEGIN\_READ\_TXN \| FWPM\_ACTRL\_BEGIN\_WRITE\_TXN \| FWPM\_ACTRL\_CLASSIFY \| FWPM\_ACTRL\_ENUM \| FWPM\_ACTRL\_OPEN \| FWPM\_ACTRL\_READ \| FWPM\_ACTRL\_READ\_STATS \| FWPM\_ACTRL\_SUBSCRIBE \| FWPM\_ACTRL\_WRITE


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Fwpmu.h</dt> </dl> |



## See also

<dl> <dt>

[Windows Filtering Platform Access Control Model](access-control.md)
</dt> <dt>

[Standard Access Rights](/windows/desktop/SecAuthZ/standard-access-rights)
</dt> </dl>

 


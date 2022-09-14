---
description: KTM defines the following enlistment access masks to be used when opening enlistments.
ms.assetid: 93773eb7-141a-49f3-9306-ffbda2f4ab9f
title: Enlistment Access Masks (WinNT.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Enlistment Access Masks

KTM defines the following enlistment access masks to be used when opening enlistments.

<dl> <dt>

<span id="ENLISTMENT_QUERY_INFORMATION"></span><span id="enlistment_query_information"></span>**ENLISTMENT\_QUERY\_INFORMATION**
</dt> <dd> <dl> <dt>

0x00001
</dt> <dt>



The caller can query KTM for information about the enlistment.


</dt> </dl> </dd> <dt>

<span id="ENLISTMENT_SET_INFORMATION"></span><span id="enlistment_set_information"></span>**ENLISTMENT\_SET\_INFORMATION**
</dt> <dd> <dl> <dt>

0x00002
</dt> <dt>



The caller can set information about the enlistment.


</dt> </dl> </dd> <dt>

<span id="ENLISTMENT_RECOVER"></span><span id="enlistment_recover"></span>**ENLISTMENT\_RECOVER**
</dt> <dd> <dl> <dt>

0x00004
</dt> <dt>



The caller can recover an enlistment.


</dt> </dl> </dd> <dt>

<span id="ENLISTMENT_SUBORDINATE_RIGHTS"></span><span id="enlistment_subordinate_rights"></span>**ENLISTMENT\_SUBORDINATE\_RIGHTS**
</dt> <dd> <dl> <dt>

0x00008
</dt> <dt>



The caller can complete actions that a resource manager does on behalf of the transaction. The following is a list of actions:

-   [**CommitComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-commitcomplete)
-   [**PrepareComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-preparecomplete)
-   [**PrePrepareComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-prepreparecomplete)
-   [**RollbackComplete**](/windows/desktop/api/Ktmw32/nf-ktmw32-rollbackcomplete)
-   [**ReadOnlyEnlistment**](/windows/desktop/api/Ktmw32/nf-ktmw32-readonlyenlistment)
-   [**RollbackEnlistment**](/windows/desktop/api/Ktmw32/nf-ktmw32-rollbackenlistment)
-   [**SinglePhaseReject**](/windows/desktop/api/Ktmw32/nf-ktmw32-singlephasereject)


</dt> </dl> </dd> <dt>

<span id="ENLISTMENT_SUPERIOR_RIGHTS"></span><span id="enlistment_superior_rights"></span>**ENLISTMENT\_SUPERIOR\_RIGHTS**
</dt> <dd> <dl> <dt>

0x00010
</dt> <dt>



The caller can enlist in the transaction as a superior transaction manager.


</dt> </dl> </dd> <dt>

<span id="ENLISTMENT_GENERIC_READ"></span><span id="enlistment_generic_read"></span>**ENLISTMENT\_GENERIC\_READ**
</dt> <dd> <dl> <dt>

0x20001
</dt> <dt>



The caller has the following privileges: **STANDARD\_RIGHTS\_READ** and **ENLISTMENT\_QUERY\_INFORMATION**.


</dt> </dl> </dd> <dt>

<span id="ENLISTMENT_GENERIC_WRITE"></span><span id="enlistment_generic_write"></span>**ENLISTMENT\_GENERIC\_WRITE**
</dt> <dd> <dl> <dt>

0x2001E
</dt> <dt>



The caller has the following privileges: **STANDARD\_RIGHTS\_WRITE**, **ENLISTMENT\_SET\_INFORMATION**, and **ENLISTMENT\_RECOVER**.


</dt> </dl> </dd> <dt>

<span id="ENLISTMENT_GENERIC_EXECUTE"></span><span id="enlistment_generic_execute"></span>**ENLISTMENT\_GENERIC\_EXECUTE**
</dt> <dd> <dl> <dt>

0x2001C
</dt> <dt>



The caller has the following privileges: **STANDARD\_RIGHTS\_EXECUTE**, **ENLISTMENT\_RECOVER**, and **ENLISTMENT\_SUBORDINATE\_RIGHTS**.


</dt> </dl> </dd> <dt>

<span id="ENLISTMENT_ALL_ACCESS"></span><span id="enlistment_all_access"></span>**ENLISTMENT\_ALL\_ACCESS**
</dt> <dd> <dl> <dt>

0xF001F
</dt> <dt>



This value sets all valid bits for an enlistment access value.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                     |
| Header<br/>                   | <dl> <dt>WinNT.h</dt> </dl> |



 

 





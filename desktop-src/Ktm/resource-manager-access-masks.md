---
description: KTM defines the following enlistment access masks to be used when opening a resource manager.
ms.assetid: 6b901b73-516d-4f27-b258-3b93a8f9675f
title: Resource Manager Access Masks (WinNT.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Resource Manager Access Masks

KTM defines the following enlistment access masks to be used when opening a resource manager.

<dl> <dt>

<span id="RESOURCEMANAGER_QUERY_INFORMATION"></span><span id="resourcemanager_query_information"></span>**RESOURCEMANAGER\_QUERY\_INFORMATION**
</dt> <dd> <dl> <dt>



The caller can query for the resource manager (RM) information.


</dt> </dl> </dd> <dt>

<span id="RESOURCEMANAGER_SET_INFORMATION"></span><span id="resourcemanager_set_information"></span>**RESOURCEMANAGER\_SET\_INFORMATION**
</dt> <dd> <dl> <dt>



The caller can set the RM information.


</dt> </dl> </dd> <dt>

<span id="RESOURCEMANAGER_RECOVER"></span><span id="resourcemanager_recover"></span>**RESOURCEMANAGER\_RECOVER**
</dt> <dd> <dl> <dt>



The caller can recover the specified RM.


</dt> </dl> </dd> <dt>

<span id="RESOURCEMANAGER_ENLIST"></span><span id="resourcemanager_enlist"></span>**RESOURCEMANAGER\_ENLIST**
</dt> <dd> <dl> <dt>



The caller can enlist an RM in a transaction.


</dt> </dl> </dd> <dt>

<span id="RESOURCEMANAGER_GET_NOTIFICATION"></span><span id="resourcemanager_get_notification"></span>**RESOURCEMANAGER\_GET\_NOTIFICATION**
</dt> <dd> <dl> <dt>



The caller can receive a notification for an RM.


</dt> </dl> </dd> <dt>

<span id="RESOURCEMANAGER_GENERIC_READ"></span><span id="resourcemanager_generic_read"></span>**RESOURCEMANAGER\_GENERIC\_READ**
</dt> <dd> <dl> <dt>



The caller has the following privileges: STANDARD\_RIGHTS\_READ, RESOURCEMANAGER\_QUERY\_INFORMATION, and RESOURCEMANAGER\_RECOVER.


</dt> </dl> </dd> <dt>

<span id="RESOURCEMANAGER_GENERIC_WRITE"></span><span id="resourcemanager_generic_write"></span>**RESOURCEMANAGER\_GENERIC\_WRITE**
</dt> <dd> <dl> <dt>



The caller has the following privileges: STANDARD\_RIGHTS\_WRITE, RESOURCEMANAGER\_SET\_INFORMATION, RESOURCEMANAGER\_ENLIST, and RESOURCEMANAGER\_GET\_NOTIFICATION.


</dt> </dl> </dd> <dt>

<span id="RESOURCEMANAGER_GENERIC_EXECUTE"></span><span id="resourcemanager_generic_execute"></span>**RESOURCEMANAGER\_GENERIC\_EXECUTE**
</dt> <dd> <dl> <dt>



The caller has the following privileges: STANDARD\_RIGHTS\_EXECUTE, RESOURCEMANAGER\_ENLIST, and RESOURCEMANAGER\_GET\_NOTIFICATION.


</dt> </dl> </dd> <dt>

<span id="RESOURCEMANAGER_ALL_ACCESS"></span><span id="resourcemanager_all_access"></span>**RESOURCEMANAGER\_ALL\_ACCESS**
</dt> <dd> <dl> <dt>



The caller has the following privilege: STANDARD\_RIGHTS\_REQUIRED.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                     |
| Header<br/>                   | <dl> <dt>WinNT.h</dt> </dl> |



 

 





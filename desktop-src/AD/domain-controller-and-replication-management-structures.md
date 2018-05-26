---
title: Domain Controller and Replication Management Structures
description: The domain controller and replication management functions use the following structures.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 42b20d3b-1799-4f5f-b74e-fe9284dd8ac3
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Domain Controller and Replication Management Structures

The domain controller and replication management functions use the following structures:

-   [**DS\_DOMAIN\_CONTROLLER\_INFO\_1**](/windows/win32/Ntdsapi/ns-ntdsapi-ds_domain_controller_info_1a?branch=master)
-   [**DS\_DOMAIN\_CONTROLLER\_INFO\_2**](/windows/win32/Ntdsapi/ns-ntdsapi-ds_domain_controller_info_2a?branch=master)
-   [**DS\_DOMAIN\_CONTROLLER\_INFO\_3**](/windows/win32/Ntdsapi/ns-ntdsapi-ds_domain_controller_info_3a?branch=master)
-   [**DS\_NAME\_RESULT**](/windows/win32/Ntdsapi/ns-ntdsapi-ds_name_resulta?branch=master)
-   [**DS\_NAME\_RESULT\_ITEM**](/windows/win32/Ntdsapi/ns-ntdsapi-ds_name_result_itema?branch=master)
-   [**DS\_REPL\_ATTR\_META\_DATA**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_attr_meta_data?branch=master)
-   [**DS\_REPL\_ATTR\_META\_DATA\_2**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_attr_meta_data_2?branch=master)
-   [**DS\_REPL\_ATTR\_META\_DATA\_BLOB**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_attr_meta_data_blob?branch=master)
-   [**DS\_REPL\_ATTR\_VALUE\_META\_DATA**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_attr_value_meta_data?branch=master)
-   [**DS\_REPL\_ATTR\_VALUE\_META\_DATA\_2**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_attr_value_meta_data_2?branch=master)
-   [**DS\_REPL\_ATTR\_VALUE\_META\_DATA\_EXT**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_attr_value_meta_data_ext?branch=master)
-   [**DS\_REPL\_CURSOR**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_cursor?branch=master)
-   [**DS\_REPL\_CURSOR\_2**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_cursor_2?branch=master)
-   [**DS\_REPL\_CURSOR\_3**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_cursor_3w?branch=master)
-   [**DS\_REPL\_CURSOR\_BLOB**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_cursor_blob?branch=master)
-   [**DS\_REPL\_CURSORS**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_cursors?branch=master)
-   [**DS\_REPL\_CURSORS\_2**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_cursors_2?branch=master)
-   [**DS\_REPL\_CURSORS\_3**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_cursors_3w?branch=master)
-   [**DS\_REPL\_KCC\_DSA\_FAILURE**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_kcc_dsa_failurew?branch=master)
-   [**DS\_REPL\_KCC\_DSA\_FAILURES**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_kcc_dsa_failuresw?branch=master)
-   [**DS\_REPL\_KCC\_DSA\_FAILUREW\_BLOB**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_kcc_dsa_failurew_blob?branch=master)
-   [**DS\_REPL\_NEIGHBOR**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_neighborw?branch=master)
-   [**DS\_REPL\_NEIGHBORS**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_neighborsw?branch=master)
-   [**DS\_REPL\_NEIGHBORW\_BLOB**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_neighborw_blob?branch=master)
-   [**DS\_REPL\_OBJ\_META\_DATA**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_obj_meta_data?branch=master)
-   [**DS\_REPL\_OBJ\_META\_DATA\_2**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_obj_meta_data_2?branch=master)
-   [**DS\_REPL\_OP**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_opw?branch=master)
-   [**DS\_REPL\_OPW\_BLOB**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_opw_blob?branch=master)
-   [**DS\_REPL\_PENDING\_OPS**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_pending_opsw?branch=master)
-   [**DS\_REPL\_QUEUE\_STATISTICSW**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_queue_statisticsw?branch=master)
-   [**DS\_REPL\_QUEUE\_STATISTICSW\_BLOB**](https://msdn.microsoft.com/library/ms676274)
-   [**DS\_REPL\_VALUE\_META\_DATA**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_value_meta_data?branch=master)
-   [**DS\_REPL\_VALUE\_META\_DATA\_2**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_value_meta_data_2?branch=master)
-   [**DS\_REPL\_VALUE\_META\_DATA\_EXT**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_value_meta_data_ext?branch=master)
-   [**DS\_REPL\_VALUE\_META\_DATA\_BLOB**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_value_meta_data_blob?branch=master)
-   [**DS\_REPL\_VALUE\_META\_DATA\_BLOB\_EXT**](/windows/win32/Ntdsapi/ns-ntdsapi-_ds_repl_value_meta_data_blob_ext?branch=master)
-   [**DS\_REPSYNCALL\_ERRINFO**](/windows/win32/Ntdsapi/ns-ntdsapi-ds_repsyncall_errinfoa?branch=master)
-   [**DS\_REPSYNCALL\_SYNC**](/windows/win32/Ntdsapi/ns-ntdsapi-ds_repsyncall_synca?branch=master)
-   [**DS\_REPSYNCALL\_UPDATE**](/windows/win32/Ntdsapi/ns-ntdsapi-ds_repsyncall_updatea?branch=master)
-   [**DS\_SCHEMA\_GUID\_MAP**](/windows/win32/Ntdsapi/ns-ntdsapi-ds_schema_guid_mapa?branch=master)
-   [**DS\_SITE\_COST\_INFO**](/windows/win32/Ntdsapi/ns-ntdsapi-ds_site_cost_info?branch=master)
-   [**SCHEDULE**](/windows/win32/Schedule/ns-schedule-_schedule?branch=master)
-   [**SCHEDULE\_HEADER**](/windows/win32/Schedule/ns-schedule-_schedule_header?branch=master)

## Related topics

<dl> <dt>

[Structures in Active Directory Domain Services](structures-in-active-directory-domain-services.md)
</dt> </dl>

 

 





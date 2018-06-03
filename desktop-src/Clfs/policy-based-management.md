---
Description: Policy-based management of log files.
ms.assetid: 50e25a66-e30c-4bc2-8943-bf0612d8ce18
title: Policy-Based Management
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Policy-Based Management

The policy-based management of log files provides several benefits. The setting of the following policies allows the log manager to handle the low-level log management for you.



| Policy                                                                          | Description                                                                                                              |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [**ClfsMgmtPolicyAutoGrow**](/windows/desktop/api/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type)<br/>              | Controls the auto-grow feature.<br/>                                                                               |
| [**ClfsMgmtPolicyAutoShrink**](/windows/desktop/api/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type)<br/>            | Controls the timing of the log-shrinking feature.<br/>                                                             |
| [**ClfsMgmtPolicyGrowthRate**](/windows/desktop/api/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type)<br/>            | Controls the rate of growth of a log.<br/>                                                                         |
| [**ClfsMgmtPolicyLogTail**](/windows/desktop/api/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type)<br/>               | Controls the amount of space that [**LOG\_TAIL\_ADVANCE\_CALLBACK**](/windows/desktop/api/Clfsmgmtw32/nc-clfsmgmtw32-plog_tail_advance_callback) requests.<br/> |
| [**ClfsMgmtPolicyMaximumSize**](/windows/desktop/api/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type)<br/>           | Specifies the maximum size of a log.<br/>                                                                          |
| [**ClfsMgmtPolicyMinimumSize**](/windows/desktop/api/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type)<br/>           | Specifies the minimum size of a log.<br/>                                                                          |
| [**ClfsMgmtPolicyNewContainerExtension**](/windows/desktop/api/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type)<br/> | Controls the extension that is given to a new container.<br/>                                                      |
| [**ClfsMgmtPolicyNewContainerPrefix**](/windows/desktop/api/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type)<br/>    | Controls the prefix that is given to a new container.<br/>                                                         |
| [**ClfsMgmtPolicyNewContainerSize**](/windows/desktop/api/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type)<br/>      | Controls the size of a new container.<br/>                                                                         |
| [**ClfsMgmtPolicyNewContainerSuffix**](/windows/desktop/api/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type)<br/>    | Controls the suffix that is given to a new container.<br/>                                                         |



 

To use the log manager, your application must call the [**RegisterManageableLogClient**](/windows/desktop/api/Clfsmgmtw32/nf-clfsmgmtw32-registermanageablelogclient) function and provide any necessary callbacks. You must have the permissions to set policies.

## Resolving Log-Full Conditions

When an application has a log-full condition, the application can call either the [**HandleLogFull**](/windows/desktop/api/Clfsmgmtw32/nf-clfsmgmtw32-handlelogfull) or [**SetLogFileWithPolicy**](/windows/desktop/api/Clfsmgmtw32/nf-clfsmgmtw32-setlogfilesizewithpolicy) function to request that the log manager resolve a log-full situation on behalf of the application.

When the [**HandleLogFull**](/windows/desktop/api/Clfsmgmtw32/nf-clfsmgmtw32-handlelogfull) function is used to resolve a log-full condition, the log manager can either add containers or request other managed clients to move their respective log tails to a new position. When the [**SetLogFileWithPolicy**](/windows/desktop/api/Clfsmgmtw32/nf-clfsmgmtw32-setlogfilesizewithpolicy) function is called, the log file grows based on the policy. The **SetLogFileWithPolicy** function can also be used to shrink the log. When adding and removing containers using **HandleLogFull** or **SetLogFileWithPolicy**, CLFS Management uses the calling application's security context.

## Avoiding Log-Full Scenarios

By using the log manager, applications can specify policies that can prevent a log-full condition from occurring in most situations. The policies can direct the log manager to either grow or shrink the log automatically.

The log manager can automatically grow or shrink the log only if an application does not insert records faster than containers can be inserted, typically around 1000 records in .5 seconds.

## Multiple Clients in a Single Log

Policy-based management provides a way for different applications to work within the same physical log, but have no specific knowledge or access to other applications' data. This allows an application to request that other managed clients of a particular log to move their tails, which can happen during log-full scenarios.

 

 





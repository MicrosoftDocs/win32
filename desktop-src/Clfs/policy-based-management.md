---
Description: 'Policy-based management of log files.'
ms.assetid: '50e25a66-e30c-4bc2-8943-bf0612d8ce18'
title: 'Policy-Based Management'
---

# Policy-Based Management

The policy-based management of log files provides several benefits. The setting of the following policies allows the log manager to handle the low-level log management for you.



| Policy                                                                          | Description                                                                                                              |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [**ClfsMgmtPolicyAutoGrow**](clfs-mgmt-policy-type.md)<br/>              | Controls the auto-grow feature.<br/>                                                                               |
| [**ClfsMgmtPolicyAutoShrink**](clfs-mgmt-policy-type.md)<br/>            | Controls the timing of the log-shrinking feature.<br/>                                                             |
| [**ClfsMgmtPolicyGrowthRate**](clfs-mgmt-policy-type.md)<br/>            | Controls the rate of growth of a log.<br/>                                                                         |
| [**ClfsMgmtPolicyLogTail**](clfs-mgmt-policy-type.md)<br/>               | Controls the amount of space that [**LOG\_TAIL\_ADVANCE\_CALLBACK**](log-tail-advance-callback.md) requests.<br/> |
| [**ClfsMgmtPolicyMaximumSize**](clfs-mgmt-policy-type.md)<br/>           | Specifies the maximum size of a log.<br/>                                                                          |
| [**ClfsMgmtPolicyMinimumSize**](clfs-mgmt-policy-type.md)<br/>           | Specifies the minimum size of a log.<br/>                                                                          |
| [**ClfsMgmtPolicyNewContainerExtension**](clfs-mgmt-policy-type.md)<br/> | Controls the extension that is given to a new container.<br/>                                                      |
| [**ClfsMgmtPolicyNewContainerPrefix**](clfs-mgmt-policy-type.md)<br/>    | Controls the prefix that is given to a new container.<br/>                                                         |
| [**ClfsMgmtPolicyNewContainerSize**](clfs-mgmt-policy-type.md)<br/>      | Controls the size of a new container.<br/>                                                                         |
| [**ClfsMgmtPolicyNewContainerSuffix**](clfs-mgmt-policy-type.md)<br/>    | Controls the suffix that is given to a new container.<br/>                                                         |



 

To use the log manager, your application must call the [**RegisterManageableLogClient**](registermanageablelogclient.md) function and provide any necessary callbacks. You must have the permissions to set policies.

## Resolving Log-Full Conditions

When an application has a log-full condition, the application can call either the [**HandleLogFull**](handlelogfull.md) or [**SetLogFileWithPolicy**](setlogfilesizewithpolicy.md) function to request that the log manager resolve a log-full situation on behalf of the application.

When the [**HandleLogFull**](handlelogfull.md) function is used to resolve a log-full condition, the log manager can either add containers or request other managed clients to move their respective log tails to a new position. When the [**SetLogFileWithPolicy**](setlogfilesizewithpolicy.md) function is called, the log file grows based on the policy. The **SetLogFileWithPolicy** function can also be used to shrink the log. When adding and removing containers using **HandleLogFull** or **SetLogFileWithPolicy**, CLFS Management uses the calling application's security context.

## Avoiding Log-Full Scenarios

By using the log manager, applications can specify policies that can prevent a log-full condition from occurring in most situations. The policies can direct the log manager to either grow or shrink the log automatically.

The log manager can automatically grow or shrink the log only if an application does not insert records faster than containers can be inserted, typically around 1000 records in .5 seconds.

## Multiple Clients in a Single Log

Policy-based management provides a way for different applications to work within the same physical log, but have no specific knowledge or access to other applications' data. This allows an application to request that other managed clients of a particular log to move their tails, which can happen during log-full scenarios.

 

 





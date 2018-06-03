---
Description: The Common Log File System (CLFS) API is controlled by the policies that are specified.
ms.assetid: 4b3d59e2-079a-4268-b1b1-52ec4ad42bff
title: CLFS Management Policies
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLFS Management Policies

The Common Log File System (CLFS) API is controlled by the policies that are specified. You can specify the policies by using the [**CLFS\_MGMT\_POLICY**](/windows/desktop/api/Clfsmgmt/ns-clfsmgmt-_clfs_mgmt_policy) structure, which is a series of various policy unions. The following policies are available in CLFS.



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



 

 

 





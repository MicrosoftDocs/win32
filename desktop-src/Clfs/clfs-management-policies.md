---
Description: The Common Log File System (CLFS) API is controlled by the policies that are specified.
ms.assetid: 4b3d59e2-079a-4268-b1b1-52ec4ad42bff
title: CLFS Management Policies
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CLFS Management Policies

The Common Log File System (CLFS) API is controlled by the policies that are specified. You can specify the policies by using the [**CLFS\_MGMT\_POLICY**](/windows/win32/Clfsmgmt/ns-clfsmgmt-_clfs_mgmt_policy?branch=master) structure, which is a series of various policy unions. The following policies are available in CLFS.



| Policy                                                                          | Description                                                                                                              |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [**ClfsMgmtPolicyAutoGrow**](/windows/win32/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type?branch=master)<br/>              | Controls the auto-grow feature.<br/>                                                                               |
| [**ClfsMgmtPolicyAutoShrink**](/windows/win32/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type?branch=master)<br/>            | Controls the timing of the log-shrinking feature.<br/>                                                             |
| [**ClfsMgmtPolicyGrowthRate**](/windows/win32/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type?branch=master)<br/>            | Controls the rate of growth of a log.<br/>                                                                         |
| [**ClfsMgmtPolicyLogTail**](/windows/win32/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type?branch=master)<br/>               | Controls the amount of space that [**LOG\_TAIL\_ADVANCE\_CALLBACK**](/windows/win32/Clfsmgmtw32/nc-clfsmgmtw32-plog_tail_advance_callback?branch=master) requests.<br/> |
| [**ClfsMgmtPolicyMaximumSize**](/windows/win32/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type?branch=master)<br/>           | Specifies the maximum size of a log.<br/>                                                                          |
| [**ClfsMgmtPolicyMinimumSize**](/windows/win32/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type?branch=master)<br/>           | Specifies the minimum size of a log.<br/>                                                                          |
| [**ClfsMgmtPolicyNewContainerExtension**](/windows/win32/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type?branch=master)<br/> | Controls the extension that is given to a new container.<br/>                                                      |
| [**ClfsMgmtPolicyNewContainerPrefix**](/windows/win32/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type?branch=master)<br/>    | Controls the prefix that is given to a new container.<br/>                                                         |
| [**ClfsMgmtPolicyNewContainerSize**](/windows/win32/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type?branch=master)<br/>      | Controls the size of a new container.<br/>                                                                         |
| [**ClfsMgmtPolicyNewContainerSuffix**](/windows/win32/Clfsmgmt/ne-clfsmgmt-_clfs_mgmt_policy_type?branch=master)<br/>    | Controls the suffix that is given to a new container.<br/>                                                         |



 

 

 





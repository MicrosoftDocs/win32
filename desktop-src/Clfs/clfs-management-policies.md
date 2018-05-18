---
Description: 'The Common Log File System (CLFS) API is controlled by the policies that are specified.'
ms.assetid: '4b3d59e2-079a-4268-b1b1-52ec4ad42bff'
title: CLFS Management Policies
---

# CLFS Management Policies

The Common Log File System (CLFS) API is controlled by the policies that are specified. You can specify the policies by using the [**CLFS\_MGMT\_POLICY**](clfs-mgmt-policy.md) structure, which is a series of various policy unions. The following policies are available in CLFS.



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



 

 

 





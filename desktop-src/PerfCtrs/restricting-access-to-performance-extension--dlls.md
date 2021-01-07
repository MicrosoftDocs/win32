---
description: Beginning with Windows Server 2003, the Performance Monitor Users group and the Performance Log Users group were made available to developers and users of performance DLLs and the Performance Data Helper (PDH) API functions.
ms.assetid: 423359be-9d41-4a5f-91cd-f6d7a6a91d9d
title: Restricting Access to Performance Extension DLLs
ms.topic: article
ms.date: 05/31/2018
---

# Restricting Access to Performance Extension DLLs

Beginning with Windows Server 2003, the Performance Monitor Users group and the Performance Log Users group were made available to developers and users of performance DLLs and the Performance Data Helper (PDH) API functions. These performance security groups are intended for use by system administrators in restricting access to the information exposed by performance DLLs to a specific list of users.

The Performance Monitor Users group is intended to include users that view counter data and do not log counter data using the Performance Logs and Alerts service. The Performance Log Users group should include users that have permission to use the Performance Logs and Alert service to log counters on the local or remote server. Privileges of this group also include creating log files on local or remote systems, using the alerts service, and running programs as part of the service.

Note that these performance security groups are not by themselves an access restriction mechanism. You must use these groups with the Windows object access-control model to do this.

Most applications communicate with the performance DLL through an IPC mechanism, typically shared memory. Therefore, you can add the members of a performance security group to the security descriptor of the shared memory object to restrict access to the DLL to those members of the security group. When doing this, you must also add the group members to the security descriptor of the system objects that the performance DLL accesses in order to provide counter data, for example, log files and folders. For more detailed information on adding ACLs to object security descriptors, refer to [Modifying an Object's ACL](/windows/desktop/SecAuthZ/modifying-the-acls-of-an-object-in-c--).

Another method you can use to modify the ACL information of an IPC system object's security descriptor is to specify the members of the performance security group list with Security Descriptor Definition Language (SDDL) and call [**ConvertStringSecurityDescriptorToSecurityDescriptor**](/windows/desktop/api/sddl/nf-sddl-convertstringsecuritydescriptortosecuritydescriptora) to create the security descriptor. This security descriptor is then attached to the IPC system object. The following shows an SDDL string that includes the Performance Monitor Users group, MU, and the Performance Log Users group, LU.

``` syntax
D:(A;OICI;GA;;;SY)(A;OICI;GA;;;BA)(A;OICI;FRFWFXSDRC;;;NS)(A;OICI;FRFWFXSDRC;;;LU)(A;OICI;FRFX;;;MU) 
```

 

 

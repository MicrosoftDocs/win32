---
description: Because files are securable objects, access to them is regulated by the access-control model that governs access to all other securable objects in Windows.
ms.assetid: 991d7d94-fae7-406f-b2e3-dee811279366
title: File Security and Access Rights
ms.topic: article
ms.date: 05/31/2018
---

# File Security and Access Rights

Because files are [securable objects](/windows/desktop/SecAuthZ/securable-objects), access to them is regulated by the access-control model that governs access to all other securable objects in Windows. For a detailed explanation of this model, see [Access Control](/windows/desktop/SecAuthZ/access-control).

You can specify a [security descriptor](/windows/desktop/api/winnt/ns-winnt-security_descriptor) for a file or directory when you call the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea), [**CreateDirectory**](/windows/desktop/api/FileAPI/nf-fileapi-createdirectorya), or [**CreateDirectoryEx**](/windows/desktop/api/WinBase/nf-winbase-createdirectoryexa) function. If you specify **NULL** for the *lpSecurityAttributes* parameter, the file or directory gets a default security descriptor. The access control lists (ACL) in the default security descriptor for a file or directory are inherited from its parent directory. Note that a default security descriptor is assigned only when a file or directory is newly created, and not when it is renamed or moved.

To retrieve the security descriptor of a file or directory object, call the [**GetNamedSecurityInfo**](/windows/desktop/api/aclapi/nf-aclapi-getnamedsecurityinfoa) or [**GetSecurityInfo**](/windows/desktop/api/aclapi/nf-aclapi-getsecurityinfo) function. To change the security descriptor of a file or directory object, call the [**SetNamedSecurityInfo**](/windows/desktop/api/aclapi/nf-aclapi-setnamedsecurityinfoa) or [**SetSecurityInfo**](/windows/desktop/api/aclapi/nf-aclapi-setsecurityinfo) function.

The valid access rights for files and directories include the **DELETE**, **READ\_CONTROL**, **WRITE\_DAC**, **WRITE\_OWNER**, and **SYNCHRONIZE** [standard access rights](/windows/desktop/SecAuthZ/standard-access-rights). The table in [**File Access Rights Constants**](file-access-rights-constants.md) lists the access rights that are specific to files and directories.

Although the **SYNCHRONIZE** access right is defined within the [standard access rights](/windows/desktop/SecAuthZ/standard-access-rights) list as the right to specify a file handle in one of the wait functions, when using asynchronous file I/O operations you should wait on the event handle contained in a properly configured [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure rather than using the file handle with the **SYNCHRONIZE** access right for synchronization.

The following are the [generic access rights](/windows/desktop/SecAuthZ/generic-access-rights) for files and directories.



<table>
<thead>
<tr class="header">
<th>Access right</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>FILE_GENERIC_EXECUTE</strong></td>
<td><dl> <strong>FILE_EXECUTE</strong><br />
<strong>FILE_READ_ATTRIBUTES</strong><br />
<strong>STANDARD_RIGHTS_EXECUTE</strong><br />
<strong>SYNCHRONIZE</strong><br />
</dl></td>
</tr>
<tr class="even">
<td><strong>FILE_GENERIC_READ</strong></td>
<td><dl> <strong>FILE_READ_ATTRIBUTES</strong><br />
<strong>FILE_READ_DATA</strong><br />
<strong>FILE_READ_EA</strong><br />
<strong>STANDARD_RIGHTS_READ</strong><br />
<strong>SYNCHRONIZE</strong><br />
</dl></td>
</tr>
<tr class="odd">
<td><strong>FILE_GENERIC_WRITE</strong></td>
<td><dl> <strong>FILE_APPEND_DATA</strong><br />
<strong>FILE_WRITE_ATTRIBUTES</strong><br />
<strong>FILE_WRITE_DATA</strong><br />
<strong>FILE_WRITE_EA</strong><br />
<strong>STANDARD_RIGHTS_WRITE</strong><br />
<strong>SYNCHRONIZE</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 

Windows compares the requested access rights and the information in the thread's access token with the information in the file or directory object's security descriptor. If the comparison does not prohibit all of the requested access rights from being granted, a handle to the object is returned to the thread and the access rights are granted. For more information about this process, see [Interaction between Threads and Securable Objects](/windows/desktop/SecAuthZ/interaction-between-threads-and-securable-objects).

By default, authorization for access to a file or directory is controlled strictly by the ACLs in the security descriptor associated with that file or directory. In particular, the security descriptor of a parent directory is not used to control access to any child file or directory. The **FILE\_TRAVERSE** [access right](/windows/desktop/SecAuthZ/access-rights-and-access-masks) can be enforced by removing the **BYPASS\_TRAVERSE\_CHECKING** [privilege](/windows/desktop/SecAuthZ/privileges) from users. This is not recommended in the general case, as many programs do not correctly handle directory traversal errors. The primary use for the **FILE\_TRAVERSE** access right on directories is to enable conformance to certain IEEE and ISO POSIX standards when interoperability with Unix systems is a requirement.

The Windows security model provides a way for a child directory to inherit, or to be prevented from inheriting, one or more of the ACEs in the parent directory's security descriptor. Each ACE contains information that determines how it can be inherited, and whether it will have an effect on the inheriting directory object. For example, some inherited ACEs control access to the inherited directory object, and these are called *effective ACEs*. All other ACEs are called *inherit-only ACEs*.

The Windows security model also enforces the automatic inheritance of ACEs to child objects according to the [ACE inheritance rules](/windows/desktop/SecAuthZ/ace-inheritance-rules). This automatic inheritance, along with the inheritance information in each ACE, determines how security restrictions are passed down the directory hierarchy.

Note that you cannot use an access-denied ACE to deny only **GENERIC\_READ** or only **GENERIC\_WRITE** access to a file. This is because for file objects, the generic mappings for both **GENERIC\_READ** or **GENERIC\_WRITE** include the **SYNCHRONIZE** access right. If an ACE denies **GENERIC\_WRITE** access to a trustee, and the trustee requests **GENERIC\_READ** access, the request will fail because the request implicitly includes **SYNCHRONIZE** access which is implicitly denied by the ACE, and vice versa. Instead of using access-denied ACEs, use access-allowed ACEs to explicitly allow the permitted access rights.

Another means of managing access to storage objects is encryption. The implementation of file system encryption in Windows is the Encrypted File System, or EFS. EFS encrypts only files and not directories. The advantage of encryption is that it provides additional protection to files that is applied on the media and not through the file system and the standard Windows access control architecture. For more information on file encryption, see [File Encryption](file-encryption.md).

In most cases, the ability to read and write the security settings of a file or directory object is restricted to kernel-mode processes. Clearly, you would not want any user process to be able to change the ownership or access restriction on your private file or directory. However, a backup application would not be able to complete its job of backing up your file if the access restrictions you have placed on your file or directory does not allow the application's user-mode process to read it. Backup applications must be able to override the security settings of file and directory objects to ensure a complete backup. Similarly, if a backup application attempts to write a backup copy of your file over the disk-resident copy, and you explicitly deny write privileges to the backup application process, the restore operation cannot complete. In this case also, the backup application must be able to override the access control settings of your file.

The **SE\_BACKUP\_NAME** and **SE\_RESTORE\_NAME** access privileges were specifically created to provide this ability to backup applications. If these privileges have been granted and enabled in the access token of the backup application process, it can then call [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) to open your file or directory for backup, specifying the standard **READ\_CONTROL** access right as the value of the *dwDesiredAccess* parameter. However, to identify the calling process as a backup process, the call to **CreateFile** must include the **FILE\_FLAG\_BACKUP\_SEMANTICS** flag in the *dwFlagsAndAttributes* parameter. The full syntax of the function call is the following:


```C++
HANDLE hFile = CreateFile( fileName,                   // lpFileName
                           READ_CONTROL,               // dwDesiredAccess
                           0,                          // dwShareMode
                           NULL,                       // lpSecurityAttributes
                           OPEN_EXISTING,              // dwCreationDisposition
                           FILE_FLAG_BACKUP_SEMANTICS, // dwFlagsAndAttributes
                           NULL );                     // hTemplateFile
```



This will allow the backup application process to open your file and override the standard security checking. To restore your file, the backup application would use the following [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) call syntax when opening your file to be written.


```C++
HANDLE hFile = CreateFile( fileName,                   // lpFileName
                           WRITE_OWNER | WRITE_DAC,    // dwDesiredAccess
                           0,                          // dwShareMode
                           NULL,                       // lpSecurityAttributes
                           CREATE_ALWAYS,              // dwCreationDisposition
                           FILE_FLAG_BACKUP_SEMANTICS, // dwFlagsAndAttributes
                           NULL );                     // hTemplateFile
```



There are situations when a backup application must be able to change the access control settings of a file or directory. An example is when the access control settings of the disk-resident copy of a file or directory is different from the backup copy. This would happen if these settings were changed after the file or directory was backed up, or if it was corrupted.

The **FILE\_FLAG\_BACKUP\_SEMANTICS** flag specified in the call to [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) gives the backup application process permission to read the access-control settings of the file or directory. With this permission, the backup application process can then call [**GetKernelObjectSecurity**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-getkernelobjectsecurity) and [**SetKernelObjectSecurity**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-setkernelobjectsecurity) to read and than reset the access-control settings.

If a backup application must have access to the system-level [access control settings](/windows/desktop/SecAuthZ/access-control-lists), the **ACCESS\_SYSTEM\_SECURITY** flag must be specified in the *dwDesiredAccess* parameter value passed to [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea).

Backup applications call [**BackupRead**](/windows/desktop/api/winbase/nf-winbase-backupread) to read the files and directories specified for the restore operation, and [**BackupWrite**](/windows/desktop/api/winbase/nf-winbase-backupwrite) to write them.

## Related topics

<dl> <dt>

[standard access rights](/windows/desktop/SecAuthZ/standard-access-rights)
</dt> </dl>

 

 

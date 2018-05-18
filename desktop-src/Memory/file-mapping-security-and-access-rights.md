---
Description: 'The Windows security model enables you to control access to file mapping objects. For more information, see Access-Control Model.'
ms.assetid: '8bbf7c98-ff83-4ed9-8b82-f08dcd31295c'
title: File Mapping Security and Access Rights
---

# File Mapping Security and Access Rights

The Windows security model enables you to control access to file mapping objects. For more information, see [Access-Control Model](security.access_control_model).

You can specify a [security descriptor](security.security_descriptors) for a file mapping object when you call the [**CreateFileMapping**](createfilemapping.md) function. If you specify **NULL**, the object gets a default security descriptor. The ACLs in the default security descriptor for a file mapping object come from the primary or impersonation token of the creator.

To retrieve the security descriptor of a file mapping object, call the [**GetNamedSecurityInfo**](security.getnamedsecurityinfo) or [**GetSecurityInfo**](security.getsecurityinfo) function. To set the security descriptor of a file mapping object, call the [**SetNamedSecurityInfo**](security.setnamedsecurityinfo) or [**SetSecurityInfo**](security.setsecurityinfo) function.

The valid access rights for file mapping objects include the **DELETE**, **READ\_CONTROL**, **WRITE\_DAC**, and **WRITE\_OWNER** [standard access rights](security.standard_access_rights). File mapping objects do not support the **SYNCHRONIZE** standard access right. The following table lists the specific access rights for file mapping objects.



| Access right                               | Meaning                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **FILE\_MAP\_ALL\_ACCESS**<br/>      | Includes all access rights to a file mapping object except **FILE\_MAP\_EXECUTE**. The [**MapViewOfFile**](mapviewoffile.md) and [**MapViewOfFileEx**](mapviewoffileex.md) functions treat this the same as specifying **FILE\_MAP\_WRITE**.<br/>                                                                                                                                                          |
| **FILE\_MAP\_EXECUTE**<br/>          | Allows mapping of executable views of the file mapping object. The object must have been created with page protection that allows execute access, such as **PAGE\_EXECUTE\_READ**, **PAGE\_EXECUTE\_WRITECOPY**, or **PAGE\_EXECUTE\_READWRITE** protection. <br/>                                                                                                                                           |
| **FILE\_MAP\_READ**<br/>             | Allows mapping of read-only or copy-on-write views of the file mapping object. <br/>                                                                                                                                                                                                                                                                                                                         |
| **FILE\_MAP\_WRITE**<br/>            | Allows mapping of read-only, copy-on-write, or read/write views of a file mapping object. The object must have been created with page protection that allows write access, such as **PAGE\_READWRITE** or **PAGE\_EXECUTE\_READWRITE** protection.<br/>                                                                                                                                                      |
| **FILE\_MAP\_TARGETS\_INVALID**<br/> | Sets all the locations in the mapped file as invalid targets for CFG. This flag is similar to **PAGE\_TARGETS\_INVALID**. It is used along with the execute access right **FILE\_MAP\_EXECUTE**. Any indirect call to locations in those pages will fail CFG checks and the process will be terminated. The default behavior for executable pages allocated is to be marked valid call targets for CFG.<br/> |



 

Mapping a copy-on-write view of a file mapping object requires the same access as mapping a read-only view. **FILE\_MAP\_COPY** is not an actual access right and should not be specified as part of a DACL in a security descriptor. This value can be used only with functions that map a view of a file mapping object, such as the [**MapViewOfFile**](mapviewoffile.md) and [**MapViewOfFileEx**](mapviewoffileex.md) functions, or with the [**OpenFileMapping**](openfilemapping.md) function, which treats **FILE\_MAP\_COPY** the same as **FILE\_MAP\_READ**.

You can request the **ACCESS\_SYSTEM\_SECURITY** access right to a file mapping object if you want to read or write the object's SACL. For more information, see [Access-Control Lists (ACLs)](security.access_control_lists_acls_) and [SACL Access Right](security.sacl_access_right).

 

 





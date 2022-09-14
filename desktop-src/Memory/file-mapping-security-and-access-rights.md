---
description: The Windows security model enables you to control access to file-mapping objects. For more information, see Access-Control Model.
ms.assetid: 8bbf7c98-ff83-4ed9-8b82-f08dcd31295c
title: File Mapping Security and Access Rights
ms.topic: article
ms.date: 10/06/2018
---

# File-mapping security and access rights

The Windows security model lets you control access to file-mapping objects. For more information, see [Access-Control Model](../secauthz/access-control-model.md).

You can specify a [security descriptor](../secauthz/security-descriptors.md) for a file-mapping object when you call the [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function. If you specify **NULL**, the object gets a default security descriptor. The ACLs in the default security descriptor for a file-mapping object come from the primary or impersonation token of the creator.

To retrieve the security descriptor of a file-mapping object, call the [**GetNamedSecurityInfo**](/windows/win32/api/aclapi/nf-aclapi-getnamedsecurityinfoa) or [**GetSecurityInfo**](/windows/win32/api/aclapi/nf-aclapi-getsecurityinfo) function. To set the security descriptor of a file-mapping object, call the [**SetNamedSecurityInfo**](/windows/win32/api/aclapi/nf-aclapi-setnamedsecurityinfoa) or [**SetSecurityInfo**](/windows/win32/api/aclapi/nf-aclapi-setsecurityinfo) function.

The valid access rights for file-mapping objects include the **DELETE**, **READ\_CONTROL**, **WRITE\_DAC**, and **WRITE\_OWNER** [standard access rights](../secauthz/standard-access-rights.md). File mapping objects do not support the **SYNCHRONIZE** standard access right. The following table lists the access rights that are specific to file-mapping objects.

| Access right | Meaning |
|-|-|
| **FILE\_MAP\_ALL\_ACCESS** | Includes all access rights to a file-mapping object except **FILE\_MAP\_EXECUTE**. The [**MapViewOfFile**](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffile) and [**MapViewOfFileEx**](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffileex) functions treat this the same as specifying **FILE\_MAP\_WRITE**. |
| **FILE\_MAP\_EXECUTE** | Allows mapping of executable views of the file-mapping object. The object must have been created with page protection that allows execute access, such as **PAGE\_EXECUTE\_READ**, **PAGE\_EXECUTE\_WRITECOPY**, or **PAGE\_EXECUTE\_READWRITE** protection.  |
| **FILE\_MAP\_READ** | Allows mapping of read-only or copy-on-write views of the file-mapping object.  |
| **FILE\_MAP\_WRITE** | Allows mapping of read-only, copy-on-write, or read/write views of a file-mapping object. The object must have been created with page protection that allows write access, such as **PAGE\_READWRITE** or **PAGE\_EXECUTE\_READWRITE** protection. |

Mapping a copy-on-write view of a file-mapping object requires the same access as mapping a read-only view. The **FILE\_MAP\_COPY** flag is not an access right, and it should not be specified as part of a DACL in a security descriptor. This value can be used only with functions that map a view of a file-mapping object, such as the [**MapViewOfFile**](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffile) and [**MapViewOfFileEx**](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffileex) functions, or with the [**OpenFileMapping**](/windows/desktop/api/WinBase/nf-winbase-openfilemappinga) function, which treats **FILE\_MAP\_COPY** the same way it treats **FILE\_MAP\_READ**.

You can request the **ACCESS\_SYSTEM\_SECURITY** access right to a file-mapping object if you want to read or write the object's SACL. For more information, see [Access-Control Lists (ACLs)](../secauthz/access-control-lists.md) and [SACL Access Right](../secauthz/sacl-access-right.md).

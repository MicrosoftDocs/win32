---
Description: The Windows security model enables you to control access to file-mapping objects. For more information, see Access-Control Model.
ms.assetid: 8bbf7c98-ff83-4ed9-8b82-f08dcd31295c
title: File Mapping Security and Access Rights
ms.topic: article
ms.date: 10/06/2018
---

# File-mapping security and access rights

The Windows security model lets you control access to file-mapping objects. For more information, see [Access-Control Model](https://msdn.microsoft.com/en-us/library/Aa374876(v=VS.85).aspx).

You can specify a [security descriptor](https://msdn.microsoft.com/en-us/library/Aa379563(v=VS.85).aspx) for a file-mapping object when you call the [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function. If you specify **NULL**, the object gets a default security descriptor. The ACLs in the default security descriptor for a file-mapping object come from the primary or impersonation token of the creator.

To retrieve the security descriptor of a file-mapping object, call the [**GetNamedSecurityInfo**](https://msdn.microsoft.com/en-us/library/Aa446645(v=VS.85).aspx) or [**GetSecurityInfo**](https://msdn.microsoft.com/en-us/library/Aa446654(v=VS.85).aspx) function. To set the security descriptor of a file-mapping object, call the [**SetNamedSecurityInfo**](https://msdn.microsoft.com/en-us/library/Aa379579(v=VS.85).aspx) or [**SetSecurityInfo**](https://msdn.microsoft.com/en-us/library/Aa379588(v=VS.85).aspx) function.

The valid access rights for file-mapping objects include the **DELETE**, **READ\_CONTROL**, **WRITE\_DAC**, and **WRITE\_OWNER** [standard access rights](https://msdn.microsoft.com/en-us/library/Aa379607(v=VS.85).aspx). File mapping objects do not support the **SYNCHRONIZE** standard access right. The following table lists the access rights that are specific to file-mapping objects.

| Access right | Meaning |
|-|-|
| **FILE\_MAP\_ALL\_ACCESS** | Includes all access rights to a file-mapping object except **FILE\_MAP\_EXECUTE**. The [**MapViewOfFile**](https://msdn.microsoft.com/en-us/library/Aa366761(v=VS.85).aspx) and [**MapViewOfFileEx**](https://msdn.microsoft.com/en-us/library/Aa366763(v=VS.85).aspx) functions treat this the same as specifying **FILE\_MAP\_WRITE**. |
| **FILE\_MAP\_EXECUTE** | Allows mapping of executable views of the file-mapping object. The object must have been created with page protection that allows execute access, such as **PAGE\_EXECUTE\_READ**, **PAGE\_EXECUTE\_WRITECOPY**, or **PAGE\_EXECUTE\_READWRITE** protection.  |
| **FILE\_MAP\_READ** | Allows mapping of read-only or copy-on-write views of the file-mapping object.  |
| **FILE\_MAP\_WRITE** | Allows mapping of read-only, copy-on-write, or read/write views of a file-mapping object. The object must have been created with page protection that allows write access, such as **PAGE\_READWRITE** or **PAGE\_EXECUTE\_READWRITE** protection. |

Mapping a copy-on-write view of a file-mapping object requires the same access as mapping a read-only view. The **FILE\_MAP\_COPY** flag is not an access right, and it should not be specified as part of a DACL in a security descriptor. This value can be used only with functions that map a view of a file-mapping object, such as the [**MapViewOfFile**](https://msdn.microsoft.com/en-us/library/Aa366761(v=VS.85).aspx) and [**MapViewOfFileEx**](https://msdn.microsoft.com/en-us/library/Aa366763(v=VS.85).aspx) functions, or with the [**OpenFileMapping**](/windows/desktop/api/WinBase/nf-winbase-openfilemappinga) function, which treats **FILE\_MAP\_COPY** the same way it treats **FILE\_MAP\_READ**.

You can request the **ACCESS\_SYSTEM\_SECURITY** access right to a file-mapping object if you want to read or write the object's SACL. For more information, see [Access-Control Lists (ACLs)](https://msdn.microsoft.com/library/Aa374872(v=VS.85).aspx) and [SACL Access Right](https://msdn.microsoft.com/en-us/library/Aa379321(v=VS.85).aspx).

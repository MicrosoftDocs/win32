---
Description: The Windows security model enables you to control access to file mapping objects. For more information, see Access-Control Model.
ms.assetid: 8bbf7c98-ff83-4ed9-8b82-f08dcd31295c
title: File Mapping Security and Access Rights
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# File Mapping Security and Access Rights

The Windows security model enables you to control access to file mapping objects. For more information, see [Access-Control Model](https://msdn.microsoft.com/windows/desktop/fd3b718a-5eff-4894-9fc6-d157ddb67330).

You can specify a [security descriptor](https://msdn.microsoft.com/windows/desktop/4ab0e7b1-1b44-4368-b2bd-106c9d2c652c) for a file mapping object when you call the [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function. If you specify **NULL**, the object gets a default security descriptor. The ACLs in the default security descriptor for a file mapping object come from the primary or impersonation token of the creator.

To retrieve the security descriptor of a file mapping object, call the [**GetNamedSecurityInfo**](https://msdn.microsoft.com/windows/desktop/11f2119b-5314-4fa1-8016-9c01f79d037d) or [**GetSecurityInfo**](https://msdn.microsoft.com/windows/desktop/64767a6b-cd79-4e02-881a-706a078ff446) function. To set the security descriptor of a file mapping object, call the [**SetNamedSecurityInfo**](https://msdn.microsoft.com/windows/desktop/70fbba50-2576-4857-a955-119fb12bf7b6) or [**SetSecurityInfo**](https://msdn.microsoft.com/windows/desktop/f1781ba9-81eb-46f9-b530-c390b67d65de) function.

The valid access rights for file mapping objects include the **DELETE**, **READ\_CONTROL**, **WRITE\_DAC**, and **WRITE\_OWNER** [standard access rights](https://msdn.microsoft.com/windows/desktop/f43bccce-0f8c-4732-b678-5fd3218a9f84). File mapping objects do not support the **SYNCHRONIZE** standard access right. The following table lists the specific access rights for file mapping objects.



| Access right                               | Meaning                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **FILE\_MAP\_ALL\_ACCESS**<br/>      | Includes all access rights to a file mapping object except **FILE\_MAP\_EXECUTE**. The [**MapViewOfFile**](https://www.bing.com/search?q=**MapViewOfFile**) and [**MapViewOfFileEx**](https://www.bing.com/search?q=**MapViewOfFileEx**) functions treat this the same as specifying **FILE\_MAP\_WRITE**.<br/>                                                                                                                                                          |
| **FILE\_MAP\_EXECUTE**<br/>          | Allows mapping of executable views of the file mapping object. The object must have been created with page protection that allows execute access, such as **PAGE\_EXECUTE\_READ**, **PAGE\_EXECUTE\_WRITECOPY**, or **PAGE\_EXECUTE\_READWRITE** protection. <br/>                                                                                                                                           |
| **FILE\_MAP\_READ**<br/>             | Allows mapping of read-only or copy-on-write views of the file mapping object. <br/>                                                                                                                                                                                                                                                                                                                         |
| **FILE\_MAP\_WRITE**<br/>            | Allows mapping of read-only, copy-on-write, or read/write views of a file mapping object. The object must have been created with page protection that allows write access, such as **PAGE\_READWRITE** or **PAGE\_EXECUTE\_READWRITE** protection.<br/>                                                                                                                                                      |
| **FILE\_MAP\_TARGETS\_INVALID**<br/> | Sets all the locations in the mapped file as invalid targets for CFG. This flag is similar to **PAGE\_TARGETS\_INVALID**. It is used along with the execute access right **FILE\_MAP\_EXECUTE**. Any indirect call to locations in those pages will fail CFG checks and the process will be terminated. The default behavior for executable pages allocated is to be marked valid call targets for CFG.<br/> |



 

Mapping a copy-on-write view of a file mapping object requires the same access as mapping a read-only view. **FILE\_MAP\_COPY** is not an actual access right and should not be specified as part of a DACL in a security descriptor. This value can be used only with functions that map a view of a file mapping object, such as the [**MapViewOfFile**](https://www.bing.com/search?q=**MapViewOfFile**) and [**MapViewOfFileEx**](https://www.bing.com/search?q=**MapViewOfFileEx**) functions, or with the [**OpenFileMapping**](/windows/desktop/api/WinBase/nf-winbase-openfilemappinga) function, which treats **FILE\_MAP\_COPY** the same as **FILE\_MAP\_READ**.

You can request the **ACCESS\_SYSTEM\_SECURITY** access right to a file mapping object if you want to read or write the object's SACL. For more information, see [Access-Control Lists (ACLs)](https://www.bing.com/search?q=Access-Control Lists (ACLs)) and [SACL Access Right](https://msdn.microsoft.com/windows/desktop/88198243-dae5-49ac-9d54-bfae7a3a0b1a).

 

 





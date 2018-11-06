---
title: NetFile Functions
description: The network management file functions provide a way to monitor and close the file, device, and pipe resources open on a server. The file functions are listed following.
ms.assetid: 3cfb5222-7e02-4bc3-959e-0fc7bc4f0f19
ms.topic: article
ms.date: 05/31/2018
---

# NetFile Functions

The network management file functions provide a way to monitor and close the file, device, and pipe resources open on a server. The file functions are listed following.



| Function                                | Description                                                          |
|-----------------------------------------|----------------------------------------------------------------------|
| [**NetFileClose**](https://msdn.microsoft.com/library/windows/desktop/bb525377)     | Forces a resource to close.                                          |
| [**NetFileEnum**](https://msdn.microsoft.com/library/windows/desktop/bb525378)       | Returns information about open files on a server.                    |
| [**NetFileGetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525379) | Returns information about a particular opening of a server resource. |



 

Call the [**NetFileClose**](https://msdn.microsoft.com/library/windows/desktop/bb525377) function when the file cannot be closed by any other means. This function should be used with caution because **NetFileClose** does not write data cached on the client system to the file before closing the file.

The [**NetFileEnum**](https://msdn.microsoft.com/library/windows/desktop/bb525378) function returns information about resources open on a server. A file can be opened one or more times by one or more applications. Each file opening is uniquely identified. The **NetFileEnum** function returns an entry for each file opening. The [**NetFileGetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525379) function returns information about one opening of a resource.

File information is available at the following levels:

-   [**FILE\_INFO\_2**](https://msdn.microsoft.com/library/windows/desktop/bb525374)
-   [**FILE\_INFO\_3**](https://msdn.microsoft.com/library/windows/desktop/bb525375)

Levels 0 and 1 are not supported. Level 2 returns only the identification number assigned to the resource when it was opened. Level 3 returns the identification number, permissions, file locks, and the name of the user who opened the resource.

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the [**NetFileEnum**](https://msdn.microsoft.com/library/windows/desktop/bb525378) and [**NetFileGetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525379) functions. For more information, see [**IADsResource**](https://msdn.microsoft.com/library/aa706124) and [**IADsFileServiceOperations**](https://msdn.microsoft.com/library/aa706015).

 

 





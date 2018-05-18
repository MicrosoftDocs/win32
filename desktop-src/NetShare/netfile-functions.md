---
Description: 'The network file functions provide a way to monitor and close the file, device, and pipe resources open on a server. The file functions are listed following.'
ms.assetid: 'cbcdad6e-80dd-49f0-9d69-a82a7010f10b'
title: NetFile Functions
---

# NetFile Functions

The network file functions provide a way to monitor and close the file, device, and pipe resources open on a server. The file functions are listed following.



| Function                                 | Description                                                          |
|------------------------------------------|----------------------------------------------------------------------|
| [**NetFileClose**](netfileclose.md)     | Forces a resource to close.                                          |
| [**NetFileEnum**](netfileenum.md)       | Returns information about open files on a server.                    |
| [**NetFileGetInfo**](netfilegetinfo.md) | Returns information about a particular opening of a server resource. |



 

Call the [**NetFileClose**](netfileclose.md) function when the file cannot be closed by any other means. This function should be used with caution because **NetFileClose** does not write data cached on the client system to the file before closing the file.

The [**NetFileEnum**](netfileenum.md) function returns information about resources open on a server. A file can be opened one or more times by one or more applications. Each file opening is uniquely identified. The **NetFileEnum** function returns an entry for each file opening. The [**NetFileGetInfo**](netfilegetinfo.md) function returns information about one opening of a resource.

File information is available at the following levels.

<dl>

[**FILE\_INFO\_2**](file-info-2-str.md)  
[**FILE\_INFO\_3**](file-info-3-str.md)  
</dl>

Levels 0 and 1 are not supported. Level 2 returns only the identification number assigned to the resource when it was opened. Level 3 returns the identification number, permissions, file locks, and the name of the user who opened the resource.

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the [**NetFileEnum**](netfileenum.md) and [**NetFileGetInfo**](netfilegetinfo.md) functions. For more information, see [**IADsResource**](https://msdn.microsoft.com/library/aa706124) and [**IADsFileServiceOperations**](https://msdn.microsoft.com/library/aa706015).

 

 




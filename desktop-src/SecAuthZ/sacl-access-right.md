---
Description: The ACCESS\_SYSTEM\_SECURITY access right controls the ability to get or set the SACL in an objects security descriptor. The system grants this access right only if the SE\_SECURITY\_NAME privilege is enabled in the access token of the requesting thread.
ms.assetid: 88198243-dae5-49ac-9d54-bfae7a3a0b1a
title: SACL Access Right
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SACL Access Right

The ACCESS\_SYSTEM\_SECURITY access right controls the ability to get or set the SACL in an object's [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly). The system grants this access right only if the SE\_SECURITY\_NAME privilege is enabled in the [*access token*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-token-gly) of the requesting thread.

**To access an object's SACL**

1.  Call the [**AdjustTokenPrivileges**](https://msdn.microsoft.com/en-us/library/Aa375202(v=VS.85).aspx) function to enable the SE\_SECURITY\_NAME privilege.
2.  Request the ACCESS\_SYSTEM\_SECURITY access right when you open a handle to the object.
3.  Get or set the object's SACL by using a function such as [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo) or [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo).
4.  Call [**AdjustTokenPrivileges**](https://msdn.microsoft.com/en-us/library/Aa375202(v=VS.85).aspx) to disable the SE\_SECURITY\_NAME privilege.

To access a SACL using the [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa) or [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa) functions, enable the SE\_SECURITY\_NAME privilege. The function internally requests the access right.

The ACCESS\_SYSTEM\_SECURITY access right is not valid in a DACL because DACLs do not control access to a SACL. However, you can use the ACCESS\_SYSTEM\_SECURITY access right in a SACL to audit attempts to use the access right.

 

 




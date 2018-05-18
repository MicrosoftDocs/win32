---
Description: 'The ISCardAuth interface definition is provided as a standard that can be followed when developing a smart card service provider.The ISCardAuth interface can be used to expose authentication services supported by a smart card.'
ms.assetid: '6b8a5b90-49ad-48fd-813c-c3c3337ec8f1'
title: ISCardAuth interface
---

# ISCardAuth interface

\[The **ISCardAuth** interface is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](secsmart.smart_card_modules) provide similar functionality.\]

The **ISCardAuth** interface definition is provided as a standard that can be followed when developing a [*smart card*](security.s_gly#-security-smart-card-gly) [*service provider*](security.c_gly#-security-cryptographic-service-provider-gly).

The **ISCardAuth** interface can be used to expose authentication services supported by a smart card. These services include application authentication, smart card authentication, and user authentication.

The following example shows a typical use of the **ISCardAuth** interface.

**To use ISCardAuth**

1.  Create an **ISCardAuth** interface (through the corresponding [**ISCardManage**](iscardmanage.md) interface method).
2.  Call the appropriate **ISCardAuth** method ([**APP\_Auth**](iscardauth-app-auth.md), [**GetChallenge**](iscardauth-getchallenge.md), [**ICC\_Auth**](iscardauth-icc-auth.md), or [**User\_Auth**](iscardauth-user-auth.md)).
3.  Release the **ISCardAuth** interface.

## Members

The **ISCardAuth** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ISCardAuth** also has these types of members:

-   [Methods](#methods)

### Methods

The **ISCardAuth** interface has these methods.



| Method                                          | Description                                                                                    |
|:------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**APP\_Auth**](iscardauth-app-auth.md)        | Allows the application to authenticate itself using a challenge/signature protocol.<br/> |
| [**GetChallenge**](iscardauth-getchallenge.md) | Returns a challenge from the smart card.<br/>                                            |
| [**ICC\_Auth**](iscardauth-icc-auth.md)        | Allows an application to authenticate the smart card.<br/>                               |
| [**User\_Auth**](iscardauth-user-auth.md)      | Allows access to user authentication services.<br/>                                      |



 

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| End of client support<br/>    | Windows XP<br/>                                |
| End of server support<br/>    | Windows Server 2003<br/>                       |



 

 





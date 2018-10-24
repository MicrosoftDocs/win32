---
Description: Provides services for setting CHV (card holder verification) code and for verifying the user.
ms.assetid: fa40c21c-1584-475e-89f6-f81f67e3b942
title: ISCardVerify interface
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardVerify
api_type: 
- COM
api_location: 
---

# ISCardVerify interface

\[The **ISCardVerify** interface is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](https://msdn.microsoft.com/en-us/library/Dd627652(v=VS.85).aspx) provide similar functionality.\]

The following interface definition is provided as a standard that can be followed when developing a [*smart card*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) [*service provider*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx). The **ISCardVerify** interface provides services for setting CHV (card holder verification) code and for verifying the user.

The **ISCardVerify** class is defined for applications that implement application-specific CHV policy, and that have a detailed knowledge of the smart card's internal implementation.

Following is a typical use of the **ISCardVerify** interface.

The following procedure uses **ISCardVerify** to change the CHV code.

**To change the CHV code of a smart card**

1.  Create an **ISCardVerify** interface (through the corresponding [**ISCardManage**](iscardmanage.md) interface method).
2.  Call the [**ChangeCode**](iscardverify-changecode.md) method and provide new code, specifying if it is local or global and if it is enabled or disabled.
3.  Release the **ISCardVerify** interface.

## Members

The **ISCardVerify** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx) interface. **ISCardVerify** also has these types of members:

-   [Methods](#methods)

### Methods

The **ISCardVerify** interface has these methods.



| Method                                                        | Description                                                                                                                                 |
|:--------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| [**ChangeCode**](iscardverify-changecode.md)                 | Changes the current CHV code.<br/>                                                                                                    |
| [**ResetSecurityState**](iscardverify-resetsecuritystate.md) | Resets the [*security context*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) of the smart card.<br/> |
| [**Unblock**](https://msdn.microsoft.com/en-us/library/Aa377269(v=VS.85).aspx)                       | Re-enables the [*security context*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx).<br/>               |
| [**Verify**](iscardverify-verify.md)                         | Authenticates the user.<br/>                                                                                                          |



 

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| End of client support<br/>    | Windows XP<br/>                                |
| End of server support<br/>    | Windows Server 2003<br/>                       |



 

 





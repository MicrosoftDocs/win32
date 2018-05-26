---
Description: The InformationType property retrieves the security information type.
ms.assetid: 0ddd5219-8f75-413c-bc88-57e4dd3b0a25
title: FaxSecurity.InformationType property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxSecurity.InformationType property

The **InformationType** property retrieves the security information type.

This property is read/write.

## Syntax


```VB
Property InformationType As Long
```



## Property value

A **Long** that specifies or receives the security information type as bitwise flags.

## Remarks

The information type is a bitwise combination that indicates what security information will be retrieved from the server when requesting a security descriptor using the [**Descriptor**](-mfax-faxsecurity-descriptor.md) property or when refreshing the [**FaxSecurity**](-mfax-faxsecurity.md) object using the [**Refresh**](-mfax-faxsecurity-refresh-vb.md) method. The information type also determines what information is sent to the fax server when you save changes to the **FaxSecurity** object using the [**Save**](-mfax-faxsecurity-save-vb.md) method.

The bits are specified in the [SECURITY\_INFORMATION](http://msdn.microsoft.com/library/en-us/secauthz/security/security_information.asp) structure, defined in Winnt.h. Each item of security information is designated by a bit flag. The following values specify the bits applicable to the fax service.



| Value                        | Meaning                                                                                       |
|------------------------------|-----------------------------------------------------------------------------------------------|
| DACL\_SECURITY\_INFORMATION  | Indicates that the discretionary access control list (ACL) of the object is being referenced. |
| GROUP\_SECURITY\_INFORMATION | Indicates that the primary group identifier of the object is being referenced.                |
| OWNER\_SECURITY\_INFORMATION | Indicates that the owner identifier of the object is being referenced.                        |
| SACL\_SECURITY\_INFORMATION  | Indicates that the system ACL of the object is being referenced.                              |



 

You should set the **InformationType** property before you read the [**Descriptor**](-mfax-faxsecurity-descriptor.md) property to ensure that you receive the information that you want and to ensure that you request only the information for which you have the appropriate access rights. Also, the **InformationType** property will affect what information is sent to the fax server when you call the [**Save**](-mfax-faxsecurity-save-vb.md) method. If you do not set the **InformationType** property, it defaults to the flags DACL\_SECURITY\_INFORMATION, GROUP\_SECURITY\_INFORMATION, and OWNER\_SECURITY\_INFORMATION.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



 

 





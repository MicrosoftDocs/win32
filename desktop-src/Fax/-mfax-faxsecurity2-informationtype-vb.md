---
Description: Retrieves the security information type.
ms.assetid: e3417211-c493-4206-af35-af01534f0499
title: FaxSecurity2.InformationType property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxSecurity2.InformationType property

Retrieves the security information type.

This property is read/write.

## Syntax


```VB
Property InformationType As Long
```



## Property value

A **Long** that specifies or receives the security information type.

## Remarks

The information type is a bitwise combination that indicates what security information will be retrieved from the server when requesting a security descriptor using the [**Descriptor**](-mfax-faxsecurity2-descriptor.md) property, or when refreshing the [**FaxSecurity2**](-mfax-faxsecurity2.md) object using the [**Refresh**](-mfax-faxsecurity2-refresh-vb.md) method. The information type property also determines what information is sent to the fax server when you save changes to the **FaxSecurity2** object using the [**Save**](-mfax-faxsecurity2-save-vb.md) method.

The bits are specified in the [SECURITY\_INFORMATION](http://msdn.microsoft.com/library/en-us/secauthz/security/security_information.asp) structure, defined in Winnt.h. Each item of security information is designated by a bit flag. The following values specify the bits applicable to the fax service:



| Value                        | Meaning                                                                                       |
|------------------------------|-----------------------------------------------------------------------------------------------|
| DACL\_SECURITY\_INFORMATION  | Indicates that the discretionary access control list (ACL) of the object is being referenced. |
| GROUP\_SECURITY\_INFORMATION | Indicates that the primary group identifier of the object is being referenced.                |
| OWNER\_SECURITY\_INFORMATION | Indicates that the owner identifier of the object is being referenced.                        |
| SACL\_SECURITY\_INFORMATION  | Indicates that the system ACL of the object is being referenced.                              |



 

Set the **InformationType** property before you get the [**Descriptor**](-mfax-faxsecurity2-descriptor.md) property, to ensure that you receive the desired information, and that you request only the information for which you have the appropriate access rights. Also, the **InformationType** property will affect what information is sent to the fax server when you call the [**Save**](-mfax-faxsecurity2-save-vb.md) method. If you do not set the **InformationType** property, it defaults to the flags DACL\_SECURITY\_INFORMATION, GROUP\_SECURITY\_INFORMATION, and OWNER\_SECURITY\_INFORMATION.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxSecurity2**](-mfax-faxsecurity2.md)
</dt> <dt>

[**IFaxSecurity2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxsecurity2)
</dt> </dl>

 

 





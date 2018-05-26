---
Description: Used by a fax client application to configure the security on a fax server, and permit the calling application to set and retrieve a security descriptor for the fax server.
ms.assetid: 213e555a-1509-4081-a21b-f33fc4653f32
title: FaxSecurity2 object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxSecurity2 object

Used by a fax client application to configure the security on a fax server, and permit the calling application to set and retrieve a security descriptor for the fax server.

## Members

The **FaxSecurity2** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxSecurity2** object has these methods.



| Method                                           | Description                                                                   |
|:-------------------------------------------------|:------------------------------------------------------------------------------|
| [**Refresh**](-mfax-faxsecurity2-refresh-vb.md) | Refreshes **FaxSecurity2** object information from the fax server.<br/> |
| [**Save**](-mfax-faxsecurity2-save-vb.md)       | Saves the [**FaxSecurity**](-mfax-faxsecurity.md) object data.<br/>    |



 

### Properties

The **FaxSecurity2** object has these properties.



| Property                                                                    | Access type           | Description                                                                                                                                                                                                                                                                   |
|:----------------------------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Descriptor**](-mfax-faxsecurity2-descriptor.md)<br/>              | Read/write<br/> | Represents the security descriptor for a [**IFaxServer2**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxserver2?branch=master) interface.<br/>                                                                                                                                                                    |
| [**GrantedRights**](-mfax-faxsecurity2-grantedrights-vb.md)<br/>     | Read-only<br/>  | Retrieves a combination of the fax server access rights granted to the user referencing this property. For example, some users have permission to submit fax jobs with high priority while others have permission to submit jobs with normal or low priority only.<br/> |
| [**InformationType**](-mfax-faxsecurity2-informationtype-vb.md)<br/> | Read/write<br/> | Retrieves the security information type.<br/>                                                                                                                                                                                                                           |



 

## Remarks

This object is supported only on Windows Vista or later. For earlier versions of Windows use [**FaxSecurity**](-mfax-faxsecurity.md).

Only an administrator with permissions can configure the security of the fax server. For more information, see [Access Control](http://msdn.microsoft.com/library/en-us/secauthz/security/access_control.asp).

A **FaxSecurity2** object is accessed through a [**IFaxServer2**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxserver2?branch=master) interface.

![faxserver2 and faxsecurity2](images/faxsecurity2.png)

> [!Note]  
> Changes made to the **FaxSecurity2** object will not be saved until you call the [**Save**](-mfax-faxsecurity2-save-vb.md) method.

 

To create a **FaxSecurity2** object in Microsoft Visual Basic, call the [**Security2**](-mfax-faxserver2-security2-vb.md) property of the [**IFaxServer2**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxserver2?branch=master) interface.

To create a **FaxSecurity2** object in C++, call the [**Security2**](-mfax-faxserver2-security2-vb.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxSecurity2<br/>                                                          |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**IFaxSecurity2**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxsecurity2?branch=master)
</dt> </dl>

 

 





---
title: EmailRights class
description: Rights that apply to emails.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'T:Microsoft.RightsManagement.EmailRights'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["EmailRights class"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.EmailRights
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# EmailRights class

Rights that apply to emails.

## Syntax


```C++
public ref class EmailRights sealed 
```



## Members

The **EmailRights** class inherits from [IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821). **EmailRights** also has these types of members:

-   [Properties](#properties)

### Properties

The **EmailRights** class has these properties.



| Property                                            | Access type          | Description                                                                                                                                                                           |
|:----------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**All**](emailrights-all.md)<br/>           | Read-only<br/> | Gets a list of all the rights that apply to emails.                                                                                                                                   |
| [**Extract**](emailrights-extract.md)<br/>   | Read-only<br/> | Gets a right that allows content to be extracted from a protected email and placed in an unprotected, or a different protected, format. Same value as EditableDocumentRights.Extract. |
| [**Forward**](emailrights-forward.md)<br/>   | Read-only<br/> | Gets a right that allows a protected email message to be forwarded.                                                                                                                   |
| [**Print**](emailrights-print.md)<br/>       | Read-only<br/> | Gets a right that allows protected email content to be printed. Same value as EditableDocumentRights.Print.                                                                           |
| [**Reply**](emailrights-reply.md)<br/>       | Read-only<br/> | Gets a right that allows a protected email message to be replied to with a message that includes a copy of the protected content.                                                     |
| [**ReplyAll**](emailrights-replyall.md)<br/> | Read-only<br/> | Gets a right that allows reply-all to a protected email message with a message that includes a copy of the protected content.                                                         |



 

## Remarks

For more information about the built-in rights and the usage restrictions associated with them that apps should observe, see [Built-in Rights Usage Restriction Reference](built-in-rights-usage-restriction-reference.md).

## Thread Safety

Members of this class are not guaranteed to be thread safe.

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::RightsManagement<br/>                                                                      |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



## See also

<dl> <dt>

[IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821)
</dt> </dl>

 

 






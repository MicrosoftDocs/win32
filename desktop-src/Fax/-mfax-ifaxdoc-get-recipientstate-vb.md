---
Description: Sets or retrieves the RecipientState property of a FaxDoc object. The RecipientState property is a null-terminated string that contains the state of the recipient of the fax transmission.
ms.assetid: 744bb597-644b-4d34-af72-190cda53af8a
title: FaxDoc.RecipientState property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDoc.RecipientState property

Sets or retrieves the **RecipientState** property of a [FaxDoc](-mfax-faxdoc.md) object. The **RecipientState** property is a null-terminated string that contains the state of the recipient of the fax transmission.

This property is read/write.

## Syntax


```VB
Property RecipientState As String
```



## Property value

A **String** that specifies or receives the state of the recipient of the outbound fax transmission.

## Remarks

The fax recipient's state name or state abbreviation can appear on the cover page.

The **get\_RecipientState** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



 

 





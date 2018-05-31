---
Description: Sets or retrieves the RecipientDepartment property of a FaxDoc object. The RecipientDepartment property is a null-terminated string that contains the department of the recipient of the fax transmission.
ms.assetid: d0109a4b-8f2c-41fb-b3f5-509feae1bd1d
title: FaxDoc.RecipientDepartment property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDoc.RecipientDepartment property

Sets or retrieves the **RecipientDepartment** property of a [FaxDoc](-mfax-faxdoc.md) object. The **RecipientDepartment** property is a null-terminated string that contains the department of the recipient of the fax transmission.

This property is read/write.

## Syntax


```VB
Property RecipientDepartment As String
```



## Property value

A **String** that specifies or receives the department identifier of the recipient of the outbound fax transmission.

## Remarks

The sender's fax number can appear on the cover page.

The **get\_RecipientDepartment** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxDoc**](-mfax-faxdoc-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxDoc**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxdoc)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 





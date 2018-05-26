---
Description: Sets or retrieves the SenderFax property of a FaxDoc object. The SenderFax property is a null-terminated string that contains the fax number of the sender of the outbound fax transmission.
ms.assetid: e2d9bbbe-6878-4546-a2b9-be776dc18897
title: FaxDoc.SenderFax property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxDoc.SenderFax property

Sets or retrieves the **SenderFax** property of a [FaxDoc](-mfax-faxdoc.md) object. The **SenderFax** property is a null-terminated string that contains the fax number of the sender of the outbound fax transmission.

This property is read/write.

## Syntax


```VB
Property SenderFax As String
```



## Property value

A **String** that specifies or receives the fax number of the sender of the outbound fax transmission.

## Remarks

The sender's fax number can appear on the cover page.

The **get\_SenderFax** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**IFaxDoc**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxdoc?branch=master)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 





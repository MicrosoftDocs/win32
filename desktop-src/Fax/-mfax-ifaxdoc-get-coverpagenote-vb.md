---
Description: Sets or retrieves the CoverpageNote property of a FaxDoc object. The CoverpageNote property is a null-terminated string that contains the text of a message or note from the sender that pertains to the fax transmission.
ms.assetid: 7dd00d29-1eb2-4b9d-bcbc-b511aa37c73b
title: FaxDoc.CoverpageNote property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDoc.CoverpageNote property

Sets or retrieves the **CoverpageNote** property of a [FaxDoc](-mfax-faxdoc.md) object. The **CoverpageNote** property is a null-terminated string that contains the text of a message or note from the sender that pertains to the fax transmission.

This property is read/write.

## Syntax


```VB
Property CoverpageNote As String
```



## Property value

A **String** that specifies or receives the text of a message or note from the sender that pertains to the fax transmission. The text will appear on the cover page.

## Remarks

The cover page note can appear on the cover page.

The **get\_CoverpageNote** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](https://msdn.microsoft.com/windows/desktop/8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[SysFreeString](https://msdn.microsoft.com/windows/desktop/8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 





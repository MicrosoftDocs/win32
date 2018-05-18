---
Description: 'Sets or retrieves the RecipientName property of a FaxDoc object. The RecipientName property is a null-terminated string that contains the name of the recipient of the fax transmission.'
ms.assetid: '13756bf1-98b6-4339-9c00-d6cb6dc4edf3'
title: 'FaxDoc.RecipientName property'
---

# FaxDoc.RecipientName property

Sets or retrieves the **RecipientName** property of a [FaxDoc](-mfax-faxdoc.md) object. The **RecipientName** property is a null-terminated string that contains the name of the recipient of the fax transmission.

This property is read/write.

## Syntax


```VB
Property RecipientName As String
```



## Property value

A **String** that specifies or receives the name of the recipient of the outbound fax transmission.

## Remarks

The fax recipient's name can appear on the cover page.

The **get\_RecipientName** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**IFaxDoc**](-mfax-ifaxdoc.md)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 





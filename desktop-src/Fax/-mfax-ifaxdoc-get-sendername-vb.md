---
Description: 'Sets or retrieves the SenderName property of a FaxDoc object. The SenderName property is a null-terminated string that contains the name of the sender of the fax transmission.'
ms.assetid: '1c6710e2-97ae-4f7b-9cee-a733be5a67ef'
title: 'FaxDoc.SenderName property'
---

# FaxDoc.SenderName property

Sets or retrieves the **SenderName** property of a [FaxDoc](-mfax-faxdoc.md) object. The **SenderName** property is a null-terminated string that contains the name of the sender of the fax transmission.

This property is read/write.

## Syntax


```VB
Property SenderName As String
```



## Property value

A **String** that specifies or receives the name of the sender of the outbound fax transmission.

## Remarks

The fax sender's name can appear on the cover page.

The **get\_SenderName** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

 

 





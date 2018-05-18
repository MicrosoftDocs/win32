---
Description: 'Sets or retrieves the EmailAddress property of a FaxDoc object. The EmailAddress property is a null-terminated string that contains the email address of the sender of the fax transmission.'
ms.assetid: 'e396a47c-4955-4d81-ba4a-13600c9ff985'
title: 'FaxDoc.EmailAddress property'
---

# FaxDoc.EmailAddress property

Sets or retrieves the **EmailAddress** property of a [FaxDoc](-mfax-faxdoc.md) object. The **EmailAddress** property is a null-terminated string that contains the email address of the sender of the fax transmission.

This property is read/write.

## Syntax


```VB
Property EmailAddress As String
```



## Property value

A **String** that specifies or receives the email address of the user who sent the fax transmission.

## Remarks

The fax server uses the **EmailAddress** property to send delivery reports (DRs) and nondelivery reports (NDRs) to the sender of the transmission. The email address must be a valid address or alias in the Microsoft Exchange Server global address list (GAL).

The **get\_EmailAddress** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

 

 





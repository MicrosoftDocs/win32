---
Description: Sets or retrieves the ServerMapiProfile property for a FaxServer object. The ServerMapiProfile property is a null-terminated string that contains the MAPI user profile that the fax server uses for routing incoming fax transmissions.
ms.assetid: c81b523f-2515-4fb0-b8d4-d22caf8c692b
title: FaxServer.ServerMapiProfile property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxServer.ServerMapiProfile property

Sets or retrieves the **ServerMapiProfile** property for a [FaxServer](-mfax-faxserver-client.md) object. The **ServerMapiProfile** property is a null-terminated string that contains the MAPI user profile that the fax server uses for routing incoming fax transmissions.

This property is read/write.

## Syntax


```VB
Property ServerMapiProfile As String
```



## Property value

A **String** that specifies or receives the MAPI user profile that the fax server uses for routing incoming fax transmissions. The fax server also uses the profile for sending delivery reports (DRs) and nondelivery reports (NDRs).

## Remarks

> [!Note]  
> This function is not supported in Windows XP.

 

The **IFaxServer::get\_ServerMapiProfile** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxServer**](-mfax-faxserver-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[FaxServer](-mfax-faxserver-client.md)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 





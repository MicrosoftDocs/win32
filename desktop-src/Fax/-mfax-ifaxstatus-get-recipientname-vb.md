---
Description: Retrieves the RecipientName property for a FaxStatus object. The RecipientName property is a null-terminated string that contains the name of the recipient of an inbound fax transmission.
ms.assetid: b09347e9-7949-442b-a438-1b7b0727ae8c
title: FaxStatus.RecipientName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxStatus.RecipientName property

Retrieves the **RecipientName** property for a [FaxStatus](-mfax-faxstatus.md) object. The **RecipientName** property is a null-terminated string that contains the name of the recipient of an inbound fax transmission.

This property is read-only.

## Syntax


```VB
Property RecipientName As String
```



## Property value

A **String** that receives the name of the fax recipient. Note that the **RecipientName** property is valid only if the [**Receive**](-mfax-ifaxstatus-get-receive-vb.md) property is equal to **True**.

## Remarks

If the information is not available, the **IFaxStatus::get\_RecipientName** method returns an empty string.

The **IFaxStatus::get\_RecipientName** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](https://msdn.microsoft.com/windows/desktop/8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxStatus**](-mfax-faxstatus-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxStatus**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxstatus)
</dt> <dt>

[**Receive**](-mfax-ifaxstatus-get-receive-vb.md)
</dt> <dt>

[**IFaxPorts**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxports)
</dt> <dt>

[**IFaxPort**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxport)
</dt> <dt>

[SysFreeString](https://msdn.microsoft.com/windows/desktop/8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 





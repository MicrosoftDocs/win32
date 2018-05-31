---
Description: The Csid property is a null-terminated string that contains the called station identifier (CSID) associated with the fax port.
ms.assetid: d9f7755a-9b7b-4cb7-9303-c8ba6276e243
title: FaxPort.Csid property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxPort.Csid property

The **Csid** property is a null-terminated string that contains the called station identifier (CSID) associated with the fax port.

This property is read/write.

## Syntax


```VB
Property Csid As String
```



## Property value

A **String** that specifies or receives the CSID for the fax port.

## Remarks

> [!Note]  
> Before setting a value for this property, a fax client application can call the [**CanModify**](-mfax-ifaxport-get-canmodify-vb.md) property to ensure that the client has permission to modify configuration information for the specified fax port.

 

Only printable characters such as English letters, numeric symbols, and punctuation marks (ASCII range 0x20 to 0x7F) can be used in a CSID.

When the fax service receives a fax on a port, the service transmits the CSID to the sending device.

The T.30 specification of the International Telecommunication Union (ITU) restricts the value of a CSID to 20 ASCII characters. If a fax client application specifies a CSID that contains non-ASCII characters, the fax service removes them. If the CSID exceeds 20 characters, the service truncates the extra characters.

**Csid** allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxPort**](-mfax-faxport-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxPort**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxport)
</dt> <dt>

[**IFaxPorts**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxports)
</dt> </dl>

 

 





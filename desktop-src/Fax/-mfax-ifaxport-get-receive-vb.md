---
Description: 'The Receive property is a Boolean value that indicates whether a specified fax port is enabled to receive faxes.'
ms.assetid: '17d98cd9-b305-495b-a0ae-5a92d0b71169'
title: 'FaxPort.Receive property'
---

# FaxPort.Receive property

The **Receive** property is a Boolean value that indicates whether a specified fax port is enabled to receive faxes.

This property is read/write.

## Syntax


```VB
Property Receive As Boolean
```



## Property value

A **Boolean** that specifies or receives whether receiving faxes is enabled or disabled for the fax port. If this parameter is equal to TRUE, receiving faxes is enabled for the port.

## Remarks

> [!Note]  
> Before setting a value for this property, a fax client application can call the [**CanModify**](-mfax-ifaxport-get-canmodify-vb.md) property to ensure that the client has permission to modify configuration information for the specified fax port.

 

The **Receive** property returns a value of TRUE if the fax port is enabled to receive faxes. If a fax client application passes a value of TRUE to the property, it enables the fax port to receive faxes.

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

[**IFaxPort**](-mfax-ifaxport.md)
</dt> <dt>

[**IFaxPorts**](-mfax-ifaxports.md)
</dt> </dl>

 

 





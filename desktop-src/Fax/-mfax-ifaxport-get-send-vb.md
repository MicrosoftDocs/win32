---
Description: 'The Send property is a Boolean value that indicates whether a fax port is enabled to send faxes.'
ms.assetid: 'dcd870cf-2116-4f68-ab3a-979418b96a07'
title: 'FaxPort.Send property'
---

# FaxPort.Send property

The **Send** property is a Boolean value that indicates whether a fax port is enabled to send faxes.

This property is read/write.

## Syntax


```VB
Property Send As Boolean
```



## Property value

A **Boolean** that specifies or receives whether sending faxes is enabled or disabled for the fax port. To enable a fax port to send faxes, a fax client application must pass a value of TRUE to the property.

## Remarks

> [!Note]  
> Before setting a value for this property, a fax client application can call the [**CanModify**](-mfax-ifaxport-get-canmodify-vb.md) property to ensure that the client has permission to modify configuration information for the specified fax port.

 

The **Send** property returns a value of TRUE if the fax port is enabled to send faxes. If a fax client application passes a value of TRUE to the property, it enables the fax port to send faxes.

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

 

 





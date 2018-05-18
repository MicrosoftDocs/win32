---
Description: 'The Count returns the number of fax routing methods associated with a FaxPort object.'
ms.assetid: 'f0368c01-0b25-4cb0-a1c4-8150e8a7d199'
title: 'FaxRoutingMethods.Count property'
---

# FaxRoutingMethods.Count property

The **Count** returns the number of fax routing methods associated with a [FaxPort](-mfax-faxport.md) object.

This property is read-only.

## Syntax


```VB
Property Count As Long
```



## Property value

A **Long** that receives the number of fax routing methods associated with this fax port.

## Remarks

After calling the **Count** property, a fax client application can call the [**Item**](-mfax-ifaxroutingmethods-get-item-vb.md) property to retrieve one or more [FaxRoutingMethod](-mfax-faxroutingmethod.md) objects.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxRoutingMethods**](-mfax-faxroutingmethods-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[FaxRoutingMethods](-mfax-faxroutingmethods.md)
</dt> <dt>

[**Item**](-mfax-ifaxroutingmethods-get-item-vb.md)
</dt> <dt>

[FaxRoutingMethod](-mfax-faxroutingmethod.md)
</dt> <dt>

[**GetRoutingMethods**](-mfax-ifaxport-getroutingmethods-vb.md)
</dt> </dl>

 

 





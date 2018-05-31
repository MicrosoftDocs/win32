---
Description: The Item method creates a FaxRoutingMethod object for a specified fax routing method. The object allows enumeration of fax routing information for a specified FaxPort object.
ms.assetid: 77df7911-91c2-4c85-91c0-462551b2c99c
title: FaxRoutingMethods.Item property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxRoutingMethods.Item property

The **Item** method creates a [FaxRoutingMethod](-mfax-faxroutingmethod.md) object for a specified fax routing method. The object allows enumeration of fax routing information for a specified [FaxPort](-mfax-faxport.md) object.

This property is read-only.

## Syntax


```VB
Property Item( _
  ByVal lCount As Long _
) As Object
```



## Property value

An **Object** that receives a [FaxRoutingMethod](-mfax-faxroutingmethod.md) object.

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

[**Count**](-mfax-ifaxroutingmethods-get-count-vb.md)
</dt> <dt>

[FaxRoutingMethod](-mfax-faxroutingmethod.md)
</dt> <dt>

[**GetRoutingMethods**](-mfax-ifaxport-getroutingmethods-vb.md)
</dt> </dl>

 

 





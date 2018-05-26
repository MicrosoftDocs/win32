---
Description: The Item property returns a FaxInboundRoutingMethod object from the FaxInboundRoutingMethods collection.
ms.assetid: d628a3f7-1362-46a4-97ce-98e7108fcceb
title: FaxInboundRoutingMethods.Item property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxInboundRoutingMethods.Item property

The **Item** property returns a [**FaxInboundRoutingMethod**](-mfax-faxinboundroutingmethod.md) object from the [**FaxInboundRoutingMethods**](-mfax-faxinboundroutingmethods.md) collection.

This property is read-only.

## Syntax


```VB
Property Item( _
  ByVal vIndex As Variant _
) As IFaxInboundRoutingMethod
```



## Property value

A variable of type [**IFaxInboundRoutingMethod**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxinboundroutingmethod?branch=master) that receives a [**FaxInboundRoutingMethod**](-mfax-faxinboundroutingmethod.md) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-routing-extensions-and-routing-methods.md)
</dt> <dt>

[**FaxInboundRoutingMethods**](-mfax-faxinboundroutingmethods.md)
</dt> </dl>

 

 





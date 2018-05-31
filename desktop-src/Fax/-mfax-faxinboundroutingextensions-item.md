---
Description: The Item property returns a FaxInboundRoutingExtension object from the FaxInboundRoutingExtensions collection.
ms.assetid: c8a2f15d-24ba-4a7a-acb3-28dcae96a2c5
title: FaxInboundRoutingExtensions.Item property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxInboundRoutingExtensions.Item property

The **Item** property returns a [**FaxInboundRoutingExtension**](-mfax-faxinboundroutingextension.md) object from the [**FaxInboundRoutingExtensions**](-mfax-faxinboundroutingextensions.md) collection.

This property is read-only.

## Syntax


```VB
Property Item( _
  ByVal vIndex As Variant _
) As IFaxInboundRoutingExtension
```



## Property value

A variable of type [**IFaxInboundRoutingExtension**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxinboundroutingextension) that receives A [**FaxInboundRoutingExtension**](-mfax-faxinboundroutingextension.md) object.

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

[**FaxInboundRoutingExtensions**](-mfax-faxinboundroutingextensions.md)
</dt> </dl>

 

 





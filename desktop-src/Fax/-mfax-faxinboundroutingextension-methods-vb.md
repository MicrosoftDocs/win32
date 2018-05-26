---
Description: The Methods property is an array of GUIDs that uniquely identify the inbound routing methods exposed by the fax routing extension.
ms.assetid: 2db89dd2-c22a-435b-98a1-ce4b130bfd53
title: FaxInboundRoutingExtension.Methods property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxInboundRoutingExtension.Methods property

The **Methods** property is an array of GUIDs that uniquely identify the inbound routing methods exposed by the fax routing extension.

This property is read-only.

## Syntax


```VB
Property Methods As Variant
```



## Property value

A **Variant** that receives an array of GUIDs. Each GUID represents an inbound routing method exposed by the fax routing extension.

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

[**FaxInboundRoutingExtension**](-mfax-faxinboundroutingextension.md)
</dt> <dt>

[**IFaxInboundRoutingExtension**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxinboundroutingextension?branch=master)
</dt> </dl>

 

 





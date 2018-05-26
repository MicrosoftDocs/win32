---
Description: The Refresh method refreshes FaxOutboundRoutingRule object information from the fax server.
ms.assetid: 7b8521ef-80e9-493b-ac09-a4633a4bfd4a
title: FaxOutboundRoutingRule.Refresh method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutboundRoutingRule.Refresh method

The **Refresh** method refreshes [**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md) object information from the fax server.

## Syntax


```VB
FaxOutboundRoutingRule.Refresh() As Long
```



## Parameters

This method has no parameters.

## Remarks

When the **Refresh** method is called, any configuration changes made after the last [**Save**](-mfax-faxoutboundroutingrule-save-vb.md) method call are lost.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-creating-and-managing-outbound-routing-rules.md)
</dt> <dt>

[**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md)
</dt> <dt>

[**IFaxOutboundRoutingRule**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutboundroutingrule?branch=master)
</dt> </dl>

 

 





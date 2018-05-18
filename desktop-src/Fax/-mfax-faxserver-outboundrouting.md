---
Description: 'The OutboundRouting property creates a FaxOutboundRouting configuration object. The object permits users to configure outbound routing groups and rules.'
ms.assetid: '04bc7832-c205-42e3-bc53-b68bcfb7b430'
title: 'FaxServer.OutboundRouting property'
---

# FaxServer.OutboundRouting property

The **OutboundRouting** property creates a [**FaxOutboundRouting**](-mfax-faxoutboundrouting.md) configuration object. The object permits users to configure outbound routing groups and rules.

This property is read-only.

## Syntax


```VB
Property OutboundRouting As FaxOutboundRouting
```



## Property value

A [**FaxOutboundRouting**](-mfax-faxoutboundrouting.md) object.

## Remarks

This property is not supported in Windows XP, and will return the error: [FAX\_E\_NOT\_SUPPORTED\_ON\_THIS\_SKU](-mfax-fax-error-codes.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-outbound-routing-groups.md)
</dt> <dt>

[**FaxServer**](-mfax-faxserver.md)
</dt> <dt>

[**IFaxServer**](-mfax-faxserver-cpp.md)
</dt> </dl>

 

 





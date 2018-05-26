---
Description: The FaxOutboundRouting configuration object is used by a fax client application to configure the outbound routing groups (FaxOutboundRoutingGroups objects) and outbound routing rules (FaxOutboundRoutingRules objects).
ms.assetid: 64ff05d6-6ebe-4155-96cd-7b925c979492
title: FaxOutboundRouting object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutboundRouting object

The **FaxOutboundRouting** configuration object is used by a fax client application to configure the outbound routing groups ([**FaxOutboundRoutingGroups**](-mfax-faxoutboundroutinggroups.md) objects) and outbound routing rules ([**FaxOutboundRoutingRules**](-mfax-faxoutboundroutingrules.md) objects).

## Members

The **FaxOutboundRouting** object has these types of members:

-   [Methods](#methods)

### Methods

The **FaxOutboundRouting** object has these methods.



| Method                                                  | Description                                                                                                                        |
|:--------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| [**GetGroups**](-mfax-faxoutboundrouting-getgroups.md) | The [**GetGroups**](-mfax-faxoutboundrouting-getgroups.md) method retrieves the collection of outbound routing groups.<br/> |
| [**GetRules**](-mfax-faxoutboundrouting-getrules.md)   | The [**GetRules**](-mfax-faxoutboundrouting-getrules.md) method retrieves the collection of outbound routing groups.<br/>   |



 

## Remarks

A **FaxOutboundRouting** object is accessed through a [**FaxServer**](-mfax-faxserver.md) object.

![faxserver and faxoutboundrouting objects](images/faxoutboundrouting.png)

To create a **FaxOutboundRouting** object in Microsoft Visual Basic, call the [**OutboundRouting**](-mfax-faxserver-outboundrouting.md) property of the [**FaxServer**](-mfax-faxserver.md) object.

To create a **FaxOutboundRouting** object in C++, call the [**OutboundRouting**](-mfax-faxserver-outboundrouting.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxOutboundRouting<br/>                                                    |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> </dl>

 

 





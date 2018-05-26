---
Description: The RoutingInformation property is a null-terminated string that indicates inbound routing information for the fax message.
ms.assetid: 9b4677de-cb69-4ef3-8f63-eb9991bc86ff
title: FaxIncomingMessage.RoutingInformation property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingMessage.RoutingInformation property

The **RoutingInformation** property is a null-terminated string that indicates inbound routing information for the fax message.

This property is read-only.

## Syntax


```VB
Property RoutingInformation As String
```



## Property value

A **String** that receives the inbound routing information for the fax message.

## Remarks

For more information about routing information, see the [**RoutingInfo**](/windows/previous-versions/FaxDev/ns-faxdev-_fax_dev_status?branch=master) member of the **FAX\_DEV\_STATUS** structure.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-incoming-archive.md)
</dt> <dt>

[**FaxIncomingMessage**](-mfax-faxincomingmessage.md)
</dt> <dt>

[**IFaxIncomingMessage**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingmessage?branch=master)
</dt> </dl>

 

 





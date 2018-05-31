---
Description: The GetExtensions method retrieves the collection of inbound routing extensions registered with the fax service.
ms.assetid: ecd9a5bb-1624-4cfe-a2d9-b9a5ed722fc4
title: FaxInboundRouting.GetExtensions method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxInboundRouting.GetExtensions method

The **GetExtensions** method retrieves the collection of inbound routing extensions registered with the fax service.

## Syntax


```VB
FaxInboundRouting.GetExtensions() As FaxInboundRoutingExtensions
```



## Parameters

This method has no parameters.

## Return value

Type: **[**FaxInboundRoutingExtensions**](-mfax-faxinboundroutingextensions.md)\*\***

A [**FaxInboundRoutingExtensions**](-mfax-faxinboundroutingextensions.md) object.

## Remarks

To use this method, a user must have the [****farQUERY\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

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

[**FaxInboundRouting**](-mfax-faxinboundrouting.md)
</dt> </dl>

 

 





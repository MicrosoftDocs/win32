---
Description: The Item property returns a FaxOutboundRoutingGroup object from the FaxOutboundRoutingGroups collection.
ms.assetid: 7e62c037-1fe9-4186-a0aa-d4147b024af7
title: FaxOutboundRoutingGroups.Item property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutboundRoutingGroups.Item property

The Item property returns a [**FaxOutboundRoutingGroup**](-mfax-faxoutboundroutinggroup.md) object from the [**FaxOutboundRoutingGroups**](-mfax-faxoutboundroutinggroups.md) collection.

This property is read-only.

## Syntax


```VB
Property Item( _
  ByVal vIndex As Variant _
) As FaxOutboundRoutingGroup
```



## Property value

A [**FaxOutboundRoutingGroup**](-mfax-faxoutboundroutinggroup.md) object.

## Remarks

To return the group consisting of all of the devices, set *vIndex* equal to the constant [bstrGROUPNAME\_ALLDEVICES](-mfax-bstrgroupname-alldevices.md).

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

[**FaxOutboundRoutingGroups**](-mfax-faxoutboundroutinggroups.md)
</dt> <dt>

[**IFaxOutboundRoutingGroups**](-mfax-faxoutboundroutinggroups-cpp.md)
</dt> </dl>

 

 





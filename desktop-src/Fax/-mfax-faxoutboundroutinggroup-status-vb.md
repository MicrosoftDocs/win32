---
Description: The Status property indicates the collective status of the fax devices in the outbound routing group.
ms.assetid: 9b6493d7-eec2-49f8-93b2-3c8cbcb032c6
title: FaxOutboundRoutingGroup.Status property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutboundRoutingGroup.Status property

The **Status** property indicates the collective status of the fax devices in the outbound routing group.

This property is read-only.

## Syntax


```VB
Property Status As Integer
```



## Property value

[**FAX\_GROUP\_STATUS\_ENUM**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_group_status_enum) description for the status of the devices in the outbound routing group.

## Remarks

When devices are added to or removed from a group, the group's status does not change.

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

[**FaxOutboundRoutingGroup**](-mfax-faxoutboundroutinggroup.md)
</dt> <dt>

[**IFaxOutboundRoutingGroup**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutboundroutinggroup)
</dt> </dl>

 

 





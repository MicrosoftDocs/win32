---
Description: The Remove method removes an item from the FaxOutboundRoutingGroups collection.
ms.assetid: 9d8241ae-4e8e-4c67-a40e-713cb5dfaf41
title: FaxOutboundRoutingGroups.Remove method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutboundRoutingGroups.Remove method

The **Remove** method removes an item from the [**FaxOutboundRoutingGroups**](-mfax-faxoutboundroutinggroups.md) collection.

> [!Note]  
> You cannot remove the special **All Devices** routing group.

 

## Syntax


```VB
FaxOutboundRoutingGroups.Remove( _
  ByVal vIndex As Variant _
) As Long
```



## Parameters

<dl> <dt>

*vIndex* 
</dt> <dd>

Type: **Variant**

[Variant](https://msdn.microsoft.com/windows/desktop/e305240e-9e11-4006-98cc-26f4932d2118) that specifies the item to remove from the collection.

If this parameter is type VT\_I2 or VT\_I4, it specifies the index of the item to remove from the collection. Valid values for this parameter are in the range from 1 to n, where n is the number of objects returned by a call to the [**Count**](-mfax-faxoutboundroutinggroups-count-vb.md) method. The index is 1-based. If this parameter is type VT\_BSTR, the parameter is a unique name that identifies the outbound routing group to remove. Other types are not supported.

</dd> </dl>

## Remarks

To use this method, a user must have the [**farMANAGE\_CONFIG**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

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

[**IFaxOutboundRoutingGroups**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutboundroutinggroups)
</dt> </dl>

 

 





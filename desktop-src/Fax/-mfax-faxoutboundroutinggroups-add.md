---
Description: 'The Add method adds an outbound routing group to the FaxOutboundRoutingGroups collection.'
ms.assetid: '5e65a35a-61cc-4c23-aeb2-406cc7f832ac'
title: 'FaxOutboundRoutingGroups.Add method'
---

# FaxOutboundRoutingGroups.Add method

The **Add** method adds an outbound routing group to the [**FaxOutboundRoutingGroups**](-mfax-faxoutboundroutinggroups.md) collection.

## Syntax


```VB
FaxOutboundRoutingGroups.Add( _
  ByVal bstrName As String, _
  ByVal FaxOutboundRoutingGroup As FaxOutboundRoutingGroup _
) As Long
```



## Parameters

<dl> <dt>

*bstrName* 
</dt> <dd>

Type: **String**

Null-terminated string that indicates the name of the group to add. Note that you cannot add the special **All Devices** routing group.

</dd> <dt>

*FaxOutboundRoutingGroup* 
</dt> <dd>

Type: **[**FaxOutboundRoutingGroup**](-mfax-faxoutboundroutinggroup.md)\*\***

A [**FaxOutboundRoutingGroup**](-mfax-faxoutboundroutinggroup.md) object.

</dd> </dl>

## Remarks

To use this method, a user must have the [**farMANAGE\_CONFIG**](-mfax-fax-access-rights-enum.md) access right.

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

 

 





---
Description: The Remove method removes an outbound routing rule (FaxOutboundRoutingRule object) from the FaxOutboundRoutingRules collection using the routing rule's index.
ms.assetid: 1377b3e1-3480-4e16-964e-c3b143613c5f
title: FaxOutboundRoutingRules.Remove method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutboundRoutingRules.Remove method

The **Remove** method removes an outbound routing rule ([**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md) object) from the [**FaxOutboundRoutingRules**](-mfax-faxoutboundroutingrules.md) collection using the routing rule's index.

## Syntax


```VB
FaxOutboundRoutingRules.Remove( _
  ByVal lIndex As Long _
) As Long
```



## Parameters

<dl> <dt>

*lIndex* 
</dt> <dd>

Type: **Long**

A **Long** value that specifies the index of the outbound routing rule to remove from the collection. Valid values for this parameter are in the range from 1 to n, where n is the number of rules returned by a call to the [**Count**](-mfax-faxoutboundroutingrules-count-vb.md) method.

</dd> </dl>

## Remarks

The default outbound routing rule cannot be removed.

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

[Visual Basic Example](-mfax-creating-and-managing-outbound-routing-rules.md)
</dt> <dt>

[**FaxOutboundRoutingRules**](-mfax-faxoutboundroutingrules.md)
</dt> <dt>

[**IFaxOutboundRoutingRules**](-mfax-faxoutboundroutingrules-cpp.md)
</dt> </dl>

 

 





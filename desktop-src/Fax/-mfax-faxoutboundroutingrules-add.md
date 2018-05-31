---
Description: The Add method adds an outbound routing rule (FaxOutboundRoutingRule object) to the FaxOutboundRoutingRules collection.
ms.assetid: 9046fd0e-29bb-4743-bf78-a90b31c0313f
title: FaxOutboundRoutingRules.Add method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutboundRoutingRules.Add method

The **Add** method adds an outbound routing rule ([**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md) object) to the [**FaxOutboundRoutingRules**](-mfax-faxoutboundroutingrules.md) collection.

## Syntax


```VB
FaxOutboundRoutingRules.Add( _
  ByVal lCountryCode As Long, _
  ByVal lAreaCode As Long, _
  ByVal bUseDevice As Boolean, _
  ByVal bstrGroupName As String, _
  ByVal lDeviceId As Long _
) As FaxOutboundRoutingRule
```



## Parameters

<dl> <dt>

*lCountryCode* 
</dt> <dd>

Type: **Long**

A **Long** value that specifies the country/region code to associate with the outbound routing rule. Specifying [**frrcANY\_CODE**](-mfax-fax-routing-rule-code-enum.md) will add a rule that applies to any country/region code.

</dd> <dt>

*lAreaCode* 
</dt> <dd>

Type: **Long**

Specifies a **Long** value that indicates the area code to associate with the outbound routing rule. Specifying [**frrcANY\_CODE**](-mfax-fax-routing-rule-code-enum.md) will add a rule that applies to any area code within the specified country/region code.

</dd> <dt>

*bUseDevice* 
</dt> <dd>

Type: **Boolean**

Specifies a Boolean value that indicates whether the outbound routing rule points to a single fax device rather than to a group of devices.

</dd> <dt>

*bstrGroupName* 
</dt> <dd>

Type: **String**

Specifies a null-terminated string that contains the name of the outbound routing group to which the new routing rule belongs. If *bUseDevice* is set to **True**, this should be an empty string.

</dd> <dt>

*lDeviceId* 
</dt> <dd>

Type: **Long**

Specifies the device to associate with the outbound routing rule. If *bUseDevice* is set to **False**, this parameter is ignored.

</dd> </dl>

## Return value

Type: **[**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md)\*\***

A [**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md) object.

## Remarks

This method can also return remote procedure call (RPC) return values. For more information, see [RPC Return Values](http://msdn.microsoft.com/library/en-us/rpc/rpc/rpc_return_values.asp).

To read or to write to this property, a user must have the [**farMANAGE\_CONFIG**](-mfax-fax-access-rights-enum.md) access right.

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

 

 





---
Description: The Submit method submits a single fax document to the fax service for processing.
ms.assetid: 50062e89-9e97-43aa-bb60-7ddf6448585d
title: FaxDocument.Submit method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxDocument.Submit method

The **Submit** method submits a single fax document to the fax service for processing.

## Syntax


```VB
FaxDocument.Submit( _
  ByVal bstrFaxServerName As String _
) As Variant
```



## Parameters

<dl> <dt>

*bstrFaxServerName* \[in\]
</dt> <dd>

Type: **String**

**String** that specifies a fax server. If this parameter is **NULL** or an empty string, the local fax server is specified.

</dd> </dl>

## Return value

Type: **Variant\***

**Variant** that specifies a collection of outbound job IDs, one for each recipient of the fax.

## Remarks

You must provide the server name when submitting the document. To submit the document to the local server, set the *bstrFaxServerName* parameter to **Null** or an empty string. The method returns a collection of fax job IDs, one for each recipient of the fax.

To succeed, the **Submit** method requires that the [**FaxDocument**](-mfax-faxdocument.md) object have at least one recipient, and either a cover page or a fax body. You can only use this method if the server (remote or local) is installed as a network printer on the local computer.

This method is not supported for a remote connection to a fax server running Windows XP Home Edition or Windows XP Professional, and will return the error [FAX\_E\_NOT\_SUPPORTED\_ON\_THIS\_SKU](-mfax-fax-error-codes.md).

To use this method, a user must have the [****farSUBMIT\_LOW****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master), [****farSUBMIT\_NORMAL****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master), or [****farSUBMIT\_HIGH****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right, depending on the [**Priority**](-mfax-faxdocument-priority-vb.md) of the fax document.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-broadcasting-a-fax.md)
</dt> <dt>

[**FaxDocument**](-mfax-faxdocument.md)
</dt> <dt>

[**IFaxDocument**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxdocument?branch=master)
</dt> </dl>

 

 





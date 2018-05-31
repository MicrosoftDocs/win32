---
Description: The ConnectedSubmit method submits a single fax document to the connected FaxServer. The method returns an array of fax job ID strings, one for each recipient of the fax.
ms.assetid: 61bf59fd-b921-4356-a3ab-4b83757cc346
title: FaxDocument.ConnectedSubmit method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDocument.ConnectedSubmit method

The **ConnectedSubmit** method submits a single fax document to the connected [**FaxServer**](-mfax-faxserver.md). The method returns an array of fax job ID strings, one for each recipient of the fax.

## Syntax


```VB
FaxDocument.ConnectedSubmit( _
  ByVal FaxServer As FaxServer _
) As Variant
```



## Parameters

<dl> <dt>

*FaxServer* \[in\]
</dt> <dd>

Type: **FaxServer\***

A [**FaxServer**](-mfax-faxserver.md) object that specifies a connected fax server.

</dd> </dl>

## Return value

Type: **Variant\***

**Variant** that holds an array of outbound job ID strings, one for each recipient of the fax.

## Remarks

> [!Note]  
> To succeed, the **ConnectedSubmit** method requires that the [**FaxDocument**](-mfax-faxdocument.md) object have at least one recipient, and either a cover page or a fax body. You can only use this method if the server (remote or local) is installed as a network printer on the local computer.

 

This method is not supported for a remote connection to a fax server running Windows XP Home Edition or Windows XP Professional, and will return the error: [FAX\_E\_NOT\_SUPPORTED\_ON\_THIS\_SKU](-mfax-fax-error-codes.md).

To use this method, a user must have the [**farSUBMIT\_LOW**](-mfax-fax-access-rights-enum.md), [**farSUBMIT\_NORMAL**](-mfax-fax-access-rights-enum.md), or [**farSUBMIT\_HIGH**](-mfax-fax-access-rights-enum.md) access right, depending on the [**Priority**](-mfax-faxdocument-priority-vb.md) of the fax document.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-sending-a-fax.md)
</dt> <dt>

[**FaxDocument**](-mfax-faxdocument.md)
</dt> <dt>

[**IFaxDocument**](-mfax-faxdocument-cpp.md)
</dt> </dl>

 

 





---
Description: The Item method creates a FaxPort object for a specified fax port. The object allows enumeration of port configuration information for a specific connection to a fax server.
ms.assetid: 57b3edfb-e925-461e-a606-a2ce45f33e93
title: FaxPorts.Item property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxPorts.Item property

The **Item** method creates a [FaxPort](-mfax-faxport.md) object for a specified fax port. The object allows enumeration of port configuration information for a specific connection to a fax server.

This property is read-only.

## Syntax


```VB
Property Item( _
  ByVal lCount As Long _
) As Object
```



## Property value

An **Object** that receives a [FaxPort](-mfax-faxport.md) object.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxPorts**](-mfax-faxports-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[FaxPorts](-mfax-faxports.md)
</dt> <dt>

[**Count**](-mfax-ifaxports-get-count-vb.md)
</dt> <dt>

[FaxPort](-mfax-faxport.md)
</dt> <dt>

[**GetPorts**](-mfax-ifaxserver-getports-vb.md)
</dt> </dl>

 

 





---
Description: Retrieves the DocumentSize property for the FaxStatus object of a parent FaxPort object. The DocumentSize property is the size of the fax document associated with the active outbound job on a specific port.
ms.assetid: 6de5b4f4-fa72-4fda-9e01-98343155c89e
title: FaxStatus.DocumentSize property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxStatus.DocumentSize property

Retrieves the **DocumentSize** property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **DocumentSize** property is the size of the fax document associated with the active outbound job on a specific port.

This property is read-only.

## Syntax


```VB
Property DocumentSize As Long
```



## Property value

A **Long** that receives the size, in bytes, of an active outbound fax document.

## Remarks

You can use the **DocumentSize** property of a [FaxStatus](-mfax-faxstatus.md) object in conjunction with the [**DocumentName**](-mfax-ifaxstatus-get-documentname-vb.md) property of the object to inform users about the size of outbound jobs.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxStatus**](-mfax-faxstatus-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxStatus**](-mfax-ifaxstatus.md)
</dt> <dt>

[**DocumentName**](-mfax-ifaxstatus-get-documentname-vb.md)
</dt> <dt>

[**IFaxPorts**](-mfax-ifaxports.md)
</dt> <dt>

[**IFaxPort**](-mfax-ifaxport.md)
</dt> </dl>

 

 





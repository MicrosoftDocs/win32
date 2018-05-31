---
Description: Retrieves the PageCount property for the FaxStatus object of a parent FaxPort object. The PageCount property represents the total number of pages in an outbound fax transmission.
ms.assetid: ae44f8d7-9447-425f-b7c4-fe0208205798
title: FaxStatus.PageCount property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxStatus.PageCount property

Retrieves the **PageCount** property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **PageCount** property represents the total number of pages in an outbound fax transmission.

This property is read-only.

## Syntax


```VB
Property PageCount As Long
```



## Property value

A **Long** that receives the total page count for an outbound fax job on the specified port.

## Remarks

If the page count is not available, the **IFaxStatus::get\_PageCount** method returns zero.

You can use the **PageCount** property of a [FaxStatus](-mfax-faxstatus.md) object in conjunction with the [**CurrentPage**](-mfax-ifaxstatus-get-currentpage-vb.md) property of the object to provide users with a running page count for an outbound fax job. For example, you could inform a user that the fax server is currently transmitting the second page of a four page transmission.

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

[**IFaxStatus**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxstatus)
</dt> <dt>

[**CurrentPage**](-mfax-ifaxstatus-get-currentpage-vb.md)
</dt> <dt>

[**IFaxPorts**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxports)
</dt> <dt>

[**IFaxPort**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxport)
</dt> </dl>

 

 





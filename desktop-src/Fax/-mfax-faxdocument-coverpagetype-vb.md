---
Description: The CoverPageType property is a value from an enumeration that indicates whether a specified cover page template file (.cov) is a server-based cover page file or a local-computer-based cover page file. You can also specify that no file is used.
ms.assetid: 6313301b-06ec-494d-9671-66dc06a2ec1c
title: FaxDocument.CoverPageType property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxDocument.CoverPageType property

The **CoverPageType** property is a value from an enumeration that indicates whether a specified cover page template file (.cov) is a server-based cover page file or a local-computer-based cover page file. You can also specify that no file is used.

This property is read/write.

## Syntax


```VB
Property CoverPageType As Integer
```



## Property value

A variable of type [**FAX\_COVERPAGE\_TYPE\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_coverpage_type_enum?branch=master) that specifies or receives a value indicating whether the cover page template file specified by the **CoverPageType** property is a local computer cover page or a server-based cover page. It can also specify that no file is used. For possible values, see **FAX\_COVERPAGE\_TYPE\_ENUM**.

## Remarks

By default, **CoverPageType** is set to 0, indicating that no file is used.

Provide the name of the cover page in the [**CoverPage**](-mfax-faxdocument-coverpage-vb.md) property.

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

[**IFaxDocument**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxdocument?branch=master)
</dt> </dl>

 

 





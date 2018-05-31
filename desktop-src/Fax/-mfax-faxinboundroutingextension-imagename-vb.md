---
Description: The ImageName property is a null-terminated string that contains the executable image name (DLL path and file name) of the fax routing extension.
ms.assetid: 5b44f833-ce51-416a-830a-9669cdf2a718
title: FaxInboundRoutingExtension.ImageName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxInboundRoutingExtension.ImageName property

The **ImageName** property is a null-terminated string that contains the executable image name (DLL path and file name) of the fax routing extension.

This property is read-only.

## Syntax


```VB
Property ImageName As String
```



## Property value

A **String** that receives the fully qualified path and file name of the fax routing extension's DLL.

## Remarks

The path can include valid environment variables, for example, `%SYSTEMDRIVE%` and `%SYSTEMROOT%`.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-routing-extensions-and-routing-methods.md)
</dt> <dt>

[**FaxInboundRoutingExtension**](-mfax-faxinboundroutingextension.md)
</dt> <dt>

[**IFaxInboundRoutingExtension**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxinboundroutingextension)
</dt> </dl>

 

 





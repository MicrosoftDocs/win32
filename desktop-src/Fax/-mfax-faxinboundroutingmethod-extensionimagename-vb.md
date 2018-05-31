---
Description: The ExtensionImageName property is a null-terminated string that contains the executable image name (DLL path and file name) of the fax routing extension that exports the fax routing method.
ms.assetid: d9da1e49-1572-46d7-99fd-cfe434fb8e16
title: FaxInboundRoutingMethod.ExtensionImageName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxInboundRoutingMethod.ExtensionImageName property

The **ExtensionImageName** property is a null-terminated string that contains the executable image name (DLL path and file name) of the fax routing extension that exports the fax routing method.

This property is read-only.

## Syntax


```VB
Property ExtensionImageName As String
```



## Property value

A **String** that receives the fully qualified path and file name of the fax routing extension DLL that exports the fax routing method.

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

[**FaxInboundRoutingMethod**](-mfax-faxinboundroutingmethod.md)
</dt> <dt>

[**IFaxInboundRoutingMethod**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxinboundroutingmethod)
</dt> </dl>

 

 





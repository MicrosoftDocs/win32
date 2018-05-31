---
Description: The MajorVersion property is a value that specifies the major part of the version number for the fax routing extension's DLL.
ms.assetid: a323cd83-0a12-4e15-8144-6740cea0738f
title: FaxInboundRoutingExtension.MajorVersion property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxInboundRoutingExtension.MajorVersion property

The **MajorVersion** property is a value that specifies the major part of the version number for the fax routing extension's DLL.

This property is read-only.

## Syntax


```VB
Property MajorVersion As Long
```



## Property value

A **Long** that receives the major part of the version number for the DLL.

## Remarks

The standard format for build numbers is MajorVersion.MinorVersion.MajorBuild.MinorBuild.

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

[**IFaxInboundRoutingExtension**](-mfax-faxinboundroutingextension-cpp.md)
</dt> </dl>

 

 





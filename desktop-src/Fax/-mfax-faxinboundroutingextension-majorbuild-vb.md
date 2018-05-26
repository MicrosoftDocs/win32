---
Description: The MajorBuild property is a value that specifies the major part of the build number for the fax routing extensions DLL.
ms.assetid: c588ef7d-0387-468e-95d6-9d89fe447659
title: FaxInboundRoutingExtension.MajorBuild property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxInboundRoutingExtension.MajorBuild property

The **MajorBuild** property is a value that specifies the major part of the build number for the fax routing extension's DLL.

This property is read-only.

## Syntax


```VB
Property MajorBuild As Long
```



## Property value

A **Long** that receives the major part of the build number for the DLL.

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

[**IFaxInboundRoutingExtension**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxinboundroutingextension?branch=master)
</dt> </dl>

 

 





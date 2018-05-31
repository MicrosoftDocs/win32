---
Description: The MinorBuild property is a value that specifies the minor part of the build number for the fax service.
ms.assetid: c94e7dee-1018-4a42-bddc-063dde864794
title: FaxServer.MinorBuild property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxServer.MinorBuild property

The **MinorBuild** property is a value that specifies the minor part of the build number for the fax service.

This property is read-only.

## Syntax


```VB
Property MinorBuild As Long
```



## Property value

A **Long** that receives the minor part of the build number (the decimal portion) for the fax service.

## Remarks

The format for the fax service build number is MajorVersion.MinorVersion.MajorBuild.MinorBuild.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-retrieving-server-properties.md)
</dt> <dt>

[**FaxServer**](-mfax-faxserver.md)
</dt> <dt>

[**IFaxServer**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxserver)
</dt> </dl>

 

 





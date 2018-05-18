---
Description: 'The MajorVersion property is a value that specifies the major part of the version number for the fax service.'
ms.assetid: 'a4f5af45-8f86-4a58-b3cb-bea29b5e3ed7'
title: 'FaxServer.MajorVersion property'
---

# FaxServer.MajorVersion property

The **MajorVersion** property is a value that specifies the major part of the version number for the fax service.

This property is read-only.

## Syntax


```VB
Property MajorVersion As Long
```



## Property value

A **Long** that receives the major part of the version number for the fax service.

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

[**IFaxServer**](-mfax-faxserver-cpp.md)
</dt> </dl>

 

 





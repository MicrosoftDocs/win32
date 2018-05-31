---
Description: The DatabasePath property is a null-terminated string that contains the path to the activity log database file.
ms.assetid: 2861eb8d-150d-4a03-a673-031c06ae78a6
title: FaxActivityLogging.DatabasePath property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxActivityLogging.DatabasePath property

The **DatabasePath** property is a null-terminated string that contains the path to the activity log database file.

This property is read/write.

## Syntax


```VB
Property DatabasePath As String
```



## Property value

A **String** that specifies or receives the fully qualified, null-terminated path of the directory where the activity log database file resides.

## Remarks

> [!Note]  
> If you change the path to the activity log directory, be sure to use a secured directory.

 

To read or write to this property, a user must have the [****farQUERY\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxActivityLogging**](-mfax-faxactivitylogging.md)
</dt> <dt>

[**IFaxActivityLogging**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxactivitylogging)
</dt> </dl>

 

 





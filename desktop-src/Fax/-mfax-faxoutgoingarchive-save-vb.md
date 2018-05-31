---
Description: The Save method saves the FaxOutgoingArchive object data.
ms.assetid: b7262962-489a-4412-96d9-09e5dc41900b
title: FaxOutgoingArchive.Save method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingArchive.Save method

The **Save** method saves the [**FaxOutgoingArchive**](-mfax-faxoutgoingarchive.md) object data.

## Syntax


```VB
FaxOutgoingArchive.Save() As Long
```



## Parameters

This method has no parameters.

## Remarks

> [!Note]  
> In Windows Vista, Windows Server 2008, and later versions of Windows, this method is not supported and returns an error.

 

To use this method, a user must have the [**farMANAGE\_CONFIG**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) and **farQUERY\_CONFIG** access rights.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-outgoing-archive.md)
</dt> <dt>

[**FaxOutgoingArchive**](-mfax-faxoutgoingarchive.md)
</dt> <dt>

[**IFaxOutgoingArchive**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingarchive)
</dt> </dl>

 

 





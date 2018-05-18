---
Description: 'The Refresh method refreshes FaxOutgoingArchive object information from the fax server. When the Refresh method is called, any configuration changes made after the last Save method call are lost.'
ms.assetid: '8a0994c7-b8c3-4219-9f72-47cdc5c7b1fe'
title: 'FaxOutgoingArchive.Refresh method'
---

# FaxOutgoingArchive.Refresh method

The **Refresh** method refreshes [**FaxOutgoingArchive**](-mfax-faxoutgoingarchive.md) object information from the fax server. When the **Refresh** method is called, any configuration changes made after the last [**Save**](-mfax-faxoutgoingarchive-save-vb.md) method call are lost.

## Syntax


```VB
FaxOutgoingArchive.Refresh() As Long
```



## Parameters

This method has no parameters.

## Remarks

> [!Note]  
> In Windows Vista, Windows Server 2008, and later versions of Windows, this method is not supported and returns an error.

 

To use this method, a user must have the [**farQUERY\_CONFIG**](-mfax-fax-access-rights-enum.md) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-opening-a-fax-from-the-outgoing-archive.md)
</dt> <dt>

[**FaxOutgoingArchive**](-mfax-faxoutgoingarchive.md)
</dt> <dt>

[**IFaxOutgoingArchive**](-mfax-faxoutgoingarchive-cpp.md)
</dt> </dl>

 

 





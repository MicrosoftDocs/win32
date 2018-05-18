---
Description: 'The Refresh method refreshes FaxIncomingArchive object information from the fax server. When the Refresh method is called, any configuration changes made after the last Save method call are lost.'
ms.assetid: '840d3caa-9082-4da5-9a77-be8c9e13597b'
title: 'FaxIncomingArchive.Refresh method'
---

# FaxIncomingArchive.Refresh method

The **Refresh** method refreshes [**FaxIncomingArchive**](-mfax-faxincomingarchive.md) object information from the fax server. When the **Refresh** method is called, any configuration changes made after the last [**Save**](-mfax-faxincomingarchive-save-vb.md) method call are lost.

## Syntax


```VB
FaxIncomingArchive.Refresh()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

> [!Note]  
> In Windows Vista, Windows Server 2008, and later versions of Windows, this method is not supported and returns an error.

 

To use this method, a user must have the [****farQUERY\_CONFIG****](-mfax-fax-access-rights-enum.md) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-opening-a-fax-from-the-incoming-archive.md)
</dt> <dt>

[**FaxIncomingArchive**](-mfax-faxincomingarchive.md)
</dt> <dt>

[**IFaxIncomingArchive**](-mfax-faxincomingarchive-cpp.md)
</dt> </dl>

 

 





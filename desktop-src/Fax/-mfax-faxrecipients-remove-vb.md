---
Description: 'The Remove method removes an item from the FaxRecipients collection.'
ms.assetid: '1c68631b-8cca-4109-9431-11983ccc8dba'
title: 'FaxRecipients.Remove method'
---

# FaxRecipients.Remove method

The **Remove** method removes an item from the [**FaxRecipients**](-mfax-faxrecipients.md) collection.

## Syntax


```VB
FaxRecipients.Remove() As Long
```



## Parameters

This method has no parameters.

## Return value

Type: **Long**

A **Long** that specifies the index of the item to remove from the collection. Valid values for this parameter are in the range from 1 to *n*, where *n* is the number of recipients returned by a call to the [**Count**](-mfax-faxrecipients-count-vb.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxRecipients**](-mfax-faxrecipients.md)
</dt> <dt>

[**IFaxRecipients**](-mfax-faxrecipients-cpp.md)
</dt> <dt>

[Broadcasting a Fax](-mfax-broadcasting-a-fax.md)
</dt> </dl>

 

 





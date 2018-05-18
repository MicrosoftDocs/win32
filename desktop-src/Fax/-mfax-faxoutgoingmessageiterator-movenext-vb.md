---
Description: 'The MoveNext method moves the archive cursor to the next fax message in the outbound archive.'
ms.assetid: '300a794f-fa56-4bcb-b66e-a6e8d1d709ec'
title: 'FaxOutgoingMessageIterator.MoveNext method'
---

# FaxOutgoingMessageIterator.MoveNext method

The **MoveNext** method moves the archive cursor to the next fax message in the outbound archive.

## Syntax


```VB
FaxOutgoingMessageIterator.MoveNext() As Long
```



## Parameters

This method has no parameters.

## Remarks

The method will fail if the [**AtEOF**](-mfax-faxoutgoingmessageiterator-ateof-vb.md) property is equal to **True**.

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

[**FaxOutgoingMessageIterator**](-mfax-faxoutgoingmessageiterator.md)
</dt> <dt>

[**IFaxOutgoingMessageIterator**](-mfax-faxoutgoingmessageiterator-cpp.md)
</dt> </dl>

 

 





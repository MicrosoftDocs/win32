---
Description: The SaveDefaultSender method stores information about the default sender from the FaxSender object.
ms.assetid: e77a73b1-19c8-4bc4-9c59-c2e921346ae3
title: FaxSender.SaveDefaultSender method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxSender.SaveDefaultSender method

The **SaveDefaultSender** method stores information about the default sender from the [**FaxSender**](-mfax-faxsender.md) object.

## Syntax


```VB
FaxSender.SaveDefaultSender() As Long
```



## Parameters

This method has no parameters.

## Remarks

To load the default sender information into a [**FaxSender**](-mfax-faxsender.md) object, use the [**LoadDefaultSender**](-mfax-faxsender-loaddefaultsender-vb.md) method.

This method can return remote procedure call (RPC) return values. For more information, see [RPC Return Values](http://msdn.microsoft.com/library/en-us/rpc/rpc/rpc_return_values.asp).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-sending-a-fax.md)
</dt> <dt>

[**FaxSender**](-mfax-faxsender.md)
</dt> <dt>

[**IFaxSender**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxsender)
</dt> </dl>

 

 





---
Description: Returns a FaxAccount object from a IFaxAccounts collection.
ms.assetid: eab831e4-a260-4822-8582-532f7717dab8
title: FaxAccounts.Item property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxAccounts.Item property

Returns a [**FaxAccount**](-mfax-faxaccount.md) object from a [**IFaxAccounts**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccounts) collection.

This property is read-only.

## Syntax


```VB
Property Item( _
  ByVal vIndex As Variant _
) As IFaxAccount
```



## Property value

A variable of type [**IFaxAccount**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccount) that receives the [**FaxAccount**](-mfax-faxaccount.md) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxAccounts**](-mfax-faxaccounts.md)
</dt> <dt>

[**IFaxAccounts**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccounts)
</dt> </dl>

 

 





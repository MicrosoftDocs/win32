---
Description: Returns a FaxAccount object from a IFaxAccounts collection.
ms.assetid: eab831e4-a260-4822-8582-532f7717dab8
title: FaxAccounts.Item property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxAccounts.Item property

Returns a [**FaxAccount**](-mfax-faxaccount.md) object from a [**IFaxAccounts**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccounts?branch=master) collection.

This property is read-only.

## Syntax


```VB
Property Item( _
  ByVal vIndex As Variant _
) As IFaxAccount
```



## Property value

A variable of type [**IFaxAccount**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccount?branch=master) that receives the [**FaxAccount**](-mfax-faxaccount.md) object.

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

[**IFaxAccounts**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccounts?branch=master)
</dt> </dl>

 

 





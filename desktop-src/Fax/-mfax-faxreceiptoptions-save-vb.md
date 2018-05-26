---
Description: The Save method saves the FaxReceiptOptions object data.
ms.assetid: 26941564-4c2e-490e-a9a9-a3b90d3d0301
title: FaxReceiptOptions.Save method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxReceiptOptions.Save method

The **Save** method saves the [**FaxReceiptOptions**](-mfax-faxreceiptoptions.md) object data.

## Syntax


```VB
FaxReceiptOptions.Save() As Long
```



## Parameters

This method has no parameters.

## Remarks

This method is not supported for Windows XP when the receipt type is set to [****frtMAIL****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_receipt_type_enum?branch=master), or if [**UseForInboundRouting**](-mfax-faxreceiptoptions-useforinboundrouting-vb.md) is set to **True**. In these cases, this method will return the error: [FAX\_E\_NOT\_SUPPORTED\_ON\_THIS\_SKU](-mfax-fax-error-codes.md).

To use this method, a user must have the [****farMANAGE\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) and [****farQUERY\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access rights.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxReceiptOptions**](-mfax-faxreceiptoptions.md)
</dt> <dt>

[**IFaxReceiptOptions**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxreceiptoptions?branch=master)
</dt> <dt>

[Setting Receipt Options](-mfax-setting-receipt-options.md)
</dt> </dl>

 

 





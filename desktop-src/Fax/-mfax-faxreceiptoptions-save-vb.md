---
Description: 'The Save method saves the FaxReceiptOptions object data.'
ms.assetid: '26941564-4c2e-490e-a9a9-a3b90d3d0301'
title: 'FaxReceiptOptions.Save method'
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

This method is not supported for Windows XP when the receipt type is set to [****frtMAIL****](-mfax-fax-receipt-type-enum.md), or if [**UseForInboundRouting**](-mfax-faxreceiptoptions-useforinboundrouting-vb.md) is set to **True**. In these cases, this method will return the error: [FAX\_E\_NOT\_SUPPORTED\_ON\_THIS\_SKU](-mfax-fax-error-codes.md).

To use this method, a user must have the [****farMANAGE\_CONFIG****](-mfax-fax-access-rights-enum.md) and [****farQUERY\_CONFIG****](-mfax-fax-access-rights-enum.md) access rights.

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

[**IFaxReceiptOptions**](-mfax-faxreceiptoptions-cpp.md)
</dt> <dt>

[Setting Receipt Options](-mfax-setting-receipt-options.md)
</dt> </dl>

 

 





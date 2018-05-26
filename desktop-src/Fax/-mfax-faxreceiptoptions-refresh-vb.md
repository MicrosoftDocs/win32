---
Description: The Refresh method refreshes FaxReceiptOptions object information from the fax server. When the Refresh method is called, any configuration changes made after the last Save method call are lost.
ms.assetid: 3df8ab53-b0c2-4015-8bba-f05f31aa53f7
title: FaxReceiptOptions.Refresh method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxReceiptOptions.Refresh method

The **Refresh** method refreshes [**FaxReceiptOptions**](-mfax-faxreceiptoptions.md) object information from the fax server. When the **Refresh** method is called, any configuration changes made after the last [**Save**](-mfax-faxreceiptoptions-save-vb.md) method call are lost.

## Syntax


```VB
FaxReceiptOptions.Refresh() As Long
```



## Parameters

This method has no parameters.

## Remarks

To use this method, a user must have the [****farQUERY\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

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
</dt> </dl>

 

 





---
Description: The Refresh method refreshes FaxReceiptOptions object information from the fax server. When the Refresh method is called, any configuration changes made after the last Save method call are lost.
ms.assetid: 3df8ab53-b0c2-4015-8bba-f05f31aa53f7
title: FaxReceiptOptions.Refresh method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

To use this method, a user must have the [****farQUERY\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

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

[**IFaxReceiptOptions**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxreceiptoptions)
</dt> </dl>

 

 





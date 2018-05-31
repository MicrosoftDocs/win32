---
Description: The UseForInboundRouting property sets or retrieves whether to use the FaxReceiptOptions settings for the Microsoft Routing Extension, which allows incoming faxes to be routed to email addresses.
ms.assetid: 8491a5c0-c46e-43a9-ab87-44b5ff03f83e
title: FaxReceiptOptions.UseForInboundRouting property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxReceiptOptions.UseForInboundRouting property

The **UseForInboundRouting** property sets or retrieves whether to use the [**FaxReceiptOptions**](-mfax-faxreceiptoptions.md) settings for the Microsoft Routing Extension, which allows incoming faxes to be routed to email addresses.

This property is read/write.

## Syntax


```VB
Property UseForInboundRouting  As Boolean
```



## Property value

A **Boolean** that specifies or receives whether to use the [**FaxReceiptOptions**](-mfax-faxreceiptoptions.md) settings for the Microsoft Routing Extension.

## Remarks

If the settings are not used (property is set to **False**), then the Microsoft Routing Extension is disabled, and users will not be able to receive faxes to email addresses. If the settings are used (property is set to **True**), then the Microsoft Routing Extension is enabled, and users will be able to receive faxes to email addresses.

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

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
</dt> <dt>

[Setting Receipt Options](-mfax-setting-receipt-options.md)
</dt> </dl>

 

 





---
Description: Sets the copy count.
ms.assetid: DF788C8F-DA60-47F1-83DB-2E1947E41142
title: IPrintSchemaTicket::JobCopiesAllDocuments property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintSchemaTicket::JobCopiesAllDocuments property

Sets the copy count.

This property is write-only.

## Syntax


```C++
HRESULT put_JobCopiesAllDocuments(
  [in] ULONG ulJobCopiesAllDocuments
);
```



## Property value

The copy count.

## Error codes

Returns an **HRESULT** value. If the property call was not successful, it returns the appropriate **HRESULT** error code.

## Remarks

Be aware of the fact that the [**IPrintSchemaTicket::GetCapabilities**](iprintschematicket-getcapabilities.md) method retrieves a new PrintCapabilities document, which it also caches every time it is invoked. This means that if you use **IPrintSchemaTicket::put\_JobCopiesAllDocuments** or [**IPrintSchemaFeature::SelectedOption**](iprintschemafeature-put-selectedoption.md) on PrintTicket, the cached PrintCapabilities document gets corrupted or modified and the cache will be purged.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchemaTicket**](iprintschematicket-interface.md)
</dt> <dt>

[**IPrintSchemaFeature::SelectedOption**](iprintschemafeature-put-selectedoption.md)
</dt> <dt>

[**IPrintSchemaTicket::GetCapabilities**](iprintschematicket-getcapabilities.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaTicket::JobCopiesAllDocuments%20property%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")






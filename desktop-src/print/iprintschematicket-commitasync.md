---
Description: 'Gets an asynchronous PrintTicket commit operation context.'
ms.assetid: 'CFEDCABF-A875-4A69-954D-267765350E9D'
title: 'IPrintSchemaTicket::CommitAsync method'
---

# IPrintSchemaTicket::CommitAsync method

Gets an asynchronous PrintTicket commit operation context.

## Syntax


```C++
HRESULT CommitAsync(
  [in]  IPrintSchemaTicket         *pPrintTicketCommit,
  [out] IPrintSchemaAsyncOperation **ppAsyncOperation
);
```



## Parameters

<dl> <dt>

*pPrintTicketCommit* \[in\]
</dt> <dd>

The print ticket to commit.

</dd> <dt>

*ppAsyncOperation* \[out\]
</dt> <dd>

The asynchronous commit operation context.

</dd> </dl>

## Return value

This method returns an **HRESULT** value.

## Remarks

To perform the commit operation, call the [**IPrintSchemaAsyncOperation::Start**](iprintschemaasyncoperation-start.md) method to validate the given *pPrintTicketCommit* and then apply the validated PrintTicket settings to the current PrintTicket object. When the commit operation is completed or if an error occurs during the commit operation, the [**IPrintSchemaAsyncOperationEvent::Completed**](iprintschemaasyncoperationevent-completed.md) event is fired.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchemaTicket**](iprintschematicket-interface.md)
</dt> <dt>

[**IPrintSchemaAsyncOperation::Start**](iprintschemaasyncoperation-start.md)
</dt> <dt>

[**IPrintSchemaAsyncOperationEvent::Completed**](iprintschemaasyncoperationevent-completed.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaTicket::CommitAsync%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")






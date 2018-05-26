---
Description: Is called when asynchronous PrintSchema operation that is represented by an IPrintSchemaAsyncOperation context is completed.
ms.assetid: B1599F21-D6DD-497D-9CD8-6C637ABAA33A
title: IPrintSchemaAsyncOperationEventCompleted method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintSchemaAsyncOperationEvent::Completed method

Is called when asynchronous PrintSchema operation that is represented by an [**IPrintSchemaAsyncOperation**](iprintschemaasyncoperation-interface.md) context is completed.

## Syntax


```C++
HRESULT Completed(
  [in] IPrintSchemaTicket *pTicket,
  [in] HRESULT            hrOperation
);
```



## Parameters

<dl> <dt>

*pTicket* \[in\]
</dt> <dd>

The print ticket.

</dd> <dt>

*hrOperation* \[in\]
</dt> <dd>

The result of the completed operation.

</dd> </dl>

## Return value

This method returns an **HRESULT** value.

## Remarks

The print ticket passed to the **Completed** method is the final validated, merged, or committed print ticket.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Version<br/>         | Windows 8<br/>                                                                          |
| Header<br/>          | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchemaAsyncOperationEvent**](iprintschemaasyncoperationevent-interface.md)
</dt> <dt>

[**IPrintSchemaTicket**](iprintschematicket-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaAsyncOperationEvent::Completed%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")






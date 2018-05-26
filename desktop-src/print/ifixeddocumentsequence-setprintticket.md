---
Description: The SetPrintTicket method inserts a print ticket into the fixed document sequence.
ms.assetid: 636db99c-9195-4476-b1a6-a8067f27c6bd
title: IFixedDocumentSequenceSetPrintTicket method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IFixedDocumentSequence::SetPrintTicket method

The **SetPrintTicket** method inserts a print ticket into the fixed document sequence.

## Syntax


```C++
HRESULT SetPrintTicket(
  [in] IPartPrintTicket *pPrintTicket
);
```



## Parameters

<dl> <dt>

*pPrintTicket* \[in\]
</dt> <dd>

A pointer to the print ticket to be inserted.

</dd> </dl>

## Return value

**SetPrintTicket** returns an **HRESULT** value.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IFixedDocumentSequence::SetPrintTicket%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





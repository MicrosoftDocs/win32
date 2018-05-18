---
title: IVMSerialPortCollection Item property
description: The Item property contains the IVMSerialPort object that corresponds to the given index in this collection.
ms.assetid: '4c81c810-b421-468f-811c-28e257df63f9'
keywords: ["Item property Virtual Server", "Item property Virtual Server , IVMSerialPortCollection interface", "IVMSerialPortCollection interface Virtual Server , Item property", "Item property Virtual Server , VMSerialPortCollection interface", "VMSerialPortCollection interface Virtual Server , Item property"]
topic_type:
- apiref
api_name:
- IVMSerialPortCollection.Item
- IVMSerialPortCollection.get_Item
- VMSerialPortCollection.Item
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMSerialPortCollection::Item property

The **Item** property contains the [**IVMSerialPort**](ivmserialport.md) object that corresponds to the given index in this collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]  long          index,
  [out] IVMSerialPort **serialPort
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VMSerialPortCollection.Item( _
  ByVal index, _
  ByRef serialPort _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**IVMSerialPort**](ivmserialport.md) object found at the given index.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                                                                       |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>                                                      |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *serialPort* parameter is **NULL**.<br/>                                            |
| <dl> <dt>DISP\_E\_BADINDEX</dt> </dl>   | The index of the requested item does not correspond to an item in this collection.<br/> |
| <dl> <dt> VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                                                      |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>  | An unexpected error occurred.<br/>                                                      |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMSerialPortCollection**](ivmserialportcollection.md)
</dt> </dl>

 

 






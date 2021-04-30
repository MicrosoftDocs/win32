---
description: Fills an array of pointers to IWiaItem2 interfaces.
ms.assetid: 35fd5bdf-7e6c-431f-a9c6-62a86ee05f95
title: IEnumWiaItem2::Next method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEnumWiaItem2.Next
api_type: 
- COM
api_location: 
- Wia.h
---

# IEnumWiaItem2::Next method

Fills an array of pointers to [**IWiaItem2**](-wia-iwiaitem2.md) interfaces.

## Syntax


```C++
HRESULT Next(
  [in]      ULONG     cElt,
  [out]     IWiaItem2 **ppIWiaItem2,
  [in, out] ULONG     *pcEltFetched
);
```



## Parameters

<dl> <dt>

*cElt* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the number of array elements in the array indicated by the *ppIWiaItem2* parameter.

</dd> <dt>

*ppIWiaItem2* \[out\]
</dt> <dd>

Type: **[**IWiaItem2**](-wia-iwiaitem2.md)\*\***

Receives the address of an array of [**IWiaItem2**](-wia-iwiaitem2.md) interface pointers. **IEnumWiaItem2::Next** fills this array with interface pointers.

</dd> <dt>

*pcEltFetched* \[in, out\]
</dt> <dd>

Type: **ULONG\***

On output, this parameter receives the number of interface pointers actually stored in the array indicated by the *ppIWiaItem2* parameter. When the enumeration is complete, this parameter contains zero.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The Windows Image Acquisition (WIA) 2.0 run-time system represents WIA 2.0 hardware devices as a hierarchical tree of [**IWiaItem2**](-wia-iwiaitem2.md) objects. Applications use the **IEnumWiaItem2::Next** method to obtain an **IWiaItem2** interface pointer for each item in the current folder of a hardware device's **IWiaItem2** object tree.

To obtain the list of pointers, the application passes an array of [**IWiaItem2**](-wia-iwiaitem2.md) interface pointers that it allocates. It also passes the number of array elements in the parameter *cElt*. The **IEnumWiaItem2::Next** method fills the array with pointers to **IWiaItem2** interfaces.

Until the enumeration process completes, the **IEnumWiaItem2::Next** method returns S\_OK. Each time it does, it sets the value pointed to by *pcEltFetched* to the number of items it inserted into the array. When **IEnumWiaItem2::Next** finishes the process of enumerating [**IWiaItem2**](-wia-iwiaitem2.md) objects, it returns S\_FALSE and sets the memory location pointed to by *pcEltFetched* to zero.

Applications must call the [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) method on the interface pointers they receive through the *ppIWiaItem2* parameter.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 

---
description: The IWiaItem2::EnumRegisterEventInfo method creates an enumerator that you can use to obtain information about events for which an application is registered.
ms.assetid: 9c25e9ae-bd3e-46a6-b4c2-c0bbcd265d51
title: IWiaItem2::EnumRegisterEventInfo method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaItem2.EnumRegisterEventInfo
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaItem2::EnumRegisterEventInfo method

The **IWiaItem2::EnumRegisterEventInfo** method creates an enumerator that you can use to obtain information about events for which an application is registered.

## Syntax


```C++
HRESULT EnumRegisterEventInfo(
  [in]        LONG              lFlags,
  [in]  const GUID              *pEventGUID,
  [out]       IEnumWIA_DEV_CAPS **ppIEnum
);
```



## Parameters

<dl> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Not used. Set to 0.

</dd> <dt>

*pEventGUID* \[in\]
</dt> <dd>

Type: **const GUID\***

Pointer to an identifier that specifies the hardware event for which you want to obtain registration information.

</dd> <dt>

*ppIEnum* \[out\]
</dt> <dd>

Type: **[**IEnumWIA\_DEV\_CAPS**](/windows/desktop/api/wia_xp/nn-wia_xp-ienumwia_dev_caps)\*\***

The address of a pointer to the [**IEnumWIA\_DEV\_CAPS**](/windows/desktop/api/wia_xp/nn-wia_xp-ienumwia_dev_caps) interface.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

An application calls this method to create an enumerator object for the event information. **IWiaItem2::EnumRegisterEventInfo** stores the address of the [**IEnumWIA\_DEV\_CAPS**](/windows/desktop/api/wia_xp/nn-wia_xp-ienumwia_dev_caps) interface of the enumerator object in the *ppIEnum* parameter. The program then uses the interface pointer to enumerate the properties of the event for which it is registered.

Applications must call the [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) method on the interface pointers that they receive through the *ppIEnum* parameter.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl> |



 

 

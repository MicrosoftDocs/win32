---
description: Windows Imaging Component (WIC) proxy function for IPropertyBag2::Write.
ms.assetid: b97caba6-298a-4b36-9f39-9b5440b866c3
title: IPropertyBag2_Write_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPropertyBag2_Write_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IPropertyBag2\_Write\_Proxy function

Windows Imaging Component (WIC) proxy function for IPropertyBag2::Write.

## Syntax


```C++
HRESULT IPropertyBag2_Write_Proxy(
  _In_ IPropertyBag2 *THIS_PTR,
  _In_ ULONG         cProperties,
  _In_ PROPBAG2      *ppropBag,
  _In_ VARIANT       *pvarValue
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[IPropertyBag2](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768192(v=vs.85))\***

PARAMDESC

</dd> <dt>

*cProperties* \[in\]
</dt> <dd>

Type: **ULONG**

</dd> <dt>

*ppropBag* \[in\]
</dt> <dd>

Type: **[PROPBAG2](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768188(v=vs.85))\***

</dd> <dt>

*pvarValue* \[in\]
</dt> <dd>

Type: **VARIANT\***

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 


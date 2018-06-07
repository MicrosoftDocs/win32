---
Description: Windows Imaging Component (WIC) proxy function for IPropertyBag2::Write.
ms.assetid: b97caba6-298a-4b36-9f39-9b5440b866c3
title: IPropertyBag2\_Write\_Proxy function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[IPropertyBag2](http://msdn.microsoft.com/en-us/library/Aa768192(VS.85).aspx)\***

PARAMDESC

</dd> <dt>

*cProperties* \[in\]
</dt> <dd>

Type: **ULONG**

</dd> <dt>

*ppropBag* \[in\]
</dt> <dd>

Type: **[PROPBAG2](http://msdn.microsoft.com/en-us/library/Aa768188(VS.85).aspx)\***

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



|                                     |                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 





---
description: Determines whether an input device supports multitouch.
ms.assetid: 4fef7060-2235-4bee-a37b-40d827732b30
title: ITablet3::IsMultiTouch method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITablet3.IsMultiTouch
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITablet3::IsMultiTouch method

Determines whether an input device supports multitouch.

## Syntax


```C++
HRESULT IsMultiTouch(
  [out] BOOL *bIsMultiTouch
);
```



## Parameters

<dl> <dt>

*bIsMultiTouch* \[out\]
</dt> <dd>

Indicates whether the device is multitouch.

</dd> </dl>

## Return value

Returns **S\_OK** on success, otherwise returns an error code such as **E\_FAIL**.

## Remarks

After determining through [**IRealTimeStylus3::MultiTouchEnabled**](/windows/desktop/api/rtscom/nf-rtscom-irealtimestylus3-get_multitouchenabled) or **ITablet3::IsMultiTouch** that multitouch is available, an application may choose to opt in for multitouch input messages. Additional information on filtering multitouch methods is available in the **IRealTimeStylus3::MultiTouchEnabled** property section.

## Examples


```C++
CComQIPtr<ITablet3> spITablet3 = g_spITablet3;
VARIANT_BOOL b;
spITablet3->get_IsMultiTouch(&b);
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



## See also

<dl> <dt>

[**ITablet3**](itablet3.md)
</dt> <dt>

[**MultiTouchEnabled**](/windows/desktop/api/rtscom/nf-rtscom-irealtimestylus3-get_multitouchenabled)
</dt> </dl>

 

 





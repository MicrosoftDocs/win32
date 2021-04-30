---
title: MM_ACM_FORMATCHOOSE message (Msacm.h)
description: The MM\_ACM\_FORMATCHOOSE message notifies an acmFormatChoose dialog hook function before adding an element to one of the three drop-down list boxes.
ms.assetid: f77e41c6-14e9-45c0-971e-4d6325145f1c
keywords:
- MM_ACM_FORMATCHOOSE message Windows Multimedia
topic_type:
- apiref
api_name:
- MM_ACM_FORMATCHOOSE
api_location:
- Msacm.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MM\_ACM\_FORMATCHOOSE message

The **MM\_ACM\_FORMATCHOOSE** message notifies an [**acmFormatChoose**](/windows/desktop/api/Msacm/nf-msacm-acmformatchoose) dialog hook function before adding an element to one of the three drop-down list boxes. This message allows an application to further customize the selections available through the user interface.


```C++
MM_ACM_FORMATCHOOSE 
wParam = (WPARAM) wDropDown 
lParam = (LONG) lCustom 
```



## Parameters

<dl> <dt>

<span id="wDropDown"></span><span id="wdropdown"></span><span id="WDROPDOWN"></span>*wDropDown*
</dt> <dd>

Drop-down list box being initialized and a verify or add operation.



| Requirement | Value |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FORMATCHOOSE\_CUSTOM\_VERIFY    | The *lParam* parameter is a pointer to a [**WAVEFORMATEX**](/windows/win32/api/mmeapi/ns-mmeapi-waveformatex) structure to be added to the custom Name drop-down list box.                                                                                                   |
| FORMATCHOOSE\_FORMAT\_ADD       | The *lParam* parameter is a pointer to a buffer that will accept a [**WAVEFORMATEX**](/windows/win32/api/mmeapi/ns-mmeapi-waveformatex) structure to be added to the Format drop-down list box. The application must copy the format structure to be added into this buffer. |
| FORMATCHOOSE\_FORMAT\_VERIFY    | The *lParam* parameter is a pointer to a [**WAVEFORMATEX**](/windows/win32/api/mmeapi/ns-mmeapi-waveformatex) structure to be added to the Format drop-down list box.                                                                                                        |
| FORMATCHOOSE\_FORMATTAG\_ADD    | The *lParam* parameter is a pointer to a variable that will accept a waveform-audio format tag to be added to the Format Tag drop-down list box.                                                                                             |
| FORMATCHOOSE\_FORMATTAG\_VERIFY | The *lParam* parameter is a waveform-audio format tag to be listed in the Format Tag drop-down list box.                                                                                                                                     |



 

</dd> <dt>

<span id="lCustom"></span><span id="lcustom"></span><span id="LCUSTOM"></span>*lCustom*
</dt> <dd>

Value defined by the listbox specified in the **wParam** parameter.

</dd> </dl>

## Return Value

Returns **TRUE** if an application handles this message or **FALSE** otherwise.

## Remarks

If the application processes the FILTERCHOOSE\_FORMAT\_ADD operation, the size of the memory buffer supplied in *lParam* will be determined from the [**acmMetrics**](/windows/desktop/api/Msacm/nf-msacm-acmmetrics) function.

If your application is processing a verify operation, it can prevent the dialog box from listing this selection by calling the **SetWindowLong** function with *nIndex* set to DWL\_MSGRESULT and *lNewLong* set to **FALSE** (cast to a **LONG** data type). To allow the dialog box to list this selection, call this function with *lNewLong* set to **TRUE**.

If your application is processing an add operation, it can indicate that no more additions are required by calling the **SetWindowLong** function with *nIndex* set to DWL\_MSGRESULT and *lNewLong* set to **FALSE** (cast to a **LONG** data type). To indicate more additions are required, call this function with *lNewLong* set to **TRUE**.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Msacm.h</dt> </dl> |



## See also

<dl> <dt>

[Audio Compression Manager](audio-compression-manager.md)
</dt> <dt>

[Audio Compression Messages](audio-compression-messages.md)
</dt> </dl>

 


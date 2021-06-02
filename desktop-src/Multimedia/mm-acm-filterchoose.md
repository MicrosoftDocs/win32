---
title: MM_ACM_FILTERCHOOSE message (Msacm.h)
description: The MM\_ACM\_FILTERCHOOSE message notifies an acmFilterChoose dialog box hook function before adding an element to one of the three drop-down list boxes.
ms.assetid: f3c68240-a9aa-4771-96b9-1cb3bb5ea906
keywords:
- MM_ACM_FILTERCHOOSE message Windows Multimedia
topic_type:
- apiref
api_name:
- MM_ACM_FILTERCHOOSE
api_location:
- Msacm.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MM\_ACM\_FILTERCHOOSE message

The **MM\_ACM\_FILTERCHOOSE** message notifies an [**acmFilterChoose**](/windows/desktop/api/Msacm/nf-msacm-acmfilterchoose) dialog box hook function before adding an element to one of the three drop-down list boxes. This message allows an application to further customize the selections available through the user interface.


```C++
        MM_ACM_FILTERCHOOSE
        wParam = (WPARAM) wDropDown
        lParam = (LONG) lCustom
      
```



## Parameters

<dl> <dt>

<span id="wDropDown"></span><span id="wdropdown"></span><span id="WDROPDOWN"></span>*wDropDown*
</dt> <dd>

Drop-down list box being initialized and a verify or add operation.



| Requirement | Value |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FILTERCHOOSE\_CUSTOM\_VERIFY    | The *lParam* parameter is a pointer to a [**WAVEFILTER**](/windows/desktop/api/Mmreg/ns-mmreg-wavefilter) structure to be added to the custom Name drop-down list box.                                                                                                   |
| FILTERCHOOSE\_FILTER\_ADD       | The *lParam* parameter is a pointer to a buffer that will accept a [**WAVEFILTER**](/windows/desktop/api/Mmreg/ns-mmreg-wavefilter) structure to be added to the Filter drop-down list box. The application must copy the filter structure to be added into this buffer. |
| FILTERCHOOSE\_FILTER\_VERIFY    | The *lParam* parameter is a pointer to a [**WAVEFILTER**](/windows/desktop/api/Mmreg/ns-mmreg-wavefilter) structure to be added to the Filter drop-down list box.                                                                                                        |
| FILTERCHOOSE\_FILTERTAG\_ADD    | The *lParam* parameter is a pointer to a **DWORD** that will accept a waveform-audio filter tag to be added to the Filter Tag drop-down list box.                                                                                        |
| FILTERCHOOSE\_FILTERTAG\_VERIFY | The *lParam* parameter is a waveform-audio filter tag to be listed in the Filter Tag drop-down list box.                                                                                                                                 |



 

</dd> <dt>

<span id="lCustom"></span><span id="lcustom"></span><span id="LCUSTOM"></span>*lCustom*
</dt> <dd>

Value defined by the list box specified in the **wParam** parameter.

</dd> </dl>

## Return Value

Returns **TRUE** if an application handles this message or **FALSE** otherwise.

## Remarks

If the application processes the FILTERCHOOSE\_FILTER\_ADD operation, the size of the memory buffer supplied in *lParam* will be determined from the [**acmMetrics**](/windows/desktop/api/Msacm/nf-msacm-acmmetrics) function.

If the application processes a verify operation, the application must precede the return value with **SetWindowLong** (hwnd, DWL\_MSGRESULT, (LONG) **FALSE**) to prevent the dialog box from listing this selection or with **SetWindowLong** (hwnd, DWL\_MSGRESULT, (LONG)**TRUE**) to allow the dialog box to list this selection. If processing an add operation, the application must precede the return with **SetWindowLong** (hwnd, DWL\_MSGRESULT, (LONG)**FALSE**) to indicate that no more additions are required or with **SetWindowLong** (hwnd, DWL\_MSGRESULT, (LONG)**TRUE**) if more additions are required.

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

 

 






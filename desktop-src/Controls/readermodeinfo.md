---
title: READERMODEINFO structure
description: Contains information required to initialize the DoReaderMode function.
ms.assetid: 7b9c73bc-b093-4592-befd-67508fb86fe0
keywords:
- READERMODEINFO structure Windows Controls
- PREADERMODEINFO structure pointer Windows Controls
topic_type:
- apiref
api_name:
- READERMODEINFO
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# READERMODEINFO structure

\[**READERMODEINFO** is supported through Windows XP with Service Pack 2 (SP2). It might be unsupported in subsequent versions.\]

Contains information required to initialize the [**DoReaderMode**](doreadermode.md) function.

## Syntax


```C++
typedef struct tagReaderModeInfo {
  UINT                       cbSize;
  HWND                       hwnd;
  DWORD                      fFlags;
  LPRECT                     prc;
  PFNREADERSCROLL            pfnScroll;
  PFNREADERTRANSLATEDISPATCH fFlags;
  LPARAM                     lParam;
} READERMODEINFO, *PREADERMODEINFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Required. The size of the structure, in bytes. Set this parameter to **sizeof(READERMODE)** before you call [**DoReaderMode**](doreadermode.md).

</dd> <dt>

**hwnd**
</dt> <dd>

Type: **[**HWND**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Required. The handle of the window to be used for reader mode.

</dd> <dt>

**fFlags**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Flags customizing the functionality of the reader mode window. This parameter can be 0; otherwise, one or more of the following values.



| Value                                                                                                                                                                                                                                  | Meaning                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RMF_ZEROCURSOR"></span><span id="rmf_zerocursor"></span><dl> <dt>**RMF\_ZEROCURSOR**</dt> <dt>0x01</dt> </dl>             | Sets the cursor in the center of the area specified in **prc**. If this flag is not specified, the cursor position remains unchanged.<br/> |
| <span id="RMF_VERTICALONLY"></span><span id="rmf_verticalonly"></span><dl> <dt>**RMF\_VERTICALONLY**</dt> <dt>0x02</dt> </dl>       | Allows only vertical scrolling.<br/>                                                                                                       |
| <span id="RMF_HORIZONTALONLY"></span><span id="rmf_horizontalonly"></span><dl> <dt>**RMF\_HORIZONTALONLY**</dt> <dt>0x04</dt> </dl> | Allows only horizontal scrolling.<br/>                                                                                                     |



 

</dd> <dt>

**prc**
</dt> <dd>

Type: **LPRECT**

</dd> <dd>

A pointer to a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure that specifies the scrolling area in the reader mode window. If this member is **NULL**, then the entire window is used as the scrolling area.

</dd> <dt>

**pfnScroll**
</dt> <dd>

Type: **PFNREADERSCROLL**

</dd> <dd>

A pointer to an application-defined [*ReaderScroll*](readerscroll.md) callback function used to notify the application that the window needs to be scrolled in a particular direction.

</dd> <dt>

**fFlags**
</dt> <dd>

Type: **PFNREADERTRANSLATEDISPATCH**

</dd> <dd>

A pointer to an application-defined [*TranslateDispatch*](translatedispatch.md) callback function used to get first notification of any messages sent to the reader mode window.

</dd> <dt>

**lParam**
</dt> <dd>

Type: **[**LPARAM**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Additional information as needed by the application, read by the caller in the [*ReaderScroll*](readerscroll.md) callback function.

</dd> </dl>

## Remarks

This structure is not declared in any public header. To use it, you must include the declaration shown above in your own header.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows Vista \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>          |



 


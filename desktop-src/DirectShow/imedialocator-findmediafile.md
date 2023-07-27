---
description: The FindMediaFile method searches for a file and, if successful, retrieves the path to the file.
ms.assetid: ddfa2c75-e51f-4aad-afe6-8a60c46e8d35
title: IMediaLocator::FindMediaFile method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMediaLocator.FindMediaFile
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IMediaLocator::FindMediaFile method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `FindMediaFile` method searches for a file and, if successful, retrieves the path to the file.

## Syntax


```C++
HRESULT FindMediaFile(
   BSTR Input,
   BSTR FilterString,
   BSTR *pOutput,
   long Flags
);
```



## Parameters

<dl> <dt>

*Input* 
</dt> <dd>

File name, including path, where the file was last known to reside. For source objects in the timeline, use the current media name.

</dd> <dt>

*FilterString* 
</dt> <dd>

A **BSTR** containing pairs of filter strings, formatted as required by the **lpstrFilter** member of the [**OPENFILENAME**](/windows/win32/api/commdlg/ns-commdlg-openfilenamea) structure. The media locator uses this filter if it displays a File Open dialog box. The value can be **NULL** if the *Flags* parameter does not include the SFN\_VALIDATEF\_POPUP flag.

</dd> <dt>

*pOutput* 
</dt> <dd>

Pointer to a variable that receives the actual path to the file, if it differs from the value contained in *Input* and if the method successfully locates the file.

</dd> <dt>

*Flags* 
</dt> <dd>

Bitwise combination of zero or more flags. For a list of possible flags, see [**File Name Validation Flags**](file-name-validation-flags.md).

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The filter string for the File Open dialog, which is specified by the *FilterString* parameter, contains internal Null characters. For example, Video\\0\*.avi\\0\\0 is a valid filter string. You cannot use the **SysAllocStr** function to allocate the BSTR, because that function expects a Null-terminated string and will truncate the string at the first Null character. Therefore, use a function such as **SysAllocStringLen**, which includes an explicit parameter for the length:


```C++
BSTR filter = SysAllocStringLen(L"Video\0*.avi\0", 12);
// Note: SysAllocStringLen appends an additional '\0' to the string.
```



If the user cancels the File Open dialog, the method returns E\_FAIL.

The method allocates memory for the **BSTR** in *pOutput*. The application must call **SysFreeString** to free the memory.

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IMediaLocator Interface**](imedialocator.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 

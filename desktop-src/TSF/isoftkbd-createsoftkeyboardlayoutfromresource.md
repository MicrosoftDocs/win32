---
title: ISoftKbd CreateSoftKeyboardLayoutFromResource method (Softkbdc.h)
description: The ISoftKbd CreateSoftKeybboardLayoutFromResource method creates a soft keyboard layout from the specified resource.
ms.assetid: c1b2f8bd-8065-426d-9c23-67fa46a33dc8
keywords:
- CreateSoftKeyboardLayoutFromResource method Text Services Framework
- CreateSoftKeyboardLayoutFromResource method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , CreateSoftKeyboardLayoutFromResource method
topic_type:
- apiref
api_name:
- ISoftKbd.CreateSoftKeyboardLayoutFromResource
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::CreateSoftKeyboardLayoutFromResource method

The **ISoftKbd::CreateSoftKeybboardLayoutFromResource** method creates a soft keyboard layout from the specified resource.

## Syntax


```C++
HRESULT CreateSoftKeyboardLayoutFromResource(
  [in]  WCHAR *lpszResFile,
  [in]  WCHAR *lpszResType,
  [in]  WCHAR *lpszXMLResString,
  [out] DWORD *lpdwLayoutCookie
);
```



## Parameters

<dl> <dt>

*lpszResFile* \[in\]
</dt> <dd>

Pointer to a zero-terminated string indicating the name of the resource file.

</dd> <dt>

*lpszResType* \[in\]
</dt> <dd>

Pointer to a zero-terminated string indicating the type of resource.

</dd> <dt>

*lpszXMLResString* \[in\]
</dt> <dd>

Pointer to a zero-terminated string identifying the resource.

</dd> <dt>

*lpdwLayoutCookie* \[out\]
</dt> <dd>

Pointer to the buffer in which this method retrieves a soft keyboard layout cookie.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                        | Description                                    |
|----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method was successful.<br/>          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | One or more parameters are invalid.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                        |
| Header<br/>                   | <dl> <dt>Softkbdc.h</dt> </dl>  |
| IDL<br/>                      | <dl> <dt>Softkbd.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Softkbd.dll</dt> </dl> |



## See also

<dl> <dt>

[**ISoftKbd**](isoftkbd.md)
</dt> <dt>

[**ISoftKbd::CreateSoftKeyboardLayoutFromXMLFile**](isoftkbd-createsoftkeyboardlayoutfromxmlfile.md)
</dt> <dt>

[**ISoftKbd::ShowSoftKeyboard**](isoftkbd-showsoftkeyboard.md)
</dt> </dl>

 

 






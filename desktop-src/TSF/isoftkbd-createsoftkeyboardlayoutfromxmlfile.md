---
title: ISoftKbd CreateSoftKeyboardLayoutFromXMLFile method (Softkbdc.h)
description: The ISoftKbd CreateSoftKeyboardLayoutFromXMLFile method creates a soft keyboard layout from the specified XML file.
ms.assetid: e665adab-1d75-4e41-87bf-c8ce0f7a0399
keywords:
- CreateSoftKeyboardLayoutFromXMLFile method Text Services Framework
- CreateSoftKeyboardLayoutFromXMLFile method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , CreateSoftKeyboardLayoutFromXMLFile method
topic_type:
- apiref
api_name:
- ISoftKbd.CreateSoftKeyboardLayoutFromXMLFile
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::CreateSoftKeyboardLayoutFromXMLFile method

The **ISoftKbd::CreateSoftKeyboardLayoutFromXMLFile** method creates a soft keyboard layout from the specified XML file.

## Syntax


```C++
HRESULT CreateSoftKeyboardLayoutFromXMLFile(
  [in]  WCHAR *lpszKeyboardDesFile,
  [in]  INT   szFileStrLen,
  [out] DWORD *pdwLayoutCookie
);
```



## Parameters

<dl> <dt>

*lpszKeyboardDesFile* \[in\]
</dt> <dd>

Pointer to a zero-terminated string indicating the name of the XML file.

</dd> <dt>

*szFileStrLen* \[in\]
</dt> <dd>

Zero-terminated string indicating the length of the XML file.

</dd> <dt>

*pdwLayoutCookie* \[out\]
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

[**ISoftKbd::CreateSoftKeyboardLayoutFromResource**](isoftkbd-createsoftkeyboardlayoutfromresource.md)
</dt> </dl>

 

 






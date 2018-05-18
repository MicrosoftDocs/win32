---
Description: 'The CreateStream method copies the source of a manifest or module into a stream.'
ms.assetid: '3b3726cc-91c2-4614-a3a7-3f89f201e04a'
title: 'IAssemblyCacheItem::CreateStream method'
---

# IAssemblyCacheItem::CreateStream method

The **CreateStream** method copies the source of a manifest or module into a stream.

## Syntax


```C++
HRESULT CreateStream(
  [in]       DWORD          dwFlags,
  [in]       LPCWSTR        pszStreamName,
  [in]       DWORD          dwFormat,
  [in]       DWORD          dwFormatFlags,
             IStream        **ppIStream,
  [optional] ULARGE_INTEGER *puliMaxSize
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved.

</dd> <dt>

*pszStreamName* \[in\]
</dt> <dd>

Pointer to a string value containing the name of the manifest. This becomes the name of the stream.

</dd> <dt>

*dwFormat* \[in\]
</dt> <dd>

This parameter specifies whether a module or manifest is being copied to a stream.



| Value                                                                                                                                                                                                              | Meaning                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <span id="STREAM_FORMAT_COMPLIB_MODULE"></span><span id="stream_format_complib_module"></span><dl> <dt>**STREAM\_FORMAT\_COMPLIB\_MODULE**</dt> </dl>       | Copy the source of a module for a non-Windows assembly to a stream.<br/>   |
| <span id="STREAM_FORMAT_COMPLIB_MANIFEST"></span><span id="stream_format_complib_manifest"></span><dl> <dt>**STREAM\_FORMAT\_COMPLIB\_MANIFEST**</dt> </dl> | Copy the source of a manifest for a non-Windows assembly to a stream.<br/> |
| <span id="STREAM_FORMAT_WIN32_MODULE"></span><span id="stream_format_win32_module"></span><dl> <dt>**STREAM\_FORMAT\_WIN32\_MODULE**</dt> </dl>             | Copy the source of a module for a Windows assembly to a stream.<br/>       |
| <span id="STREAM_FORMAT_WIN32_MANIFEST"></span><span id="stream_format_win32_manifest"></span><dl> <dt>**STREAM\_FORMAT\_WIN32\_MANIFEST**</dt> </dl>       | Copy the source of a manifest for a Windows assembly to a stream.<br/>     |



 

</dd> <dt>

*dwFormatFlags* \[in\]
</dt> <dd>

Reserved.

</dd> <dt>

*ppIStream* 
</dt> <dd>

Pointer to the location that contains the pointer to the IStream interface that receives the information.

</dd> <dt>

*puliMaxSize* \[optional\]
</dt> <dd>

Reserved.

</dd> </dl>

## Return value

This method can return one of these values.



| Return value                                                                        | Description                            |
|-------------------------------------------------------------------------------------|----------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>    | The method succeeded.<br/>       |
| <dl> <dt>S\_FALSE</dt> </dl> | The method did not succeed.<br/> |



 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| DLL<br/>                      | <dl> <dt>Sxs.dll</dt> </dl> |



## See also

<dl> <dt>

[**IAssemblyCacheItem**](iassemblycacheitem.md)
</dt> </dl>

 

 





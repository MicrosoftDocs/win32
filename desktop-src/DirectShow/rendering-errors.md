---
description: Rendering Errors
ms.assetid: 8901eb78-bb7f-4dfe-bc01-0a267af5140f
title: Rendering Errors
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Rendering Errors

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

Microsoft® DirectShow® Editing Services (DES) defines various error codes used to log rendering errors. If a project does not render correctly, the render engine calls the [**IAMErrorLog::LogError**](iamerrorlog-logerror.md) method. The following table summarizes the parameters given to **LogError**:

-   The error code is contained in the *ErrorCode* parameter.
-   The description is contained in the ErrorString parameter.
-   The description is contained in the *ErrorString* parameter.
-   If there is extra information, the **VARIANT** type is contained in the **vt** member of the **VARIANT** pointed to by *pExtraInfo*.

> [!Note]  
> The error codes described here are not **HRESULT** values. For a list of **HRESULT** return values specific to DES, see [Error and Success Codes](error-and-success-codes.md).

 




| Error code | Description | Extra information | Variant type | 
|------------|-------------|-------------------|--------------|
| DEX_IDS_BAD_SOURCE_NAME | File name doesn't exist, or DirectShow doesn't recognize the file extension. | File name | <strong>BSTR</strong> | 
| DEX_IDS_BAD_SOURCE_NAME2 | File type does not match the file extension or the file is corrupt. | File name | <strong>BSTR</strong> | 
| DEX_IDS_MISSING_SOURCE_NAME | File name was required, but wasn't given. | None | Not applicable | 
| DEX_IDS_UNKNOWN_SOURCE | Cannot parse data source provided by this source. | None | Not applicable | 
| DEX_IDS_INSTALL_PROBLEM | Unexpected error. Some DirectShow component is not installed properly. | None | Not applicable | 
| DEX_IDS_NO_SOURCE_NAMES | Source filter does not accept file names. | None | Not applicable | 
| DEX_IDS_BAD_MEDIATYPE | Group's media type is not supported. | Group number | <strong>int</strong> | 
| DEX_IDS_STREAM_NUMBER | Invalid stream number for this source. | Stream number | <strong>int</strong> | 
| DEX_IDS_OUTOFMEMORY | Out of memory. | None | Not applicable | 
| DEX_IDS_DIBSEQ_NOTALLSAME | One bitmap in the sequence was not the same type as the others. | Bitmap name | <strong>BSTR</strong> | 
| DEX_IDS_CLIPTOOSHORT | Clip's media times are invalid, or the device-independent bitmap (DIB) sequence is too short.<blockquote>[!Note]<br />If other rendering errors occur, this error might occur even though the media times are valid.</blockquote><br /> | None | Not applicable | 
| DEX_IDS_INVALID_DXT | Class identifier (CLSID) of the effect or transition is not valid. | CLSID | <strong>BSTR</strong> | 
| DEX_IDS_INVALID_DEFAULT_DXT | The CLSID of the default effect or transition is not valid. | CLSID | <strong>BSTR</strong> | 
| DEX_IDS_NO_3D | Your version of DirectX does not support three-dimensional transitions. | CLSID | <strong>BSTR</strong> | 
| DEX_IDS_BROKEN_DXT | This effect is not the right kind, or is broken. | CLSID | <strong>BSTR</strong> | 
| DEX_IDS_NO_SUCH_PROPERTY | No such property exists on the object. | Property name | <strong>BSTR</strong> | 
| DEX_IDS_ILLEGAL_PROPERTY_VAL | Illegal value for this property. | Value specified | <strong>VARIANT</strong> | 
| DEX_IDS_INVALID_XML | Syntax error in XML file. | Line number | VT_I4 (4-byte integer) | 
| DEX_IDS_CANT_FIND_FILTER | Cannot find filter specified in XML by category and instance. | Friendly name (instance) | <strong>BSTR</strong> | 
| DEX_IDS_DISK_WRITE_ERROR | Error writing XML file to disk. | None | Not applicable | 
| DEX_IDS_INVALID_AUDIO_FX | CLSID not a valid DirectShow audio effect filter. | CLSID | <strong>BSTR</strong> | 
| DEX_IDS_CANT_FIND_COMPRESSOR | Cannot find a compressor to produce the specified compression format. | None | Not applicable | 




 

The following errors should never occur. If you encounter one of these errors, please send a bug report to Microsoft.



| Error code                 | Description                                 |
|----------------------------|---------------------------------------------|
| DEX\_IDS\_TIMELINE\_PARSE  | Unexpected error parsing the timeline.      |
| DEX\_IDS\_GRAPH\_ERROR     | Unexpected error building the filter graph. |
| DEX\_IDS\_GRID\_ERROR      | Unexpected error with the internal grid.    |
| DEX\_IDS\_INTERFACE\_ERROR | Unexpected error getting an interface.      |



 

 

 





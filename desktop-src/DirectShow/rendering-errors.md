---
description: Rendering Errors
ms.assetid: 8901eb78-bb7f-4dfe-bc01-0a267af5140f
title: Rendering Errors
ms.topic: article
ms.date: 05/31/2018
---

# Rendering Errors

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

Microsoft® DirectShow® Editing Services (DES) defines various error codes used to log rendering errors. If a project does not render correctly, the render engine calls the [**IAMErrorLog::LogError**](iamerrorlog-logerror.md) method. The following table summarizes the parameters given to **LogError**:

-   The error code is contained in the *ErrorCode* parameter.
-   The description is contained in the ErrorString parameter.
-   The description is contained in the *ErrorString* parameter.
-   If there is extra information, the **VARIANT** type is contained in the **vt** member of the **VARIANT** pointed to by *pExtraInfo*.

> [!Note]  
> The error codes described here are not **HRESULT** values. For a list of **HRESULT** return values specific to DES, see [Error and Success Codes](error-and-success-codes.md).

 



<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Error code</th>
<th>Description</th>
<th>Extra information</th>
<th>Variant type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DEX_IDS_BAD_SOURCE_NAME</td>
<td>File name doesn't exist, or DirectShow doesn't recognize the file extension.</td>
<td>File name</td>
<td><strong>BSTR</strong></td>
</tr>
<tr class="even">
<td>DEX_IDS_BAD_SOURCE_NAME2</td>
<td>File type does not match the file extension or the file is corrupt.</td>
<td>File name</td>
<td><strong>BSTR</strong></td>
</tr>
<tr class="odd">
<td>DEX_IDS_MISSING_SOURCE_NAME</td>
<td>File name was required, but wasn't given.</td>
<td>None</td>
<td>Not applicable</td>
</tr>
<tr class="even">
<td>DEX_IDS_UNKNOWN_SOURCE</td>
<td>Cannot parse data source provided by this source.</td>
<td>None</td>
<td>Not applicable</td>
</tr>
<tr class="odd">
<td>DEX_IDS_INSTALL_PROBLEM</td>
<td>Unexpected error. Some DirectShow component is not installed properly.</td>
<td>None</td>
<td>Not applicable</td>
</tr>
<tr class="even">
<td>DEX_IDS_NO_SOURCE_NAMES</td>
<td>Source filter does not accept file names.</td>
<td>None</td>
<td>Not applicable</td>
</tr>
<tr class="odd">
<td>DEX_IDS_BAD_MEDIATYPE</td>
<td>Group's media type is not supported.</td>
<td>Group number</td>
<td><strong>int</strong></td>
</tr>
<tr class="even">
<td>DEX_IDS_STREAM_NUMBER</td>
<td>Invalid stream number for this source.</td>
<td>Stream number</td>
<td><strong>int</strong></td>
</tr>
<tr class="odd">
<td>DEX_IDS_OUTOFMEMORY</td>
<td>Out of memory.</td>
<td>None</td>
<td>Not applicable</td>
</tr>
<tr class="even">
<td>DEX_IDS_DIBSEQ_NOTALLSAME</td>
<td>One bitmap in the sequence was not the same type as the others.</td>
<td>Bitmap name</td>
<td><strong>BSTR</strong></td>
</tr>
<tr class="odd">
<td>DEX_IDS_CLIPTOOSHORT</td>
<td>Clip's media times are invalid, or the device-independent bitmap (DIB) sequence is too short.
<blockquote>
[!Note]<br />
If other rendering errors occur, this error might occur even though the media times are valid.
</blockquote>
<br/></td>
<td>None</td>
<td>Not applicable</td>
</tr>
<tr class="even">
<td>DEX_IDS_INVALID_DXT</td>
<td>Class identifier (CLSID) of the effect or transition is not valid.</td>
<td>CLSID</td>
<td><strong>BSTR</strong></td>
</tr>
<tr class="odd">
<td>DEX_IDS_INVALID_DEFAULT_DXT</td>
<td>The CLSID of the default effect or transition is not valid.</td>
<td>CLSID</td>
<td><strong>BSTR</strong></td>
</tr>
<tr class="even">
<td>DEX_IDS_NO_3D</td>
<td>Your version of DirectX does not support three-dimensional transitions.</td>
<td>CLSID</td>
<td><strong>BSTR</strong></td>
</tr>
<tr class="odd">
<td>DEX_IDS_BROKEN_DXT</td>
<td>This effect is not the right kind, or is broken.</td>
<td>CLSID</td>
<td><strong>BSTR</strong></td>
</tr>
<tr class="even">
<td>DEX_IDS_NO_SUCH_PROPERTY</td>
<td>No such property exists on the object.</td>
<td>Property name</td>
<td><strong>BSTR</strong></td>
</tr>
<tr class="odd">
<td>DEX_IDS_ILLEGAL_PROPERTY_VAL</td>
<td>Illegal value for this property.</td>
<td>Value specified</td>
<td><strong>VARIANT</strong></td>
</tr>
<tr class="even">
<td>DEX_IDS_INVALID_XML</td>
<td>Syntax error in XML file.</td>
<td>Line number</td>
<td>VT_I4 (4-byte integer)</td>
</tr>
<tr class="odd">
<td>DEX_IDS_CANT_FIND_FILTER</td>
<td>Cannot find filter specified in XML by category and instance.</td>
<td>Friendly name (instance)</td>
<td><strong>BSTR</strong></td>
</tr>
<tr class="even">
<td>DEX_IDS_DISK_WRITE_ERROR</td>
<td>Error writing XML file to disk.</td>
<td>None</td>
<td>Not applicable</td>
</tr>
<tr class="odd">
<td>DEX_IDS_INVALID_AUDIO_FX</td>
<td>CLSID not a valid DirectShow audio effect filter.</td>
<td>CLSID</td>
<td><strong>BSTR</strong></td>
</tr>
<tr class="even">
<td>DEX_IDS_CANT_FIND_COMPRESSOR</td>
<td>Cannot find a compressor to produce the specified compression format.</td>
<td>None</td>
<td>Not applicable</td>
</tr>
</tbody>
</table>



 

The following errors should never occur. If you encounter one of these errors, please send a bug report to Microsoft.



| Error code                 | Description                                 |
|----------------------------|---------------------------------------------|
| DEX\_IDS\_TIMELINE\_PARSE  | Unexpected error parsing the timeline.      |
| DEX\_IDS\_GRAPH\_ERROR     | Unexpected error building the filter graph. |
| DEX\_IDS\_GRID\_ERROR      | Unexpected error with the internal grid.    |
| DEX\_IDS\_INTERFACE\_ERROR | Unexpected error getting an interface.      |



 

 

 





---
error-parsing-yaml: 
---

# IVMDisplay::Thumbnail property

The **Thumbnail** property contains an array of pixels representing a thumbnail image of the virtual machine's screen.

This property is read-only.

## Syntax


```C++
HRESULT get_Thumbnail(
  [out] VARIANT *thumbnailImage
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VMDisplay.Thumbnail( _
  ByRef thumbnailImage _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

An array of **Objects** containing unsigned **Integer** entries, one for each pixel in the thumbnail.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                  |
|-----------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter is **NULL**.<br/>    |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/> |



## Remarks

This interface returns the thumbnail less efficiently than the [**\_GenerateThumbnail**](ivmdisplay--generatethumbnail.md) method, but is usable from scripting clients. The thumbnail is always 64 pixels wide by 48 pixels high. Each pixel is 32 bits. The first 64 elements in the array is the first row of pixels in the thumbnail, the next 64 elements is the second row, and so on.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDisplay**](ivmdisplay.md)
</dt> </dl>

 

 






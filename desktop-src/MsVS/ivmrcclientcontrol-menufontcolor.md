---
error-parsing-yaml: 
---

# IVMRCClientControl::MenuFontColor property

The **MenuFontColor** property contains the client's menu font color specified in HTML hex string format.

This property is read/write.

## Syntax


```C++
HRESULT put_MenuFontColor(
  [in]  BSTR menuBackColor
);

HRESULT get_MenuFontColor(
  [out] BSTR *menuFontColor
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
<td><pre><code>VMRCClientControl.MenuFontColor( _
  ByRef menuFontColor, _
  ByVal menuBackColor _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The client's menu font color specified in HTML hex string format.

This property value is read/write.

## Error codes



| Name                                                                                     | Meaning                                                  |
|------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>                 |
| <dl> <dt>S\_FALSE</dt> </dl>      | This property cannot be changed at this time.<br/> |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *menuFontColor* parameter was **NULL**.<br/>   |



## Remarks

The color is specified using the standard HTML six-digit hex string format. This is in the form of "*rrggbb*". For example, "**000000**" represents black, "**FFFFFF**" represents white, and "**FF0000**" represents red.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VMRCClientControl.h</dt> </dl>    |
| Library<br/>  | <dl> <dt>VMRCClientControl.lib</dt> </dl>  |



## See also

<dl> <dt>

[**IVMRCClientControl**](ivmrcclientcontrol.md)
</dt> </dl>

 

 






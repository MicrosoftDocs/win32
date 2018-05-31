---
error-parsing-yaml: 
---

# IVMRCAuthenticator::Type property

The **Type** property contains an internal value representing the authentication type.

This property is read-only.

## Syntax


```C++
HRESULT get_Type(
  [out] VMRCAuthenticationType *type
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
<td><pre><code>VMRCAuthenticator.Type( _
  ByRef type _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The type of authentication provided by this object represents.

This property value is read-only.

## Error codes



| Name                                                                                  | Meaning                                                   |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>     | The property value was retrieved successfully.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl> | The *type* parameter is **NULL**.<br/>              |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMRCAuthenticator**](ivmrcauthenticator.md)
</dt> </dl>

 

 






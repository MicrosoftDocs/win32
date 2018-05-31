---
error-parsing-yaml: 
---

# IVMVirtualServer::Locale property

The **Locale** property sets the user interface locale of the Virtual Server service.

This property is write-only.

## Syntax


```C++
HRESULT put_Locale(
  [in] ULONG inLocale
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
<td><pre><code>VMVirtualServer.Locale( _
  ByVal inLocale _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The desired Windows locale ID to use for the Virtual Server service.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                                                     |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                                    |
| <dl> <dt>E\_FAIL</dt> </dl>            | The locale specified by the *inLocale* parameter is not supported by the Virtual Server service.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                                                                    |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> <dt>

[**DefaultLocale**](ivmvirtualserver-defaultlocale.md)
</dt> <dt>

[**QueryLocale**](ivmvirtualserver-querylocale.md)
</dt> </dl>

 

 






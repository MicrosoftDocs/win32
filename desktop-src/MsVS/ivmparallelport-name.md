---
error-parsing-yaml: 
---

# IVMParallelPort::Name property

The **Name** property contains the name of the parallel port.

This property is read/write.

## Syntax


```C++
HRESULT put_Name(
  [in]  BSTR portName
);

HRESULT get_Name(
  [out] BSTR *portName
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
<td><pre><code>VMParallelPort.Name( _
  ByRef portName, _
  ByVal portName _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The name of the parallel port (for example, "LPT1").

This property value is read/write.

## Error codes



| Name                                                                                           | Meaning                                                                 |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>                                |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *portName* parameter is **NULL**.<br/>                        |
| <dl> <dt>E\_INVALIDARG</dt> </dl>       | The *portName* parameter refers to an invalid parallel port.<br/> |
| <dl> <dt> VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                                |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>  | An unexpected error occurred.<br/>                                |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMParallelPort**](ivmparallelport.md)
</dt> </dl>

 

 






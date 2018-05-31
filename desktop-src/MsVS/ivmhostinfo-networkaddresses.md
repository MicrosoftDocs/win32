---
error-parsing-yaml: 
---

# IVMHostInfo::NetworkAddresses property

The **NetworkAddresses** property contains an array of TCP/IP addresses in the host computer.

This property is read-only.

## Syntax


```C++
HRESULT get_NetworkAddresses(
  [out] VARIANT *hostAddresses
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
<td><pre><code>VMHostInfo.NetworkAddresses( _
  ByRef hostAddresses _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains an array of TCP/IP address strings in dotted-decimal notation.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                       |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                      |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *hostAddresses* parameter referenced **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                      |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHostInfo**](ivmhostinfo.md)
</dt> </dl>

 

 






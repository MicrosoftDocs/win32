---
error-parsing-yaml: 
---

# IVMVirtualNetwork::PacketsSentHistory property

The **PacketsSentHistory** property contains the recent number of packets sent per second by this virtual network (as an array of number of packets).

This property is read-only.

## Syntax


```C++
HRESULT get_PacketsSentHistory(
  [out] VARIANT *packetsSent
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
<td><pre><code>VMVirtualNetwork.PacketsSentHistory( _
  ByRef packetsSent _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The recent number of packets sent per second by this virtual network as an unsigned **Integer** array of 60 elements, representing the number of packets sent at each second over the past minute.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                               |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>              |
| <dl> <dt>E\_POINTER</dt> </dl>         | The **packetsSent** parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>              |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualNetwork**](ivmvirtualnetwork.md)
</dt> </dl>

 

 






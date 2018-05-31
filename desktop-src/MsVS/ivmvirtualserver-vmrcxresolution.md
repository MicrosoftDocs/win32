---
error-parsing-yaml: 
---

# IVMVirtualServer::VMRCXResolution property

The **VMRCXResolution** property contains the horizontal resolution used for server administration.

This property is read/write.

## Syntax


```C++
HRESULT put_VMRCXResolution(
  [in]  long vmrcXResolution
);

HRESULT get_VMRCXResolution(
  [out] long *vmrcXResolution
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
<td><pre><code>VMVirtualServer.VMRCXResolution( _
  ByRef vmrcXResolution, _
  ByVal vmrcXResolution _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The horizontal resolution used for server administration.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                 |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter *vmrcXResolution* is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                |



## Examples

The following example displays the **VMRCXResolution** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "VMRC X-Resolution: " & objVS.VMRCXResolution
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 






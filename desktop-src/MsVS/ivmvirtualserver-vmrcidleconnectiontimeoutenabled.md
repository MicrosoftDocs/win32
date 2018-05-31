---
error-parsing-yaml: 
---

# IVMVirtualServer::VMRCIdleConnectionTimeoutEnabled property

The **VMRCIdleConnectionTimeoutEnabled** property indicates whether idle VMRC connections are automatically disconnected.

This property is read/write.

## Syntax


```C++
HRESULT put_VMRCIdleConnectionTimeoutEnabled(
  [in]  VARIANT_BOOL shouldEnable
);

HRESULT get_VMRCIdleConnectionTimeoutEnabled(
  [out] VARIANT_BOOL *isEnabled
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
<td><pre><code>VMVirtualServer.VMRCIdleConnectionTimeoutEnabled( _
  ByRef isEnabled, _
  ByVal shouldEnable _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the VMRC server disconnects idle connections.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                      |
|-----------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>     |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/> |



## Remarks

The VMRC connection idle timeout is specified in seconds.

## Examples

The following example displays the **VMRCIdleConnectionTimeoutEnabled** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Wscript.Echo "Name: " & objVS.Name

Wscript.Echo "VMRC idle connection timeout enabled: " & _
             objVS.VMRCIdleConnectionTimeoutEnabled
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

 

 






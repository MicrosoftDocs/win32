---
error-parsing-yaml: 
---

# IVMVirtualServer::VMRCEncryptionCertificateRequest property

The **VMRCEncryptionCertificateRequest** property contains the current security certificate request.

This property is read-only.

## Syntax


```C++
HRESULT get_VMRCEncryptionCertificateRequest(
  [out] BSTR *certificateRequest
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
<td><pre><code>VMVirtualServer.VMRCEncryptionCertificateRequest( _
  ByRef certificateRequest _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The current Base-64 encoded security certificate request. If a zero-length string is returned, it indicates that no certificate request is pending.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                               |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                              |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter *certificateRequest* referenced is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                              |



## Examples

The following example displays the **VMRCEncryptionCertificateRequest** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name

If objVS.VMRCEncryptionCertificateRequest = "" Then
  Wscript.Echo "VMRC encryption certificate request: [none]"
Else
  Wscript.Echo "VMRC encryption certificate request: " & _
                objVS.VMRCEncryptionCertificateRequest
End If
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

 

 






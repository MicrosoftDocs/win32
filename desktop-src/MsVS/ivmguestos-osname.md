---
error-parsing-yaml: 
---

# IVMGuestOS::OSName property

The **OSName** property contains the name of the guest operating system running in the virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_OSName(
  [out] BSTR *guestOSName
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
<td><pre><code>VMGuestOS.OSName( _
  ByRef guestOSName _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The full name (including suite name) of the guest operating system.

This property value is read-only.

## Error codes



| Name                                                                                                             | Meaning                                                                            |
|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                                 | The operation was successful.<br/>                                           |
| <dl> <dt>E\_POINTER</dt> </dl>                            | *guestOSName* was not specified.<br/>                                        |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> </dl>               | The virtual machine is not running.<br/>                                     |
| <dl> <dt>VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL</dt> </dl> | The virtual machine is not fully booted or Additions are not installed.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>                    | An unexpected error occurred.<br/>                                           |



## Remarks

The virtual machine must be running (that is, fully booted and not shutting down) and Additions must be installed when this method is invoked.

The following is a list of the possible names returned by the various Microsoft operating systems:

-   Windows Server 2003
-   Windows Server 2003, Standard Edition
-   Windows Server 2003, Enterprise Edition
-   Windows Server 2003, Datacenter Edition
-   Windows Server 2003, Web Edition
-   Windows Advanced Server, Limited Edition
-   Windows XP Home Edition
-   Windows XP Professional
-   Windows XP Embedded
-   Windows XP 64-Bit Edition
-   Windows XP Media Center Edition
-   Windows XP Tablet PC Edition
-   Windows XP 64-Bit Edition Version 2003
-   Windows 2000
-   Windows 2000 Professional
-   Windows 2000 Server
-   Windows 2000 Advanced Server
-   Windows 2000 Datacenter Server

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMGuestOS**](ivmguestos.md)
</dt> </dl>

 

 






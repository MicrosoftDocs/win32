---
title: IVMRCClientControl AdministratorMode property
description: The AdministratorMode property indicates whether the administrator features of the client are enabled.
ms.assetid: '14bb89f4-f41a-411c-bb26-482136f4c585'
keywords: ["AdministratorMode property Virtual Server", "AdministratorMode property Virtual Server , IVMRCClientControl interface", "IVMRCClientControl interface Virtual Server , AdministratorMode property", "AdministratorMode property Virtual Server , VMRCClientControl interface", "VMRCClientControl interface Virtual Server , AdministratorMode property"]
topic_type:
- apiref
api_name:
- IVMRCClientControl.AdministratorMode
- IVMRCClientControl.get_AdministratorMode
- IVMRCClientControl.put_AdministratorMode
- VMRCClientControl.AdministratorMode
api_location:
- VMRCClientControl.lib
- VMRCClientControl.dll
api_type:
- COM
---

# IVMRCClientControl::AdministratorMode property

The **AdministratorMode** property indicates whether the administrator features of the client are enabled.

This property is read/write.

## Syntax


```C++
HRESULT put_AdministratorMode(
  [in]  VARIANT_BOOL adminMode
);

HRESULT get_AdministratorMode(
  [out] VARIANT_BOOL *adminMode
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
<td><pre><code>VMRCClientControl.AdministratorMode( _
  ByRef adminMode, _
  ByVal adminMode _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the administrator features of the client are enabled.

This property value is read/write.

## Error codes



| Name                                                                                     | Meaning                                                  |
|------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>                 |
| <dl> <dt>S\_FALSE</dt> </dl>      | This property cannot be changed at this time.<br/> |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *adminMode* parameter was **NULL**.<br/>       |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VMRCClientControl.h</dt> </dl>    |
| Library<br/>  | <dl> <dt>VMRCClientControl.lib</dt> </dl>  |



## See also

<dl> <dt>

[**IVMRCClientControl**](ivmrcclientcontrol.md)
</dt> </dl>

 

 






---
title: IVMRCClientControl HostKey property
description: The HostKey property contains the key identifier for the current host key.
ms.assetid: fc3dff71-4f2e-4369-a27b-adc9a9de9130
keywords:
- HostKey property Virtual Server
- HostKey property Virtual Server , IVMRCClientControl interface
- IVMRCClientControl interface Virtual Server , HostKey property
- HostKey property Virtual Server , VMRCClientControl interface
- VMRCClientControl interface Virtual Server , HostKey property
topic_type:
- apiref
api_name:
- IVMRCClientControl.HostKey
- IVMRCClientControl.get_HostKey
- IVMRCClientControl.put_HostKey
- VMRCClientControl.HostKey
api_location:
- VMRCClientControl.lib
- VMRCClientControl.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMRCClientControl::HostKey property

The **HostKey** property contains the key identifier for the current host key.

This property is read/write.

## Syntax


```C++
HRESULT put_HostKey(
  [in]  BSTR hostKey
);

HRESULT get_HostKey(
  [out] BSTR *hostKey
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
<td><pre><code>VMRCClientControl.HostKey( _
  ByRef hostKey, _
  ByVal hostKey _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The key identifier for the current host key.

This property value is read/write.

## Error codes



| Name                                                                                     | Meaning                                                  |
|------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>                 |
| <dl> <dt>S\_FALSE</dt> </dl>      | This property cannot be changed at this time.<br/> |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *hostKey* parameter was **NULL**.<br/>         |



## Remarks

The value for the host key defaults to the right Alt key on a standard 101-key AT keyboard and is represented by the "**Key\_RightAlt**" string. A list of valid key identifier strings can be found on the [**IVMRCClientControl::SendKeySequence**](ivmrcclientcontrol-sendkeysequence.md) topic.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VMRCClientControl.h</dt> </dl>    |
| Library<br/>  | <dl> <dt>VMRCClientControl.lib</dt> </dl>  |



## See also

<dl> <dt>

[**IVMRCClientControl**](ivmrcclientcontrol.md)
</dt> </dl>

 

 





